import requests

r = requests.post("http://127.0.0.1:5000/doit", data={"test":123})
print(r.status_code, r.reason)
