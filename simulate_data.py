import csv
import random
from datetime import datetime, timedelta
import uuid

pickup_locations = ['Downtown', 'Airport', 'Mall', 'University', 'Stadium']
statuses = ['completed', 'cancelled', 'no_show']

def generate_ride():
    trip_id = str(uuid.uuid4())
    driver_id = random.randint(1, 50)
    pickup_time = datetime.now() - timedelta(hours=random.randint(0, 48))
    trip_duration = random.randint(5, 60)
    dropoff_time = pickup_time + timedelta(minutes=trip_duration)
    pickup_location = random.choice(pickup_locations)
    fare_amount = round(random.uniform(5.0, 100.0), 2)
    status = random.choice(statuses)

    return [trip_id, driver_id, pickup_time.isoformat(), dropoff_time.isoformat(), pickup_location, fare_amount, status]

with open('data/rides.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['trip_id', 'driver_id', 'pickup_time', 'dropoff_time', 'pickup_location', 'fare_amount', 'status'])
    for _ in range(1500):
        writer.writerow(generate_ride())
