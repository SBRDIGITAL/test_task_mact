from os.path import dirname, abspath, join

class DirPaths:
    BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
    print(f'BASE_DIR: {BASE_DIR}')
    APPS_DIR = join(BASE_DIR, 'app')
    CONFIG_DIR = join(APPS_DIR, 'config')
    TEMPLATES_DIR = join(APPS_DIR, 'templates')
    STATIC_DIR = join(APPS_DIR, 'static')
    MEDIA_DIR = join(APPS_DIR, 'media')
    DATABASE_DIR = join(APPS_DIR, 'database')
    DB_DIR = join(DATABASE_DIR, 'db')
    # LOGS_DIR = join(APPS_DIR, 'logs')
    # FIXTURES_DIR = join(APPS_DIR, 'fixtures')
    
    
class FilesPaths:
    DB_FILE = join(DirPaths.DB_DIR, 'sqlite3.db')