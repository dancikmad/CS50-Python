import requests
import json

coindesk_api = "https://api.coindesk.com/v1/bpi/currentprice.json"

def get_data(api):
    response = requests.get(api)
    data = response.json()
    json_object = json.dumps(data, indent=4)
    return json_object

def write_json(object):
    with open("coindesk_data.json", "w") as outfile:
        outfile.write(object)

def main():
    object = get_data(coindesk_api)
    write_json(object)

main()
