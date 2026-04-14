import requests

payload = {
    "firstname" : "Shivam",
    "lastname" : "Test",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

resp = requests.post("https://restful-booker.herokuapp.com/booking",json=payload)
assert resp.status_code == 200
print(resp.json())