from head import primary_key
from XDB_to_RAM.exceptions import Exceptions

class settings():
    primary_key=primary_key("key")
    dbd_version = ('dbd.version', )            ### ????
    def __init__(self, key, value, valueb):
        self.key = key
        self.value=value
        self.valueb=valueb
