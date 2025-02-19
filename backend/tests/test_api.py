from typing import Optional
from datetime import datetime
import pytest

from asyncio import run
from types import NoneType
from traceback import print_exc

from aiohttp_client.app.app import AsyncHttpClient



class ApiClient:
    """
    ## Класс ApiClient для взаимодействия с `API`.

    Этот класс предоставляет методы для выполнения запросов к `API`, включая получение списка пользователей.

    Attributes:
        BASE_URL (str): Базовый URL для API.
        USERS_ROUTER (str): Путь к маршруту пользователей.
        client (AsyncHttpClient): Экземпляр клиента для выполнения `HTTP`-запросов.
    """
    BASE_URL = "http://127.0.0.1:8000/"
    USERS_ROUTER = "users/"
    client = AsyncHttpClient()
    
    @classmethod
    async def insert_users(cls, endpoint: str = "create_users", data: Optional[dict] = None):
        try:
            return await cls.client.fetch(
                url=f'{cls.BASE_URL}{cls.USERS_ROUTER}{endpoint}',
                method="POST", mode="JSON", json=data
            )
        
        except Exception as ex:
            raise ex
    
    @classmethod
    async def get_users(cls, endpoint: str = "get_users", params: Optional[dict] = None) -> dict:
        """
        ## Получает список пользователей из `API`.
        
        Этот метод отправляет `GET`-запрос к `API` для получения списка пользователей.

        Args:
            endpoint (str): Конечная точка для получения пользователей. По умолчанию 'get_users'.
            params (Optional[dict]): Параметры запроса.

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.

        Returns:
            dict: Ответ `API`, содержащий информацию о пользователях.
        """        
        try:
            return await cls.client.fetch(
                url=f'{cls.BASE_URL}{cls.USERS_ROUTER}{endpoint}',
                method="GET", mode="JSON", params=params
            )
        
        except Exception as ex:
            raise ex


class Tester:
    """
    ## Класс `Tester` для выполнения тестов `API`.

    Этот класс содержит методы для тестирования функциональности `API`, 
    включая проверку корректности данных, получаемых от `API`.
    """
    @pytest.mark.asyncio
    async def test_get_users(self) -> None:
        """
        ## Тестирует метод `get_users` класса `ApiClient`.

        Этот метод выполняет тестирование на корректность данных, получаемых 
        из `API`, проверяя типы и значения полей.

        Raises:
            AssertionError: Если проверки не проходят, выбрасывается ошибка 
                утверждения с описанием проблемы.
        """    
        res = await ApiClient.get_users()
        total_count = res.get("total_count")
        users = res.get("users")
        assert isinstance(res, dict), "Ответ должен быть словарем."
        assert isinstance(users, list), "Пользователи должны быть в виде списка."
        assert isinstance(total_count, int), "Общее количество должно быть целым числом."
        assert total_count >= 0, "Общее количество пользователей не может быть отрицательным."
        for user in users:
            assert isinstance(user, dict), "Пользователь в списке должен быть словарём"
            assert isinstance(user.get("id"), int), "Идентификатор обязательно должен быть int"
            assert isinstance(user.get("first_name", None), (NoneType, str,)), "Имя может быть NoneType или str"
            assert isinstance(user.get("last_name", None), (NoneType, str,)),  "Фамилия может быть NoneType или str"
            assert isinstance(user.get("nickname"), str), "Никнейм должен быть str"
    
    @pytest.mark.asyncio
    async def test_insert_users(self) -> None:
        """
        ## Тестирует метод `insert_users` класса `ApiClient`.

        Этот метод выполняет тестирование функциональности добавления пользователей в 
        базу данных через `API`. Он отправляет данные о пользователях и проверяет 
        корректность ответа от `API`.

        ### Raises:
            AssertionError: Если проверки не проходят, выбрасывается ошибка 
                утверждения с описанием проблемы.

        ### Returns:
            None
        """   
        data = {
            "users": [
                {
                    "first_name": "tester",
                    "last_name": "tester2",
                    "nickname": f"nickname_{int(datetime.now().timestamp())}"
                }
            ]
        }
        res = await ApiClient.insert_users(data=data)
        assert isinstance(res, dict), "Ответ должен быть словарём"
        status = res.get('status')
        assert isinstance(status, int), "Код ответа должен быть int"
        if status != 200:
            assert res.get("detail"), "Должно быть в ключе detail сообщение: 'Ошибка при сохранении пользователей.'"
        assert status == 200, "Код ответа должен быть 200" 
        assert res.get("message") == "Пользователи успешно добавлены в базу данных.", "Нет ответа о добавлении"
    
    @pytest.mark.asyncio
    async def test_get_users_pagination(self, page: int = 1, page_size: int = 2) -> None:
        """
        ## Тестирует пагинацию в методе `get_users` класса `ApiClient`.
        
        Этот тест проверяет, что `API` корректно обрабатывает параметры `page` и `page_size`.

        Args:
            page (int): номер страницы. Defaults to 1.
            page_size (int): количество элементов на страницу. Defaults to 2.
        """        
        res = await ApiClient.get_users(params={"page":page, "page_size": page_size})
        
        assert isinstance(res, dict), "Ответ должен быть словарем."
        assert isinstance(res.get("users"), list), "Пользователи должны быть в виде списка."
        assert len(res.get("users")) <= page_size, "Количество пользователей не должно превышать page_size."
        total_count = res.get("total_count")
        assert isinstance(total_count, int), "Общее количество должно быть целым числом."
        assert total_count >= 0, "Общее количество пользователей не может быть отрицательным."
    
    @pytest.mark.asyncio 
    async def run_tests(self) -> None:
        """
        ## Запускает все тесты.

        Этот метод инициирует выполнение всех тестов, определённых в классе `Tester`.
        """      
        await self.test_get_users()
        await self.test_insert_users()
        await self.test_get_users_pagination()



if __name__ == '__main__':
    try:
        tester = Tester()
        run(tester.run_tests())
    except:
        print_exc()