import json
import requests
from flask import request, current_app


class DsmHandler():
    def __init__(self):
        self.server = current_app.config['DSM_SERVER']
        self.page_size = current_app.config['DSM_PAGE_SIZE']

    def _make_local_filter(self):
        if 'filter' in request.query_string:
            local_filter = lambda d: d.get('connectedHost')
            for fil in filter(local_filter, json.loads(request.args['filter'])):
                a = 1

    def get_devices(self, filter=None):
        # Inside #
        self._make_local_filter()
        url_req = f"{self.server}/device_info?page[size]={self.page_size}"
        url_req += f"&{request.query_string.decode('utf-8')}" if request.query_string else ""

        res = requests.get(url_req)
        device_info = res.json()

        return device_info