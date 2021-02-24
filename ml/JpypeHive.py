# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: JpypeHive.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/14 9:19
# ---
import jpype
from jpype import *

# 指定jar包位置, 或者.class文件
class_path = 'E:/SinaifMock/utils/Test.class'
jar_path = r"C:\Users\CBH\IdeaProjects\pg\target\pg-1.0-SNAPSHOT.jar"

# JVM的路径位置
JVM_path = r"C:\Program Files\Java\jre1.8.0_202\bin\server\jvm.dll"

# 开启JVM，且指定jar包, 或者.class文件位置

jpype.startJVM(JVM_path,"-ea","-Djava.class.path=C:\\Users\\CBH\\IdeaProjects\\HiveUtil\\target\\HiveUtil-1.0-SNAPSHOT.jar")


# 打印hello, word
jpype.java.lang.System.out.println("hello World")

TA = jpype.JPackage('com.sbh.tj').ConnectorHiveUtil

TA = TA()
a = TA.GetHiveConnctor('jdbc:hive2://192.168.8.10:10000/default','show databases')
a = TA.newGetCon()
# 关闭JVM
jpype.shutdownJVM()

#python 三方包连接hive

from pyhive import hive
conn = hive.Connection(host="192.168.8.10", port='10000', username='root',password='123456',database='default',auth="LDAP")
cursor = conn .cursor()
cursor.execute("select * from xxx")
result = cursor.fetchall()
df = pd.DataFrame(list(result))