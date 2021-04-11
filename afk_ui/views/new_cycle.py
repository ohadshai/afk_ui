from flask_appbuilder import BaseView, expose, has_access

from ..extensions import db, dsm_handler
from ..models import JobType
from .utils import get_property_info, get_device_image


HW_PROP = [{"key": "4", "val": [
    {"label": "4", "value": 3.1},
    {"label": "4", "value": 3.2},
    {"label": "4", "value": 3.3},
    {"label": "4S", "value": 4.1}
]}, {"key": "5", "val": [
    {"label": "5", "value": 5.1},
    {"label": "5", "value": 5.2},
    {"label": "5C", "value": 5.3},
    {"label": "5C", "value": 5.4},
    {"label": "5S", "value": 6.1},
    {"label": "5S", "value": 6.2}
]}, {"key": "6", "val": [
    {"label": "6", "value": 7.2},
    {"label": "6 Plus", "value": 7.1},
    {"label": "6S", "value": 8.1},
    {"label": "6S Plus", "value": 8.2}
]}, {"key": "SE 1Gen", "val": [
    {"label": "SE", "value": 8.4}
]}, {"key": "7", "val": [
    {"label": "7", "value": 9.1},
    {"label": "7", "value": 9.3},
    {"label": "7 Plus", "value": 9.2},
    {"label": "7 Plus", "value": 9.4}
]}, {"key": "8", "val": [
    {"label": "8", "value": 10.1},
    {"label": "8", "value": 10.4},
    {"label": "8 Plus", "value": 10.2},
    {"label": "8 Plus", "value": 10.5},
]}, {"key": "X", "val": [
    {"label": "X", "value": 10.3},
    {"label": "X", "value": 10.6}
]}, {"key": "XR", "val": [
    {"label": "XR", "value": 11.8},
    {"label": "XR", "value": 11.2}
]}, {"key": "XS", "val": [
    {"label": "XS Max", "value": 11.6},
    {"label": "XS Max", "value": 11.4},
]}, {"key": "11", "val": [
    {"label": "11", "value": 12.1},
    {"label": "11 Pro", "value": 12.3},
    {"label": "11 Pro Max", "value": 12.5},
]}, {"key": "SE 2Gen", "val": [
    {"label": "SE", "value": 12.8},
]}, {"key": "12", "val": [
    {"label": "12 Mini", "value": 13.1},
    {"label": "12", "value": 13.2},
    {"label": "12 Pro", "value": 13.3},
    {"label": "12 Pro Max", "value": 13.4}]}

           ]


class NewCycle(BaseView):
    default_view = "new cycle"

    @expose("/")
    @has_access
    def get_page(self):
        job_types = db.session.query(JobType).all()
        job_names = [job_type.to_json()['name'] for job_type in job_types]
        # OUTSIDE
        import json
        with open('afk_ui/devices/device_info_example.json') as f:
            devices_info = json.load(f)
        # INSIDE
        # devices_info = dsm_handler.get_devices()
        # hw prop - To Be Completed
        return self.render_template("new_cycle.html", job_names=job_names, devices_info=devices_info['data'],
                                    hw_prop=HW_PROP[::-1], get_property_info=get_property_info , get_device_image = get_device_image)