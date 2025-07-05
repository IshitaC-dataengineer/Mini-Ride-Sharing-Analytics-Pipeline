import pandas as pd

df = pd.read_csv('data/rides.csv')

def validate(df):
    assert df['trip_id'].notnull().all(), "NULL trip_id found"
    assert df['fare_amount'].notnull().all(), "NULL fare_amount found"
    assert (df['fare_amount'] > 0).all(), "Non-positive fare_amount found"
    print("✅ Data quality checks passed!")

validate(df)
