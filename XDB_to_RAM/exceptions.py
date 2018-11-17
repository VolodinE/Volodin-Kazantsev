class BaseException(Exception):
    def __init__(self, exception_type):
        self.exception_type=exception_type
    def message(self):
        print(self.exception_type)


"""class IsNull(Exception):
    def __init__(self, exception_type):
        self.exception_type = exception_type
    def message(self):
        print(self.exception_type, " is Null")
"""

class IsNull(BaseException):
    def __init__(self, exception_type):
        super().__init__(exception_type)
    def message(self):
        print(self.exception_type, " is Null")

"""class IsNotUnique(Exception):
    def __init__(self, exception_type):
        self.exception_type = exception_type
    def message(self):
        print(self.exception_type, "is not Unique")
"""

class IsNotUnique(BaseException):
    def __init__(self, exception_type):
        super.__init__(exception_type)
    def message(self):
        print(self.exception_type, "is not Unique")

class IsNotPrimaryKey(BaseException):
    def __init__(self, exception_type):
        super.__init__(exception_type)
    def message(self):
        print(self.exception_type, "is not primary key")

class IsWrongType(BaseException):
    def __init__(self,exception_type, var_type_right, var_type_wrong):
        super.__init__(exception_type)
        self.var_type_right=var_type_right
        self.var_type_wrong=var_type_wrong
    def message(self):
        print(self.exception_type, " is not ", self.var_type_wrong, " it is ", self.var_type_right)



class Exceptions():
    def __init__(self):
        self.IsNull = IsNull(str)
        self.IsUnique = IsNotUnique(str)
        self.IsWrongType = IsWrongType(str,str,str)
        self.IsNotPrimaryKey = IsNotPrimaryKey(str)


