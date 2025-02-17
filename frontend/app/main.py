import sys, os
from datetime import datetime

from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QListView, QPushButton, QMessageBox, QLabel,
    QTextEdit,)
from PyQt6.QtCore import QStringListModel, Qt

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.api.api_config import ApiConfig
from utils.requests_utils import Requester




class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.click_count = 0
        self.api_config = ApiConfig(proto='http', base_url='127.0.0.1:8000')
        self.requester = Requester(self.api_config)
        self.data_getted = False

    def initUI(self):
        self.setWindowTitle('Тут название поменяешь')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText('Тут текст введёшь')
        layout.addWidget(self.line_edit)

        # Создаем QLabel для плейсхолдера
        self.placeholder_label = QLabel('Тут данные посмотришь 👇', self)
        self.placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем текст
        layout.addWidget(self.placeholder_label)
        
        self.list_view = QListView(self)
        self.model = QStringListModel()
        self.list_view.setModel(self.model)
        layout.addWidget(self.list_view)
        

        self.post_button = QPushButton('Отправить POST', self)
        self.post_button.clicked.connect(self.send_post_request)
        layout.addWidget(self.post_button)

        self.get_button = QPushButton('Получить данные (GET)', self)
        self.get_button.clicked.connect(self.send_get_request)
        layout.addWidget(self.get_button)

        self.setLayout(layout)

    def send_post_request(self):
        self.click_count += 1
        text = self.line_edit.text()
        current_time = datetime.now()
        data = {
            'text': text,
            'date': current_time.strftime('%Y-%m-%d'),
            'time': current_time.strftime('%H:%M:%S'),
            'click_count': self.click_count
        }

        try:
            response = self.requester.send_request(method='POST', router='users', endpoint='post_data', json=data)
            if response and response.get('status') == 'success':  # Предполагается, что сервер возвращает статус
                QMessageBox.information(self, 'Успех', 'Данные успешно отправлены!')
            else:
                QMessageBox.warning(self, 'Ошибка', 'Не удалось отправить данные.')
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Произошла ошибка: {str(e)}')

    def send_get_request(self):
        try:
            response = self.requester.send_request(method='GET', router='users', endpoint='get_users')
            
            # Отладочная информация
            print(f'Response from GET request: {response}')  # Выводим ответ в консоль для отладки
            
            if isinstance(response, dict) and 'users' in response:  # Проверяем, что ответ - это словарь и содержит ключ 'users'
                user_list = [f"{user['first_name']} {user['last_name']} ({user['nickname']})" for user in response['users'] if 'first_name' in user]
                self.model.setStringList(user_list)
            else:
                QMessageBox.warning(self, 'Ошибка', 'Не удалось получить данные. Ответ сервера не содержит пользователей.')
                
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Произошла ошибка: {str(e)}')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())


""" 
Запуск:
Перейти в директорию frontend > app и запустить python.exe ./main.py
"""