from sqlalchemy import MetaData, Table

from config.enums import TableNames
from database.mapping.mapping_imports import UTM
from database.models.column_creater import ColumnCreater



class User:
    
    def __init__(self, metadata_obj: MetaData) -> None:
        """
        ## Инициализация объекта.

        Args:
            metadata_obj (MetaData): объект метаданных.
        
        Attributes:
            metadata_obj (MetaData): объект метаданных.
            user_table (Table): таблица пользователей.
        """        
        self.metadata_obj = metadata_obj
        self.user_table: Table = self.__register_user_model()
    
    def __register_user_model(self) -> None:
        """ ## Создаёт модель таблицы пользователей. """   
        return Table(
            TableNames.USERS.value,
            self.metadata_obj,
            ColumnCreater.get_primary_key_int_column(UTM.ID),
            ColumnCreater.get_string_type_column(UTM.FIRST_NAME, nullable=True),
            ColumnCreater.get_string_type_column(UTM.LAST_NAME, nullable=True),
            ColumnCreater.get_string_type_column(UTM.NICKNAME, 50, nullable=False, unique=True),
        )