from collections import defaultdict
#from collections import
import xml.etree.ElementTree as ET
from xml.dom.minidom import parse
from xml_to_ram.develop.classes_of_schema_in_ram import *
attribute = 0
value = 1


class set_for_tables(set):                      #класс определен для изменения процесса сравнивания множеств
    def __hash__(self):
        return hash(self)

    def __eq__(self, other):
        # сравнение множеств происходит в два этапа
        # находятся хэши для всех значений в схеме, если есть такое - оно не добавляется
        # затем происходит сравнение множеств за счет нахождения суммы хэшей

        tuple_of_hashes_self = set_for_tables()         #множества будут содержать окончательные данные
        tuple_of_hashes_other = set_for_tables()

        hash_sum_self = 0                               #значения хэш-сумм
        hash_sum_other = 0

        for i in self:                                                  #заполнение множеств
            tuple_of_hashes_self.add(hash((i.description,i.pk)))
        for i in other:
            tuple_of_hashes_other.add(hash((i.description,i.pk)))

        for i in tuple_of_hashes_self:                                  #поиск хэш-сумм
            hash_sum_self+=hash(i)
        for i in tuple_of_hashes_other:
            hash_sum_other+=hash(i)

        if (hash_sum_self==hash_sum_other):
            return True
        return False

class primare_key:
    types = set_for_tables()                              #множество всех типов в таблице
    num_of_string_of_type = defaultdict(int)              #словарь количества ключей для каждого типа, все значения
    def __init__(self,type):                              #на старте равны нулю
        self.id = primare_key.num_of_string_of_type[type] #ставит в соответствие значению ключа для каждого объекта
        self.type = type                                  #записывает полученный тип
        primare_key.types.add(type)                       #если указанного типа еще нет - занином в множество всех типов
        primare_key.num_of_string_of_type[type]+=1        #увеличивает значение количества ключей

    def __eq__(self, other):
        if (self.type == self.type
            and self.id==other.id                         #сравнение по типу и id
            ):
            return True
        return False

    def __hash__(self):
        return hash((self.type,self.id,))

    def pk(self):
        return tuple(self.id, self.type,)

    def set_default():                                    #вызывается при создании новой схемы в ram
        primare_key.types.clear()                         #очистка множества всех типов в схеме
        primare_key.num_of_string_of_type.clear()         #очистка словаря соответсвий тип:количество эл-ов типа


class schema:

    def __init__(self,xdb_file):
        self.xdb_file = ET.parse(xdb_file)         #парсинг файла

        primare_key.set_default()               #сброс всей информации о ключах в схеме (всех, если до этого уже созд-сь)

        root = self.xdb_file.getroot()
        if (root.tag=="dbd_schema"):
            self.schema_despription = root.attrib
        # else exception
        not_allowed = set()
        not_allowed.add("dbd_schema")

        self.set_of_domains = set()
        self.set_of_tables = set_for_tables()
        self.set_of_constraints = set()
        self.set_of_indexes = set()

        l = list()
        for i in root:
            if (i.tag == "domains"):
                for domain_ in i:
                    self.set_of_domains.add((domain((domain_.attrib))))
            if(i.tag == "tables"):
                table_id = 0
                for table_ in i:
                    print(table_.attrib)
                    self.set_of_tables.add(table(table_.attrib))

        # for i in l:
        #     print(i.description)
        # for i in root[2]:
        #     print(i.attrib)
        #
        # for table in tables:
        #     for element in table:
        #         if(element.tag == "field"):
        #             set_of_fields.add(field(element.attrib,table_id))


    def __eq__(self, other):
        # if (    self.domains == other.domains   #если все множества значений равны - схемы однаковы
        #     and self.fields == other.fields
        #     and self.tables == other.tables
        #     ):
        #     return True
        # else:
        #     return False
        if (
            self.set_of_domains==other.set_of_domains
            and self.set_of_tables == other.set_of_tables
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