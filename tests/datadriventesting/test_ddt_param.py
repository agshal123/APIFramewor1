import openpyxl
import requests
import pytest
from SRC.Helpers.api_requests_wrappers import *
from SRC.Constants.api_constants import *
from SRC.Helpers.utils import *


def read_credentials_from_excel(file_path):
    credentials =[]
    workbook = openpyxl.load_workbook(file_path)
    sheet= workbook.active

    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credentials.append({"username": username,"password":password})
    return credentials

def make_request_auth(username,password):
    payload = {
    "username" : "username",
    "password" : "password"
        }
    response = requests.post(url=url_create_token(),headers=common_headers_json(),auth=None,json=payload)
    return response

@pytest.mark.parametrize("user_cred",read_credentials_from_excel("C:\\Users\\gupta\\PycharmProjects\\APIFramewor1\\tests\\datadriventesting\\testdata_ddt.xlsx"))
def test_post_create_token(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print (username,password)
    response = make_request_auth(username,password)
    print (response.json())
    for key,value in response.json().items():
        print(key,value)
        if username=="admin" and password=="password123" and key=="token":
            print("valid username/password")
        else:
            print("invalid username/password")



