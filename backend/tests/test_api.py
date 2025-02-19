from asyncio import run
from traceback import print_exc
from types import NoneType

from aiohttp_client.app.app import AsyncHttpClient



class ApiClient:
    """
    ## Класс ApiClient для взаимодействия с `API`.

    Attributes:
        BASE_URL (str): Базовый URL для API.
        USERS_ROUTER (str): Путь к маршруту пользователей.
        client (AsyncHttpClient): Экземпляр клиента для выполнения `HTTP`-запросов.
    """
    BASE_URL = 'http://127.0.0.1:8000/'
    USERS_ROUTER = 'users/'
    client = AsyncHttpClient()
    
    @classmethod
    async def get_users(cls, endpoint: str = 'get_users') -> dict:
        """
        ## Получает список пользователей из `API`.

        Args:
            endpoint (str, optional): Конечная точка для получения пользователей. По умолчанию 'get_users'.

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.

        Returns:
            dict: Ответ API, содержащий информацию о пользователях.
        """        
        try:
            return await cls.client.fetch(
                url=f'{cls.BASE_URL}{cls.USERS_ROUTER}{endpoint}',
                method='GET', mode='JSON',
            )
        
        except Exception as ex:
            raise ex


class Tester:
    """
    ## Класс `Tester` для выполнения тестов `API`.
    """
    
    @classmethod
    async def test_get_users(cls) -> None:
        """
        ## Тестирует метод `get_users` класса `ApiClient`.

        Raises:
            AssertionError: Если проверки не проходят.
        """       
        res = await ApiClient.get_users()
        total_count = res.get('total_count')
        users = res.get('users')
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
    
    @classmethod    
    async def run_tests(cls) -> None:
        """
        ## Запускает все тесты.

        Returns:
            None
        """      
        await cls.test_get_users()



if __name__ == '__main__':
    try:
        run(Tester.run_tests())
    except:
        print_exc()