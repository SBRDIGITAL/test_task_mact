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
        
        
        
user_dao = UserDAO()