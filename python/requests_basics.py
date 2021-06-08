#================
# Install
#=========
#python -m pip install requests

# %%
import requests

# %%
response = requests.get("https://randomuser.me/api/")
print(f"Response Status Code: {response.status_code}")
print(f"Response Reason: {response.reason}")
print(f"Response Headers: {response.headers}")
print(f"Response Text: {response.text}")

# %%
# Info on initial request
request = response.request
print(f"Request url: {request.url}")
print(f"Request path: {request.path_url}")
print(f"Request method: {request.method}")
print(f"Request headers: {request.headers}")

# Headers
# Get content type
# %%
response.headers.get("Content-Type")

# %%
# Send custom headers
headers = {"X-Request-Id": "<my-request-id>"}
response = requests.get("https://example.org", headers=headers)
response.request.headers
# %%


# %%
# Response Content
# User .text for text data & .content for everything else
response = requests.get("http://placegoat.com/200/200")
print(response.headers.get("Content-Type"))
# print(response.content)

# Write the response content to a file
with open("goat.jpeg", "wb") as file:
    file.write(response.content)


# %%
# Use built-in json() method to serialise json data into python object
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
print(response.headers.get("Content-Type"))
print(type(response.json()))
response.json()

# %%
# HTTP Methods
requests.post("https://api.thedogapi.com/v1/breeds/1")
requests.get("https://api.thedogapi.com/v1/breeds/1")
requests.put("https://api.thedogapi.com/v1/breeds/1")
requests.delete("https://api.thedogapi.com/v1/breeds/1")

# %%
# Query paramters

# Normal way of adding params
requests.get("https://randomuser.me/api/?gender=female&nat=de")

# Better way
query_params = {"gender": "female", "nat": "de"}
requests.get("https://randomuser.me/api/", params=query_params)

# RECOMMENDED WAY
query_params = {"q": "labradoodle"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
requests.get(endpoint, params=query_params)