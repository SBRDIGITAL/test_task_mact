from typing import Any, Optional

from sqlalchemy import Engine, Table
from sqlalchemy import select, insert
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError, NoResultFound

from database.sessions.sqlite_engine import engine
from database.tables.tables_data import metadata_obj



class DataBaseManager:
    """
    ## Менеджер для работы с базой данных.
    
    ### Args:
        engine (Engine): Объект подключения к базе данных.
    
    ### Attributes:
        engine (Engine): Объект подключения к базе данных.
        session (Session): Сессия для работы с базой данных.
    
    ### Может:
        - создавать таблицы.
        - удалять таблицы.
        - возращать сессию для работы.
    """
    def __init__(self, engine: Engine) -> None:
        """ ## Инициализация класса."""
        self.engine = engine
        self.session = self.get_session()
    
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

    def get_session(self) -> Session:
        """ ## Получение сессии для работы с базой данных. """
        Session = sessionmaker(bind=self.engine)
        return Session()



class DataBaseCRUD(DataBaseManager):
    """ 
    ## `CRUD` для работы с базой данных.
    
    Args:
        engine (Engine): Объект подключения к базе данных.
    
    Attributes:
        engine (Engine): Объект подключения к базе данных.
        session (Session): Сессия для работы с базой данных.
    """
    def __init__(self, engine: Engine = engine) -> None:
        """ ## Инициализация класса. """
        super().__init__(engine)

    def insert_one(self, table: Table, **kwargs) -> None:
        """
        ## Добавление одной записи в базу данных.
        
        Args:
            table (Table): SQLAlchemy объект таблицы.
            **kwargs: Поля и значения для вставки.
        """
        try:
            with self.session as session:
                with session.begin():
                    stmt = insert(table).values(**kwargs)
                    session.execute(stmt)
                    
        except IntegrityError as ex:
            raise ex

        except Exception as ex:
            raise ex
    
    def insert_many(self, table: Table, data: list[dict]) -> None:
        """
        ## Пакетная вставка записей в базу данных.
        
        Args:
            table (Table): SQLAlchemy объект таблицы.
            data (list[dict]): Список словарей с данными для вставки.
        """
        if not data:
            return  # Нечего вставлять

        try:
            with self.session as session:
                with session.begin():
                    stmt = insert(table)
                    session.execute(stmt, data)  # Передаём список словарей
                    
        except IntegrityError as ex:
            raise ex
        
        except Exception as ex:
            raise ex
    
    def get_one(self, table: Table, **kwargs) -> Optional[Any]:
        """
        ## Получение одной записи из базы данных по заданным условиям.
        
        Args:
            table (Table): SQLAlchemy объект таблицы.
            **kwargs: Условия для фильтрации записи.
        
        Returns:
            Optional[Any]: Найденная запись или None, если запись не найдена.
        """
        try:
            with self.session as session:
                stmt = select(table).filter_by(**kwargs)
                result = session.execute(stmt).scalar_one_or_none()  # Получаем одну запись или None
                return result

        except NoResultFound:
            return None  # Если запись не найдена, возвращаем None

        except Exception as ex:
            raise ex
    
    def get_all(self, table: Table, **kwargs) -> list[Any]:
        """
        ## Получение всех записей из базы данных по заданным условиям.
        
        Args:
            table (Table): SQLAlchemy объект таблицы.
            **kwargs: Условия для фильтрации записей.
        
        Returns:
            list[Any]: Список найденных записей.
        """
        try:
            with self.session as session:
                with session.begin():
                    stmt = select(table).filter_by(**kwargs)
                    results = session.execute(stmt).fetchall()
                    return results

        except Exception as ex:
            raise ex



db_crud = DataBaseCRUD(engine)