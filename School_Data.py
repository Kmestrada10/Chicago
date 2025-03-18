import pandas as pd

def load_school_data():
    # Path to the CSV file
    csv_file_path = 'static/data/Chicago_Public_Schools.csv'
    
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Select specific columns: Long_Name, School_Type, School_Latitude, School_Longitude
    selected_columns = ['Long_Name', 'School_Latitude', 'School_Longitude']
    df_selected = df[selected_columns]
    
    # Display the first few rows of the selected columns
    print("First few rows of the selected columns:")
    print(df_selected.head())
    
    # Return the DataFrame for further use (optional)
    return df_selected

# Call the function to load and display the data
if __name__ == '__main__':
    load_school_data()