from flask import request, Response
import requests

TITLE_ICON_MAP = {
    "UDID": {
            "icon": "fingerprint",
            "title": "udid",
    },
    "ECID": {
            "icon": "fingerprint",
            "title": "ecid",
    },
    "name": {
            "icon": "person",
            "title": "device name",
    },
    "connectedHost": {
            "icon": "computer",
            "title": "host ip",
    },
    "batteryCurrentCapacity": {
            "icon": "battery_charging_full",
            "title": "battery",
    },
}

IMAGE_MAP  = {
    "XS":"XR.jpeg",
    "XR":"XR.jpeg",
    "X":"XR.jpeg",
    "SE":"SE.jpeg",
    "11":"11.jpeg",
    "12":"12.png",
    "4": "4.jpeg",
    "5": "4.jpeg",
    "6": "6.jpeg",
    "7": "7.jpeg",
    "8": "8.jpeg"

}

def get_property_info(key):
    return TITLE_ICON_MAP.get(key, None)


def get_device_image(modelName):
    dev_image = "XR.jpeg"
    for key in IMAGE_MAP:
        if key in modelName:
            dev_image = IMAGE_MAP[key]
    return dev_image

def _proxy(new_server):
    resp = requests.request(
        method=request.method,
        url=request.url.replace(request.host_url, new_server).replace("api/v1/", ""),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response


