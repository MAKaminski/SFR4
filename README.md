# SFR4: Gentrification Investment Model

A modular, scalable tool to identify and rank real estate investment opportunities based on accelerating gentrification trends.

## Features
- Data ingestion from public APIs (crime, real estate, amenities, demographics)
- Gentrification scoring engine (trend acceleration)
- Investment analysis (IRR, cash flows)
- GraphQL API for querying top zips, neighborhoods, and properties
- Streamlit dashboard for visualization

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run backend API:
   ```bash
   uvicorn backend.api.main:app --reload
   ```
3. Run dashboard:
   ```bash
   streamlit run frontend/app.py
   ```

## Project Structure
- `backend/` - API, models, ETL, scoring, DB
- `frontend/` - Streamlit dashboard 