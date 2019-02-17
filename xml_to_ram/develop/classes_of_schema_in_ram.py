
class table:
    def __init__(self, items):
        self.pk = primare_key("table")
        self.description = (items)

        def __hash__(self):
            return hash(self.description, )

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


class domain:
    def __init__(self,items):
        self.primary_key = primare_key("domain")
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
    def __init__(self,items,table_id):
        self.pk = primare_key("field")
        self.description = dict(items)
        self.table_id = table_id
    def __hash__(self):
        return hash(tuple(self.description,))

    def __eq__(self, other):
        if (
            self.table_id == other.table_id and
            self.description == other.description):
            return True
        else:
            return False

    # def print_field(self):
    #     print(self.description)
