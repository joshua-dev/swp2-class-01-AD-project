import requests
import json


def showAvailables():
    res = requests.get(
        'https://us-central1-kcc-library.cloudfunctions.net/showAvailables')
    result = res.json()
    for id in result.keys():
        val = result[id]
        for key in val.keys():
            print(f'{key}: {val[key]}')


def showNotAvailables():
    res = requests.get(
        'https://us-central1-kcc-library.cloudfunctions.net/showNotAvailables')
    result = res.json()
    for id in result.keys():
        val = result[id]
        for key in val.keys():
            print(f'{key}: {val[key]}')


def searchByTitle(title):
    requestData = {"title": title}
    requestData = json.dumps(requestData)
    print(requestData)
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByTitle'
    res = requests.get(url, params=requestData)
    result = res.json()

    for key in result.keys():
        print(f'{key}: {result[key]}')


showAvailables()
print('-' * 20)
print('-' * 20)
showNotAvailables()
print('-' * 20)
print('-' * 20)
searchByTitle('System and mechanics of Mateerisa')
