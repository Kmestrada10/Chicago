import requests

# Chicago Data Portal API endpoint for crimes
CRIME_API_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

# Define regions based on wards
ward_to_region = {
    40: 'Far North Side', 48: 'Far North Side', 49: 'Far North Side', 50: 'Far North Side',
    32: 'North Side', 43: 'North Side', 44: 'North Side', 46: 'North Side',
    30: 'Northwest Side', 31: 'Northwest Side', 33: 'Northwest Side', 35: 'Northwest Side',
    36: 'Northwest Side', 38: 'Northwest Side', 39: 'Northwest Side', 41: 'Northwest Side', 45: 'Northwest Side',
    24: 'West Side', 27: 'West Side', 28: 'West Side', 37: 'West Side',
    2: 'Central', 3: 'Central', 4: 'Central', 25: 'Central', 42: 'Central',
    12: 'Southwest Side', 14: 'Southwest Side', 15: 'Southwest Side', 18: 'Southwest Side', 22: 'Southwest Side', 23: 'Southwest Side',
    5: 'South Side', 6: 'South Side', 7: 'South Side', 8: 'South Side', 9: 'South Side', 10: 'South Side', 20: 'South Side', 21: 'South Side',
    13: 'Far Southwest Side', 16: 'Far Southwest Side', 17: 'Far Southwest Side', 19: 'Far Southwest Side',
    34: 'Far Southeast Side', 35: 'Far Southeast Side', 36: 'Far Southeast Side', 41: 'Far Southeast Side'
}

def fetch_all_crimes():
    """
    Fetch all crime data from the API.
    """
    # Query the API for all crimes (limit to 1000 for testing purposes)
    params = {
        "$limit": 1000  # Adjust the limit as needed
    }
    print("Fetching crime data...")  # Debug print
    response = requests.get(CRIME_API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Fetched {len(data)} crimes.")  # Debug print
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def group_crimes_by_region(crime_data):
    """
    Group crimes by region using the ward_to_region mapping.
    """
    region_counts = {}
    
    for crime in crime_data:
        ward = int(crime.get("ward", 0))  # Get the ward number
        region = ward_to_region.get(ward, "Unknown")  # Map ward to region
        
        if region not in region_counts:
            region_counts[region] = 0
        region_counts[region] += 1
    
    # Convert to a list of dictionaries for D3.js
    region_data = [{"region": region, "count": count} for region, count in region_counts.items()]
    return region_data

if __name__ == '__main__':
    # Fetch all crime data
    crime_data = fetch_all_crimes()
    
    # Group crimes by region
    region_data = group_crimes_by_region(crime_data)
    
    # Print the region data
    print("Region Data:")
    for entry in region_data:
        print(entry)