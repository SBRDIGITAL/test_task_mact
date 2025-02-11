from typing import Dict
from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    nickname: str
    
    @field_validator('nickname')
    def check_nickname_length(cls, value):
        if len(value) > 50:
            raise ValueError('Никнейм должен быть не более 50 символов')
        return value
    
    
class ListUsersModel(BaseModel):
    users: Dict[str, UserModel]  # Используйте Dict для хранения пользователей по user_id
    
    @field_validator('users')
    def check_users(cls, value):
        if not value:
            raise ValueError('Список пользователей не должен быть пустым')
        return value