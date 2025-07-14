import requests
import pandas as pd
from datetime import datetime

def fetch_crime_data(zip_code: str):
    # Placeholder: Replace with real API or data source
    # Example: Fetch mock data for demonstration
    data = [
        {"date": "2023-01-01", "crime_count": 10},
        {"date": "2023-02-01", "crime_count": 8},
        {"date": "2023-03-01", "crime_count": 7},
        {"date": "2023-04-01", "crime_count": 6},
        {"date": "2023-05-01", "crime_count": 5},
    ]
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    return df

def process_crime_trend(df: pd.DataFrame):
    # Calculate month-over-month change and acceleration
    df = df.sort_values("date")
    df["change"] = df["crime_count"].diff()
    df["acceleration"] = df["change"].diff()
    return df 