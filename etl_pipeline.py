import pandas as pd
import sqlite3

# Load data
df = pd.read_csv('data/rides.csv')

# Clean data
df = df.dropna()
df = df[(df['fare_amount'] > 0) & (df['status'] == 'completed')]

# Connect to SQLite
conn = sqlite3.connect('data/rides.db')

# Save cleaned data
df.to_sql('fact_trips', conn, if_exists='replace', index=False)

# Create driver dimension table
df[['driver_id']].drop_duplicates().to_sql('dim_drivers', conn, if_exists='replace', index=False)

conn.close()
