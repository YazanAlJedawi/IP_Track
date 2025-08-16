import ipapi 
import webbrowser 
from pprint import pprint
import socket 
from ipaddress import ip_address 
import sys
import time

def geo_data(lookup):
    try:
        ip = str(ip_address(lookup))
    except ValueError:
        print("[*] Looking up Name...")
        ip = socket.gethostbyname(lookup)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        print("[*] Looking up location data...")
        return ipapi.location(ip)
    except Exception as e:
        print(f"Error getting location data: {e}")
        sys.exit(1)

def map_feed(location_result):
    print("[*] Launching browser with location coordinates...")
    latitude = location_result["latitude"]
    longitude = location_result["longitude"]
    location_query = f"https://www.google.com/maps/search/?api=1&query={latitude}%2C{longitude}"
    time.sleep(2) 
    webbrowser.open(location_query, new=2)

def main():
    if len(sys.argv) < 3:
        print("Usage: locator [geo-data | map-feed] [IP | domain-name]")
        sys.exit(1)

    command = sys.argv[1].lower()
    target = sys.argv[2]

    data = geo_data(target)

    if command == "geo-data":
        pprint(data)
    elif command == "map-feed":
        map_feed(data)
    else:
        print("Invalid command. Use 'geo-data' or 'map-feed'")
        sys.exit(1)

if __name__ == "__main__":
    main()