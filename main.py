import csv
import math
import requests
import json
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler

def read_events_from_csv(file_path):
    """
    Read events data from a CSV file.
    """
    events = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                event_name, city_name, date, time, latitude, longitude = row
                event = {
                    'event_name': event_name,
                    'city_name': city_name,
                    'date': date,
                    'time': time,
                    'latitude': float(latitude),
                    'longitude': float(longitude)
                }
                events.append(event)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error occurred while reading CSV: {e}")
    return events

def find_nearby_events(events, user_latitude, user_longitude, search_date):
    """
    Find nearby events within a certain radius from the user's location.
    """
    try:
        search_date = datetime.strptime(search_date, '%Y-%m-%d')
        end_date = search_date + timedelta(days=14)
        nearby_events = []

        for event in events:
            event_date = datetime.strptime(event['date'], '%Y-%m-%d')
            if search_date <= event_date <= end_date:
                distance = calculate_distance(user_latitude, user_longitude, event['latitude'], event['longitude'])
                nearby_events.append({
                    'event_name': event['event_name'],
                    'city_name': event['city_name'],
                    'date': event['date'],
                    'distance_km': distance
                })

        nearby_events.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
        return nearby_events
    except ValueError:
        print("Invalid date format. Please provide date in 'YYYY-MM-DD' format.")
    except Exception as e:
        print(f"Error occurred while finding nearby events: {e}")

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two coordinates using Haversine formula.
    """
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    radius = 6371  # Earth's radius in kilometers
    distance = radius * c

    return distance

# Open the CSV file
csv_file_path = r"C:\Python Projects\EventFinder\Backend_dataset.csv"
events_data = read_events_from_csv(csv_file_path)

# Test data
user_latitude = 40.7128
user_longitude = -74.0060
search_date = '2024-03-15'

nearby_events = find_nearby_events(events_data, user_latitude, user_longitude, search_date)

# Convert nearby events data to JSON
json_data = json.dumps(nearby_events)

# Create a simple HTTP request handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json_data.encode())

# Start the local server
server_address = ('localhost', 8000)
httpd = HTTPServer(server_address, RequestHandler)
print(f'Starting local server at http://{server_address[0]}:{server_address[1]}')

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
    print('Server stopped')