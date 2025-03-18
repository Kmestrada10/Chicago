import pandas as pd
from fetch_data import fetch_crime_data, preprocess_data

def calculate_statistics(df):
    # Total crimes this month
    current_month = df['month'].max()
    total_crimes = df[df['month'] == current_month].shape[0]
    
    # Most common crime type
    common_crime = df['primary_type'].mode()[0]
    
    # Most dangerous neighborhoods (by crime count)
    dangerous_neighborhoods = df['community_area'].value_counts().idxmax()
    
    # Crime rate change from last month
    previous_month = current_month - 1
    current_month_crimes = df[df['month'] == current_month].shape[0]
    previous_month_crimes = df[df['month'] == previous_month].shape[0]
    
    # Handle division by zero
    if previous_month_crimes == 0:
        crime_rate_change = 0  # No change if no crimes in the previous month
    else:
        crime_rate_change = ((current_month_crimes - previous_month_crimes) / previous_month_crimes) * 100
    
    return {
        "total_crimes": total_crimes,
        "common_crime": common_crime,
        "dangerous_neighborhoods": dangerous_neighborhoods,
        "crime_rate_change": crime_rate_change
    }

if __name__ == "__main__":
    crime_data = fetch_crime_data()
    crime_data = preprocess_data(crime_data)
    stats = calculate_statistics(crime_data)
    print(stats)