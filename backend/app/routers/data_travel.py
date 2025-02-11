import json

from fastapi import Depends
from fastapi.routing import APIRouter

from dao.user_dao import user_dao
from database.mapping.mapping_imports import UTM
from models.users import ListUsersModel, ListUsersWithIdModel, UserWithIdModel, UserModel

from utils.pydantic_utils import PydanticUtils
from utils.classes_utils import ClassesUtils
from utils.endpoints_utils import EndpointsUtils



router = APIRouter(prefix='/data_travel', tags=["data_travel"])



@router.post("/create_user", response_model=dict)
def create_user(user: UserModel):
    """
    ## Добавление пользователя в базу данных.

    Args:
        user (UserModel): Модель пользователя.

    Returns:
        dict: сообщение об успешном добавлении пользователя в базу данных.
    """    
    EndpointsUtils.create_user(user)
    return {"message": "Пользователь успешно добавлен в базу данных."}


@router.post("/create_users", response_model=dict)
def create_users(users: ListUsersModel):
    """
    ## Добавление пользователей в базу данных.

    Args:
        users (ListUsersModel): Модель списка пользователей.

    Returns:
        dict: сообщение об успешном добавлении пользователей в базу данных.
    """
    EndpointsUtils.create_users(users)
    return {"message": "Пользователи успешно добавлены в базу данных."}


@router.get("/get_users", response_model=ListUsersWithIdModel)
def get_users():
    """
    ## Получение всех пользователей из базы данных.

    Returns:
        ListUsersWithIdModel: Модель списка найденных пользователей.
    """
    return EndpointsUtils.get_all_users()