import requests

response = requests.get('https://api.github.com')
print(response)

if response:
    print('Success!')
else:
    print('An error has occurred.')