from fastapi import Depends
from fastapi.routing import APIRouter

from models.data_travel import ListUsersModel, UserModel



router = APIRouter(prefix='/data_travel', tags=["data_travel"])



@router.post("/create_user")
def create_user(user: UserModel):
    return user


@router.post("/create_users", response_model=ListUsersModel)
def create_users(users: ListUsersModel):
    return users    