import sys
from io import BytesIO
from PlaceSearch import get_response_about_place, get_coordinates_place
from PIL import Image
import requests
from MapScaling import get_scale_size
toponym_to_find = " ".join(sys.argv[1:])
json_response = get_response_about_place(toponym_to_find).json()
toponym_longitude, toponym_lattitude = get_coordinates_place(json_response)
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": get_scale_size(json_response),
    "l": "map",
    "pt": ",".join([toponym_longitude, toponym_lattitude, 'pm2dgl'])
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(
    response.content)).show()
