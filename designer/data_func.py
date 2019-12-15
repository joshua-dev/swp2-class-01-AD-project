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
    requestData = {"title": title}
    requestData = json.dumps(requestData)
    url = 'https://us-central1-kcc-library.cloudfunctions.net/searchByTitle'
    res = requests.get(url, params=requestData)
    result = res.json()
    showData(self, result)


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