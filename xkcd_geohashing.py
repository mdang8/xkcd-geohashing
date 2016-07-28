import sys
import hashlib
import requests
import math


## gets the MD5 sum of a given string 'str'
def get_MD5_sum(str):
    md5_sum = hashlib.md5(str).hexdigest()

    return md5_sum


## splits a MD5 sum string 'str' in half
def split_md5_sum(str):
    half_1 = str[:16]
    half_2 = str[16:]

    # checks that both halves have equal lengths of 16
    if not len(half_1) == len(half_2) == 16:
        raise ValueError("Length of MD5 sum halves are not 16.")

    return [half_1, half_2]


## converts the two halves of an MD5 sum to decimal
def convert_halves_decimal(halves):
    decimal_halves = []

    # converts each half of the MD5 sum to decimal
    for half in halves:
        half = float.fromhex('0.' + half)
        decimal_halves.append(half)

    return decimal_halves


## gets the latitude longitude coordinates of a given city string
def get_coords_city(city):
    if len(city.split(', ')) != 2:
        raise ValueError("Invalid city value.")

    # splits a city location by the comma delimiter
    location_split = city.split(', ')
    city = location_split[0]
    state_country = location_split[1]

    # replaces any spaces in the city to '+' for use in GET request URL
    if ' ' in city:
        city.replace(' ', '+')

    # replaces any spaces in the state/country to '+' for use in GET request URL
    if ' ' in state_country:
        state_country.replace(' ', '+')

    # sends a GET request to Google's Geocoding API
    res = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='
        + city + ',+' + state_country)

    res_json = res.json()
    coordinates = res_json['results'][0]['geometry']['location']

    return [coordinates['lat'], coordinates['lng']]


## gets the destination coordinates by appending the integer portion of the location
## coordinates to the decimal hash values
def get_destination(location, decimals):
    if not len(location) == len(decimals) == 2:
        raise ValueError("Length of location coordinates or decimals are not 2.")

    dest_coords = []

    # floors the coordinates to get the integer portions
    location_int_lat = math.floor(location[0])
    location_int_lng = math.floor(location[1])

    dest_coords.append(location_int_lat + decimals[0])
    dest_coords.append(location_int_lng + decimals[1])

    return dest_coords


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("Invalid number of arguments. You must pass ONE argument.")
    else:
        md5_sum = get_MD5_sum(sys.argv[1])
        md5_halves = split_md5_sum(md5_sum)
        decimal_halves = convert_halves_decimal(md5_halves)
        coordinates = get_coords_city(sys.argv[2])
        dest_coords = get_destination(coordinates, decimal_halves)
        print 'Destination Coordinates: (' + str(dest_coords[0]) + ', ' + str(dest_coords[1]) + ')'