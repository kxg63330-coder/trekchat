import requests

try:
    r = requests.get("https://www.google.com")
    print("Status:", r.status_code)
    print("Length:", len(r.text))
except Exception as e:
    print("Error:", e)
