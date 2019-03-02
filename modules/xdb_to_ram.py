from collections import namedtuple

Table_content_description = namedtuple("Table_content_description","fields constraints indexes")

from collections import MutableSet
class OrderedSet(MutableSet):

    def __init__(self, iterable=None):
        self.end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

from xml.etree import ElementTree
from modules import classes


class XdbParser:
    def __init__(self,file):
        self.root = ElementTree.parse(file).getroot()
        self.domains = self.Domains()
        self.schema = self.Schema()
        self.tables = self.Tables()
        self.table_content_description = self.TableContent()

    def Schema(self):
        schema = OrderedSet()
        for dbd_schema in self.root.iter("dbd_schema"):
            schema.add(classes.schema(dbd_schema.attrib))

        return schema

    def Domains(self):
        domains = OrderedSet()
        for domain in self.root.iter("domain"):
            domains.add(classes.domain(domain.attrib))
        return domains

    def Tables(self):
        tables = OrderedSet()
        for table in self.root.iter("table"):
            tables.add(classes.table(table.attrib))
        tables=frozenset(tables)
        return tables

    def TableContent(self):
        fields = OrderedSet()
        indexes = OrderedSet()
        constraints = OrderedSet()
        for t in self.root:
            if(t.tag == "tables"):
                tables = t
                for table in tables:
                    for descripttion in table:
                        tag = descripttion.tag
                        table_name = table.attrib["name"]
                        if (tag == "field"):
                            fields.add(classes.field(descripttion.attrib, table_name))
                        elif (tag == "index"):
                            indexes.add(classes.index(descripttion.attrib, table_name))
                        elif (tag == "constraint"):
                            constraints.add(classes.constraint(descripttion.attrib, table_name))

                        #обр-ка некорр-го оп-я
        return Table_content_description(fields,constraints,indexes)

    def test(self):
        f=[]
        for i in self.table_content_description.fields:
            u = []
            for k in classes.attributes.field_attr:
                u.append((k,
                    getattr(i,k)
                    )
            )
            u.append(("table",getattr(i,"table"),))
          #  print(u)

        for i in self.domains:
            u = []
            for k in classes.attributes.domain_attr:
                u.append((k,
                    getattr(i,k)
                    )
            )
            for k in classes.attributes.domain_props:
                u.append((k,
                    getattr(i,k)
                    )
            )
#            u.append(("domain",getattr(i,"domain"),))
            print(u)

    def __eq__(self, other):
        if (
            self.domains == other.domains and
            self.tables == other.tables and
            self.table_content_description == other.table_content_description and
            self.schema == other.dbd_schema
        ):
            return True
        else:
            return False
