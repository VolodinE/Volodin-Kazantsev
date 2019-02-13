from head import primary_key
from XDB_to_RAM.exceptions import Exceptions

class domain():
    id = 0
    primary_key = primary_key("id")
    def __init__(self, data_type_id, uuid, name=None, description=None, length=None, char_length = None,
                 precision = None, scale = None, width = None, align = None, show_null = None,
                 show_lead_nulls = None, thousands_separator = None, summable = None, case_sensitive=None,
                 ):
        try:
            if data_type_id is None:
                raise Exceptions.IsNull("data_type_id")
            self.data_type_id = data_type_id
            if uuid is None:
                raise Exceptions.IsNull("uuid")
            self.uuid = uuid
        except Exceptions.IsNull as IsNullErr:
            IsNullErr.message()
        self.name = name
        self.description = description
        self.data_type_id = data_type_id
        self.length = length
        self.char_length = char_length
        self.precision = precision
        self.scale = scale
        self.width = width
        self.align = align
        self.show_null = show_null
        self.show_lead_nulls = show_lead_nulls
        self.thousands_separator = thousands_separator
        self.summable = summable
        self.case_sensetive = case_sensitive

    def inc(self):
        id+=1
