import requests

url = "https://notify-api.line.me/api/notify"
access_token = 'EGh4JhvwgLMF8VbVljSUWXWGcvVmPu9btFZfUvcLYtd'
headers = {'Authorization': 'Bearer ' + access_token}

message = 'You\'ve got Postal matter!'
print(message)
payload = {'message': message}

def notify():
	r = requests.post(url, headers=headers, params=payload,)