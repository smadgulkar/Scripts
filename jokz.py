import requests

def get_dad_joke():
    resp = requests.get('https://icanhazdadjoke.com/',
                        headers={'Accept': 'text/plain'})
    return resp.content.decode('utf-8')

print(get_dad_joke())