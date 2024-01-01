import pytest
from SRC.Helpers.api_requests_wrappers import post_request
from SRC.Constants.api_constants import base_url,url_create_booking
from SRC.Helpers.utils import common_headers_json
from SRC.Helpers.payload_manager import payload_create_booking
from SRC.Helpers.Common_verification import verify_response,verify_https_status_code,verify_response_body

class Test_createBooking():
    @pytest.mark.positive
    def test_create_booking_tc1(self):
        print(url_create_booking())
        print(common_headers_json())
        print(payload_create_booking())
        response = post_request(url=url_create_booking(),headers=common_headers_json(),auth=None,payload=payload_create_booking(),in_json=False)
        print(response)
        booking_id=response.json()["bookingid"]
        verify_response(response.json()["bookingid"])
        verify_https_status_code(response,200)

    @pytest.mark.negative
    def test_crete_booking_tc2_NoHeaders(self):
        response= post_request(url=url_create_booking(),headers=common_headers_json(),auth=None,payload=None,in_json=False)
        verify_https_status_code(response,500)
        verify_response_body(response)

