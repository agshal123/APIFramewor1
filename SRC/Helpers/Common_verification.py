# HTTPS Status Verification

def verify_https_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Expected HTTP Status Code" + str(expect_data)+"but got" + str(response_data)


def verify_json_key_for_not_null(key):
    assert key != 0, "Key is non Empty" + key
    assert key > 0, "Key is greater than zero"

def verify_response(key):
    assert key is not None, "Key is not generated"

def verify_response_time():
    pass

def verify_response_body(response,expected_value):
    assert response.text ==expected_value,"Expected value is "+ str(expected_value) +"but returned" + str(response)

def verify_response_data(response,expected_value1,expected_value2):
    assert response.json()["firstname"]==expected_value1, "data1 is incorrect"
    assert response.json()["lastname"]==expected_value2, "data2 is incorrect"






