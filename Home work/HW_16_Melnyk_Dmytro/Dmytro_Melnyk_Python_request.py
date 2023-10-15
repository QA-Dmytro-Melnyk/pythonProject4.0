import requests
import json

print(70*'-')
print('Ex. Auth - CreateToken')

url = "https://restful-booker.herokuapp.com/auth"

payload = json.dumps({
  "username": "admin",
  "password": "password123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


print(70*'-')
print('Ex. Booking - GetBookingIds')

url = "https://restful-booker.herokuapp.com/booking"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


print(70*'-')
print('Ex. Booking - GetBooking')

url = "https://restful-booker.herokuapp.com/booking/807"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

print(70*'-')
print('Ex. Booking - CreateBooking')

url = "https://restful-booker.herokuapp.com/booking"

payload = json.dumps({
  "firstname": "Jim",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

print(70*'-')
print('Ex. Booking - UpdateBooking')

url = "https://restful-booker.herokuapp.com/booking/3102"

payload = json.dumps({
  "firstname": "James",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Cookie': 'token=<token_value>',
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)


print(70*'-')
print('Ex. Booking - PartialUpdateBooking')

url = "https://restful-booker.herokuapp.com/booking/1357"

payload = json.dumps({
  "firstname": "James",
  "lastname": "Brown"
})
headers = {
  'Cookie': 'token=<token_value>',
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)

print(70*'-')
print('Ex. Booking - DeleteBooking')

url = "https://restful-booker.herokuapp.com/booking/1?id=4085"

payload = {}
headers = {
  'Cookie': 'token=<token_value>',
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

print(70*'-')
print('Ex. Ping - HealthCheck')

url = "https://restful-booker.herokuapp.com/ping"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)