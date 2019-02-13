# sceme create domains

from collections import defaultdict
#from collections import

attribute = 0
value = 1

from xml.dom.minidom import parse
class schema:

    def __init__(self,xdb_file):
        self.xdb_file = parse(xdb_file)

        self.domains = self.get_domains()

    def __eq__(self, other):
        for i in self.domains:
            print(i)


        input()

        print(other.domains)
        input()

        if (self.domains == other.domains):
            return True
        else:
            return False

    def get_domains(self):

      #  domains_set = list()
        domains_set = set()
        domains = self.xdb_file.getElementsByTagName("domain")
        for domain_description in domains:

            domain_dict = defaultdict()
            for item in (domain_description.attributes.items()):
                #       domain_dict[item[attribute]]=item[value]
                domain_dict[item[attribute]] = item[value]

            domains_set.add(tuple(domain_dict.items()))
            #domains_set.update((domain.attributes.items()))

        return domains_set

class domain:
    def __init__(self,items):
        self.description = dict()
        for item in items:
            self.description[item]=item

    def description(self):
        return self.description.items()

schema1 = schema("tasks.xdb")
schema2 = schema("tasks.xdb")

print(schema1==schema2)

