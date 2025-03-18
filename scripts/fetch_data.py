import requests
from datetime import datetime

# Chicago Data Portal API endpoint for crimes
CRIME_API_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

# Chicago Data Portal API endpoint for neighborhoods
NEIGHBORHOOD_API_URL = "https://data.cityofchicago.org/resource/9wp7-iasj.json"

def fetch_recent_crimes(limit=10):
    """
    Fetch the most recent `limit` crimes.
    """
    # Query the API for the most recent crimes
    params = {
        "$order": "date DESC",  # Sort by date in descending order (most recent first)
        "$limit": limit  # Fetch only the most recent `limit` crimes
    }
    print("Fetching the most recent crimes...")  # Debug print
    response = requests.get(CRIME_API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Fetched {len(data)} crimes.")  # Debug print
        print("Sample Data:", data[:1])  # Debug print to show a sample of the data
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def format_time(date_str):
    """
    Extract and format the time from the date string into 12-hour AM/PM format.
    """
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        # Format the time as 12-hour with AM/PM
        return date_obj.strftime("%I:%M %p")
    except ValueError:
        return "Unknown"

def get_neighborhood(latitude, longitude):
    """
    Get the neighborhood name for a given latitude and longitude.
    """
    if not latitude or not longitude:
        return "Unknown"
    
    # Query the Neighborhoods API to find the neighborhood
    params = {
        "$where": f"within_circle(shape, {latitude}, {longitude}, 100)",  # 100-meter radius
        "$limit": 1
    }
    response = requests.get(NEIGHBORHOOD_API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0].get("pri_neigh", "Unknown")
    return "Unknown"

def process_crime_data(crime_data):
    """
    Process raw crime data into a structured format.
    """
    processed_data = []
    for crime in crime_data:
        # Extract and format the time
        time_formatted = format_time(crime.get("date", ""))
        
        # Get the neighborhood name
        latitude = crime.get("latitude")
        longitude = crime.get("longitude")
        neighborhood = get_neighborhood(latitude, longitude)
        
        processed_data.append({
            "type": crime.get("primary_type", "Unknown"),
            "date": crime.get("date", "Unknown").split("T")[0],  # Extract date only
            "time": time_formatted,
            "location": neighborhood,  # Use neighborhood name instead of address
            "description": crime.get("description", "No description available")
        })
    print(f"Processed {len(processed_data)} crimes.")  # Debug print
    return processed_data