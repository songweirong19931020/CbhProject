# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: ba_oracle.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/15 15:03
# ---
# -*- coding: utf-8 -*-
import cx_Oracle
import traceback
class BaOracleSQLContextManager:
    """
    oraclesQL Context Manager
    """
    def __init__(self, host="192.168.12.61", user="BI", password="CREATING2020", tnsnname="ORCL"):
        self.host = host
        self.user = user
        self.password = password
        self.tnsnname = tnsnname

    def __enter__(self):
        """
        上文管理器 返回的结果 会被赋给as 关键字之后的变量
        :return: cursor
        """
        try:
            self.db_conn = cx_Oracle.connect('{user}/{password}@{host}/{tnsnname}'
                                             .format(user=self.user,password=self.password,host=self.host,tnsnname=self.tnsnname))
            self.cursor = self.db_conn.cursor()
            return self.cursor
        except Exception as e:
            traceback.print_exc()
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        下文管理器 选择性地处理包装代码块中出现的异常
        :param exc_type: 异常类型 默认为 None,发生异常,参数被填充
        :param exc_val: 异常实例 默认为 None,发生异常,参数被填充
        :param exc_tb: 异常回溯 默认为 None,发生异常,参数被填充
        :return:
        """
        try:
            if exc_type:
                self.db_conn.rollback()
                # 返回False 传播异常
                # 返回True 终止异常 不要这么做
                # 抛出不同的异常 代替 原有异常
                return False
            else:
                self.db_conn.commit()
        except Exception as e:
            raise e
        finally:
            self.cursor.close()
            self.db_conn.close()
