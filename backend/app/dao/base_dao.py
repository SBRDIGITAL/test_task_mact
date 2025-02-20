from typing import Any, Optional
from sqlalchemy import Table

from database.crud import db_crud



class BaseDAO:
    """
    ## Базовый `Data Acces Object` для работы с базой данных.

    Этот класс предоставляет методы для выполнения основных операций с базой данных,
    таких как вставка, получение и фильтрация записей.

    Attributes:
        db: Объект для взаимодействия с базой данных, предоставляющий `CRUD`-операции.
    """
    
    def __init__(self) -> None:
        """ 
        ## Инициализация класса.

        Инициализирует объект для работы с базой данных.
        """
        self.db = db_crud
    
    def insert_one(self, table: Table, **kwargs) -> None:
        """
        ## Добавление одной записи в указанную таблицу.

        Args:
            table (Table): SQLAlchemy объект таблицы, в которую будет добавлена запись.
            **kwargs: Параметры записи в виде ключевых аргументов.
                      Ключи должны соответствовать названиям колонок таблицы.

        Example:
            >>> dao = BaseDAO()
            >>> dao.insert_one(user_table, name="John", age=30)
        """      
        self.db.insert_one(table=table, **kwargs)

    def insert_many(self, table: Table, data: list[dict]) -> None:
        """
        ## Пакетная вставка нескольких записей в указанную таблицу.

        Args:
            table (Table): SQLAlchemy объект таблицы, в которую будут добавлены записи.
            data (list[dict]): Список словарей, где каждый словарь представляет одну запись.
                               Ключи словарей должны соответствовать названиям колонок таблицы.

        Example:
            >>> dao = BaseDAO()
            >>> dao.insert_many(user_table, [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}])
        """     
        self.db.insert_many(table=table, data=data)
    
    def get_one(self, table: Table, **kwargs) -> Optional[Any]:
        """ 
        ## Получение одной записи из таблицы по заданным условиям.

        Args:
            table (Table): SQLAlchemy объект таблицы, из которой будет получена запись.
            **kwargs: Условия для фильтрации записи. Ключи должны соответствовать названиям колонок таблицы.

        Returns:
            Optional[Any]: Найденная запись или None, если запись не найдена.

        Example:
            >>> dao = BaseDAO()
            >>> user = dao.get_one(user_table, id=1)
            >>> print(user)
            {'id': 1, 'name': 'John', 'age': 30}
        """
        return self.db.get_one(table=table, **kwargs)

    def get_all(self, table: Table, **kwargs) -> list[Any]:
        """ 
        ## Получение всех записей из таблицы, соответствующих заданным условиям.

        Args:
            table (Table): SQLAlchemy объект таблицы, из которой будут получены записи.
            **kwargs: Условия для фильтрации записей. Ключи должны соответствовать названиям колонок таблицы.

        Returns:
            list[Any]: Список найденных записей. Если записи не найдены, возвращается пустой список.

        Example:
            >>> dao = BaseDAO()
            >>> users = dao.get_all(user_table, age=30)
            >>> print(users)
            [{'id': 1, 'name': 'John', 'age': 30}, {'id': 2, 'name': 'Jane', 'age': 30}]
        """
        return self.db.get_all(table=table, **kwargs)
       
        
        
base_dao = BaseDAO()