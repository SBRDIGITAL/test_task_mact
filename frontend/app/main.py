import sys, os

from PyQt6.QtWidgets import QApplication

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.literals import AppLiterals as AL
from dependencies.app import MyApp



class StartUp:
    """
    ## StartUp

    Класс, отвечающий за инициализацию и запуск приложения.

    Методы:
        start(): Запускает приложение, создавая экземпляр `QApplication` и отображая главное окно.
    """
    
    @staticmethod
    def start(proto: AL.Proto = 'http', base_url: str = '127.0.0.1:8000'):
        """ 
        ## Запуск приложения

        Перейдите в директорию `frontend > app` и запустите `python.exe ./main.py`.

        Этот метод создает экземпляр `QApplication`, инициализирует главное окно приложения
        с помощью класса `MyApp`, передавая параметры `proto` и `base_url`,
        отображает его и запускает главный цикл обработки событий.

        Args:
            proto (AL.Proto): Протокол для API (по умолчанию 'http').
            base_url (str): Базовый URL для API (по умолчанию '127.0.0.1:8000').

        Примечание:
            Этот метод должен вызываться, когда скрипт запускается напрямую.
        """
        app = QApplication(sys.argv)
        ex = MyApp(proto, base_url)
        ex.show()
        sys.exit(app.exec())



if __name__ == '__main__':
    StartUp.start()