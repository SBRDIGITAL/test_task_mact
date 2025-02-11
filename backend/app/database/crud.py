from typing import Type, TypeVar, Generic, List, Optional

from sqlalchemy import Engine, Table
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database.sessions.sqlite_engine import engine
from database.tables.tables_data import Tables, metadata_obj



class CRUDBase:
    
    def __init__(self, engine: Engine) -> None:
        """ ## Инициализация класса. """
        self.engine = engine
    
    def __create_tables(self) -> None:
        """ ## Создание таблиц в базе данных. """
        metadata_obj.create_all(self.engine)
    
    def __drop_tables(self) -> None:
        """ ## Удаление таблиц из базы данных. """
        metadata_obj.drop_all(self.engine)  
    
    def start(self, drop_tables: bool = False) -> None:
        """ ## Запуск работы с базой данных. """
        if drop_tables:
            self.__drop_tables()
        else:
            self.__create_tables()

    def insert(self, table: Table, **kwargs) -> BaseModel:
        """ ## Добавление записи в базу данных. """
        with self.get_session() as session:
            with session.begin():
                instance = table(**kwargs)
                session.add(instance)

    def get_session(self) -> Session:
        """ ## Получение сессии для работы с базой данных. """
        return Session(bind=self.engine)
    
    
crud = CRUDBase(engine)