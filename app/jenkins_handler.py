import requests


JENKINS_URL = "http://localhost:8080"

# replace with Token in future
AUTHENTICATION_INFO = ('ohads', '1234')


class JenkinsHandler():
    def __init__(self, url=JENKINS_URL):
        self.url = url

    def get_jobs_info(self, filter=None):
        """

        :param filter: list of keys to filter
        :return:
        """
        res = requests.get(f"{self.url}/api/json?tree=jobs\[name,color\]", auth=AUTHENTICATION_INFO)
        if not res.ok:
            res.raise_for_status()
        jobs_info = res.json()['jobs']
        if filter:
            jobs_info = { key: jobs_info[key] for key in filter}
        return jobs_info




