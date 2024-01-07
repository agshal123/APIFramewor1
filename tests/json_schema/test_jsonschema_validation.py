import json
import os
import pytest
from SRC.Helpers.api_requests_wrappers import post_request
from SRC.Constants.api_constants import base_url, url_create_booking
from SRC.Helpers.utils import common_headers_json
from SRC.Helpers.payload_manager import payload_create_booking
from SRC.Helpers.Common_verification import verify_response, verify_https_status_code, verify_response_body
from SRC.Helpers.jsonschema import *
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class Test_createBooking():

    def load_schema(self, schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)

    def test_create_booking_jsonschema(self):
        print(url_create_booking())
        print(common_headers_json())
        print(payload_create_booking())
        response = post_request(url=url_create_booking(), headers=common_headers_json(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        print(response)
        response_json = response.json()
        print(response_json)
        booking_id = response.json()["bookingid"]
        verify_response(response.json()["bookingid"])
        verify_https_status_code(response, 200)
        # json_schema = jsonschema_create_booking()
        file1 = os.getcwd()+"/schema.json"
        print(file1)
        json_schema = self.load_schema(file1)
        print(json_schema)
        try:
            validate(instance=response_json, schema=json_schema)
        except ValidationError as e:
            print(e.message)
