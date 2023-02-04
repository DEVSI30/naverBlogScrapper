import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup


def get_driver():
    driver = webdriver.Chrome()

    chrome_options = Options()

    user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
    chrome_options.add_argument('user-agent=' + user_agent)
    chrome_options.add_argument("lang=ko_KR")

    return driver


def get_status(driver):
    try:
        driver.title
        return True
    except WebDriverException:
        return False


class Crawler(object):
    def __init__(self):
        self.driver = None

    def move(self, url):
        if self.driver is None:
            self.driver = get_driver()

        if not get_status(driver=self.driver):
            self.driver = get_driver()

        self.driver.get(url)

    def get_source(self):
        return self.driver.page_source

    def switch_to_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    def find_element_by_id(self, id):
        return self.driver.find_element(By.ID, id)

    def find_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath)
        except:
            return None

    def find_element_by_selector(self, selector):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, selector)
        except:
            return None


def save_html_file():
    file_name = "test"
    with open(f"{file_name}.html", "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html>' + "\n")
        f.write('<html lang="en">' + "\n")
        f.write('<head>' + "\n")
        f.write('    <meta charset="UTF-8">' + "\n")
        f.write('    <meta http-equiv="X-UA-Compatible" content="IE=edge">' + "\n")
        f.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">' + "\n")
        f.write(f'    <title>{file_name}</title>' + "\n")
        f.write('</head>' + "\n")
        f.write('<body>' + "\n")
        f.write('</body>' + "\n")
        f.write('</html>' + "\n")

if __name__ == '__main__':
    save_html_file()



