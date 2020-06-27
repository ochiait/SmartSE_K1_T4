import requests

url = "https://notify-api.line.me/api/notify"
access_token = '*****' # input your token
headers = {'Authorization': 'Bearer ' + access_token}

message = 'Hello LINE! This is a test for post auto-detect system.'
payload = {'message': message}

def notify():
	r = requests.post(url, headers=headers, params=payload,)
