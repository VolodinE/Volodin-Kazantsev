#from xml.dom.minidom import parse
from collections import namedtuple

#from collections import ChainMap
schema_description = namedtuple("schema_description", ["atributes", "domains", "tables"])
from xdb_to_ram import *
from xml_classes import *
class primary_key():
    def __init__(self,id):
        self.id

class schema:
    """
    def __init__(self,schema_attributes,domains,tables):

        self.schema_attributes = schema_attributes
        self.domains = domains
        self.tables = tables
    """

    shema_attr = frozenset( [
        "fulltext_engine",         #Описание характеристик схемы
        "version",
        "name",
        "description"
    ] )


    def __init__(self,xdb_file):
        #self.schema_description_ = schema_description
        self.schema_description_ = xdb_to_ram.create_xdb_schema(xdb_file)



    def __eq__(self, other):
        #isEqual = True
        if (
            self.schema_description_.domains == other.domains
          #          and
          #  self.schema_description_.atributes == other.atributes and
          #  self.schema_description_.tables == other.tables
            ):
            return True
        else:
            return False

    def __eq_domains__(self,other):
        if (self.schema_description_.domains == other.schema_description_.domains):
            return True
        else:
            return False
class domain:
    #id = 0
 #   primary_key = primary_key("id")
    """
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


   # def __init__(self,**props):
    """

    domains_attrinutes = frozenset ( [
        "name",
        "description",
        "char_length",
        "length",                           #Описание возможных
        "precision",                        #характеристик домена.
        "scale",                            #
        "width",
        "align",
        "show_null",
        "show_lead_nulls",
        "thousands_separator",
        "summable",
        "case_sensitive",
    ])

    def __init__(self,domain):
     #   id+=id+1
        self.atributes=domain

    def __eq__(self, other):
        if (
            self.atriputes == other.atributes
        ):
            return True
        else:
            return False





class constraint():
    def __init__(self, table_id, uuid, id=None, name=None, constraint_type=None, reference=None,
                 unique_key_id=None, has_value_edit=None, cascading_delete=None, expression=None,
                 ):
        self.id = id + 1
        self.table_id = table_id
        self.name = name
        self.constraint_type = constraint_type
        self.reference = reference
        self.unique_key_id = unique_key_id
        self.has_value_edit = has_value_edit
        self.cascading_delete = cascading_delete
        self.expression = expression
        self.uuid = uuid
