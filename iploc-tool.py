#!/usr/bin/env python3
import requests
import pyfiglet

# Function to fetch location data
def get_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url).json()
    if response['status'] == 'success':
        return {
            'Country': response['country'],
            'City': response['city'],
            'Region': response['regionName'],
            'Latitude': response['lat'],
            'Longitude': response['lon']
        }
    else:
        return "Invalid IP address or error in fetching data."

# Function to display banner
def display_banner():
    ascii_banner = pyfiglet.figlet_format("ip-loc Tool")
    print(ascii_banner)
    print("=" * 30)
    print("Developed by Alien (unauthorised community)")
    print("=" * 30)

# Main function
def main():
    display_banner()
    while True:
        ip_address = input("\nEnter an IP address (or type 'exit' to quit): ").strip()
        if ip_address.lower() == 'exit':
            print("Exiting the tool. Goodbye!")
            break
        location = get_location(ip_address)
        if isinstance(location, dict):
            print("\nLocation Details:")
            for key, value in location.items():
                print(f"{key}: {value}")
        else:
            print(f"\nError: {location}")

# Run the tool
if __name__ == "__main__":
    main()