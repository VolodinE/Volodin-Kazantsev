from xml_classes import *


default_way="materials/tasks.xdb"

#xdb_file1 = open(default_way)
schema1 = sc_test(default_way)
#xdb_file1.close()

#xdb_file2 = open(default_way)
schema2=sc_test(default_way)
#xdb_file2.close()

print(schema1==schema2)