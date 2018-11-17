from head import primary_key
from XDB_to_RAM.exceptions import Exceptions

class fields():
    id = 0
    primary_key = primary_key("id")

    def __init__(self, domain_id, table_id, position, name, russian_short_name, uuid, id=None, description=None,
                 can_input=None, can_edit=None, show_in_grid=None, show_in_detailes=None, is_mean=None,
                 autocalculated=None, required=None):

        try:
            if id is None:
                raise Exceptions.IsNull("id")
            if domain_id is None:
                raise Exceptions.IsNull("domain_id")
            self.domain_id = domain_id
            if table_id is None:
                raise Exceptions.IsNull("table_id")
            self.table_id = table_id
            if position is None:
                raise Exceptions.IsNull("position")
            self.position = position
            if name is None:
                raise Exceptions.IsNull("name")
            self.name = name
            if russian_short_name is None:
                raise Exceptions.IsNull("russian_short_name")
            if uuid is None:
                raise Exceptions.IsNull("uuid")
        except Exceptions.IsNull as error:
            error.message()

        self.id = id

        self.description = description

        self.can_input = can_input
        self.can_edit = can_edit
        self.show_in_grid = show_in_grid
        self.show_in_details = show_in_detailes
        self.is_mean = is_mean
        self.autocalculated = autocalculated
        self.required = required

    def inc(self):
        id += 1

    """

create index "idx.7UAKR6FT7" on dbd$fields(table_id);
create index "idx.7HJ6KZXJF" on dbd$fields(position);
create index "idx.74RSETF9N" on dbd$fields(name);
create index "idx.6S0E8MWZV" on dbd$fields(domain_id);
create index "idx.88KWRBHA7" on dbd$fields(uuid);

    """
