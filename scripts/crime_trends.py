import pandas as pd
import matplotlib.pyplot as plt
from fetch_data import fetch_crime_data, preprocess_data

def plot_crime_trends(df):
    # Group by month and count crimes
    monthly_crimes = df.groupby('month').size()
    
    # Plot crime trends
    plt.figure(figsize=(10, 6))
    monthly_crimes.plot(kind='line', marker='o')
    plt.title("Crime Trends Over Time")
    plt.xlabel("Month")
    plt.ylabel("Number of Crimes")
    plt.grid(True)
    plt.savefig("crime_trends.png")
    plt.show()

if __name__ == "__main__":
    crime_data = fetch_crime_data()
    crime_data = preprocess_data(crime_data)
    plot_crime_trends(crime_data)