from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,QTime)

from gui import Ui_Dialog
from crawler import Crawler
from option import Option
from htmlParser import HtmlParser
import sys
import os


class Main(object):
    def __init__(self):
        self.crawler = Crawler()
        self.option = Option()
        self.htmlParser = HtmlParser()
        self.category_dict = {}
        self.init_ui()

    def init_ui(self):
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(Dialog)
        
        self.ui.txtURL.setPlainText(self.option.url)
        self.ui.btnMove.clicked.connect(lambda x: self.crawler.move(self.ui.txtURL.toPlainText()))

        self.ui.btnChangeDirectory.clicked.connect(lambda x: self.change_directory())
        self.ui.extractCategory.clicked.connect(lambda x: self.extract_category())

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

    def extract_category(self):
        self.crawler.switch_to_frame("mainFrame")
        source = self.crawler.get_source()
        self.category_dict = self.htmlParser.extract_category(source)

        model = QStandardItemModel()
        for category in self.category_dict:
            item_text = f"{' -' if not category['parent_yn'] else ''}{category['text']}"
            model.appendRow(QStandardItem(item_text))
        self.ui.listViewCategory.setModel(model)

if __name__ == "__main__":
    main = Main()







