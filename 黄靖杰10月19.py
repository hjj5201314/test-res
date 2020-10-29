import time

from selenium import webdriver
import re


# class JD:
def name_error():
    try:
        driver=webdriver.Chrome('E:\\python\\chromedriver.exe')
        driver.get('C:\\Users\\dell\\Desktop\\jd_reg\\demo.html')
        name_element=driver.find_element_by_xpath('//*[@id="userName"]')
        name_element.send_keys('11')
        error_info=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/span').text
        error_image=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/i').value_of_css_property('background')
        error_image_info=re.search('error.png',error_image).group()
        time.sleep(3)
        if error_info=='格式错误，仅支持汉字、字母、数字、“-”“_”的组合' and error_image_info=='error.png':
            print('pass')
        else:
            print('faild')
    except Exception as e:
        print('未知异常')
    # finally:
    #     driver.quit()
    # def password_error(self):
    #     try:
    #         driver=webdriver.Chrome('E:\\python\\chromedriver.exe')
    #         driver.get('C:\\Users\\dell\\Desktop\\jd_reg\\demo.html')
    #         password_element=driver.find_element_by_id('pwd')
    #         password_element.send_keys('12345')
    #         time.sleep(3)
    #         password_error=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/span').text
    #         password_imarge=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/i').value_of_css_property('background')
    #         password_imarge_info=re.search('error.png',password_imarge).group()
    #         if password_error=='密码长度应在6-20个字符之间' and password_imarge_info=='error.png':
    #             print('pass')
    #         else:
    #             print('failed')
    #     except Exception as a:
    #         print('未知错误')
    #     finally:
    #         driver.quit()
    #
    # def passwodr_two(self):
    #     try:
    #         driver = webdriver.Chrome('E:\\python\\chromedriver.exe')
    #         driver.get('C:\\Users\\dell\\Desktop\\jd_reg\\demo.html')
    #         password_element = driver.find_element_by_xpath('//*[@id="pwd2"]')
    #         password_element.send_keys('12345')
    #         time.sleep(3)
    #         password_error = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/span').text
    #         password_imarge = driver.find_element_by_xpath(
    #             '/html/body/div[2]/div/div[3]/div[2]/i').value_of_css_property('background')
    #         password_imarge_info = re.search('error.png', password_imarge).group()
    #         if password_error == '两次密码不一致' and password_imarge_info == 'error.png':
    #             print('pass')
    #         else:
    #             print('failed')
    #     except Exception as a:
    #         print('未知错误')
    #     finally:
    #         driver.quit()
    #
    # def passwodr_correct(self):
    #     try:
    #         driver = webdriver.Chrome('E:\\python\\chromedriver.exe')
    #         driver.get('C:\\Users\\dell\\Desktop\\jd_reg\\demo.html')
    #         password_element = driver.find_element_by_xpath('//*[@id="pwd"]')
    #         password_element.send_keys('123456')
    #         time.sleep(3)
    #         correct_info = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/i').value_of_css_property('background')
    #         correct_info2 = driver.find_element_by_xpath(
    #             '/html/body/div[2]/div/div[2]/div[1]/i').value_of_css_property('background')
    #         password_imarge_info=re.search('images/ruo.png',correct_info).group()
    #         password_imarge_info2 = re.search('images/right.png', correct_info2).group()
    #         if password_imarge_info == 'images/ruo.png' and password_imarge_info2 == 'images/right.png':
    #             print('pass,密码弱')
    #         else:
    #             print('failed')
    #     except Exception as a:
    #         print('未知错误')
    #     finally:
    #         driver.quit()
    #
    # def zhuche(self):
    #     try:
    #         driver = webdriver.Chrome('E:\\python\\chromedriver.exe')
    #         driver.get('C:\\Users\\dell\\Desktop\\jd_reg\\demo.html')
    #         name_element = driver.find_element_by_xpath('//*[@id="userName"]')
    #         name_element.send_keys('1234')
    #         password_element = driver.find_element_by_xpath('//*[@id="pwd"]')
    #         password_element.send_keys('123456')
    #         password2_element = driver.find_element_by_xpath('//*[@id="pwd2"]')
    #         password2_element.send_keys('123456')
    #         e_mail=driver.find_element_by_xpath('//*[@id="email"]')
    #         e_mail.send_keys('41523540')
    #         ptho=driver.find_element_by_xpath('//*[@id="mobile"]')
    #         ptho.send_keys('23632')
    #         driver.find_element_by_xpath('//*[@id="ck"]').click()#点击我已阅读并同意《京东用户注册协议》
    #         time.sleep(3)
    #         driver.find_element_by_xpath('//*[@id="btn"]').click()
    #         time.sleep(3)
    #         tskuang = driver.switch_to.alert
    #         time.sleep(3)
    #         tskuang=tskuang.text
    #         if tskuang=='可以注册':
    #             print('pass,成功')
    #         else:
    #             print('failed')
    #     except Exception as a:
    #         print('未知错误')
    #     finally:
    #         driver.quit()
if __name__=='__main__':
    # jd=JD()
    name_error()
    # jd.password_error()
    # jd.passwodr_two()
    # jd.passwodr_correct()
    # jd.zhuche()