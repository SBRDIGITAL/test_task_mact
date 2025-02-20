from os.path import dirname, abspath, join


class DirPaths:
    """
    ## DirPaths

    Класс, содержащий пути к основным директориям проекта.

    Attributes:
        BASE_DIR (str): Основной каталог проекта, полученный из текущего файла.
        APPS_DIR (str): Каталог приложения, находящийся в BASE_DIR.
        CONFIG_DIR (str): Каталог конфигурации, находящийся в APPS_DIR.
        DATABASE_DIR (str): Каталог базы данных, находящийся в APPS_DIR.
        DB_DIR (str): Каталог, содержащий файлы базы данных, находящийся в DATABASE_DIR.
    """
    # BASE_DIR = dirname(dirname(dirname(__file__)))
    BASE_DIR = join('.')
    print(f'{BASE_DIR=}')
    APPS_DIR = join(BASE_DIR, 'app')
    CONFIG_DIR = join(APPS_DIR, 'config')
    DATABASE_DIR = join(APPS_DIR, 'database')
    DB_DIR = join(DATABASE_DIR, 'db')

    
class FilesPaths:
    """
    ## FilesPaths

    Класс, содержащий пути к файлам, используемым в приложении.

    Attributes:
        DB_FILE (str): Полный путь к файлу базы данных `SQLite`, находящемуся в `DB_DIR`.
    """
    DB_FILE = join(DirPaths.DB_DIR, 'sqlite3.db')
    print(f'{DB_FILE=}')