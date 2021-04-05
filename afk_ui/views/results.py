from flask_appbuilder import BaseView, expose, has_access

from ..extensions import db
from ..models import Job


class Results(BaseView):
    default_view = "results"

    @expose("/")
    @has_access
    def get_page(self):
        # do something with param1
        # and return to previous page or index
        return self.render_template("results.html")


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