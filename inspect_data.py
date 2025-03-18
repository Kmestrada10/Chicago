import requests

# Chicago Data Portal API endpoint for crimes
CRIME_API_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

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

def inspect_data(data):
    """
    Inspect the structure and content of the fetched data.
    """
    if not data:
        print("No data to inspect.")
        return
    
    # Print the keys of the first record
    print("\nKeys in the first record:")
    print(data[0].keys())
    
    # Print the structure of the first record
    print("\nStructure of the first record:")
    for key, value in data[0].items():
        print(f"{key}: {value}")
    
    # Print sample records
    print("\nSample records:")
    for i, record in enumerate(data[:5]):  # Print the first 5 records
        print(f"\nRecord {i + 1}:")
        for key, value in record.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    # Fetch all crime data
    crime_data = fetch_all_crimes()
    
    # Inspect the data
    inspect_data(crime_data)