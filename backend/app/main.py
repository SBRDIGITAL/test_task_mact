import sys, os
from typing import Union

from fastapi import FastAPI

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.crud import db_crud
from routers.data_travel import router as data_travel_router



""" 
1. Написать методы получения данных в CRUD
2. Написать методы получения данных в BaseDAO
3. Написать методы получения данных в UserDao
4. Написать ендпоинт для получения данных на FastAPI
5. Написать логгирование
6. Написать тесты
7. Написать экспепшены
"""



class FastAPIapp:
    
    def __init__(self) -> None:
        """ ## Инициализация приложения. """
        self.app = FastAPI()
        self.__post_init()
        
    def __post_init(self) -> None:
        """ ## Основные настройки приложения. """
        self.__include_routers()
        self.__start_db()
        self.__start()
    
    def __start_db(self) -> None:
        """ ## Запуск работы с базой данных. """
        db_crud.start(drop_tables=False)
    
    def __include_routers(self) -> None:
        """ ## Подключение роутеров. """
        self.app.include_router(data_travel_router)
    
    def __start(self):
        """ ## Запуск приложения. """
        yield self.app

fast_api_app = FastAPIapp()
app = fast_api_app.app


    
""" 
Запуск
Перейти в директорию backend\app> и выполнить команду uvicorn main:app --reload
"""