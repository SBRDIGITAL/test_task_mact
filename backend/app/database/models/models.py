from typing import Optional

from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry

from database.models.users import User



mapper_registry = registry()
empty_metadata_obj: MetaData = mapper_registry.metadata


class RegisterModels:
    
    def __init__(self, metatadata_obj: MetaData) -> None:
        """ Инициализирует объекты. """
        self.metadata_obj = metatadata_obj
        self.users_table: Optional[Table] = None

    def __update_metadata(self, metadata_obj: MetaData) -> None:
        """ Обновляет метаданные. """
        self.metadata_obj = metadata_obj
    
    def __register_user_model(self) -> None:
        """ Регистрируем модель таблицы пользователей. """        
        self.user = User(self.metadata_obj)
        self.users_table = self.user.user_table
        self.__update_metadata(self.user.metadata_obj)
    
    def register(self) -> None:
        """ Регистрирует модели таблиц. """        
        self.__register_user_model()



models = RegisterModels(empty_metadata_obj)
models.register()
metadata_obj = models.metadata_obj  # Объет метаданных, содеражщий в себе информацию о таблицах