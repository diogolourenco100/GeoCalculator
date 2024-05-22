from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import geocoder as gc
from colora import green, cyan, red, yellow
import pyfiglet
import time
import os

def geocalc():
    try:
        os.system("cls" if os.name == "nt" else "clear")
        geocoder = Nominatim(user_agent="Dev: Diogo S. Lourenco")

        banner = pyfiglet.figlet_format("GeoCalc", font="big")

        print("-"*38)
        print(cyan(banner))
        print(red("by Diogo S. Lourenco"))
        print("-"*38)
        print()

        print(green("Source location: "))
        location = input(green("$ ")).strip().upper()

        def auto_loc():
            g = gc.ip('me')

            city = g.city.upper()

            state = g.state.upper()

            country = g.country.upper()

            return city, state, country

        print()
        print(green("Target location: "))
        target = input(green("$ ")).strip().upper()

        if not location:
            print(red("\n* Collecting IP address..."))
            time.sleep(1)

            print(yellow("* Getting SOURCE location..."))

            location = auto_loc()

            print(green("* Location collected."))
            time.sleep(1)

        if not target:
            print(red("\n* Collecting IP address..."))
            time.sleep(1)

            print(yellow("* Getting TARGET location..."))

            target = auto_loc()

            print(green("* Location collected."))
            time.sleep(1)

        source_location = geocoder.geocode(location)
        target_location = geocoder.geocode(target)

        if source_location is None:
            print(red("There was an error in your source location. Try again."))
            return

        if target_location is None:
            print(red("There was an error in your target location. Try again."))
            return

        def get_coordinates(location):
            return (location.latitude, location.longitude)

        source_coordinates = get_coordinates(source_location)
        target_coordinates = get_coordinates(target_location)

        distance = geodesic(source_coordinates, target_coordinates).kilometers
        distance_formatted = "{:.2f}".format(distance)

        location = yellow(location)
        distance_formatted = cyan(distance_formatted)
        target = green(target)

        os.system("cls" if os.name == "nt" else "clear")
        print()
        print(f"{location} -------------- {distance_formatted} Km -------------- {target}")
 
    except Exception as e:
        os.system("cls" if os.name == "nt" else "clear")
        print(red(f"\nThere was an unexpected error. Try again.\nError: {str(e)}"))

geocalc()
