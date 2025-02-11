from typing import Dict, List, Optional, Union

from pydantic import BaseModel, field_validator


    
# МОДЕЛИ ПОЛЬЗОВАТЕЛЕЙ БЕЗ ИДЕНТИФИКАТОРА   
class UserModel(BaseModel):
    """ ## Модель пользователя БЕЗ ИДЕНТИФИКАТОРА. """
    first_name: Optional[str]
    last_name: Optional[str]
    nickname: str
    
    @field_validator('nickname')
    def check_nickname_length(cls, value):
        if len(value) > 50:
            raise ValueError('Никнейм должен быть не более 50 символов')
        return value


class ListUsersModel(BaseModel):
    """ ## Модель списка пользователей БЕЗ ИДЕНТИФИКАТОРА. """
    users: List[UserModel]  # Используйте Dict для хранения пользователей по user_id
    
    @field_validator('users')
    def check_users(cls, value):
        if not value:
            raise ValueError('Объект пользователей не должен быть пустым')
        return value
    
    class Config:
        from_attributes = True  # Включаем ORM-режим для UserModel
    
########################################################################################################################

# МОДЕЛИ ПОЛЬЗОВАТЕЛЕЙ С ИДЕНТИФИКАТОРОМ
class UserId(BaseModel):
    """ # Модель для идентификатора пользователя. """
    id: int
    

class UserWithIdModel(UserId):
    """ ## Модель пользователя С ИДЕНТИФИКАТОРОМ. """
    first_name: Optional[str]
    last_name: Optional[str]
    nickname: str
    
    @field_validator('nickname')
    def check_nickname_length(cls, value):
        if len(value) > 50:
            raise ValueError('Никнейм должен быть не более 50 символов')
        return value
    
    
class ListUsersWithIdModel(BaseModel):
    """ ## Модель списка пользователей С ИДЕНТИФИКАТОРОМ. """
    users: List[UserWithIdModel]  # Используйте Dict для хранения пользователей по user_id
    
    # @field_validator('users')
    # def check_users(cls, value):
    #     if not value:
    #         raise ValueError('Объект пользователей не должен быть пустым')
    #     return value