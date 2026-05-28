import requests

try:
    r = requests.get("https://newsdata.io/api/1/news?apikey=pub_dae6d697dfed43c1b007d6a203faf607&country=us")
    print("Status:", r.status_code)
    print("Length:", len(r.text))
    print(r.text[:300])
except Exception as e:
    print("Error:", e)
