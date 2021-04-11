import requests
from flask import request, current_app


class DsmHandler():
    def __init__(self):
        self.server = current_app.config['DSM_SERVER']
        self.page_size = current_app.config['DSM_PAGE_SIZE']

    def get_devices(self, filter=None):
        # Inside #
        url_req = f"{self.server}/device_info?page[size]={self.page_size}"
        url_req += f"&{request.query_string.decode('utf-8')}" if request.query_string else ""

        res = requests.get(url_req)
        device_info = res.json()

        return device_info