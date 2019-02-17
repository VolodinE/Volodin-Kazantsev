# sceme create domains

from collections import defaultdict
#from collections import

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

from xml.dom.minidom import parse
class schema:

    def __init__(self,xdb_file):
        self.xdb_file = parse(xdb_file)         #парсинг файла

        primare_key.set_default()               #сброс всей информации о ключах в схеме (всех, если до этого уже созд-сь)

        self.domains = self.get_domains()       #получение данных схемы
        self.fields = self.get_fields()
        self.tables = self.get_tables()

    def __eq__(self, other):
        if (    self.domains == other.domains   #если все множества значений равны - схемы однаковы
            and self.fields == other.fields
            and self.tables == other.tables
            ):
            return True
        else:
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
        tables_ = self.xdb_file.getElementsByTagName("table")

        set_of_tables = set_for_tables()
        for_items = set_for_tables()
        for table_description in tables_:
            for_items.add(tuple(table_description.attributes.items()))

        for table_description in for_items:
            if (table(table_description)) not in set_of_tables:
                set_of_tables.add((table(table_description)))

        tables_set = set_for_tables(set_of_tables)
        return tables_set

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

    # def print_field(self):
    #     print(self.description)

class table:
    def __init__(self,items):
        self.pk = primare_key("table")
        self.description = (tuple(dict(items)))

        def __hash__(self):
            return hash(self.description,)
        
        def __eq__(self, other):
            input()
            if (
                self.description == other.description
                ):
                return True
            else:
                return False

    def description(self):
        return self.description


schema1 = schema("tasks1.xdb")
schema2 = schema("tasks.xdb")

print(schema1==schema2)