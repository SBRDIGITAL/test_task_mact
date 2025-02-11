from typing import Dict, List, Optional, Union

from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    user_id: Optional[int]
    first_name: str
    last_name: str
    nickname: str
    
    @field_validator('nickname')
    def check_nickname_length(cls, value):
        if len(value) > 50:
            raise ValueError('Никнейм должен быть не более 50 символов')
        return value
    
    
class ListUsersModel(BaseModel):
    users: List[UserModel]  # Используйте Dict для хранения пользователей по user_id
    
    @field_validator('users')
    def check_users(cls, value):
        if not value:
            raise ValueError('Объект пользователей не должен быть пустым')
        return value