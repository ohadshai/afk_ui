from flask import request, make_response, jsonify
from flask_appbuilder.api import BaseApi, expose

from afk_ui.models import JobType


class JobsApi(BaseApi):
    resource_name = "jobs"
    openapi_spec_tag = "Jobs"

    # def add_apispec_components(self, api_spec):
    #     super(SecurityApi, self).add_apispec_components(api_spec)
    #     jwt_scheme = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    #     api_spec.components.security_scheme("jwt", jwt_scheme)
    #     api_spec.components.security_scheme("jwt_refresh", jwt_scheme)

    @expose("/results/summary/", methods=["GET"])
    def results_summary(self):
        """Get all job's results from SQL DB according to filter json in body
        ---
        get:
          description: >-
            Get all job's results from SQL DB according to filter json in body
          requestBody:
            description: filter jobs json
            required: false
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    job_id:
                      description: Id of Job
                      example: 6e4fd45a93e0
                      type: string
                      required: false
                    page:
                      description: number of page (for pagination)
                      example: 2
                      type: integer
                      required: false
                    page_block:
                      description: number of rows per page (for pagination)
                      example: 20
                      type: integer
                      required: false
                    job_type:
                      description: job type
                      example: PE
                      type: string
                      required: false
                      enum:
                      - PE
                      - RCE
                      - DEV
                      - QA
                    status:
                      description: status of job
                      example: running
                      type: string
                      required: false
                      enum:
                      - pending
                      - running
                      - passed
                      - failed
                      - cancelled
                      - internal_error
                    user:
                      description: name of job's submitter
                      example: john
                      type: string
                      required: false
                    date:
                      description: datetime job was launched
                      example: "2021-01-07 15:06:46"
                      type: Datetime
                      required: false
          responses:
            200:
              description: jobs summary
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      job_type:
                        description: job type
                        example: running
                        type: string
                      job_id:
                        type: Id of job
                        example: 6e4fd45a93e0
                        type: string
                      user:
                        description: name of job's submitter
                        example: john
                        type: string
                      status:
                        description: status of job
                        example: running
                        type: string
                      date:
                        description: datetime job was launched
                        example: "2021-01-07 15:06:46"
                        type: Datetime
                      total_tests:
                        description: number tests to run
                        example: 500
                        type: integer
                      success_tests:
                        description: number successful tests
                        example: 100
                        type: integer
                      failed_tests:
                        description: number failed tests
                        example: 20
                        type: integer
                      pending_tests:
                        description: number pending tests
                        example: 370
                        type: integer
                      crashed_tests:
                        description: number tests with crash
                        example: 10
                        type: integer
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
        """
        if not request.is_json:
            return self.response_400(message="Request payload is not JSON")
        resp = dict()
        return self.response(200, **resp)

    @expose("/results/summary/<job_id>", methods=["POST"])
    def update_summary(self, job_id):
        """update specific job in SQL DB according to json
        ---
        post:
          description: >-
            update specific job according json
          parameters:
          - in: path
            schema:
              type: string
            name: job_id
            required: true
          requestBody:
            description: update job json
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    status:
                      description: status of job
                      example: running
                      type: string
                      required: false
                    device_id:
                      description: device id (udid/other identifier)
                      type: string
                      required: false
          responses:
              200:
                description: Update job success
                content:
                  application/json:
                    schema:
                      type: object
                      properties:
                        message:
                          description: success message of update job
                          type: string
                          example: "Update job was successful"
              404:
                $ref: '#/components/responses/404'
              500:
                $ref: '#/components/responses/500'
        """
        if not request.is_json:
            return self.response_400(message="Request payload is not JSON")
        resp = dict()
        return self.response(200, **resp)

    @expose("/results/subjobs/", methods=["GET"])
    def results_subjobs(self):
        """Get all subjobs results from ELK according to filter json in body
        ---
        get:
          description: >-
            Get all job's results from ELK according to filter json in body
          requestBody:
            description: filter jobs json
            required: false
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    job_id:
                      description: Id of Job
                      example: 6e4fd45a93e0
                      type: string
                      required: false
                    sub_job_id:
                      description: Id of SubJob
                      example: 564fdcdfe932
                      type: string
                      required: false
                    page:
                      description: number of page (for pagination)
                      example: 2
                      type: integer
                      required: false
                    page_block:
                      description: number of rows per page (for pagination)
                      example: 20
                      type: integer
                      required: false
                    job_type:
                      description: job type
                      example: PE
                      type: string
                      required: false
                      enum:
                      - PE
                      - RCE
                      - DEV
                      - QA
                    status:
                      description: status of job
                      example: running
                      type: string
                      required: false
                      enum:
                      - pending
                      - running
                      - passed
                      - failed
                      - cancelled
                      - internal_error
                    user:
                      description: name of job's submitter
                      example: john
                      type: string
                      required: false
                    date:
                      description: datetime job was launched
                      example: "2021-01-07 15:06:46"
                      type: Datetime
                      required: false
          responses:
              200:
                description: subjobs information
                content:
                  application/json:
                    schema:
                      type: array
                      items:
                          type: object
                          properties:
                            job_type:
                              description: job type
                              example: running
                              type: string
                            job_id:
                              description: Id of job
                              example: 6e4fd45a93e0
                              type: string
                            subjob_id:
                              description: Id of Subjob
                              example: 6e4fd45a93e0
                              type: string
                            user:
                              description: name of job's submitter
                              example: john
                              type: string
                            status:
                              description: status of subjob
                              example: running
                              type: string
                            date:
                              description: datetime job was launched
                              example: "2021-01-07 15:06:46"
                              type: Datetime
                            results:
                              type: array
                              items:
                                  description: run_results of subjob
                                  type: object
                                  properties:
                                    number_test:
                                      description: number of run inside of subjob
                                      example: 2
                                      type: integer
                                    test_name:
                                      description: test name
                                      example: test_rce
                                      type: string
                                    status:
                                      description: status of run
                                      example: failed
                                      type: string
                                    error_reason:
                                      description: reason for error in test(if necessary)
                                      example:
                                      type: string
                                    xxx_session_link:
                                      description: xxx session link for this run
                                      example: http://xxxx
                                      type: string
                                    xxx_result:
                                      description: xxx result for this run
                                      type: object
                                    crash_link:
                                      description: xxx crash link for this run (if exists)
                                      example: http://xxxx
                                      type: string
                                    console_log_link:
                                      description: xxx console log link for this run (if exists)
                                      example: http://xxxx
                                      type: string


              400:
                $ref: '#/components/responses/400'
              401:
                $ref: '#/components/responses/401'
              500:
                $ref: '#/components/responses/500'
        """

    @expose("/run", methods=["POST"])
    def run(self):
        """
            Run job with config json through REST of Jenkins Create random job id
        ---
        post:
          description: >-
            Run job with config json through REST of Jenkins. Create random job id
          requestBody:
            description: job config - config of all subjobs
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    device_filter:
                      description: filter of devices with number of devices
                      type: object
                      properties:
                        hardware:
                          description: hardware unit/range of devices
                          type: string
                          example: "> XS Max"
                        software:
                          description: software unit/range of devices
                          type: string
                          example: "> 14.1"
                        user:
                          description: user name (to get user's host devices)
                          type: string
                          example: "john"
                        pac:
                          description: if device is under/above 'X' hardware
                          type: boolean
                          example: true
                    test_params:
                        description: tests parameters for each filter
                        type: object
                        properties:
                          test_repo_info:
                            description: test repository information
                            type: object
                            properties:
                                test_repo_path:
                                  description: test repository path
                                  type: string
                                  example: "http://gitlab/pe/tests"
                                branch:
                                  description: test repository branch
                                  type: string
                                  example: "master"
                                commit:
                                  description: test repository commit
                                  type: string
                                  example: "a30c49a033d625aabbb3e26025fd"
                          url:
                            description: host
                            type: string
                            example: "2.2.2.2"
                          tool_type:
                            description: tool type to run
                            type: string
                            example: "Persistent"


          responses:
            200:
              description: Submittion Success
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        description: success message
                        type: string
                        example: "Run submittion ended successfully"
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
        """
        resp = {}
        return self.response(200, **resp)

    @expose("/cancel/<job_id>", methods=["POST"])
    def cancel(self, job_id):
        """
            Cancel specific job by id through REST of Jenkins
        ---
        post:
          description: >-
            Cancel specific job by id through REST of Jenkins
          parameters:
          - in: path
            schema:
              type: string
            name: job_id
          responses:
            200:
              description: cancel success
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        description: success message of cancel job
                        type: string
                        example: "Cancel Job succeeded"
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
          security:
            - jwt_refresh: []
        """
        resp = {}
        return self.response(200, **resp)

    @expose("/download_artifacts/<job_id>", methods=["GET"])
    def download_artifacts(self, job_id):
        """
            Download all artifacts of job by id from JFrog
        ---
        get:
          description: >-
            Download all artifacts of job by id from JFrog
          parameters:
          - in: path
            schema:
              type: string
            name: job_id
          responses:
            200:
              description: download success
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        description: message success of download artifact
                        type: string
                        example: "Download artifact ended successfully"
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
        """
        resp = {}
        return self.response(200, **resp)

    @expose("/types", methods=["GET"])
    def job_types(self):
        from afk_ui.extensions import db
        job_types = db.session.query(JobType).all()
        job_types_list = [job_type.to_json() for job_type in job_types]
        _ret_json = jsonify(job_types_list)
        resp = make_response(_ret_json, 200)
        resp.headers["Content-Type"] = "application/json; charset=utf-8"
        return resp
