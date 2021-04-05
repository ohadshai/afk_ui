import requests
from flask import request, current_app


class DsmHandler():
    def __init__(self):
        self.server = current_app.config['DSM_SERVER']
        self.page_size = current_app.config['DSM_PAGE_SIZE']

    def get_devices(self, filter=None):
        import json
        with open('afk_ui/devices/device_info_example.json') as f:
            device_info = json.load(f)
        # Inside #

        # url_req = (f"{self.server}/device_info
        # if request.query_string:
        #     url_req+= f"?{request.query_string.decode('utf-8')}"
        # url_req += f"page[size]={self.page_size}"
        # device_info = requests.get(url_req)
        return device_info