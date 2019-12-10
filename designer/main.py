from library import *


def main():
    import sys
    app = QApplication(sys.argv)
    ex = Library()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
