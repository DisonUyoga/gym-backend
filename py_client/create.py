import requests



endpoint="http://localhost:8000/api/users/"

data={
  "name":"Jordyn",
  "email":"jordyn233@gmail.com",
  "password1":"disonnnnnnn123",
  "password2":"disonnnnnnn123",
  "member_type":"premium"

}

response=requests.post(endpoint, json=data)

print(response.json())