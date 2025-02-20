import sys, os

from fastapi import FastAPI

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.crud import db_crud
from routers.users import router as users_router



class FastAPIapp:
    
    def __init__(self) -> None:
        """
        ## Инициализация приложения. 
        
        Attributes:
            app (FastAPI): объект FastAPI.
        """
        self.app = FastAPI(lifespan=self.lifespan)
        
    def __post_init(self) -> None:
        """
        ## Основные настройки приложения.
        
        Подключает роутеры, устанавливает соединение с базой данных.
        """
        self.__include_routers()
        self.__start_db()

    def lifespan(self, app: FastAPI):
        """
        ## Вызывается во время жизненного цикла приложения.
        
        Запускает подключение к базе данных и возвращает управление приложению.

        ### Args:
            app (FastAPI): Экземпляр `FastAPI`.
        """
        self.__post_init()
        yield
    
    def __start_db(self) -> None:
        """ ## Запуск работы с базой данных. """
        db_crud.start(drop_tables=False)
    
    def __include_routers(self) -> None:
        """ ## Подключение роутеров. """
        self.app.include_router(users_router)
    


fast_api_app = FastAPIapp()
app = fast_api_app.app



""" 
Запуск
Перейти в директорию backend\app> и выполнить команду uvicorn main:app --reload
"""