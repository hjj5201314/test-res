import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from cry_sys.base.broweroperation import BrowserOperation
from cry_sys.base.usebrower import UseBrowser
from cry_sys.config.log_crm import AutoLog


class Login:

    def __init__(self,url):
        # self.log=AutoLog()
        # self.driver=webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.get(url)
        # time.sleep(5)
        self.log = AutoLog()
        self.ub = UseBrowser()
        self.br = BrowserOperation(UseBrowser.driver)
        self.br.open_url(url)
        time.sleep(5)
    def login(self,username='',password=''):
        self.log.set_mes('登录功能开始','info')
        # username_e=self.driver.find_element_by_name('userNum')
        # username_e.send_keys(username)
        self.br.send_keys('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input',username)
        self.log.set_mes('---输入用户名---'+username,'info')
        # password_e=self.driver.find_element_by_name('userPw')
        # password_e.send_keys(password)
        self.br.send_keys('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input', password)
        self.log.set_mes('输入密码'+password,'info')
        # self.driver.find_element_by_id('in1').click()
        self.br.click_element('//*[@id="in1"]')
        time.sleep(3)
        self.log.set_mes('点击登录','info')
    # def swi_frame(self):
    #     self.driver.switch_to.frame('topFrame')
    #     return self.driver.find_element_by_xpath(
    #         '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div').text
    def add_client(self):
        # self.br.change_from('topFrame')
        self.br.change_from('topFrame')
        self.br.click_element('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/table/tbody/tr/td/div/a')
        # keh_element = self.driver.find_element_by_link_text('客户信息')
        # time.sleep(2)
        # keh_element.click()
        # self.driver.switch_to.parent_frame()
    def add_keh_info(self,**kwargs):
        # self.driver.switch_to.frame('mainFrame')
        # add_keh=self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input')
        # time.sleep(3)
        # add_keh.click()
        # self.driver.find_element_by_name('customerName').send_keys(client_uaername)
        # self.log.set_mes('客户姓名'+client_uaername,'info')
        # self.driver.find_element_by_name('customerBirthday').click()
        # time.sleep(3)
        # self.driver.find_element_by_name('customerAddMan').send_keys(create_person)
        # self.log.set_mes('创建人' + create_person, 'info')
        # self.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        # self.driver.find_element_by_id('customerBirthday').clear()
        # self.driver.find_element_by_id('customerBirthday').send_keys(client_birthday)
        # self.log.set_mes('出生日期' + client_birthday, 'info')
        # self.driver.find_element_by_name('customerEmail').send_keys(email)
        # self.log.set_mes('email'+email,'info')
        # button=self.driver.find_element_by_name('submit')
        # self.driver.execute_script("arguments[0].click()",button)
        self.br.change_from('mainFrame')
        self.br.click_element('/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input')
        self.br.send_keys('/html/body/form/table[1]/tbody/tr[8]/td[2]/input',kwargs.get('client_uaername',''))
        self.br.send_keys('/html/body/form/table[1]/tbody/tr[8]/td[2]/input', kwargs.get('create_person', ''))
        self.br.send_keys('/html/body/form/table[1]/tbody/tr[8]/td[2]/input', kwargs.get('lient_birthday', ''))
        self.br.send_keys('/html/body/form/table[1]/tbody/tr[8]/td[2]/input', kwargs.get('customerEmail', ''))
        self.ub.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.ub.driver.find_element_by_id('customerBirthday').clear()
        self.br.send_keys('/html/body/form/table[1]/tbody/tr[8]/td[2]/input', kwargs.get('client_birthday', ''))
        button = self.ub.driver.find_element_by_name('submit')
        self.ub.driver.execute_script("arguments[0].click()",button)

    def update_kehu_info(self,email):
        # self.driver.switch_to.frame('mainFrame')
        # update_keh = self.driver.find_element_by_xpath(
        #     '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[13]/div/span/a[1]')
        # update_keh.click()
        # self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[7]/td[2]/input').send_keys(email)
        # self.driver.find_element_by_name('submit').click()
        # self.log.set_mes('客户修改成功--保存成功', 'info')
        self.br.change_from('mainFrame')
        self.br.click_element('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[13]/div/span/a[1]')
        self.br.send_keys('/html/body/form/table[1]/tbody/tr[7]/td[2]/input',email)
        self.br.click_element('/html/body/form/table[2]/tbody/tr/td[2]/input')

    def alert_text(self):
        alrtt = Alert(self.br.driver)
        return alrtt.text