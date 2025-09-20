import requests
import pandas as pd
import os
from sqlalchemy import create_engine

# 🔑 BEA API Key (https://apps.bea.gov/api/signup/)
BEA_API_KEY = os.getenv("BEA_API_KEY", "YOUR_API_KEY_HERE")

# BEA API endpoint
BASE_URL = "https://apps.bea.gov/api/data/"

# Postgres connection (from docker-compose.yml)
DB_USER = os.getenv("DB_USER", "superset")
DB_PASS = os.getenv("DB_PASS", "superset")
DB_HOST = os.getenv("DB_HOST", "localhost")  # use "postgres" if running inside Docker
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "superset")

CONNECTION_STRING = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def fetch_gdp_data(year_start=2015, year_end=2023, frequency="A"):
    """
    Fetch GDP by Industry data from BEA API.
    """
    params = {
        "UserID": BEA_API_KEY,
        "method": "GetData",
        "datasetname": "GDPbyIndustry",
        "TableID": "6",  # Example: Value Added by Industry
        "Year": f"{year_start},{year_end}",
        "Frequency": frequency,
        "ResultFormat": "json",
    }

    print("📡 Fetching BEA GDP by Industry data...")
    resp = requests.get(BASE_URL, params=params)

    if resp.status_code != 200:
        raise Exception(f"❌ Error fetching data: {resp.text}")

    data = resp.json()

    try:
        records = data["BEAAPI"]["Results"]["Data"]
    except KeyError:
        raise Exception(f"❌ Unexpected response format: {data}")

    df = pd.DataFrame(records)
    print(f"✅ Fetched {len(df)} records from BEA API.")
    return df


def save_to_postgres(df, table_name="gdp"):
    """
    Save DataFrame directly into Postgres.
    """
    engine = create_engine(CONNECTION_STRING)

    # Ensure schema matches dbt source
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",  # replace table each run
        index=False,
        chunksize=1000,
        method="multi",
    )
    print(f"✅ Saved BEA data to Postgres table: {table_name}")


if __name__ == "__main__":
    df = fetch_gdp_data()
    save_to_postgres(df)
