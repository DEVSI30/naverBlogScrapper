from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


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


# <a href="https://blog.naver.com/PostView.naver?blogId=ssunris&amp;logNo=221636240966&amp;categoryNo=46&amp;parentCategoryNo=0&amp;viewDate=&amp;currentPage=12&amp;postListTopCurrentPage=&amp;from=postList" class="pcol2 _setTop _setTopListUrl">17.정관(正官)의 분석과 정관격(正官格) (2)</a>
# https://blog.naver.com/ssunris/221636240966
class Crawler(object):
    def __init__(self):
        self.driver = None

    def move(self, url):
        if self.driver is None:
            self.driver = get_driver()

        if not get_status(driver=self.driver):
            self.driver = get_driver()

        self.driver.get(url)

