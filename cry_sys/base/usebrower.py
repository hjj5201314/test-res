

from selenium import webdriver

class UseBrowser:
    driver=None
    def __init__(self):
        self.driver=webdriver.Chrome('C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        UseBrowser.driver=self.driver
        self.driver.switch_to.parent_frame()

    @classmethod
    def quit(cls):
        UseBrowser.driver.quit()