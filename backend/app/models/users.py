from datetime import datetime
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field, field_validator


    
# МОДЕЛИ ПОЛЬЗОВАТЕЛЕЙ БЕЗ ИДЕНТИФИКАТОРА   
class UserModel(BaseModel):
    """
    ## Модель пользователя БЕЗ ИДЕНТИФИКАТОРА.

    Эта модель используется для представления данных пользователя, исключая идентификатор.
    Подходит для создания новых пользователей или передачи данных без ID.

    Attributes:
        first_name (Optional[str]): Имя пользователя. Может быть пустым.
        last_name (Optional[str]): Фамилия пользователя. Может быть пустым.
        nickname (str): Уникальный никнейм пользователя. Должен быть не длиннее 50 символов.

    Raises:
        ValueError: Если длина никнейма превышает 50 символов.

    Example:
        >>> user = UserModel(first_name="John", last_name="Doe", nickname="johndoe")
        >>> print(user)
        first_name='John' last_name='Doe' nickname='johndoe'
    """
    first_name: Optional[str]
    last_name: Optional[str]
    nickname: str
    
    @field_validator('nickname')
    def check_nickname_length(cls, value) -> str:
        """
        ## Валидация длины никнейма.

        Args:
            value (str): Значение никнейма.

        Returns:
            str: Проверенный никнейм.

        Raises:
            ValueError: Если длина никнейма превышает 50 символов.
        """
        if len(value) > 50:
            raise ValueError('Никнейм должен быть не более 50 символов')
        return value


class ListUsersModel(BaseModel):
    """
    ## Модель списка пользователей БЕЗ ИДЕНТИФИКАТОРА.

    Эта модель используется для представления списка пользователей без идентификаторов.
    Включает дополнительные метаданные, такие как дата, время и порядковый номер клика.

    Attributes:
        users (List[UserModel]): Список пользователей.
        current_date (Optional[str]): Текущая дата в формате 'YYYY-MM-DD'. Заполняется автоматически.
        current_time (Optional[str]): Текущее время в формате 'HH:MM:SS'. Заполняется автоматически.
        click_number (Optional[int]): Порядковый номер клика. Должен быть положительным числом.

    Raises:
        ValueError: Если список пользователей пуст или номер клика отрицательный.

    Example:
        >>> users = [
        ...     UserModel(first_name="John", last_name="Doe", nickname="johndoe"),
        ...     UserModel(first_name="Alice", last_name="Smith", nickname="alice")
        ... ]
        >>> list_users = ListUsersModel(users=users, click_number=1)
        >>> print(list_users)
        users=[UserModel(first_name='John', last_name='Doe', nickname='johndoe'), ...] current_date='2023-10-01' current_time='12:34:56' click_number=1
    """
    users: List[UserModel]  # Используйте Dict для хранения пользователей по user_id
    current_date: Optional[str] = Field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d'))
    current_time: Optional[str] = Field(default_factory=lambda: datetime.now().strftime('%H:%M:%S'))
    click_number: Optional[int] = None
    
    @field_validator('users')
    def check_users(cls, value) -> List[UserModel]:
        """
        ## Валидация списка пользователей.

        Args:
            value (List[UserModel]): Список пользователей.

        Returns:
            List[UserModel]: Проверенный список пользователей.

        Raises:
            ValueError: Если список пользователей пуст.
        """
        if not value:
            raise ValueError('Объект пользователей не должен быть пустым')
        return value
    
    @field_validator('click_number')
    def check_click_number(cls, value) -> Optional[int]:
        """
        ## Валидация порядкового номера клика.

        Args:
            value (Optional[int]): Номер клика.

        Returns:
            Optional[int]: Проверенный номер клика.

        Raises:
            ValueError: Если номер клика отрицательный.
        """
        if value is not None and value < 0:
            raise ValueError('Порядковый номер клика на кнопку должен быть положительным целым числом')
        return value
    
    class Config:
        from_attributes = True  # Включаем ORM-режим для UserModel
    
########################################################################################################################

# МОДЕЛИ ПОЛЬЗОВАТЕЛЕЙ С ИДЕНТИФИКАТОРОМ
class UserId(BaseModel):
    """
    ## Модель для идентификатора пользователя.

    Эта модель используется для представления идентификатора пользователя.

    Attributes:
        id (int): Уникальный идентификатор пользователя.

    Example:
        >>> user_id = UserId(id=1)
        >>> print(user_id)
        id=1
    """
    id: int
    

class UserWithIdModel(UserId):
    """
    ## Модель пользователя С ИДЕНТИФИКАТОРОМ.

    Эта модель используется для представления данных пользователя, включая его идентификатор.

    Attributes:
        id (int): Уникальный идентификатор пользователя.
        first_name (Optional[str]): Имя пользователя. Может быть пустым.
        last_name (Optional[str]): Фамилия пользователя. Может быть пустым.
        nickname (str): Уникальный никнейм пользователя. Должен быть не длиннее 50 символов.

    Raises:
        ValueError: Если длина никнейма превышает 50 символов.

    Example:
        >>> user = UserWithIdModel(id=1, first_name="John", last_name="Doe", nickname="johndoe")
        >>> print(user)
        id=1 first_name='John' last_name='Doe' nickname='johndoe'
    """
    first_name: Optional[str]
    last_name: Optional[str]
    nickname: str
    
    @field_validator('nickname')
    def check_nickname_length(cls, value) -> str:
        """
        ## Валидация длины никнейма.

        Args:
            value (str): Значение никнейма.

        Returns:
            str: Проверенный никнейм.

        Raises:
            ValueError: Если длина никнейма превышает 50 символов.
        """
        if len(value) > 50:
            raise ValueError('Никнейм должен быть не более 50 символов')
        return value
    
    
class ListUsersWithIdModel(BaseModel):
    """
    ## Модель списка пользователей С ИДЕНТИФИКАТОРОМ.

    Эта модель используется для представления списка пользователей с их идентификаторами.
    Включает общее количество пользователей.

    Attributes:
        total_count (int): Общее количество пользователей.
        users (List[UserWithIdModel]): Список пользователей с идентификаторами.

    Example:
        >>> users = [
        ...     UserWithIdModel(id=1, first_name="John", last_name="Doe", nickname="johndoe"),
        ...     UserWithIdModel(id=2, first_name="Alice", last_name="Smith", nickname="alice")
        ... ]
        >>> list_users = ListUsersWithIdModel(total_count=2, users=users)
        >>> print(list_users)
        total_count=2 users=[UserWithIdModel(id=1, first_name='John', last_name='Doe', nickname='johndoe'), ...]
    """
    total_count: int
    users: List[UserWithIdModel]  # Используйте Dict для хранения пользователей по user_id