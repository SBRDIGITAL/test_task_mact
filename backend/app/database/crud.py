from typing import Type, TypeVar, Generic, List, Optional

from sqlalchemy import Engine, Table
from sqlalchemy import insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from pydantic import BaseModel

from database.sessions.sqlite_engine import engine
from database.tables.tables_data import Tables, metadata_obj



class DataBaseCRUD:
    
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

    def insert_one(self, table: Table, **kwargs) -> BaseModel:
        """ ## Добавление одной записи в базу данных. """
        try:
            with self.get_session() as session:
                with session.begin():
                    stmt = insert(table).values(**kwargs)
                    session.execute(stmt)
                    
        except IntegrityError as ex:
            raise ex

        except Exception as ex:
            raise ex
    
    def insert_many(self, table: Table, data: list[dict]) -> None:
        """ ## Пакетная вставка записей в базу данных.
        
        Args:
            table (Table): SQLAlchemy объект таблицы.
            data (list[dict]): Список словарей с данными для вставки.
        """
        if not data:
            return  # Нечего вставлять

        try:
            with self.get_session() as session:
                with session.begin():
                    stmt = insert(table)
                    session.execute(stmt, data)  # Передаём список словарей
                    
        except IntegrityError as ex:
            raise ex
        
        except Exception as ex:
            raise ex
    
    def get_session(self) -> Session:
        """ ## Получение сессии для работы с базой данных. """
        return Session(bind=self.engine)
    
    
db_crud = DataBaseCRUD(engine)