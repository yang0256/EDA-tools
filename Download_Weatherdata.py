import csv
import requests

def download_weather_data(city, data_type, row_limit):
    # The data to be submitted with the form
    form_data = {
        'formdata': 'ok',
        'type': data_type,
        'limit': str(row_limit),
        'submit': 'Download'
    }
    
    # Web server URL to download the weather data
    url = f"https://{city}.weatherstats.ca/download.html"
    
    # Send a POST request to the URL to retrieve the CSV file data
    response = requests.post(url, data=form_data)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the CSV file data to a file
        filename = f"weatherstats_{city}_{data_type}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for line in response.text.strip().split("\n"):
                writer.writerow(line.split(","))
        print(f"CSV file saved to {filename}.")
    else:
        print("Error: Could not retrieve CSV file.")
        
# Prompt the user for the city name, data type, and row limit
city = input("Enter the name of the city (e.g. victoria): ")
data_type = input("Enter the data type (e.g. daily, hourly, normal_daily): ")
row_limit = int(input("Enter the row limit: "))

# Call the download_weather_data function with the user input
download_weather_data(city, data_type, row_limit)
