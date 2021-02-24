# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: MyOrm.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/12 15:16
# ---
#需求
#属性描述值
import numbers
class Field:
    pass

    pass

class IntField(Field):
    # 初始化实例
    def __init__(self,db_column,min_value=None,max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if not isinstance(min_value,numbers.Integral):
                raise ValueError("min value需要整型")
            elif min_value < 0:
                raise ValueError("min value必须是正数")
        if max_value is not None:
            if not isinstance(max_value,numbers.Integral):
                raise ValueError("max value需要整型")
            elif max_value < 0:
                raise ValueError("max value必须是正数")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("最小值不应该大于最大值")

    #数据描述符
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("Int value neeed!")
        if value < self.min_value or value > self.max_value:
            raise ValueError("输入值必须在最大值和最小值之间")
        self._value = value

class CharField(Field):
    def __init__(self,db_column,max_length = None):
        self._value = None
        self.db_column = db_column
        if max_length is None:
            raise ValueError("你必须数据最大值长度限制")
        self.max_length = max_length
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value,str):
            raise ValueError("输入值必须是字符串类型")
        if len(value) > self.max_length:
            raise ValueError("长度超出限制最大长度")
        self._value = value




#重点元类 Metaclass
class ModelMetaClass(type):
    # def __new__(cls, *args, **kwargs):
    #     pass
    #name = classname  bases基类，attr拆包
    def __new__(cls, name,bases,attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls,name,bases,attrs,**kwargs)
        fields = {}
        for key,value in attrs.items():
            if isinstance(value,Field):
                fields[key] = value
        atts_meta = attrs.get("Meta",None)
        _meta = {}
        db_table = name.lower()
        if atts_meta is not None:
            table = getattr(atts_meta,"db_table")
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls,name,bases,attrs, **kwargs)

class BaseModel(metaclass=ModelMetaClass):
    def __init__(self,*args,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        return super().__init__() #将用户入参初始化
    def save(self):
        # 保存逻辑
        fields = []
        values =[]
        for key,value in self.fields.items():
            db_column = value.db_columnschematool -dbType mysql -initSchema
            if db_column is None or len(db_column)==0:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self,key)
            values.append(str(value))
        sql = "inser into {db_table}({fields}) value ({values}))".format(db_table=self._meta["db_table"],fields=','.join(fields),values=','.join(values))
        print(sql)
class User(BaseModel):
    name = CharField(db_column="",max_length=10)
    age = IntField(db_column="",min_value=0,max_value=100)

    class Meta:
        db_table = "user"
if __name__ == '__main__':
    user = User(name="lelsie",age = 18)
    user.save()