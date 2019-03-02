from collections import defaultdict
from collections import namedtuple

class attributes:
    schema_attr = [
        'fulltext_engine',
        'version',
        'name',
        'description'
    ]

    schema_props = [

    ]
    schema_list = [
        'domains',  # Список вложенных доменов
        'tables'  # Список вложенных таблиц
    ]

    table_attr = [
        'schema_id',
        'name',
        'description',
        'ht_table_flags',
        'access_level',
        'temporal_mode',
        'means'
    ]

    table_props = [
        'add',
        'edit',
        'delete'
    ]

    table_list = [
        'fields',  # Список вложенных полей
        'constraints',  # Список вложенных ограничений
        'indexes'  # Список вложенных индексов
    ]

    index_attr = [
        'name',
        'field'
    ]

    index_props = [
        'uniqueness',
        'fulltext',
        'local',
        'expression',
        'descend'
    ]

    constraint_attr = [
        'name',
        'kind',
        'items',
        'reference',
        'expression'
    ]

    constraint_props = [
        'has_value_edit',
        'cascading_delete',
        'full_cascading_delete'
    ]

    domain_attr = [
        'name',
        'description',
        'type',
        'align',
        'length',
        'width',
        'precision',
        'char_length',
        'scale'
    ]

    domain_props = [
        'show_null',
        'show_lead_nulls',
        'thousands_separator',
        'summable',
        'case_sensitive'
    ]

    field_attr = [
        'name',
        'rname',
        'domain',
        'description'
    ]

    field_props = [
        'input',
        'edit',
        'show_in_grid',
        'show_in_details',
        'is_mean',
        'autocalculated',
        'required'
    ]

class description:
    def __init__(self,type_name,items):
        self.type_name = type_name
        for prop in getattr(attributes, str(self.type_name) + "_props"):
            setattr(self, prop, False)
        if (dict.get(items,"props")):
            for prop in getattr(attributes, str(self.type_name) + "_props"):
                if (prop in prop):
                    setattr(self,prop,True)
        setattr(self,"type_name",type_name)
        for attr in getattr(attributes,self.type_name+"_attr"):
            setattr(self,attr,None)
        for attr in getattr(attributes,self.type_name+"_attr"):
            if (attr in dict.keys(items)):
                setattr(self,attr,items[attr])

    def __hash__(self):
        hash_sum = 0
        for i in getattr(attributes, self.type_name + "_attr"):
            if not(i is None):
                hash_sum+=hash(i)
        return hash_sum

    def __eq__(self, other):
        for i in getattr(attributes,self.type_name+"_attr"):
            if not(getattr(self,i)==getattr(other,i)):
                return False
        return True

class schema(description):
    def __init__(self,items):
        super(schema, self).__init__(str(type(self)).split(".")[-1].split("'")[0],items)

class table(description):
    def __init__(self,items):
        super(table, self).__init__(str(type(self)).split(".")[-1].split("'")[0],items)

class index(description):
    def __init__(self,items,table):
        super(index, self).__init__(str(type(self)).split(".")[-1].split("'")[0],items)
        setattr(self, "table", table)

class domain(description):
    def __init__(self,items):
        super(domain, self).__init__(str(type(self)).split(".")[-1].split("'")[0],items)

class field(description):
    def __init__(self,items,table):
        super(field, self).__init__(str(type(self)).split(".")[-1].split("'")[0],items)
        setattr(self, "table", table)

class constraint(description):
    def __init__(self,items,table):
        super(constraint, self).__init__(str(type(self)).split(".")[-1].split("'")[0],items)
        setattr(self,"table",table)
