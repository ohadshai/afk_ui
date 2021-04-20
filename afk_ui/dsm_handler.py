import json
import requests
from flask import request, current_app


class DsmHandler():
    def __init__(self):
        self.server = current_app.config['DSM_SERVER']
        self.page_size = current_app.config['DSM_PAGE_SIZE']
        self.query_dict_base = {'page[size]': self.page_size}

    def _check_for_host_filter(self, query_dict):
        if 'connectedHost' in query_dict.get('filter', ""):
            filters = []
            for _filter in json.loads(query_dict['filter']):
                if _filter['name'] == 'connectedHost':
                    _filter['val'] = request.remote_addr
                filters.append(_filter)
            query_dict['filter'] = json.dumps(filters)

    def get_devices(self):
        # Inside #
        query_dict = dict(self.query_dict_base, **request.args.to_dict())
        self._check_for_host_filter(query_dict)
        base_url = f"{self.server}/device_info?"
        url_req = base_url + '&'.join(['%s=%s' % (key, value) for (key, value) in query_dict.items()])
        a = 1
        # res = requests.get(url_req)
        # device_info = res.json()
        #
        # return device_info