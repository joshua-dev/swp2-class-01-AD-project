from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QIcon, QPixmap
from data_func import *


class Library(QWidget):

    # constructor
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        기본 레이아웃 설정

        hbox1(검색 콤보박스, 검색 창, 검색 버튼)
        hbox2(전체, 대여 가능한, 대여 불가능한 책들 보여주기)
        hbox3(책들의 목록)
        hbox4(대여하기, 반납하기 버튼)
        hbox5(대여 시도 결과 상태 창)
        hobox6(로고)

        """
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()

        # 검색 타입 콤보 박스
        self.search_box = QComboBox()
        self.search_box.setMaximumWidth(100)
        self.search_box.addItem('Title')
        self.search_box.addItem('Author')
        self.search_box.addItem('Publisher')

        # 검색 창
        self.search_bar = QLineEdit("")

        # 검색 버튼
        self.search_btn = QPushButton("검색")
        self.search_btn.setMaximumWidth(70)

        # 반납하기 버튼
        self.return_btn = QPushButton("반납하기")

        # 대여하기 버튼
        self.lend_btn = QPushButton("대여하기")

        # 책 리스트를 보여주는 콤보박스
        self.show_box = QComboBox()
        self.show_button = QPushButton("보기")
        self.show_box.addItem("모든 책들")
        self.show_box.addItem("대여 가능한 책들")
        self.show_box.addItem("대여 중인 책들")

        # 데이터 창
        self.result_text = QTableWidget(self)
        self.result_text.setMinimumWidth(400)
        self.result_text.setSelectionMode(QAbstractItemView.SingleSelection)
        self.result_text.setColumnCount(3)
        self.setResult_textData("모든 책들")

        # 대여 성공여부 창
        self.show_lender = QTextEdit("책을 선택한 뒤 대출하기나 반납을 눌러주세요!")
        self.show_lender.setReadOnly(True)
        self.show_lender.setMaximumHeight(200)

        # 로고 창
        self.lb = QLabel(self)
        self.pixmap = QPixmap('test.png')
        self.lb.setPixmap(self.pixmap)
        self.lb.setMaximumHeight(100)
        self.hbox6.addWidget(self.lb)

        # hbox에 아이템 담기
        self.hbox1.addWidget(self.search_box)
        self.hbox1.addWidget(self.search_bar)
        self.hbox1.addWidget(self.search_btn)
        self.hbox2.addWidget(self.show_box)
        self.hbox2.addWidget(self.show_button)
        self.hbox3.addWidget(self.result_text)
        self.hbox4.addWidget(self.lend_btn)
        self.hbox4.addWidget(self.return_btn)
        self.hbox5.addWidget(self.show_lender)

        # vbox1은 상태창 하나, vbox2에 나머지 구성 담기, hbox에 두 vbox 담기.
        self.hbox = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox1.addLayout(self.hbox3)
        self.vbox2.addLayout(self.hbox6)
        self.vbox2.addLayout(self.hbox1)
        self.vbox2.addLayout(self.hbox2)
        self.vbox2.addLayout(self.hbox4)
        self.vbox2.addLayout(self.hbox5)
        self.hbox.addLayout(self.vbox1)
        self.hbox.addLayout(self.vbox2)

        self.setLayout(self.hbox)

        # 버튼 누르기 구현
        self.search_btn.clicked.connect(self.buttonClicked)
        self.show_button.clicked.connect(self.buttonClicked)
        self.return_btn.clicked.connect(self.buttonClicked)
        self.lend_btn.clicked.connect(self.buttonClicked)

        # 클릭 구현
        self.result_text.cellClicked.connect(self.cell_func)

        self.setGeometry(600, 200, 600, 800)
        self.setWindowTitle('KCC_Library')
        self.setWindowIcon(QIcon("study.png"))
        self.show()

    def closeEvent(self, event):
        button_reply = QMessageBox.information(
            self, "message", "종료하시겠습니까?", QMessageBox.Yes, QMessageBox.No)
        if button_reply == QMessageBox.Yes:
            pass
        else:
            event.ignore()

    def setResult_textData(self, str):
        # 작동시 모든 책 보여주기 설정
        column_headers = ['title', 'author', 'publisher']
        self.result_text.setHorizontalHeaderLabels(column_headers)
        if str == "모든 책들":
            showAll(self)

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == "검색":
            key = self.search_box.currentText()
            ser = self.search_bar.text()
            if key == 'Title':
                searchByTitle(self, ser)
            elif key == 'Author':
                searchByAuthor(self, ser)
            elif key == 'Publisher':
                searchByPublisher(self, ser)

        elif sender.text() == "보기":
            key = self.show_box.currentText()
            if key == "모든 책들":
                showAll(self)
            elif key == "대여 가능한 책들":
                showAvailables(self)
            elif key == "대여 중인 책들":
                showNotAvailables(self)

        elif sender.text() == "대여하기":
            br = self.show_lender.toPlainText()
            if br == "대여가 완료되었어요!" or br == "대여에 실패했어요" or br == "반납이 완료되었어요!" or br == "반납이 완료되었어요!" or br == "반납에 실패했어요":
                self.show_lender.setText("책을 선택해 주세요")
            else:
                self.show_lender.setText(borrow(self, br))

        elif sender.text() == "반납하기":
            gv = self.show_lender.toPlainText()
            if gv == "대여가 완료되었어요!" or gv == "대여에 실패했어요" or gv == "반납이 완료되었어요!" or gv == "반납이 완료되었어요!" or gv == "반납에 실패했어요":
                self.show_lender.setText("책을 선택해 주세요")
            else:
                self.show_lender.setText(giveBack(self, gv))

    def cell_func(self, row, col):
        cell = self.result_text.item(row, col)
        self.show_lender.setText(cell.text())
        if cell is not None:
            return cell.text()

    # destructor
    def __del__(self):
        return
