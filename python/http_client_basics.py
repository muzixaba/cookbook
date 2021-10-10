import http.client

conn = http.client.HTTPSConnection("www.example.com")
payload = ''
headers = {
  'x-access-token': 'my-example-access-token-1234',
  'Content-Type': 'application/json'
}
conn.request("GET", "/api/endpoint", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


#------------------------
# API REQUEST COMPONENTS
#------------------------

# 1: The endpoint
url = "example.com/path"

# 2: HTTP method
# GET, PUT, POST, DELETE, PATCH

# 3: Headers
# "Application-Type: json", 

# 4: Body
{"id": 3, "name": "Muzi"}