def base_url():
    base_url = "https://restful-booker.herokuapp.com"
    return base_url


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_patch_put_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)


class API_Constants():

    @staticmethod
    def base_url():
        base_url = "https://restful-booker.herokuapp.com"
        return base_url

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    def url_patch_put_delete_booking(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
