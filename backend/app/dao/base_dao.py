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
       
        
        
base_dao = BaseDAO()