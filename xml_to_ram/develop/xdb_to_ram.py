import xml.etree.ElementTree as ET
from xml_to_ram.develop.classes_of_schema_in_ram import *

class schema:

    def __init__(self,xdb_file):
        self.xdb_file = ET.parse(xdb_file)         #парсинг файла

        root = self.xdb_file.getroot()
        if (root.tag=="dbd_schema"):
            self.schema_despription = root.attrib
        # else exception
        not_allowed = set()
        not_allowed.add("dbd_schema")

        self.set_of_sets_of_fields_in_tables = set()
        self.set_of_sets_of_fields_in_tables = set()
        self.set_of_sets_of_indexes_in_tables = set()
        self.set_of_sets_of_constraints_in_tables = set()
        self.set_of_sets_of_description__of_tables = set()

        self.set_of_domains = set()
        set_of_tables = set_for_fields()
        set_of_constraints = set()
        set_of_indexes = set()
        set_of_fields = set_for_fields()
        set_of_sets_of_filelds = set_for_fields()
        table_id = 0
        for i in root:
            if (i.tag == "domains"):
                for domain_ in i:
                    self.set_of_domains.add(domain(domain_.attrib))
            if(i.tag == "tables"):
                for table_ in i:

                    for string in table_:
                        if (string.tag=="field"):
                            set_of_fields.add(field(string.attrib,table_id))
                        if (string.tag=="index"):
                            set_of_indexes.add(index(string.attrib,table_id))
                        if (string.tag=="constraint"):
                            set_of_constraints.add(constraint(string.attrib,table_id))


                    self.set_of_sets_of_fields_in_tables.add(frozenset(set_of_fields))
                    self.set_of_sets_of_indexes_in_tables.add(frozenset(set_of_indexes))
                    self.set_of_sets_of_constraints_in_tables.add(frozenset(set_of_constraints))


                    set_of_fields.clear()
                    set_of_indexes.clear()
                    set_of_constraints.clear()
                    set_of_tables.clear()

    def __eq__(self, other):
        if (
            self.set_of_domains==other.set_of_domains
            and self.set_of_sets_of_fields_in_tables == other.set_of_sets_of_fields_in_tables
            and self.set_of_sets_of_constraints_in_tables == other.set_of_sets_of_constraints_in_tables
            and self.set_of_sets_of_indexes_in_tables == other.set_of_sets_of_indexes_in_tables
        ):
            return True
        return False

    def get_domains(self):
        # получение значений типов доменов
        # из данных, полученных парсингом требуемого файла, получаем требуемые значения по типам
        # проходя по всем спискам описаний домена, узаем, было-ли это описание уже добавленно в множество описаний доменов
        # еще не добавленные описания добавляем в множество описаний
        domains_set = set()
        domains = self.xdb_file.getElementsByTagName("domain")
        for domain_description in domains:
            if domain(domain_description.attributes.items()) not in domains_set:
                domains_set.add(domain(domain_description.attributes.items()))
        return domains_set

    def get_fields(self):
        # получение значений описаний полей
        # из данных, полученных парсингом требуемого файла, получаем требуемые значения по типам
        # проходя по всем спискам описаний домена, узаем, было-ли это описание уже добавленно в множество описаний полей
        # еще не добавленные описания добавляем в множество описаний
        fields_set = set()
        fields = self.xdb_file.getElementsByTagName("field")
        for field_description in fields:
            if field(field_description.attributes.items()) not in fields_set:
                fields_set.add(field(field_description.attributes.items()))
        return fields_set

    def get_tables(self):
        # получаем опсания таблиц
        # добавляются затем описания в виде описаний в аттрибутах в множество таких описаний
        # затем пополняем список таблиц значениями из схемы, если их там нет,
        # т.к. множество содержит один уникальный элемент
        # то переносим в множество, этим убирая повторяющиеся элементы
        #
        # tables_ = self.xdb_file.getElementsByTagName("table")
        #
        # set_of_tables = set_for_tables()
        # for_items = set_for_tables()
        # for table_description in tables_:
        #     for_items.add(tuple(table_description.attributes.items()))
        #
        # for table_description in for_items:
        #     if (table(table_description)) not in set_of_tables:
        #         set_of_tables.add((table(table_description)))

        # tables_set = set_of_tables
        # return tables_set

        schema_ = (self.xdb_file)
        root = schema_.getroot()
        print(root.tag,root.attrib)



schema1 = schema("tasks1.xdb")
schema2 = schema("tasks.xdb")

print(schema1==schema2)