#Common Headers
import requests
def common_headers_json():
    headers = {
        "Content-Type": "application/json",
    }
    return headers

def common_headers_xml():
    headers = {
        "Content-Type": "application/xml",
    }
    return headers

def delete_update_headers():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers
