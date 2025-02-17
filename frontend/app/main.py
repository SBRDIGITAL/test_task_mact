import sys, os

from PyQt6.QtWidgets import QApplication

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dependencies.app import MyApp



class StartUp:
    """
    ## StartUp

    Класс, отвечающий за инициализацию и запуск приложения.

    Методы:
        start(): Запускает приложение, создавая экземпляр `QApplication` и отображая главное окно.
    """
    
    @staticmethod
    def start():
        """ 
        ## Запуск приложения

        Перейдите в директорию `frontend > app` и запустите `python.exe ./main.py`.

        Этот метод создает экземпляр `QApplication`, инициализирует главное окно приложения
        с помощью класса `MyApp`, отображает его и запускает главный цикл обработки событий.

        Примечание:
            Этот метод должен вызываться, когда скрипт запускается напрямую.
        """
        app = QApplication(sys.argv)
        ex = MyApp()
        ex.show()
        sys.exit(app.exec())



if __name__ == '__main__':
    StartUp.start()