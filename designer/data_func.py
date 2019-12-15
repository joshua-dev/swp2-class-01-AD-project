import requests
from library import *


def showAll(self):
    res = requests.get(
        'https://us-central1-kcc-library.cloudfunctions.net/showAll')
    result = res.json()
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


def showAvailables(self):
    pass


def showNotAvailables(self):
    pass
