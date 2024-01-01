from SRC.Helpers.api_requests_wrappers import *
from SRC.Constants.api_constants import *
from SRC.Helpers.payload_manager import *
from SRC.Helpers.utils import *
from SRC.Helpers.Common_verification import *
import pytest


class TestCreateBooking():

    @pytest.mark.positive
    def test_create_token(self):
        response = post_request(url=url_create_token(),headers=None,auth=None,payload=payload_create_token(),in_json=False)
        print(response.json())
        verify_response(response.json()["token"])
        verify_https_status_code(response,200)
        token = response.json()["token"]
        return token

    def test_create_booking(self):
        response = post_request(url_create_booking(),headers=common_headers_json(),auth=None,payload=payload_create_booking_Dynamic(),in_json=False)
        verify_https_status_code(response,200)
        bookingid=response.json()["bookingid"]
        print(bookingid)
        return bookingid

    def test_get_booking(self):
        bookingid=self.test_create_booking()
        print (bookingid)
        response = get_request(url_patch_put_delete_booking(bookingid),headers=None,auth=None,in_json=False)
        print(response.json())
        verify_https_status_code(response,200)

    def test_delete_booking(self):
        bookingid = self.test_create_booking()
        print(bookingid)
        # token = self.test_create_token()
        # print(token)
        response = delete_request(url=url_patch_put_delete_booking(bookingid),headers=delete_update_headers(),auth=None,in_json=False)
        print(url_patch_put_delete_booking(bookingid))
        print(delete_update_headers())
        verify_response_body(response,"Created")


    def test_update_booking(self):
        bookingid=self.test_create_booking()
        url = url_patch_put_delete_booking(bookingid)
        print(bookingid)
        print(url)
        response = put_request(url=url,headers=delete_update_headers(),auth=None,payload=payload_update_booking(),in_json=False)
        print (response.json()["firstname"])
        verify_https_status_code(response,200)
        verify_response_data(response,"Smith1","Allen1")


