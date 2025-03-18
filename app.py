from flask import Flask, render_template, request, jsonify
from prepare_d3_data import fetch_all_crimes, group_crimes_by_region
from School_Data import load_school_data
from crime_data import fetch_recent_crimes, process_crime_data  # Import crime-related functions

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch and process crime data
    crime_data = fetch_all_crimes()
    region_data = group_crimes_by_region(crime_data)
    
    # Pass the region data to the template
    return render_template('index.html', region_data=region_data)

# Route for school safety page
@app.route('/school-safety')
def school_safety():
    # Load school data
    school_data = load_school_data()
    
    # Convert the DataFrame to a list of dictionaries for easier use in the template
    school_data_list = school_data.to_dict(orient='records')
    
    # Fetch and process crime data from the last year
    crime_data = fetch_recent_crimes(limit=1000)  # Adjust limit as needed
    processed_crime_data = process_crime_data(crime_data)
    
    # Pass the school and crime data to the template
    return render_template('school_safety.html', school_data=school_data_list, crime_data=processed_crime_data)

# Route to handle search requests
@app.route('/search-school', methods=['GET'])
def search_school():
    # Get the search query from the request
    query = request.args.get('query', '').lower()
    
    # Load school data
    school_data = load_school_data()
    
    # Filter schools based on the query
    filtered_schools = school_data[
        school_data['Long_Name'].str.lower().str.contains(query)
    ].to_dict(orient='records')
    
    # Return the filtered schools as JSON
    return jsonify(filtered_schools)

# Other routes (shootings, crimes, etc.)
@app.route('/shootings')
def shootings():
    return render_template('shootings.html')

@app.route('/crimes')
def crimes():
    return render_template('crimes.html')

@app.route('/air-quality')
def air_quality():
    return render_template('air_quality.html')

@app.route('/public-transportation')
def public_transportation():
    return render_template('public_transportation.html')

@app.route('/business-safety')
def business_safety():
    return render_template('business_safety.html')

@app.route('/community-resources')
def community_resources():
    return render_template('community_resources.html')

if __name__ == '__main__':
    app.run(debug=True)