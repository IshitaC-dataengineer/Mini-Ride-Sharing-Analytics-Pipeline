import time
import pandas as pd

df = pd.read_csv('data/rides.csv')
df = df[df['status'] == 'completed']

trip_count = 0
total_fare = 0
window_size = 20  # number of records to simulate "per minute"

for i, row in df.iterrows():
    trip_count += 1
    total_fare += row['fare_amount']

    if i % window_size == 0 and i != 0:
        print(f"Rolling Metrics (Next {window_size} trips):")
        print(f"- Trips per minute: {window_size}")
        print(f"- Avg fare: {round(total_fare / trip_count, 2)}\n")
        time.sleep(1)  # simulate stream delay
