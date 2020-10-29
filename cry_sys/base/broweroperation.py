from selenium.webdriver.common.alert import Alert


class BrowserOperation:

    def __init__(self,driver):
        self.driver=driver

    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error')

    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not find')

    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,'element not find')

    def get_text(self,xpath):
        try:
            text=self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e,'element not find')
        return text

    def change_from(self,frame_name):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame_name)

    def change_window(self,title):
        for window_id in self.driver.window_handles:
            self.driver.switch_to.window(window_id)
            if self.driver.title==title:
                break


# if __name__=='__main__':
#     ub= UseBrowser()
#     bo=BrowserOperation(UseBrowser.driver)
#     bo.open_url('http://localhost:8080/JavaPrj_6/login.do')
#     bo.send_keys('//*[@id="UserName"]','2222')
#     bo.send_keys('//*[@id="Password"]','2222')
#     bo.click_element('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')
#     UseBrowser.quit()