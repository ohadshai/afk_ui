from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi


from .extensions import appbuilder, db
from .models import JobType


from flask_appbuilder import BaseView, expose, has_access


class NewCycle(BaseView):
    default_view = "new cycle"

    @expose("/")
    @has_access
    def get_page(self):
        # do something with param1
        # and return to previous page or index
        job_types = db.session.query(JobType).all()
        job_names = [job_type.to_json()['name'] for job_type in job_types]
        return self.render_template("new_cycle.html", job_names=job_names)


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
