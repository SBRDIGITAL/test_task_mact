from os.path import dirname, abspath, join


class DirPaths:
    """
    ## DirPaths

    Класс, содержащий пути к основным директориям приложения.

    Attributes:
        BASE_DIR (str): Основной каталог проекта, полученный из текущего файла.
        APPS_DIR (str): Каталог приложения, находящийся в BASE_DIR.
        CONFIG_DIR (str): Каталог конфигурации, находящийся в APPS_DIR.
        STATIC_DIR (str): Каталог статических файлов, находящийся в APPS_DIR.
        IMAGES_DIR (str): Каталог изображений, находящийся в STATIC_DIR.
    """   
    BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
    print(f'BASE_DIR: {BASE_DIR}')
    APPS_DIR = join(BASE_DIR, 'app')
    CONFIG_DIR = join(APPS_DIR, 'config')
    STATIC_DIR = join(APPS_DIR, 'static')
    IMAGES_DIR = join(STATIC_DIR, 'img')


class StaticFilesName:
    """
    ## StaticFilesName

    Класс, содержащий имена статических файлов, используемых в приложении.

    Attributes:
        MAIN_ICON_FILE (str): Имя основного файла иконки приложения.
    """   
    MAIN_ICON_FILE = join('icon.png')    


class StaticFilesPaths:
    """
    ## StaticFilesPaths

    Класс, содержащий пути к статическим файлам приложения.

    Attributes:
        MAIN_ICON_PATH (str): Полный путь к основному файлу иконки приложения,
        сформированный на основе DirPaths и StaticFilesName.
    """   
    MAIN_ICON_PATH = join(DirPaths.IMAGES_DIR, StaticFilesName.MAIN_ICON_FILE)