import requests
print(requests.__version__)
req = requests.get("http://google.com/")
print(req)
print(req.text)
