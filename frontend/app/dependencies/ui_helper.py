from typing import Optional

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit, QSpinBox, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from config.paths import StaticFilesPaths



class UIHelper:
    """
    ## Вспомогательный класс для управления `UI` компонентами `PyQt6` приложения.
    """
    def __init__(self,
        app: QWidget,
        page_update_method,
        send_data,
        get_data,
        window_title: str = 'Тут название поменяешь',
        window_size: list[int] = [100, 100, 600, 500]
    ) -> None:
        """
        ## Инициализирует `UIHelper` с указанными параметрами.

        Args:
            app (QWidget): Основное окно приложения.
            page_update_method (Callable): Метод обновления страницы.
            send_data (Callable): Метод отправки данных в API.
            get_data (Callable): Метод получения данных из API.
            window_title (str): Заголовок окна. По умолчанию 'Тут название поменяешь'.
            window_size (list[int]): Размеры окна [x, y, width, height]. По умолчанию [100, 100, 600, 500].
        """      
        self.app = app
        self.update_page = page_update_method  # метод обновления layout
        self.send_data = send_data  # метод отправки данных к API
        self.get_data = get_data  # метод получения данных от API
        self.window_title = window_title
        self.window_size = window_size
        self.layout: Optional[QVBoxLayout] = None
        self.pagination_layout: Optional[QHBoxLayout] = None
    
    def __set_window(self) -> None:
        """
        ## Устанавливает заголовок и размеры главного окна приложения.
        """     
        self.app.setWindowTitle(self.window_title)
        self.app.setGeometry(*self.window_size)
    
    def __create_layout(self) -> None:
        """
        ## Создаёт основной и дополнительный контейнеры для размещения элементов `UI`.
        """       
        self.layout = QVBoxLayout()  # Главный контейнер
        self.pagination_layout = QHBoxLayout()  # Контейнер для пагинации (страница + количество элементов)
    
    def __create_line_edit(self) -> None:
        """
        ## Создаёт поле ввода текста `QLineEdit` для ввода имени, фамилии и никнейма.
        """
        self.line_edit = QLineEdit(self.app)
        self.line_edit.setPlaceholderText('Тут текст введёшь с пробелами в формате: имя фамилия никнейм(можно без никнейма)')

    def __create_placeholder_label(self):
        """
        ## Создаёт `QLabel` для отображения вспомогательного текста.
        """
        self.app.placeholder_label = QLabel('Тут данные посмотришь 👇', self.app)
        self.app.placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем текст

    def __create_data_getted_field(self):
        """
        ## Создаёт `QTextEdit` для отображения полученных данных из `API`.
        """
        self.app.text_edit = QTextEdit(self.app)
        self.app.text_edit.setReadOnly(True)

    def __create_pagination_selector(self):
        """
        ## Создаёт `QSpinBox` для выбора страницы пагинации и привязывает его к обновлению страницы.
        """
        self.app.pagination_spinbox = QSpinBox(self.app)
        self.app.pagination_spinbox.setMinimum(1)
        self.app.pagination_spinbox.setValue(1)  # Начальная страница - 1
        self.app.pagination_spinbox.setPrefix("Страница: ")
        self.app.pagination_spinbox.valueChanged.connect(self.update_page)
    
    def __create_elements_count_perpage_selector(self):
        """
        ## Создаёт `QSpinBox` для выбора количества элементов на странице и привязывает его к обновлению страницы.
        """
        self.app.page_size_spinbox = QSpinBox(self.app)
        self.app.page_size_spinbox.setMinimum(1)  # Минимум 1 элемент
        self.app.page_size_spinbox.setMaximum(100)  # Ограничение на 100 элементов
        self.app.page_size_spinbox.setValue(5)  # По умолчанию 5 элементов на страницу
        self.app.page_size_spinbox.setPrefix("Кол-во: ")  # Префикс
        self.app.page_size_spinbox.valueChanged.connect(self.update_page)
    
    def __create_send_data_button(self):
        """
        ## Создаёт кнопку для отправки данных в `API` (`POST` запрос).
        """
        self.app.send_data_button = QPushButton('Тут данные отправишь (POST)', self.app)
        self.app.send_data_button.clicked.connect(self.send_data)
    
    def __create_get_data_button(self):
        """
        ## Создаёт кнопку для получения данных из `API` (`GET` запрос).
        """
        self.app.get_data_button = QPushButton('Тут данные получишь (GET)', self.app)
        self.app.get_data_button.clicked.connect(lambda: self.get_data(self.app.pagination_spinbox.value()))
    
    def layout_add_widgets(self, widgets: list):
        """
        ## Добавляет переданный список виджетов в главный `layout`.
        
        Args:
            widgets (list): Список виджетов для добавления.
        """
        [self.layout.addWidget(w) for w in widgets] 
        # Добавляем горизонтальный layout в основной layout
        self.layout.addLayout(self.pagination_layout)  
        self.app.setLayout(self.layout)
    
    def initUI(self) -> None:
        """
        ## Инициализирует пользовательский интерфейс, \
        создавая все необходимые элементы и размещая их в макете.
        """     
        self.__set_window()
        self.__create_layout()
        self.__create_line_edit()
        self.__create_placeholder_label()
        self.__create_data_getted_field()
        self.__create_pagination_selector()
        self.__create_elements_count_perpage_selector()
        self.__create_send_data_button()
        self.__create_get_data_button()
        self.app.setWindowIcon(QIcon(StaticFilesPaths.MAIN_ICON_PATH))  # Устанавливаем icon