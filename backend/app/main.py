import sys, os
from typing import Union

from fastapi import FastAPI

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.crud import crud
from routers.data_travel import router as data_travel_router



""" 
1. Написать CRUD
2. Написать BaseDAO
3. Написать UserDao
4. Написать Ендпоинты на FastAPI и модели Pydantic
"""


class FastAPIapp:
    
    def __init__(self) -> None:
        """ ## Инициализация приложения. """
        self.app = FastAPI()
        self.__post_init()
        
    def __post_init(self) -> None:
        """ ## Основные настройки приложения. """
        self.__include_routers()
        self.__start()
    
    def __include_routers(self) -> None:
        """ ## Подключение роутеров. """
        self.app.include_router(data_travel_router)
    
    def __start(self):
        """ ## Запуск приложения. """
        crud.start(drop_tables=False)
        yield self.app
        # return self.app

fast_api_app = FastAPIapp()
app = fast_api_app.app



# if __name__ == '__main__':
#     crud.start(drop_tables=False)
    
""" 
Запуск
Перейти в директорию backend\app> и выполнить команду uvicorn main:app --reload
"""