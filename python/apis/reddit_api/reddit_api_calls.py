#%%
import requests as r
import pandas as pd
import creds
# %%
# set auth info on requests
auth = r.auth.HTTPBasicAuth(
        creds.CLIENT_ID,
        creds.SECRET_KEY
)

data = {
    'grant_type': 'password',
    'username': creds.uname,
    'password': creds.pword
}

# set headers
headers = {'User-Agent': 'MyAPI/0.0.1'}
# %%
resp = r.post(
    'https://www.reddit.com/api/v1/access_token',
    auth=auth, data=data,headers=headers
)
# %%
TOKEN = resp.json()['access_token']
# %%
# Add token to headers
headers['Authorization'] = f"bearer {TOKEN}"
# %%
# Access subreddit
res = r.get("https://oauth.reddit.com/r/jse_bets/hot", headers=headers)
# %%
df = pd.DataFrame()

for post in res.json()['data']['children']:
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title']},
        ignore_index=True)

# %%
df
# %%
