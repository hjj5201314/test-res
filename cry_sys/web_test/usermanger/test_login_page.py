import time
import  unittest
import sys
sys.path.append('E:\\Program Files')

from HTMLTestRunner import HTMLTestRunner
from cry_sys.config.excl_operation import OperationExcel
from cry_sys.config.log_crm import AutoLog
from cry_sys.web_func.usermanger.login_page import Login

class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.op=OperationExcel('../../config/用例.xls','用例参数')
        # self.client=OperationExcel('../../config/客户.xls','用例参数')
        self.logins=Login(self.op.get_cell(1,1))
        self.log=AutoLog()
    def test_login_name_null(self):#
        self.logins.login(self.op.get_cell(1,2),self.op.get_cell(1,3))
        alert_text=self.logins.alert_text()
        self.log.set_mes('-获取弹出框内容-','info')
        self.assertEqual(alert_text,self.op.get_cell(1,4))

    def test_password_null(self):
        self.logins.login(self.op.get_cell(2, 2), self.op.get_cell(2, 3))
        alert_text = self.logins.alert_text()
        self.log.set_mes('-获取弹出框内容-', 'info')
        self.assertEqual(alert_text, self.op.get_cell(2,4))

    def test_name_password_null(self):
        self.logins.login(self.op.get_cell(3, 2), self.op.get_cell(3, 3))
        alert_text = self.logins.alert_text()
        self.log.set_mes('-获取弹出框内容-', 'info')
        self.assertEqual(alert_text,self.op.get_cell(3,4))

    def test_name_password_error(self):#
        self.logins.login(self.op.get_cell(4, 2), self.op.get_cell(4, 3))
        alert_text = self.logins.alert_text()
        self.log.set_mes('-获取弹出框内容-', 'info')
        self.assertEqual(alert_text, self.op.get_cell(4,4))

    def test_name_password_sucess(self):#
        self.logins.login(self.op.get_cell(5, 2), self.op.get_cell(5, 3))
        self.logins.br.change_from('topFrame')
        sucess_text = self.logins.br.get_text('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div')
        self.log.set_mes('-获取登录成功信息-', 'info')
        self.assertEqual(sucess_text, self.op.get_cell(5,4))
    # def test_add_client(self):
    #     self.logins.login(self.op.get_cell(5, 2), int(self.op.get_cell(5, 3)))
    #     self.logins.add_client()
    #     self.op = OperationExcel('../../config/用例.xls', '用例参数2')
    #     self.logins.add_keh_info(self.op.get_cell(1,2),self.op.get_cell(1,3),self.op.get_cell(1,4),self.op.get_cell(1,5))
    #     time.sleep(2)
    #     alert_text=self.logins.alert_text()
    #     self.log.set_mes('-获取添加客户信息成功-','info')
    #     self.assertEqual(alert_text,self.op.get_cell(1,6))
    # def test_update_client(self):
    #     self.logins.login(self.op.get_cell(5, 2), int(self.op.get_cell(5, 3)))
    #     self.logins.add_client()
    #     self.op = OperationExcel('../../config/用例.xls', '用例参数3')
    #     # self.client=OperationExcel('../../config/客户.xls','用例参数')
    #     self.logins.update_kehu_info(self.op.get_cell(1,5))
    #     time.sleep(2)
    #     alert_text=self.logins.alert_text()
    #     self.log.set_mes('-获取修改客户信息成功-','info')
    #     self.assertEqual(alert_text,self.op.get_cell(1,6))

    def tearDown(self) -> None:
        self.logins.ub.quit()

if __name__=='__main__':
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite.addTests(test_case)
    # runner= unittest.TextTestRunner()
    # runner.run(suite)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../log_info/report'+'.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title='auto_case', description='ui_auto_case')
        runner.run(suite)





