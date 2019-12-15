import requests

res = requests.get(
    'https://us-central1-kcc-library.cloudfunctions.net/showAll')

result = res.json()

for key in result.keys():
    val = result[key]
    for k in val.keys():
        print(f'{k}: {val[k]}')
