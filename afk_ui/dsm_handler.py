import requests
from flask import request
from .utils import _proxy


class DsmHandler():
    def __init__(self, server=None):
        from .extensions import config
        self.server = server or config.get('DSM_SERVER')

    def get_devices(self, filter=None):
        import json
        with open('afk_ui/devices/device_info_example.json') as f:
            device_info = json.load(f)
        # Inside #

        # url_req = (f"{self.server}/device_info
        # if request.query_string:
        #     url_req+= f"?{request.query_string.decode('utf-8')}"
        # device_info = requests.get(url_req)
        return device_info