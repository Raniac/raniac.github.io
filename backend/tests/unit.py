import requests
import json

def test():
    r = requests.get("http://0.0.0.0:1470/healthcheck", data=json.dumps({"data": "hello"}))
    print(r.text)

if __name__ == "__main__":
    test()
