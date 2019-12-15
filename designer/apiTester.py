import requests
import json


def showAll() -> None:
    url = 'https://us-central1-kcc-library.cloudfunctions.net/showAll'
    res = requests.get(url=url, params=None)

    result = res.json()
    for id in result.keys():
        val = result[id]
        for key in val.keys():
            print(f'{key}: {val[key]}')


def showAvailables() -> None:
    url = 'https://us-central1-kcc-library.cloudfunctions.net/showAvailables'
    res = requests.get(url=url, params=None)

    result = res.json()
    for id in result.keys():
        val = result[id]
        for key in val.keys():
            print(f'{key}: {val[key]}')


def showNotAvailables() -> None:
    url = 'https://us-central1-kcc-library.cloudfunctions.net/showNotAvailables'
    res = requests.get(url=url, params=None)

    result = res.json()
    for id in result.keys():
        val = result[id]
        for key in val.keys():
            print(f'{key}: {val[key]}')


def searchByTitle(title: str) -> None:
    reqData = {'title': title}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByTitle'

    res = requests.get(url=url, params=reqData)
    result = res.json()

    for key in result.keys():
        print(f'{key}: {result[key]}')


def searchByAuthor(author: str) -> None:
    reqData = {'author': author}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByAuthor'

    res = requests.get(url=url, params=reqData)
    result = res.json()

    for key in result.keys():
        print(f'{key}: {result[key]}')


def searchByPublisher(publisher: str) -> None:
    reqData = {'publisher': publisher}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByPublisher'

    res = requests.get(url=url, params=reqData)
    result = res.json()

    for key in result.keys():
        print(f'{key}: {result[key]}')


if __name__ == '__main__':
    showAll()
    print('-' * 20)
    searchByTitle('C++ Programming')
    print('-' * 20)
    searchByAuthor('Alan Walker')
    print('-' * 20)
    searchByPublisher('Wiley')
    print('-' * 20)
