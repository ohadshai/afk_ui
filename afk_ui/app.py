import os
from flask import Flask
from elasticapm.contrib.flask import ElasticAPM

from log import configure_logger
from .security import AfkUiSecurityManager
from .index import AfkUiIndexView

from .extensions import db, appbuilder
from .jenkins_handler import JenkinsHandler


from .devices.api import DevicesApi
from .jobs.api import JobsApi


def create_app() -> Flask:
    app = Flask(__name__)

    try:
        app = Flask(__name__)
        load_config(app)
        apm = ElasticAPM(app)
        configure_logger(app, apm)

        # Allow user to override our config completely
        # config_module = os.environ.get("AFK_UI_CONFIG", "superset.config")
        # app.config.from_object(config_module)

        app_initializer = app.config.get("APP_INITIALIZER", AfkUiAppInitializer)(app)
        app_initializer.init_app()

        return app

    # Make sure that bootstrap errors ALWAYS get logged
    except Exception as ex:
        app.logger.exception("Failed to create app")
        raise ex


def load_config(app):
    env = os.environ.get('FLASK_ENV', 'production')
    config_obj = ''.join(['config.', env.capitalize(), 'Config'])
    app.config.from_object(config_obj)


class AfkUiAppInitializer:
    def __init__(self, app: Flask) -> None:
        self.app = app
        self.config = app.config

    def pre_init(self) -> None:
        """
        Called before all other init tasks are complete
        """
        pass

    def post_init(self) -> None:
        """
        Called after any other init tasks
        """
        pass

    def init_app(self) -> None:
        """
        Main entry point which will delegate to other methods in
        order to fully init the app
        """
        self.pre_init()
        # self.setup_db()
        with self.app.app_context():
            self.setup_db()
            self.configure_fab()
            self.init_views()
        self.post_init()

    def setup_db(self):
        from .models import JobType
        print ("setup db")
        db.init_app(self.app)
        db.create_all()
        jenkins_handler = JenkinsHandler()
        if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
            jobs_info = jenkins_handler.get_jobs_info()
            for job_info in jobs_info:
                job_name = job_info['name'].lstrip('afk_')
                existing_job_type = db.session.query(JobType).filter(JobType.name == job_name).one_or_none()
                if existing_job_type:
                    # TO BE DONE - get jobs parameters
                    pass
                    # job_keys = existing_job_type.to_json().keys() & job_info.keys()
                    # job_keys = list(filter(lambda x: x not in ('id', 'name'), job_keys))
                    # if job_keys:
                    #     job_type_update = {key: job_info.get(key, None) for key in job_keys}
                    #     existing_job_type.__dict__.update(job_type_update)
                else:
                    job_type = JobType(name=job_name, test_params=None, results_params=None)
                    db.session.add(job_type)
                db.session.commit()

    def configure_fab(self) -> None:
        appbuilder.indexview = AfkUiIndexView
        appbuilder.base_template = "baselayout.html"
        appbuilder.security_manager_class = AfkUiSecurityManager
        appbuilder.init_app(self.app, db.session)

    def init_views(self) -> None:
        from .views import NewCycle, Results

        appbuilder.add_view_no_menu(NewCycle())
        appbuilder.add_view_no_menu(Results())
        appbuilder.add_link("New Cycle", icon="fa fa-tasks", href="/newcycle")
        appbuilder.add_link("Results", icon="fa fa-table", href="/results")

        appbuilder.add_api(DevicesApi)
        appbuilder.add_api(JobsApi)