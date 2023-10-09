import requests
from bs4 import BeautifulSoup
import csv

# URL Gismeteo for Chisinau
url = "https://www.gismeteo.ru/diary/4980/2023/9/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

try:
    # Send a GET request to the page
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for request success

    # Parse the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing weather data
    table = soup.find("table")

    # Get all rows within the table
    rows = table.find_all("tr")

    # Create a CSV file to save the data
    with open("dataset.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write headers
        csv_writer.writerow(["Day", "Temperature", "Pressure", "Cloudiness", "Wind"])

        # Loop through each row and extract data
        for row in rows:
            columns = row.find_all("td")
            if len(columns) >= 5:
                day = columns[0].text.strip()
                temperature = columns[1].text.strip()
                pressure = columns[2].text.strip()
                cloudiness_img = columns[3].find("img")
                if cloudiness_img:
                    cloudiness = "https:" + cloudiness_img.get("src")
                else:
                    cloudiness = ""
                wind = columns[5].text.strip()

                # Write data to the CSV file
                csv_writer.writerow([day, temperature, pressure, cloudiness, wind])
    print("Weather data has been saved to the dataset.csv file.")
except requests.exceptions.RequestException as e:
    print(f"Error while making the request: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
