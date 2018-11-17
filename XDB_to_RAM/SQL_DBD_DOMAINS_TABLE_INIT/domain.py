from collections import namedtuple

"""\
pragma foreign_keys = on;

begin transaction;

--
-- Каталог схем для таблиц
--
create table dbd$schemas (
    id integer primary key autoincrement not null,
    name varchar not null -- имя схемы
);
"""


