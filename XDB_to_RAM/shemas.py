from head import primary_key
from XDB_to_RAM.exceptions import Exceptions

class schemas():
    id = 0
    primary_key=primary_key("id")
    def __init__(self, name):
        self.id=self.inc(id)
        try:
            if name is None:
                raise Exceptions.IsNull("name")
            self.name = name
        except Exceptions.IsNull as IsNullErr:
            IsNullErr.message()
    def __inc__(self):
        id+=1
        return id
