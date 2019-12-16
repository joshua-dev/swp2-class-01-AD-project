import requests


def showAll() -> int:
    url = 'https://us-central1-kcc-library.cloudfunctions.net/showAll'
    res = requests.get(url=url, params=None)

    result = res.json()
    for id in result.keys():
        val = result[id]
        for key in val.keys():
            print(f'{key}: {val[key]}')

    return res.status_code


def showAvailables() -> int:
    url = 'https://us-central1-kcc-library.cloudfunctions.net/showAvailables'
    res = requests.get(url=url, params=None)

    result = res.json()
    for id in result.keys():
        val = result[id]
        for key in val.keys():
            print(f'{key}: {val[key]}')

    return res.status_code


def showNotAvailables() -> int:
    url = 'https://us-central1-kcc-library.cloudfunctions.net/showNotAvailables'
    res = requests.get(url=url, params=None)

    result = res.json()
    for id in result.keys():
        val = result[id]
        for key in val.keys():
            print(f'{key}: {val[key]}')

    return res.status_code


def searchByTitle(title: str) -> int:
    reqData = {'title': title}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByTitle'

    res = requests.get(url=url, params=reqData)
    result = res.json()

    print(result)

    return res.status_code


def searchByAuthor(author: str) -> int:
    reqData = {'author': author}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByAuthor'

    res = requests.get(url=url, params=reqData)
    result = res.json()

    print(result)

    return res.status_code


def searchByPublisher(publisher: str) -> int:
    reqData = {'publisher': publisher}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByPublisher'

    res = requests.get(url=url, params=reqData)
    result = res.json()

    print(result)

    return res.status_code


def borrow(title: str) -> int:
    reqData = {'title': title}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/borrow'

    res = requests.get(url=url, params=reqData)
    result = res.json()

    for key in result.keys():
        print(f'{key}: {result[key]}')

    return res.status_code


def giveBack(title: str) -> int:
    reqData = {'title': title}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/giveBack'

    res = requests.get(url=url, params=reqData)
    result = res.json()

    for key in result.keys():
        print(f'{key}: {result[key]}')

    return res.status_code
