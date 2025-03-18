import folium
from fetch_data import fetch_crime_data, preprocess_data


def create_crime_map(df):
    # Create a base map centered on Chicago
    chicago_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11)
    
    # Add crime points to the map
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=3,
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(chicago_map)
    
    # Save the map to an HTML file
    chicago_map.save("crime_map.html")

if __name__ == "__main__":
    crime_data = fetch_crime_data()
    crime_data = preprocess_data(crime_data)
    create_crime_map(crime_data)