import requests

email = "tsarev.zakaz4ik@mailforspam.net"
url = f"https://api.mailforspam.net/?to={email}"

response = requests.get(url)
data = response.json()

if data.get("success"):
    print(f"Có {data['count']} письма:")
    for email in data["data"]:
        print(email["subject"])