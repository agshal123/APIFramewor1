from faker import Faker

faker = Faker()
def payload_create_booking():
    payload = {
    "firstname" : "Smith",
    "lastname" : "Allen",
    "totalprice" : 1000,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-01-05"
    },
    "additionalneeds" : "Lunch"
    }
    return payload

def payload_create_booking_Dynamic():
    payload = {
    "firstname" : faker.first_name(),
    "lastname" : faker.last_name(),
    "totalprice" : faker.random_int(min=100,max=1000),
    "depositpaid" : faker.boolean(),
    "bookingdates" : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-01-05"
    },
    "additionalneeds" : faker.random_element(elements=("Breakfast","Parking","Wifi"))
    }
    return payload
def payload_create_token():
    token = {
    "username" : "admin",
    "password" : "password123"
        }
    return token

def payload_update_booking():
    payload = {
    "firstname" : "Smith1",
    "lastname" : "Allen1",
    "totalprice" : 1000,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-01-05"
    },
    "additionalneeds" : "Lunch"
    }
    return payload