from head import primary_key
from XDB_to_RAM.exceptions import Exceptions

class constraints():
    id = 0
    primary_key= primary_key("id")
    def __init__(self, table_id, uuid, id=None, name=None, constraint_type=None, reference=None,
                 unique_key_id=None, has_value_edit=None, cascading_delete=None, expression=None,
                 ):
        self.id = id + 1
        self.table_id = table_id
        self.name = name
        self.constraint_type = constraint_type
        self.reference = reference
        self.unique_key_id = unique_key_id
        self.has_value_edit = has_value_edit
        self.cascading_delete = cascading_delete
        self.expression = expression
        self.uuid = uuid
        """

create index "idx.6F902GEQ3" on dbd$constraints(table_id);
create index "idx.6SRYJ35AJ" on dbd$constraints(name);
create index "idx.62HLW9WGB" on dbd$constraints(constraint_type);
create index "idx.5PQ7Q3E6J" on dbd$constraints(reference);
create index "idx.92GH38TZ4" on dbd$constraints(unique_key_id);
create index "idx.6IOUMJINZ" on dbd$constraints(uuid);

        """


class constraint_details():
    id = 0
    primary_key = primary_key("id")

    def __init__(self, constraint_id, position, field_id):
        self.id = self.inc(id)
        self.constraint_id = constraint_id
        self.position = position
        self.field_id = field_id

    def inc(self):
        id += 1
        return (id)


"""

create index "idx.5CYTJWVWR" on dbd$constraint_details(constraint_id);
create index "idx.507FDQDMZ" on dbd$constraint_details(position);
create index "idx.4NG17JVD7" on dbd$constraint_details(field_id);

"""

