from typing import Any, Optional
from sqlalchemy import Table

from database.crud import db_crud



class BaseDAO:
    
    def __init__(self) -> None:
        """ ## Инициализация класса. """
        self.db = db_crud
    
    def insert_one(self, table: Table, **kwargs) -> None:
        """
        ## Добавление одной записи в базу данных.

        Args:
            table (Table): _description_
        """        
        self.db.insert_one(table=table, **kwargs)

    def insert_many(self, table: Table, data: list[dict]) -> None:
        """
        ## Пакетная вставка записей в базу данных.

        Args:
            table (Table): _description_
            data (list[dict]): _description_
        """        
        self.db.insert_many(table=table, data=data)
    
    def get_one(self, table: Table, **kwargs) -> Optional[Any]:
        """ 
        ## Получение одной записи из базы данных по заданным условиям.

        Args:
            table (Table): SQLAlchemy объект таблицы.
            **kwargs: Условия для фильтрации записи.

        Returns:
            Optional[Any]: Найденная запись или None, если запись не найдена.
        """
        return self.db.get_one(table=table, **kwargs)

    def get_many(self, table: Table, **kwargs) -> list[Any]:
        """ 
        ## Получение нескольких записей из базы данных по заданным условиям.

        Args:
            table (Table): SQLAlchemy объект таблицы.
            **kwargs: Условия для фильтрации записей.

        Returns:
            list[Any]: Список найденных записей.
        """
        return self.db.get_many(table=table, **kwargs)
       
        
        
base_dao = BaseDAO()