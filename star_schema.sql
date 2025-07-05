CREATE TABLE IF NOT EXISTS fact_trips (
    trip_id TEXT PRIMARY KEY,
    driver_id INTEGER,
    pickup_time TEXT,
    dropoff_time TEXT,
    pickup_location TEXT,
    fare_amount REAL,
    status TEXT
);

CREATE TABLE IF NOT EXISTS dim_drivers (
    driver_id INTEGER PRIMARY KEY
);

SELECT strftime('%H', pickup_time) AS hour, AVG(fare_amount) AS avg_fare
FROM fact_trips
GROUP BY hour;


SELECT driver_id, SUM(fare_amount) AS total_revenue
FROM fact_trips
GROUP BY driver_id;
