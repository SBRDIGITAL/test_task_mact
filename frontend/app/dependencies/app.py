import json
from typing import Optional

from datetime import datetime

from PyQt6.QtWidgets import QWidget, QMessageBox

from config.api.api_config import ApiConfig
from utils.requests_utils import Requester

from config.literals import AppLiterals as AL

from .ui_helper import UIHelper



class MyApp(QWidget):
    """
    ## Основной класс приложения, реализующий графический интерфейс и взаимодействие с `API`.
    """
    def __init__(self, proto: AL.Proto, base_url: str) -> None:
        """
        ## Инициализирует объект `MyApp`.
        
        Создает конфигурацию `API`, объект запроса, инициализирует интерфейс.
        """          
        super().__init__()
        
        self.click_count: int = 0
        self.data_getted: bool = False
        self.current_widget: Optional[QWidget] = None
        self.ui_helper: Optional[UIHelper] = None
        self.api_config = ApiConfig(proto, base_url)
        self.requester = Requester(self.api_config)
        self.initUI()

    def initUI(self) -> None:
        """
        ## Инициализирует пользовательский интерфейс.
        
        Создает и настраивает элементы `UI`, передает их в `UIHelper`.
        """     
        ui_helper = UIHelper(self, self.update_page, self.send_data, self.get_data)
        ui_helper.initUI()
        widgets = [
            ui_helper.line_edit, ui_helper.app.placeholder_label, ui_helper.app.text_edit, 
            ui_helper.app.pagination_spinbox, ui_helper.app.page_size_spinbox, ui_helper.app.page_size_spinbox,
            ui_helper.app.send_data_button, ui_helper.app.get_data_button,
        ]
        ui_helper.layout_add_widgets(widgets)
        
        self.current_widget = ui_helper.app
        self.ui_helper = ui_helper

    def update_page(self) -> None:
        """
        ## Обновляет данные на текущей странице, запрашивая новые данные из `API`.
        
        Получает текущие значения страницы и количества элементов на странице, затем вызывает `get_data()`.
        """        
        page = self.pagination_spinbox.value()
        page_size = self.page_size_spinbox.value()
        self.get_data(page=page, page_size=page_size)

    def send_data(self) -> None:
        """
        ## Отправляет данные о новом пользователе на сервер через `API`.
        
        Извлекает данные из поля ввода, проверяет их и отправляет `POST`-запрос.
        В случае успеха отображает сообщение, иначе предупреждение или ошибку.
        """       
        try:
            self.click_count += 1
            text = self.ui_helper.line_edit.text().strip()

            if not text:
                QMessageBox.warning(self, 'Ошибка', 'Поле ввода не может быть пустым.')
                return

            current_time = datetime.now()
            splitted_text = text.split()
            
            try:  # получаем никнейм, либо генерим его
                nick_name = splitted_text[3]
            except IndexError:
                nick_name = f"user_{current_time.strftime('%H%M%S')}"
            
            print(f'{splitted_text=}')
            data = {
                "users": [
                    {
                        "first_name": splitted_text[0] if " " in text else text,  # Разбиваем строку на имя и фамилию
                        "last_name": splitted_text[1] if " " in text else None,
                        "nickname": nick_name
                    }
                ]
            }

            response = self.requester.send_request(method='POST', router='users', endpoint='create_users', data=data)
            if response and response.get('status') == 200:  
                QMessageBox.information(self, '✅', 'Пользователь успешно создан!')
            else:
                QMessageBox.warning(self, 'Ошибка', f'Ошибка создания пользователя: {response}')

        except Exception as ex:
            QMessageBox.critical(self, 'Ошибка', f'Произошла ошибка: {ex}')

    def get_data(self, page: int = 1, page_size: int = 5) -> None:
        """
        ## Запрашивает данные пользователей с сервера с учетом пагинации.
        
        Args:
            page (int): Номер страницы. По умолчанию 1.
            page_size (int): Количество элементов на странице. По умолчанию 5.
        
        Отправляет `GET`-запрос к `API`, форматирует полученные данные и отображает их.
        В случае ошибки отображает предупреждение или критическое сообщение.
        """      
        try:
            params = {"page": page, "page_size": page_size}
            response = self.requester.send_request(method='GET', router='users', endpoint='get_users', params=params)
            
            if isinstance(response, dict):  # Проверяем, что ответ - это словарь
                formatted_json = json.dumps(response, indent=4, ensure_ascii=False)  # Форматируем JSON с отступами
                self.text_edit.setText(formatted_json)  # Отображаем в QTextEdit
            else:
                QMessageBox.warning(self, 'Ошибка', 'Ответ сервера не является JSON-объектом.')

        except Exception as ex:
            QMessageBox.critical(self, 'Ошибка', f'Произошла ошибка: {ex}')