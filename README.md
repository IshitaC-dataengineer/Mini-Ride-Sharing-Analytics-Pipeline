# 🚖 Mini Ride-Sharing Analytics Pipeline (Batch + Stream)

This project simulates a simplified **data analytics pipeline** for a ride-sharing company to analyze **daily and hourly trends** in rides and revenue. It includes batch ETL, star schema modeling, simulated real-time streaming, and data quality checks using **Python, SQLite, and PySpark (optional)**.

---

## Project Structure
├── data/
│ ├── rides.csv # Simulated input data
│ └── rides.db # SQLite database after ETL
├── simulate_data.py # Script to generate mock data
├── etl_pipeline.py # Batch ETL script (clean + load)
├── star_schema.sql # SQL schema and analysis queries
├── stream_simulator.py # Simulated real-time metrics
├── data_quality.py # Data validation script
├── architecture.png # Architecture diagram
└── README.md # This file

---

## Requirements

- Python 3.7+
- SQLite or [DB Browser for SQLite](https://sqlitebrowser.org/)
- pandas
- faker *(optional)*

Install dependencies (if needed):

```bash
pip install pandas

# Setup & Run
# 1. Generate Ride Data
# Generates 1500 mock ride records with realistic fields.

python simulate_data.py   # This creates data/rides.csv.



# 2. Run Batch ETL Pipeline
# Cleans the data and loads into rides.db with two tables: fact_trips and dim_drivers.

python etl_pipeline.py



# 3. Star Schema + SQL Queries
# Open data/rides.db in DB Browser for SQLite or run SQL directly to:
# Create star schema (if needed)
# Run analytics queries



# 4. Real-Time Metrics (Simulated Streaming)
# Simulates stream using time.sleep and prints rolling metrics every 20 records.

python stream_simulator.py


# 5. Data Quality Validation
# Ensures:
# No NULL in trip_id or fare_amount
# All fare_amount values are positive

python data_quality.py



# Star Schema Design
# fact_trips: Stores detailed ride info.
# dim_drivers: Minimal driver metadata.
fact_trips
-----------
trip_id (PK)
driver_id (FK)
pickup_time
dropoff_time
pickup_location
fare_amount
status

dim_drivers
------------
driver_id (PK)
