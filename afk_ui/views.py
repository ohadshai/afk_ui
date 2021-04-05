import requests
from flask import render_template, current_app
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from .extensions import appbuilder, db, dsm_handler
from .models import JobType

from flask_appbuilder import BaseView, expose, has_access


TITLE_ICON_MAP = {
    "UDID": {
            "icon": "fingerprint",
            "title": "udid",
    },
    "ECDI": {
            "icon": "fingerprint",
            "title": "udid",
    },
    "name": {
            "icon": "Person",
            "title": "device name",
    },
    "connectedHost":{
            "icon": "computer",
            "title": "host ip",
    },
    "batteryCurrentCapacity":{
            "icon": "battery_charging_full",
            "title": "battery",
    },
}


def get_icon(key):
    return TITLE_ICON_MAP.get(key, None)


class NewCycle(BaseView):
    default_view = "new cycle"

    @expose("/")
    @has_access
    def get_page(self):
        # do something with param1
        # and return to previous page or index
        job_types = db.session.query(JobType).all()
        job_names = [job_type.to_json()['name'] for job_type in job_types]
        # OUTSIDE
        import json
        with open('afk_ui/devices/device_info_example.json') as f:
            devices_info = json.load(f)
        hw_prop = [{"key": "4", "val": [
            {"label": "4", "value": "3,1"},
            {"label": "4", "value": "3,2"},
            {"label": "4", "value": "3,3"},
            {"label": "4S", "value": "4,1"}
        ]}, {"key": "5", "val": [
            {"label": "5", "value": "5,1"},
            {"label": "5", "value": "5,2"},
            {"label": "5C", "value": "5,3"},
            {"label": "5C", "value": "5,4"},
            {"label": "5S", "value": "6,1"},
            {"label": "5S", "value": "6,2"}
        ]}, {"key": "6", "val": [
            {"label": "6", "value": "7,2"},
            {"label": "6 Plus", "value": "7,1"},
            {"label": "6S", "value": "8,1"},
            {"label": "6S Plus", "value": "8,2"}
        ]}, {"key": "SE 1Gen", "val": [
            {"label": "SE", "value": "8,4"}
        ]}, {"key": "7", "val": [
            {"label": "7", "value": "9,1"},
            {"label": "7", "value": "9,3"},
            {"label": "7 Plus", "value": "9,2"},
            {"label": "7 Plus", "value": "9,4"}
        ]}, {"key": "8", "val": [
            {"label": "8", "value": "10,1"},
            {"label": "8", "value": "10,4"},
            {"label": "8 Plus", "value": "10,2"},
            {"label": "8 Plus", "value": "10,5"},
        ]}, {"key": "X", "val": [
            {"label": "X", "value": "10,3"},
            {"label": "X", "value": "10,6"}
        ]}, {"key": "XR", "val": [
            {"label": "XR", "value": "11,8"},
            {"label": "XR", "value": "11,2"}
        ]}, {"key": "XS", "val": [
            {"label": "XS Max", "value": "11,6"},
            {"label": "XS Max", "value": "11,4"},
        ]}, {"key": "11", "val": [
            {"label": "11", "value": "12,1"},
            {"label": "11 Pro", "value": "12,3"},
            {"label": "11 Pro Max", "value": "12,5"},
        ]}, {"key": "SE 2Gen", "val": [
            {"label": "SE", "value": "12,8"},
        ]}, {"key": "12", "val": [
            {"label": "12 Mini", "value": "13,1"},
            {"label": "12", "value": "13,2"},
            {"label": "12 Pro", "value": "13,3"},
            {"label": "12 Pro Max", "value": "13,4"}]}

                   ]
        # INSIDE
        # devices_info = requests.get(f"{current_app.config['DSM_SERVER']}/device_info")
        # devices_info = dsm_handler.get_devices()
        # hw prop - To Be Completed
        return self.render_template("new_cycle.html", job_names=job_names, devices_info=devices_info['data'],
                                    hw_prop=hw_prop, get_icon_callback=get_icon)


class Results(BaseView):
    default_view = "results"

    @expose("/")
    @has_access
    def get_page(self):
        # do something with param1
        # and return to previous page or index
        return self.render_template("results.html")

#


"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


# db.create_all()
