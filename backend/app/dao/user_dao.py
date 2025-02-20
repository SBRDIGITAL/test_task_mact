from typing import Optional, Any

from sqlalchemy import Table

from dao.base_dao import BaseDAO
from database.tables.tables_data import Tables



class UserDAO(BaseDAO):
    """
    ## Класс для работы с данными пользователей в базе данных.

    Этот класс предоставляет методы для выполнения операций с таблицей пользователей,
    таких как добавление, получение и фильтрация записей.

    Attributes:
        table (Table): `SQLAlchemy` объект таблицы пользователей.
    """
    def __init__(self) -> None:
        """ 
        ## Инициализация класса.

        Инициализирует объект для работы с таблицей пользователей.
        """
        super().__init__()
        self.table: Table = Tables.user_table
    
    def insert_user(self, **kwargs) -> None:
        """
        ## Добавление одного пользователя в таблицу пользователей.

        Args:
            **kwargs: Параметры пользователя в виде ключевых аргументов.
                Ключи должны соответствовать названиям колонок таблицы пользователей.

        Example:
            >>> user_dao = UserDAO()
            >>> user_dao.insert_user(name="John", age=30, email="john@example.com")
        """       
        self.insert_one(self.table, **kwargs)

    def insert_users(self, data: list[dict]) -> None:
        """
        ## Пакетное добавление нескольких пользователей в таблицу пользователей.

        Args:
            data (list[dict]): Список словарей, где каждый словарь представляет одного пользователя.
                Ключи словарей должны соответствовать названиям колонок таблицы пользователей.

        Example:
            >>> user_dao = UserDAO()
            >>> users_data = [
            ...     {"name": "John", "age": 30, "email": "john@example.com"},
            ...     {"name": "Alice", "age": 25, "email": "alice@example.com"}
            ... ]
            >>> user_dao.insert_users(users_data)
        """     
        self.insert_many(self.table, data=data)
        
    def get_user(self, **kwargs) -> Optional[Any]:
        """ 
        ## Получение одного пользователя из таблицы по заданным условиям.

        Args:
            **kwargs: Условия для фильтрации пользователя. Ключи должны соответствовать названиям колонок таблицы.

        Returns:
            Optional[Any]: Найденный пользователь или None, если пользователь не найден.

        Example:
            >>> user_dao = UserDAO()
            >>> user = user_dao.get_user(id=1)
            >>> print(user)
            {'id': 1, 'name': 'John', 'age': 30, 'email': 'john@example.com'}
        """
        return self.get_one(self.table, **kwargs)

    def get_all_users(self, **kwargs) -> list[Any]:
        """ 
        ## Получение всех пользователей из таблицы, соответствующих заданным условиям.

        Args:
            **kwargs: Условия для фильтрации пользователей. Ключи должны соответствовать названиям колонок таблицы.

        Returns:
            list[Any]: Список найденных пользователей. Если пользователи не найдены, возвращается пустой список.

        Example:
            >>> user_dao = UserDAO()
            >>> users = user_dao.get_all_users(age=30)
            >>> print(users)
            [
                {'id': 1, 'name': 'John', 'age': 30, 'email': 'john@example.com'},
                {'id': 2, 'name': 'Jane', 'age': 30, 'email': 'jane@example.com'}
            ]
        """
        return self.get_all(self.table, **kwargs)


  
user_dao = UserDAO()