import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from cry_sys.config.log_crm import AutoLog


class Add_client:
    def add_client(self):
        self.driver.switch_to.frame('mainFrame')
        add_keh = self.driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input')
        add_keh.click()
        name = 'hjj'
        self.driver.find_element_by_name('customerName').send_keys(name)
        self.log.set_mes('客户姓名' + name, 'info')
        chname = 'lp'
        self.driver.find_element_by_name('customerAddMan').send_keys(chname)
        self.log.set_mes('创建人' + chname, 'info')
        self.driver.find_element_by_name('customerEmail').send_keys('55412@qq.com')
        self.driver.find_element_by_name('customerBirthday').click()
        self.driver.execute_script("document.getElementById('customerBirthday').value='2020-10-22 19:22:40'")
        self.driver.find_element_by_name('submit').click()
        self.log.set_mes('客户添加成功--保存成功', 'info')
        alrtt = Alert(self.driver)
        # print(alrtt.text)
        return alrtt.text

