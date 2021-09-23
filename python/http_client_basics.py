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