# sceme create domains

from collections import defaultdict
#from collections import



attribute = 0
value = 1

class primare_key:
    def __init__(self,id,type):             # id - значение PK,
        self.id = id                        #используем  как ключ:
        self.type = type                    #имя для домена
    def __eq__(self, other):                #имя для таблицы
        if (self.id == other.id):
            return True
        return False

    def pk(self):
        return self.id



from xml.dom.minidom import parse
class schema:

    def __init__(self,xdb_file):
        self.xdb_file = parse(xdb_file)
        self.domains = self.get_domains()

    def __eq__(self, other):
        if (self.domains == other.domains):
            return True
        else:
            return False

    def get_domains(self):
        domains_set = set()
        domains = self.xdb_file.getElementsByTagName("domain")

        for domain_description in domains:

            domains_set.add(domain(domain_description.attributes.items()))
        return domains_set

class domain:
    def __init__(self,items):
        self.primary_key = primare_key(items[0][1],"domain")
        #self.name = items[0][1]
        self.description = dict()

        for item in items:
            self.description[item[0]]=item[1]
        self.description = (self.description)
    def description(self):
        return self.description


    def __hash__(self):
        return hash(self.primary_key.pk())

    def __eq__(self, other):
      #  is_Equal = True
#        if (set.difference(self.description,other.description)):
        if self.description==other.description:
            if self.primary_key.pk()==other.primary_key.pk():
                return True
                #прописать исключение для равенства значений и неравенства ключей
        return False

schema1 = schema("tasks.xdb")
schema2 = schema("tasks.xdb")

print(schema1==schema2)

