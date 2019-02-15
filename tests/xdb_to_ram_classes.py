# sceme create domains

from collections import defaultdict
#from collections import

attribute = 0
value = 1

class primare_key:
    types = set()
    num_of_string_of_type = defaultdict(int)
    def __init__(self,type):
        self.id = primare_key.num_of_string_of_type[type]
        self.type = type
        primare_key.types.add(type)
        primare_key.num_of_string_of_type[type]+=1          # id - значение PK,
                                                            #используем  как ключ:
                                                            #имя для домена
    def __eq__(self, other):                                #имя для таблицы
       # if (self.type == self.type):                    #int >=0 для поля
       #     return True
       # return False
        return True

    def __hash__(self):
        return hash(self.type)

    def pk(self):
        return (self.id, self.type)

  #  def pk_of_pk(self):
  #      return self.pk_id


from xml.dom.minidom import parse
class schema:

    def __init__(self,xdb_file):
        self.xdb_file = parse(xdb_file)
        self.domains = self.get_domains()
        self.fields = self.get_fields()

    def __eq__(self, other):
        if (self.domains == other.domains
            and self.fields == other.fields):
            return True
        else:
            return False

    def get_domains(self):
        domains_set = set()
        domains = self.xdb_file.getElementsByTagName("domain")
        for domain_description in domains:
            if domain(domain_description.attributes.items()) not in domains_set:
                domains_set.add(domain(domain_description.attributes.items()))
        return domains_set

    def get_fields(self):
        fields_set = set()
        fields = self.xdb_file.getElementsByTagName("field")
        for field_description in fields:
            if field(field_description.attributes.items()) not in fields_set:
                fields_set.add(field(field_description.attributes.items()))
        return fields_set

class domain:
    def __init__(self,items):
        self.primary_key = primare_key("domain")
        self.description = dict()
        for item in items:
            self.description[item[0]]=item[1]
        self.description = self.description
    def description(self):
        return self.description


    def __hash__(self):
        return hash(tuple(self.description,))

    def __eq__(self, other):
        if self.description==other.description:
            return True
        return False

class field:
    def __init__(self,items):
        self.pk = primare_key("field")
        self.description = dict()
        for item in items:
            self.description[item[0]]=item[1:]

    def __hash__(self):
        return hash(tuple(self.description,))

    def __eq__(self, other):
        if (#self.table_id == other.table_id
            self.description == other.description):
            return True
        else:
            return False

    def print_field(self):
        print(self.description)


schema1 = schema("tasks.xdb")
schema2 = schema("tasks.xdb")

#print(schema1.print_fields())

print(schema1==schema2)

