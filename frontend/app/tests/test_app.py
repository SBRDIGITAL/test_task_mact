import unittest
from unittest.mock import patch, MagicMock
from PyQt6.QtWidgets import QMessageBox
from app.dependencies.app import MyApp



class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        self.app = MyApp(proto='http', base_url='127.0.0.1:8000')

    @patch("app.my_app.Requester.send_request")
    def test_send_data_success(self, mock_send_request):
        """Тест успешной отправки данных"""
        mock_send_request.return_value = {"status": 200}
        self.app.ui_helper = MagicMock()
        self.app.ui_helper.line_edit.text.return_value = "John Doe"

        with patch.object(QMessageBox, "information") as mock_info:
            self.app.send_data()
            mock_info.assert_called_with(self.app, '✅', 'Пользователь успешно создан!')

    @patch("app.my_app.Requester.send_request")
    def test_send_data_empty_input(self, mock_send_request):
        """Тест отправки данных при пустом вводе"""
        self.app.ui_helper = MagicMock()
        self.app.ui_helper.line_edit.text.return_value = ""

        with patch.object(QMessageBox, "warning") as mock_warn:
            self.app.send_data()
            mock_warn.assert_called_with(self.app, 'Ошибка', 'Поле ввода не может быть пустым.')

    @patch("app.my_app.Requester.send_request")
    def test_send_data_api_error(self, mock_send_request):
        """Тест ошибки при отправке данных (API не возвращает 200)"""
        mock_send_request.return_value = {"status": 500}
        self.app.ui_helper = MagicMock()
        self.app.ui_helper.line_edit.text.return_value = "John Doe"

        with patch.object(QMessageBox, "warning") as mock_warn:
            self.app.send_data()
            mock_warn.assert_called()

    @patch("app.my_app.Requester.send_request")
    def test_get_data_success(self, mock_send_request):
        """Тест успешного получения данных"""
        mock_send_request.return_value = {"users": [{"first_name": "John", "last_name": "Doe"}]}
        self.app.text_edit = MagicMock()
        self.app.get_data()
        self.app.text_edit.setText.assert_called()

    @patch("app.my_app.Requester.send_request")
    def test_get_data_api_failure(self, mock_send_request):
        """Тест ошибки при получении данных (не JSON)"""
        mock_send_request.return_value = "Invalid response"
        with patch.object(QMessageBox, "warning") as mock_warn:
            self.app.get_data()
            mock_warn.assert_called_with(self.app, 'Ошибка', 'Ответ сервера не является JSON-объектом.')


# if __name__ == "__main__":
#     unittest.main()