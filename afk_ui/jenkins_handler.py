import jenkins
from flask import current_app

# replace with Token in future
AUTHENTICATION_INFO = {'username': 'ohads', 'password': '1234'}


class JenkinsHandler():
    def __init__(self):
        url = current_app.config['JENKINS_URI']
        self.server = jenkins.Jenkins(url, **AUTHENTICATION_INFO)

    def get_jobs_info(self, filter=None):
        """

        :param filter: list of keys to filter
        :return:
        """
        jobs_info = self.server.get_all_jobs()
        return jobs_info

    def get_job_info(self, name):
        return self.server.get_job_info(name)




