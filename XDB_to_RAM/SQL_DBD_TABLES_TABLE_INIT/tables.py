from head import primary_key
from XDB_to_RAM.exceptions import Exceptions

class tables():
    id = 0
    primary_key=primary_key("id")
    def __init__(self,name, uuid,  id = None, schema_id = None,  description = None, can_add = None,
                 can_edit = None, can_delete = None, temporal_node = None, means = None):
        id = id
        self.shema_id = schema_id
        self.name = name
        self.description = description
        self.can_add = can_add
        self.can_edit = can_edit
        self.can_delete = can_delete
        self.temporal_mode = temporal_node
        self.means = means
        self.uuid = uuid
    def inc(self):
        id+=1

    """
    create index "idx.GCOFIBEBJ" on dbd$tables(name);
    create index "idx.2J02T9LQ7" on dbd$tables(uuid);
    """

