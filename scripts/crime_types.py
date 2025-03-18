import pandas as pd
import matplotlib.pyplot as plt
from fetch_data import fetch_crime_data, preprocess_data

def plot_crime_types(df):
    # Count crime types
    crime_counts = df['primary_type'].value_counts()
    
    # Pie chart
    plt.figure(figsize=(8, 8))
    crime_counts.head(10).plot(kind='pie', autopct='%1.1f%%')
    plt.title("Top 10 Crime Types")
    plt.savefig("crime_types_pie.png")
    plt.show()
    
    # Bar graph
    plt.figure(figsize=(10, 6))
    crime_counts.head(10).plot(kind='bar')
    plt.title("Top 10 Crime Types")
    plt.xlabel("Crime Type")
    plt.ylabel("Number of Crimes")
    plt.savefig("crime_types_bar.png")
    plt.show()

if __name__ == "__main__":
    crime_data = fetch_crime_data()
    crime_data = preprocess_data(crime_data)
    plot_crime_types(crime_data)