import requests
import json

base_url = "https://tools.keycdn.com/geo.json?host={}"
ip = input("Please input ip to search\n")
url = base_url.format(ip)

r = requests.get(url)

result = json.loads(r.text)

print("\nIP searched for: {}".format(result['data']['geo']['host']))
print("Country: {}".format(result['data']['geo']['country_name']))
print("Region: {}".format(result['data']['geo']['region_name']))
print("City: {}".format(result['data']['geo']['city']))
print("ISP: {}".format(result['data']['geo']['isp']))
print("Latitude: {}".format(result['data']['geo']['latitude']))
print("Longitude: {}".format(result['data']['geo']['longitude']))