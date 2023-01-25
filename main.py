from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from gui import Ui_Dialog
from crawler import Crawler
from option import Option
import sys
import os


class Main(object):
    def __init__(self):
        self.crawler = Crawler()
        self.option = Option()
        self.init_ui()

    def init_ui(self):
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(Dialog)
        


        self.ui.txtURL.setPlainText(self.option.url)
        self.ui.btnMove.clicked.connect(lambda x: self.crawler.move(self.ui.txtURL.toPlainText()))

        self.ui.btnChangeDirectory.clicked.connect(lambda x: self.change_directory())

        self.ui.txtSaveDirectory.setPlainText(self.option.savePath)
        self.ui.txtWaitTime.setPlainText(f"{self.option.waitSeconds}")

        self.ui.progressBar.setValue(0)
        Dialog.show()
        sys.exit(app.exec_())

    def change_directory(self):
        folder_path = False
        try:
            folder_path = QFileDialog.getExistingDirectory(None, '폴더 선택', os.path.expanduser("~"))
        except Exception as e:
            print(e)
        if folder_path:
            self.ui.txtSaveDirectory.setPlainText(folder_path)


if __name__ == "__main__":
    main = Main()







