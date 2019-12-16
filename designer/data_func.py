import requests
import json
from library import *


def showAll(self):
    res = requests.get(
        'https://us-central1-kcc-library.cloudfunctions.net/showAll')
    result = res.json()
    showData(self, result)


def showAvailables(self):
    res = requests.get(
        'https://us-central1-kcc-library.cloudfunctions.net/showAvailables')
    result = res.json()
    showData(self, result)


def showNotAvailables(self):
    res = requests.get(
        'https://us-central1-kcc-library.cloudfunctions.net/showNotAvailables')
    result = res.json()
    showData(self, result)


def searchByTitle(self, title):
    reqData = {'title': title}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByTitle'
    res = requests.get(url=url, params=reqData)
    result = res.json()
    showData(self, result)


def searchByAuthor(self, author):
    reqData = {'author': author}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByAuthor'
    res = requests.get(url=url, params=reqData)
    result = res.json()
    showData(self, result)


def searchByPublisher(self, publisher):
    reqData = {'publisher': publisher}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByPublisher'
    res = requests.get(url=url, params=reqData)
    result = res.json()
    showData(self, result)


def borrow(self, title):
    reqData = {'title': title}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/borrow'
    res = requests.get(url=url, params=reqData)
    result = res.json()
    if result['result'] == 1:
        return "대여가 완료 되었어요!"
    else:
        return "대여에 실패 했어요"


def giveBack(self, title):
    reqData = {'title': title}
    url = 'https://us-central1-kcc-library.cloudfunctions.net/giveBack'
    res = requests.get(url=url, params=reqData)
    result = res.json()
    if result['result'] == 1:
        return "반납이 완료 되었어요!"
    else:
        return "반납에 실패했어요"


def showData(self, result):
    row = 0
    self.result_text.setRowCount(len(result))
    for key in result:
        val = result[key]
        for k in val.keys():
            if k == 'author':
                self.result_text.setItem(row, 1, QTableWidgetItem(val[k]))
            if k == 'title':
                self.result_text.setItem(row, 0, QTableWidgetItem(val[k]))
            if k == 'publisher':
                self.result_text.setItem(row, 2, QTableWidgetItem(val[k]))
        row += 1
