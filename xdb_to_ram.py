from exceptions import *
from xml_classes import *
from xml.dom.minidom import parse
from xml_classes import *

from collections import namedtuple
table_description = namedtuple("table","fields constraints indexes")
#schema_description = namedtuple("schema_description", "atributes domains tables")

from collections import defaultdict



class xdb_to_ram():
    @staticmethod
    def create_xdb_schema(xdb_file):
       xdb_file=parse(xdb_file)
       return schema(
           schema_description
                (
                xdb_to_ram.get_ram_shema_atributes(
                    xdb_file.getElementsByTagName("dbd_schema")
                ),
                xdb_to_ram.get_ram_domains(
                    xdb_file.getElementsByTagName("domain")
                ),
                xdb_to_ram.get_ram_tables(
                    xdb_file.getElementsByTagName("table")
                )
            )
        )

    @staticmethod
    def get_ram_shema_atributes(dbd_schema):
        return xdb_to_ram.ToDict(dbd_schema)

    @staticmethod
    def get_ram_domains(domains):
        #descriptions = list()
        descriptions = set()
        for domain in domains:
            descriptions.update(xdb_to_ram.ToDict(domain))
        return descriptions

    @staticmethod
    def get_ram_tables(tables):
        field_dict = defaultdict()
        constraint_dict = defaultdict()
        index_dict = defaultdict()

        for table in tables:
            #fields_list = list()
            fields_list=set()
            fields = table.getElementByTagName("field")
            for field in fields:
               # fields_list.append(xdb_to_ram.ToDict(field))
                fields_list.update(xdb_to_ram.ToDict(field))
            #constraint_list =list()
            constraints_list=set()
            constraints = table.getElementByTagame("constraint")
            for constraint in constraints:
                #constraint_list.append(xdb_to_ram.ToDict(constraint))
                constraints_list.update(xdb_to_ram.ToDict(constraint))
            indexes = table.getElemntByTagName("index")
            #indexes_list = list()
            indexes_list = set()
            for index in indexes:
                #indexes_list.append(xdb_to_ram.ToDict(index))
                indexes_list.update(xdb_to_ram.ToDict(index))
            table = table_description(field_dict,constraint_dict,index_dict)
        return table


    """
    @staticmethod
    def item_from_iterable_to_dict(domains_description):
        list_of_descriptions_of_domains = list()
        for domain_description in domains_description:
            dict_of_items = dict()
            for item in domain_description.attributes.items():
                dict_of_items[item[0]]=item[1]
            list_of_descriptions_of_domains.append(dict_of_items)
        return list_of_descriptions_of_domains
    """

    @staticmethod
    def ToDict(description):
        dict_of_items = defaultdict()
        #for item in description.attributes.items():
        #    dict_of_items[item[0]] = item[1]
        for attr in range(len(description.items())):
            for value in range(len(description.items()[attr])):
                dict_of_items[description.items()[attr]].update(description.items()[attr][value])
        return dict_of_items