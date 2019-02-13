from collections import namedtuple
"""
import sys
import os
from ram.exceptions import Exceptions

class primary_key():
    def __init__(self,autoincrement=False, ):
        self.autoincrement=True


class data_type():
    id=0
    def __init__(self,type_id):
        id=self.inc(id)
        self.type_id=type_id
    def inc(self):
        id+=1
        return id

class data_types():
    id=0

    def __init__(self):
        self.data_type = namedtuple("data_type", "id data_type")
        self.data_types=[]

    def __init__(self,*types):
        for i in types:
            data_type_ = data_type(self.inc(id), i)
            self.data_types.append(data_type_)

    def insert_types(self,*data_type_):
        for i in data_type_:
            data_type_ = data_type(self.inc(id), i)
            self.data_types.append(data_type_)

    def insert_type(self, data_type_value):
        data_type_=data_type(self.inc(id),data_type_value)
        self.data_types.append(data_type_)

    def inc(self):
        id+=1
        return id

    def is_unique(self,data_type):
        for data_type_ in self.data_types:
            try:
                if data_type_.data_type == data_type:
                    raise Exceptions.NotUnique()
            except Exceptions.NotUnique as NotUnique:
                return False
        return True

    def is_null(self,data_type):
        for data_type_ in self.data_types:
            try:
                if data_type_.data_type is None:
                    raise Exceptions.IsNull
            except Exceptions.IsNull as Null:
                return False
        return True
"""

class data_types():
    types = ['STRING','SMALLINT','INTEGER', 'WORD', 'BOOLEAN', 'FLOAT', 'CURRENCY', 'BCD',
             'FMTBCD','DATE','TIME','DATETIME','TIMESTAMP','BYTES','VARBYTES','BLOB','MEMO',
             'GRAPHIC','FMTMEMO','FIXEDCHAR','WIDESTRING','LARGEINT','COMP','ARRAY','FIXEDWIDECHAR',
             'WIDEMEMO','CODE','RECORDID','SET','PERIOD','BYTE']
