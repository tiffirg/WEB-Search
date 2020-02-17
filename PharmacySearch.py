import requests
import sys
from PlaceSearch import get_response_about_place, get_coordinates_place
from MapScaling import get_scale_size
from PlaceSearch import get_response_about_place
toponym_to_find = sys.argv[1:]
json_response = get_response_about_place(toponym_to_find).json()
coordinates = get_coordinates_place(json_response)
search_api_server = "https://search-maps.yandex.ru/v1/"
lang = "ru_RU"
type = "biz"
search_place = "аптека"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
search_params = {
    "apikey": api_key,
    "text": search_place,
    "lang": lang,
    "ll": coordinates,
    "type": type
}
response = requests.get(search_api_server, params=search_params)
if not response:
    pass