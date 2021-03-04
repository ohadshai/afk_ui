from flask import request

from flask_appbuilder.api import BaseApi, expose


class DevicesApi(BaseApi):

    resource_name = "devices"
    openapi_spec_tag = "Devices"

    @expose("/", methods=["GET"])
    def devices(self):
        """Get all devices from DSM according to filter
        ---
        get:
          description: >-
            Get all devices from DSM according to filter
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    num_devices:
                      description: Number of devices
                      example: 3
                      type: integer
                      required: true
                    filter:
                      description: filter of devices
                      type: object
                      required: true
                      properties:
                        hardware:
                          description: hardware filter object
                          type: object
                          required: false
                          properties:
                            value:
                              description: value/range of hardware
                              type: string/list
                              required: false
                              example: [XSMax,12]
                            logic:
                              description: logic of filter
                              type: string
                              required: false
                              example: range
                        software:
                          description: software filter object
                          type: object
                          required: false
                          properties:
                            value:
                              description: value/range of hardware
                              type: float/list
                              required: false
                              example: 14.1
                            logic:
                              description: logic of filter
                              type: string
                              required: false
                              example: exclude
                        pac:
                          description: hardware >= X
                          type: boolean
                          required: false
                          example: true
                        host:
                          description: host of device
                          type: string
                          required: false
                          example: 2.2.2.2
                        device_info_attribute:
                          description: any device attribute
                          type: string
                          required: false
                          example: iPhone8plus (DeviceName attribute)

          responses:
            200:
              description: all devices that qualify the filter the user sent
              content:
                application/json:
                  schema:
                    type: array
                    items:
                        type: object
                        properties:
                          hardware:
                            description: hardware of device
                            type: string
                            example: XSMax
                          software:
                            description: software of device
                            type: string
                            example: 14.1
                          host:
                            description: host of device
                            type: string
                            example: 2.2.2.2
                          device_info_attribute:
                            description: any device attribute
                            type: string
                            example: iPhone8plus (DeviceName attribute)

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
