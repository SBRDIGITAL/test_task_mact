import json

from fastapi import Depends
from fastapi.routing import APIRouter

from dao.user_dao import user_dao
from models.users import ListUsersModel, ListUsersWithIdModel, UserWithIdModel, UserModel
from utils.pydantic_utils import PydanticUtils



router = APIRouter(prefix='/data_travel', tags=["data_travel"])



@router.post("/create_user")
def create_user(user: UserModel):
    user_dao.insert_user(**user.model_dump())
    return user


@router.post("/create_users", response_model=ListUsersModel)
def create_users(users: ListUsersModel):
    """
    ## Добавление пользователей в базу данных.

    Args:
        users (ListUsersModel): _description_

    Returns:
        _type_: _description_
    """
    user_dao.insert_users(PydanticUtils.convert_to_list_dict(users.users))
    return users


@router.get("/get_users", response_model=ListUsersWithIdModel)
def get_users():
    """_summary_

    Returns:
        _type_: _description_
    """    
    user = UserWithIdModel(user_id=0, first_name='Юзер', last_name='Юзеров', nickname='user')
    users = ListUsersWithIdModel(users=[user])
    print(f'{users=}')
    return users