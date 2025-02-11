from typing import Optional, Any

from sqlalchemy import Table

from dao.base_dao import BaseDAO
from database.tables.tables_data import Tables



class UserDAO(BaseDAO):
    
    def __init__(self) -> None:
        """ ## Инициализация класса. """
        super().__init__()
        self.table: Table = Tables.user_table
    
    def insert_user(self, **kwargs) -> None:
        """
        ## Добавление одного пользователя в базу данных.
        
        Args:
            table (Table): _description_
        """        
        self.insert_one(self.table, **kwargs)

    def insert_users(self, data: list[dict]) -> None:
        """
        ## Добавление списка пользователей в базу данных.

        Args:
            table (Table): _description_
            data (list[dict]): _description_
        """        
        self.insert_many(self.table, data=data)
        
    def get_user(self, **kwargs) -> Optional[Any]:
        """ 
        ## Получение одного пользователя из базы данных по заданным условиям.

        Args:
            **kwargs: Условия для фильтрации пользователя.

        Returns:
            Optional[BaseModel]: Найденный пользователь или None, если пользователь не найден.
        """
        return self.get_one(self.table, **kwargs)

    def get_all_users(self, **kwargs) -> list[Any]:
        """ 
        ## Получение всех пользователей из базы данных по заданным условиям.

        Args:
            **kwargs: Условия для фильтрации пользователей.

        Returns:
            ListUsersWithIdModel: Список найденных пользователей.
        """
        return self.get_many(self.table, **kwargs)


  
user_dao = UserDAO()