import logging
import time


class AutoLog:
    def __init__(self):
        self.logger=logging.getLogger('log')

    def set_mes(self,mess,lecel_p):
        try:
            # 创建logger对象
            # logger = logging.getLogger('log')
            # 格式化时间
            now_data = time.strftime('%Y-%m-%d', time.localtime())
            # 创建文件handle
            fh = logging.FileHandler('../../log_info/auto_' + now_data + '.log')
            # 创建控制台handle
            ch = logging.StreamHandler()
            # 格式化
            fm = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
            # 对文件格式
            fh.setFormatter(fm)
            # 对控制台格式
            ch.setFormatter(fm)
            # 文件句柄加入logger
            self.logger.addHandler(fh)
            # 控制台句柄加入logger
            self.logger.addHandler(ch)
            # 设置打印级别
            self.logger.setLevel(logging.DEBUG)
            # 输入info
            if lecel_p=='debug':
                self.logger.debug(mess)
            elif lecel_p=='info':
                self.logger.info(mess)
            elif lecel_p=='warning':
                self.logger.warning(mess)
            elif lecel_p=='error':
                self.logger.error(mess)
            # logger.info('info message')
            # 移除文件句柄
            self.logger.removeHandler(fh)
            # 移除控制台对象
            self.logger.removeHandler(ch)
            # 关闭文件
            # fh.close()
        except:
            print('file exception')
        finally:
            # pass
            fh.close()
