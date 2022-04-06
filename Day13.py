import json
import requests
name=input("enter your name: ")
url="https://api.agify.io?name="+name
response = requests.get(url)
if response.status_code==200:
    data_from_json=response.json()
    print(data_from_json)
    with open("data_from_url.json", mode="w") as fout:
        json.dump(data_from_json, fout)
else:
    print('there is no name...')
    pass


