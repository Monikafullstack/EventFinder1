# EventFinder1
This README file provides an overview of the Event Finder application, its features, prerequisites, usage instructions, configuration options, contributing guidelines

Event Finder is a Python application that reads event data from a CSV file, finds nearby events based on the user's location and a specified search date, and serves the nearby events data as JSON using a local server.

## Features

- Read event data from a CSV file
- Find nearby events within a 14-day range from the search date
- Calculate the distance between the user's location and each event using the Haversine formula
- Convert nearby events data to JSON
- Serve the JSON data on a local server

## Prerequisites

- Python 3.x
- Libraries: `csv`, `math`, `requests`, `json`, `datetime`

## Usage

1. Clone the repository or download the code files.
2. Make sure you have the `Backend_dataset.csv` file in the correct location (`C:\Python Projects\EventFinder\Backend_dataset.csv`). This file should contain the event data in the following format:
    event_name,city_name,date,time,latitude,longitude
   
      Event 1,City A,2024-03-20,19:00,40.7128,-74.0060

      Event 2,City B,2024-03-25,15:30,41.8781,-87.6298

4. Open a terminal or command prompt and navigate to the project directory.
5. Run the following command to start the local server:
   This will start the local server at `http://localhost:8000`.
6. Open a web browser and visit `http://localhost:8000` to access the JSON data containing the nearby events.

## Configuration

You can modify the following parameters in the `main.py` file:

- `csv_file_path`: The path to the CSV file containing the event data.
- `user_latitude` and `user_longitude`: The latitude and longitude of the user's location.
- `search_date`: The date for which to find nearby events (in the format 'YYYY-MM-DD').

## Contributing
Contributions are welcome! If you find any issues or have suggestions for further improvements..
