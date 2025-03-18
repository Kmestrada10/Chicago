import pandas as pd
from fetch_data import fetch_crime_data, preprocess_data

def generate_recent_crimes(df):
    # Sort by date and get the last 20 crimes
    recent_crimes = df.sort_values(by='date', ascending=False).head(20)
    return recent_crimes[['date', 'primary_type', 'block']]

if __name__ == "__main__":
    crime_data = fetch_crime_data()
    crime_data = preprocess_data(crime_data)
    recent_crimes = generate_recent_crimes(crime_data)
    print(recent_crimes)