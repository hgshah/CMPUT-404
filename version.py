import requests
print(requests.__version__)
req = requests.get("http://google.com/")
print(req)
print(req.text)
req1 = requests.get("https://raw.githubusercontent.com/hgshah/CMPUT-404/master/version.py")
print(req1.text)
