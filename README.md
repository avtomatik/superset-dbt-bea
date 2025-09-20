# 📊 Superset + dbt + BEA Integration

An **end-to-end data pipeline** for U.S. Bureau of Economic Analysis (BEA) data:
- **Ingest** economic releases from the BEA API
- **Transform** datasets with [dbt](https://docs.getdbt.com/)
- **Store** in a SQL database (Postgres or DuckDB)
- **Visualize** in [Apache Superset](https://superset.apache.org/) with prebuilt dashboards

This project is a hands-on demo of **modern data stack tooling**: ingestion + transformation + BI.

---

## 🚀 Features
- 🔄 Automated **data ingestion** from BEA API (GDP, trade, PCE, etc.)
- 🧹 **dbt models** for cleaning, staging, and aggregating BEA releases
- 📦 Database integration with Postgres (default) or DuckDB
- 📊 Prebuilt **Superset dashboards** for macroeconomic analysis
- 🐳 Easy setup with `docker-compose` (Superset + Postgres + dbt)

---

## 📂 Project Structure
```

superset-dbt-bea/
│── data\_ingestion/
│    └── bea\_downloader.py   # Fetch BEA data from API
│── dbt\_project/
│    ├── models/
│    │   ├── staging/        # Clean raw BEA data
│    │   ├── marts/          # Aggregated metrics
│    │   └── metrics/        # Growth rates, ratios, rolling averages
│── superset/
│    └── dashboards/         # JSON exports of example dashboards
│── docker-compose.yml       # For Superset + Postgres + dbt
│── README.md

````

---

## 📊 Example Dashboards
### US GDP Overview
- GDP growth over time
- Contributions by industry
- QoQ vs YoY toggle

### Trade & Inflation
- Imports vs exports
- CPI / PCE inflation trends
- Trade balance as % of GDP

👉 _(Screenshots coming soon — export Superset dashboards as JSON + PNG and place them here!)_

---

## ⚡ Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/superset-dbt-bea.git
cd superset-dbt-bea
````

### 2. Start services

```bash
docker-compose up -d
```

This spins up:

* **Postgres** (data warehouse)
* **Superset** (BI tool)
* **dbt** (transformation engine)

### 3. Ingest BEA data

```bash
python data_ingestion/bea_downloader.py
```

### 4. Run dbt transformations

```bash
cd dbt_project
dbt run
```

### 5. Import dashboards into Superset

```bash
# Log in to Superset at http://localhost:8088
# Import JSON files from superset/dashboards/
```

---

## 🛠️ Tech Stack

* [Apache Superset](https://superset.apache.org/) – Visualization
* [dbt](https://www.getdbt.com/) – Data transformation
* [Postgres](https://www.postgresql.org/) / [DuckDB](https://duckdb.org/) – Storage
* [BEA API](https://apps.bea.gov/api/data/) – Data source
* [Docker Compose](https://docs.docker.com/compose/) – Local orchestration

---

## 🗺️ Roadmap

* [ ] Add support for more BEA datasets (regional GDP, income)
* [ ] Publish dbt models as a package (`dbt-bea`)
* [ ] Automate Superset dashboard import
* [ ] Add CI/CD pipeline for refreshing data (GitHub Actions)
* [ ] Deploy demo online with lightweight database (DuckDB/SQLite + Superset in container)

---

## 🤝 Contributing

Pull requests are welcome!
Ideas for improvements:

* New dbt models (e.g., employment, housing data)
* Additional Superset visualizations
* Better dashboard theming

---

## 📜 License

MIT License — feel free to use and adapt.
