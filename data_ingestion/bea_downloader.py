from http import HTTPStatus

import pandas as pd
import requests
from config import settings
from sqlalchemy import create_engine


def fetch_gdp_data(year_start=2015, year_end=2024, frequency="A"):
    """
    Fetch GDP by Industry data from BEA API.
    """
    params = {
        "UserID": settings.BEA_API_KEY,
        "method": "GetData",
        "datasetname": "GDPbyIndustry",
        "TableID": "6",  # Example: Value Added by Industry
        "Year": f"{year_start},{year_end}",
        "Frequency": frequency,
        "Industry": "ALL",
        "ResultFormat": "json",
    }

    print("📡 Fetching BEA GDP by Industry data...")
    resp = requests.get(settings.BASE_URL, params=params)

    if resp.status_code != HTTPStatus.OK:
        raise Exception(f"❌ Error fetching data: {resp.text}")

    data = resp.json()

    try:
        records = data["BEAAPI"]["Results"][0]["Data"]
    except KeyError:
        raise Exception(f"❌ Unexpected response format: {data}")

    df = pd.DataFrame(records)
    print(f"✅ Fetched {len(df)} records from BEA API.")
    return df


def save_to_postgres(df, table_name="gdp"):
    """
    Save DataFrame directly into Postgres.
    """
    engine = create_engine(settings.db_dsn)

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
