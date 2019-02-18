from collections import defaultdict

class set_for_fields(set):
    def __eq__(self, other):
        if (self.issubset(other)
            and other.issubset(self)):
            return True
        return False

class set_for_tables(set):                      #класс определен для изменения процесса сравнивания множеств
    def __hash__(self):
        return hash(self)

    def __eq__(self, other):
        # сравнение множеств происходит в два этапа
        # находятся хэши для всех значений в схеме, если есть такое - оно не добавляется
        # затем происходит сравнение множеств за счет нахождения суммы хэшей
        print("gugk")
        tuple_of_hashes_self = set_for_tables()         #множества будут содержать окончательные данные
        tuple_of_hashes_other = set_for_tables()

        hash_sum_self = 0                               #значения хэш-сумм
        hash_sum_other = 0



        for i in self:                                                  #заполнение множеств
            tuple_of_hashes_self.add(hash((tuple(i.description.items()))))

        for i in other:
            i.description = (i.description)
            tuple_of_hashes_other.add(hash((tuple(i.description.items()))))

        for i in tuple_of_hashes_self:                                  #поиск хэш-сумм
            hash_sum_self+=hash(i)
        for i in tuple_of_hashes_other:
            hash_sum_other+=hash(i)



        if (hash_sum_self==hash_sum_other):
            return True
        return False
#
# class primare_key:
#     types = set_for_tables()                              #множество всех типов в таблице
#     num_of_string_of_type = defaultdict(int)              #словарь количества ключей для каждого типа, все значения
#     def __init__(self,type):                              #на старте равны нулю
#         self.id = primare_key.num_of_string_of_type[type] #ставит в соответствие значению ключа для каждого объекта
#         self.type = type                                  #записывает полученный тип
#         primare_key.types.add(type)                       #если указанного типа еще нет - занином в множество всех типов
#         primare_key.num_of_string_of_type[type]+=1        #увеличивает значение количества ключей
#
#     def __eq__(self, other):
#         if (self.type == self.type
#             and self.id==other.id                         #сравнение по типу и id
#             ):
#             return True
#         return False
#
#     def __hash__(self):
#         return hash((self.type,self.id,))
#
#     def pk(self):
#         return tuple((self.id, self.type,))
#
#     def set_default():                                    #вызывается при создании новой схемы в ram
#         primare_key.types.clear()                         #очистка множества всех типов в схеме
#         primare_key.num_of_string_of_type.clear()         #очистка словаря соответсвий тип:количество эл-ов типа

class constraint:
    type_ = "constraint"
    def __init__(self,items,table_id):
        self.description = items
        self.table_id = table_id

    def __eq__(self, other):
        if (
            self.description==other.description
            and self.table_id == other.table_id
            and self.type_ == other.type_
        ):
            return True
        return False

    def __hash__(self):
        return hash(tuple((frozenset(self.description),self.table_id,constraint.type_)))

class table:
    type_ = "table"
    def __init__(self, items):
#        self.pk = primare_key("table")
        self.description = items

        def __hash__(self):
            return hash(self.description)

        def __eq__(self, other):
            if (self.description == other.description
            ):
                return True
            else:
                return False

    def description(self):
        return self.description

class index:
    type_ = "index"
    def __init__(self,items,table_id):
        self.description = items
        self.table_id = table_id

    def __eq__(self, other):
        if (
            self.description == other.description
            and self.table_id == other.table_id
            and self.type_ == other.type_
        ):
            return True
        return False

    def __hash__(self):
        return hash(tuple((frozenset(self.description),self.table_id,index.type_)))

class domain:
    type="domain"
    def __init__(self,items):
#        self.primary_key = primare_key("domain")
        self.description = items


    def description(self):
        return self.description


    def __hash__(self):
        return hash(tuple(self.description,))

    def __eq__(self, other):
        if self.description==other.description:
            return True
        return False

class field:
    type_="field"
    def __init__(self,items,table_id):
#        self.pk = primare_key("field")
        self.description = items
        self.table_id = table_id

    def __hash__(self):
        return hash(tuple((frozenset(self.description),self.table_id,field.type_)))

    def __eq__(self, other):
        if (
            self.table_id == other.table_id
            and self.description == other.description
            and self.type_ == other.type_):
            return True
        else:
            return False

    # def print_field(self):
    #     print(self.description)
