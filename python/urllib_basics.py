#%%
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.parse import parse_qs # read url query strings
import json

# %%
# Send a get request
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
with urlopen(url) as response:
    # read response in bytes or load as json (json.load(())
    response_content = response.read()

# %%
# change response to string
response_content.decode('utf-8')

# %%
# Read response string a json
json.loads(response_content)

# %%
# get response headers
response.getheaders()

# %%
# get a single header
response.getheader('Content-Type')

# %%
# get the status response
response.status

# %%
# reason for response status
response.reason

# %%
# passing params on get request
params = {
    "api_jey": "DEMO_KEY",
    "date": "2020-12-09"}
query_string = urlencode(params)

# %%
# create url using base & params
base_url = "https://api.nasa.gov/planetary/apod"
new_url = "?".join([base_url, query_string])

# %%
# new get request with params on url
with urlopen(new_url) as response:
    # read response in bytes or load as json (json.load(())
    json_resp = json.load(response_content)

# %%
# send a POST request
# data must be in form of a py dict
data = {"var1": "something", "var2": "another"}
# url encode the data & also encode it to asciii
post_data = urlencode(data).encode('ascii')

# %%
# send POST request
# data must be 2nd arg in urlopen
with urlopen("https://httpbin.org/post", post_data) as response:
    j_resp = json.load(response)

# %%
# send json data
j_data = {"name": "Muzi"}
# ensure json header
custom_headers = {"Content-Type": "application/json"}

# %%
# use Request obj to send request
req = Request(
    "https://httpbin.org/post",
    json.dumps(j_data).encode("ascii"),
    custom_headers
)
# send POST request using json data
with urlopen(req) as response:
    j_response = json.load(response)

# %%
# read/parse a url query string
url_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
print(repr(url_values))
# %%
# get green value
grn = url_values.get('green', [''])
print(grn)
# %%
