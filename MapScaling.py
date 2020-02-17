def get_scale_size(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_envelope = toponym["boundedBy"]["Envelope"]["lowerCorner"]
    lower_corner = [float(el) for el in toponym_envelope.split()]
    upper_corner = [float(el) for el in toponym_envelope.split()]
    size = abs(upper_corner[0] - lower_corner[0]), abs(upper_corner[1] - lower_corner[1])
    return ",".join(map(str, size))