import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from backend.db import init_db
from backend.etl.crime_data import fetch_crime_data, process_crime_trend
from backend.scoring import gentrification_score_from_crime

@strawberry.type
class ZipScore:
    zip_code: str
    score: float

@strawberry.type
class Query:
    @strawberry.field
    def top_zipcodes(self, count: int = 10) -> list[ZipScore]:
        # Placeholder: Use a static list of zip codes for demo
        zip_codes = ["10001", "10002", "10003", "10004", "10005"]
        results = []
        for zc in zip_codes:
            df = fetch_crime_data(zc)
            trend = process_crime_trend(df)
            score = gentrification_score_from_crime(trend)
            results.append(ZipScore(zip_code=zc, score=score))
        # Sort by score descending (higher = more rapid gentrification)
        results.sort(key=lambda x: x.score, reverse=True)
        return results[:count]

schema = strawberry.Schema(query=Query)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

gql_app = GraphQLRouter(schema)
app.include_router(gql_app, prefix="/graphql") 