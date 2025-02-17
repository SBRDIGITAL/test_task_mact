from .base import PrimaryKeyMapping



class UsersTableMapping(PrimaryKeyMapping):
    """ 
    ## Маппинг названий колонок модели таблицы пользователей. 
    
    Attr:
        ID: str - Идентификатор пользователя(Унаследовано).
        FIRST_NAME: str - Имя пользователя.
        LAST_NAME: str - Фамилия пользователя.
        NICKNAME: str - Никнейм пользователя.
    """
    ID = "id"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    NICKNAME = "nickname"