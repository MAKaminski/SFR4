import streamlit as st
import requests

st.title("SFR4 Gentrification Investment Model")
st.header("Top Zip Codes by Gentrification Score (Crime Trend)")

API_URL = "https://sfr4-backend.onrender.com/graphql"

query = """
query TopZipcodes($count: Int!) {
  topZipcodes(count: $count) {
    zipCode
    score
  }
}
"""

count = st.slider("Number of top zip codes", 1, 10, 5)

response = requests.post(
    API_URL,
    json={"query": query, "variables": {"count": count}},
)

if response.status_code == 200:
    data = response.json()["data"]["topZipcodes"]
    st.table([{"Zip Code": z["zipCode"], "Score": round(z["score"], 2)} for z in data])
else:
    st.error("Failed to fetch data from API.") 