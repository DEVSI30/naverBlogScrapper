import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,QTime)
from selenium.webdriver.common.by import By

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
        self.category_list = []
        self.article_list = []
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
        self.ui.extractArtcles.clicked.connect(lambda x: self.download())

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
        self.ui.progress_state_label.setText("카테고리 추출 시작")
        self.crawler.switch_to_frame("mainFrame")
        source = self.crawler.get_source()
        self.category_list = self.htmlParser.extract_category(source)

        model = QStandardItemModel()
        for category in self.category_list:
            item_text = f"{' -' if not category['parent_yn'] else ''}{category['text']}"
            model.appendRow(QStandardItem(item_text))
        self.ui.listViewCategory.setModel(model)
        self.ui.progress_state_label.setText("카테고리 추출 완료")

    def download(self):
        self.extract_articles()
        self.download_articles()

    def download_articles(self):
        pass

    def extract_articles(self):
        self.ui.progress_state_label.setText("글 목록 추출 시작")
        index = self.ui.listViewCategory.currentIndex().row()
        selected_category = self.category_list[index]

        category_id = selected_category['id']
        page_count = selected_category['page_count']

        element = self.crawler.find_element_by_id(category_id)
        element.click()
        time.sleep(self.option.waitSeconds)
        # 목록 닫혀있는거 열기 -> 처음부터 닫혀있는 경우에는?
        toplistSpanBlind = self.crawler.find_element_by_id("toplistSpanBlind")
        toplistSpanBlind.click()
        time.sleep(self.option.waitSeconds)
        # 페이지 수 변경 select box 열기
        listCountToggle = self.crawler.find_element_by_id("listCountToggle")
        listCountToggle.click()
        time.sleep(self.option.waitSeconds)
        # 보여주는 페이지 수 -> 30
        changeListCount = self.crawler.find_element_by_selector("#changeListCount > a:nth-child(5)")
        changeListCount.click()
        time.sleep(self.option.waitSeconds)

        current_page = 1
        self.article_list = []

        while True:
            for i in range(1, 31):
                selector = f"""#listTopForm > table > tbody > tr:nth-child({i}) > td.title > div > span > a"""
                article = self.crawler.find_element_by_selector(selector)
                if not article:
                    continue
                try:
                    new_article = {
                        "text": article.text,
                        "href": article.get_attribute('href')
                    }
                    self.article_list.append(new_article)
                except:
                    continue

            # 전체 페이지수를 알고 있는 경우에만 진행률을 표시
            if page_count != -1:
                self.ui.progressBar.setValue(int((len(self.article_list) / page_count) * 100))
                QApplication.processEvents()

            time.sleep(self.option.waitSeconds)

            current_page += 1 #?
            if current_page % 10 == 1:
                next_button = self.crawler.find_element_by_selector(f"""#toplistWrapper > div.wrap_blog2_paginate > div > a.next.pcol2._goPageTop._param\({current_page}\).aggregate_click_delegate""")
            else:
                next_button = self.crawler.find_element_by_selector(f"""#toplistWrapper > div.wrap_blog2_paginate > div > a.page.pcol2._goPageTop._param\({current_page}\)""")

            if not next_button:
                break

            next_button.click()
            time.sleep(self.option.waitSeconds)

        # 이러면 다 끝나야 보여지는데...
        self.ui.progressBar.setValue(100)
        model = QStandardItemModel()
        for category in self.article_list:
            item_text = f"{category['text']}"
            model.appendRow(QStandardItem(item_text))
        self.ui.listViewArticle.setModel(model)
        self.ui.progress_state_label.setText("다운로드 시작")

    def About_event(self):
        QMessageBox.about(self, 'About Title', 'About Message')


if __name__ == "__main__":
    main = Main()







