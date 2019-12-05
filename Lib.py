'''
KCC 도서관 관리 프로그램
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Library(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.scoredb = []

    def initUI(self):
        self.scoredb = []
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()

        # 첫번째 줄, 검색하는 타입, 검색창, 검색 버튼
        # 검색 타입 콤보 박스
        self.search_box = QComboBox()
        self.search_box.setMaximumWidth(100)
        self.search_box.addItem('Title')
        self.search_box.addItem('Author')
        self.search_box.addItem('Publisher')
        self.search_box.addItem('Lender')
        # 검색 창
        self.search_bar = QLineEdit("")
        self.search_bar.setMaximumWidth(200)
        # 검색 버튼
        self.search_btn = QPushButton("검색")
        self.search_btn.setMaximumWidth(50)
        self.hbox1.addWidget(self.search_box)
        self.hbox1.addWidget(self.search_bar)
        self.hbox1.addWidget(self.search_btn)

        # 두번째 줄 반납하기 버튼, 대여 가능 책들 보기, 대여기간 콤보박스, 대여하기 버튼
        # 반납하기 버튼
        self.return_btn = QPushButton("반납하기")
        self.return_btn.setMaximumWidth(150)

        # 대여기간 콤보박스
        self.date_box = QComboBox()
        self.date_box.setMaximumWidth(50)
        self.date_box.addItem('1일')
        self.date_box.addItem('2일')
        self.date_box.addItem('3일')
        self.date_box.addItem('4일')
        self.date_box.addItem('5일')
        self.date_box.addItem('6일')
        # 대여하기 버튼
        self.lend_btn = QPushButton("대여하기")
        self.lend_btn.setMaximumWidth(150)


        # 책 리스트를 보여주는 콤보박스
        self.show_box = QComboBox()
        self.show_box.setMaximumWidth(350)

        self.show_box.addItem("모든 책 보기")
        self.show_box.addItem("대여 가능한 책들 보기")
        self.show_box.addItem("대여 중인 책들 보기")

        self.hbox2.addWidget(self.show_box)
        self.hbox5.addWidget(self.date_box)
        self.hbox5.addWidget(self.lend_btn)
        self.hbox5.addWidget(self.return_btn)



        # 세번째 줄 데이터 라벨
        self.hbox3.addWidget(QLabel('Title'))
        self.hbox3.addWidget(QLabel('Author'))
        self.hbox3.addWidget(QLabel('Publisher'))
        self.hbox3.addWidget(QLabel('Lender'))
        self.hbox3.addWidget(QLabel('Date'))


        # 네번째 줄 데이터 창
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.hbox4.addWidget(self.result_text)

        self.vbox = QGridLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QGridLayout()
        self.vbox1.addLayout(self.hbox3)
        self.vbox1.addLayout(self.hbox4)
        self.vbox.addLayout(self.vbox1, 0, 0, 4, 2)
        self.vbox2.addWidget(QLabel("\n정렬하기"),0,0)
        self.vbox2.addLayout(self.hbox2, 1, 0)
        self.vbox2.addWidget(QLabel("\n\n검색하기"), 2, 0)
        self.vbox2.addLayout(self.hbox1, 3, 0)
        self.vbox2.addWidget(QLabel("\n\n대여, 반납 하기"), 4, 0)
        self.vbox2.addLayout(self.hbox5, 5, 0)
        self.vbox.addLayout(self.vbox2, 1, 2)
        self.setLayout(self.vbox)

        # 버튼 누르기 구현
        self.search_btn.clicked.connect(self.buttonClicked)
        self.return_btn.clicked.connect(self.buttonClicked)
        self.lend_btn.clicked.connect(self.buttonClicked)

        self.setGeometry(600, 200, 1200, 400)
        self.setWindowTitle('KCC_Library')
        self.show()

    def buttonClicked(self):
        sender = self.sender()

        if sender.text() == "검색":
            self.search_box.currentText()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Library()
    sys.exit(app.exec_())