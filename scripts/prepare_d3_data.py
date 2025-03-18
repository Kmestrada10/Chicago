import pandas as pd
import json
from fetch_data import fetch_crime_data, preprocess_data

def prepare_d3_data(df):
    # Group by crime type and count
    crime_counts = df['primary_type'].value_counts().reset_index()
    crime_counts.columns = ['crime_type', 'count']
    
    # Save as JSON
    crime_counts.to_json("crime_counts.json", orient='records')

if __name__ == "__main__":
    crime_data = fetch_crime_data()
    crime_data = preprocess_data(crime_data)
    prepare_d3_data(crime_data)