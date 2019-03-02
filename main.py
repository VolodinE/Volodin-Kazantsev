import argparse  # Загружаем стандартную библиотеку обработки параметров консоли
import os.path  # Загружаем модуль для работы с путями
from modules.ram_dbd import RamDbd  # Модуль конвертации ram->db
from modules.dbd_ram import DbdRam  # Модуль конвертации db->ram

from modules.xdb_to_ram import *

if __name__ == "__main__":
    #
    # Преобразование XDB -> RAM -> DBD
    #
    parser = argparse.ArgumentParser(description='Программа преобразования данных.')

    parser.add_argument('-f', '--file', default='materials/tasks.xdb',
                        help='Преобразование XDB -> RAM -> DBD.')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print("Файла {0} не существует.".format(args.file))
        exit(-1)

    ram = XdbParser(args.file)

#    ram2 = XdbParser("materials/tasks1.xdb")
#    print(ram == ram2)


    dbd_create = RamDbd(args.file.replace('.xdb', '.db'), ram)
