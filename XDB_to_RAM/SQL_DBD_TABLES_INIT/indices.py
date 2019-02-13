from head import primary_key
from XDB_to_RAM.exceptions import Exceptions

class indices():
    id = 0
    primary_key= primary_key("id")
    def __init__(self, table_id, uuid, name=None, local=None, kind=None):
        self.id = self.inc(id)
        self.table_id = table_id
        self.name = name
        self.local = local
        self.kind = kind
        self.uuid = uuid

    def inc(self):
        id += 1
        return id


"""

create index "idx.12XXTJUYZ" on dbd$indices(table_id);
create index "idx.6G0KCWN0R" on dbd$indices(name);
create index "idx.FQH338PQ7" on dbd$indices(uuid);

"""


class index_details():
    id = 0
    primary_key = primary_key("id")

    def __init__(self, index_id, position, field_id=None, expression=None, descend=None):
        self.id = self.inc(id)
        self.index_id = index_id
        self.position = position
        self.field_id = field_id
        self.expression = expression
        self.descend = descend

    def inc(self):
        id += 1
        return id

    """

create index "idx.H1KFOWTCB" on dbd$index_details(index_id);
create index "idx.BQA4HXWNF" on dbd$index_details(field_id);
"""

