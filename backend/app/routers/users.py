from fastapi import Query, HTTPException
from fastapi.routing import APIRouter

from utils.endpoints_utils import EndpointsUtils
from responses.base_responses import user_responses

from exceptions.base_exceptions import AppExceptions
from exceptions.exception_handler import AppExceptionsHandlers

from models.users import ListUsersModel, ListUsersWithIdModel, UserModel
from models.responses import SomeMessage



router = APIRouter(prefix='/users', tags=["Пользователи"])



@router.post("/create_user", response_model=SomeMessage)
def create_user(user: UserModel) -> SomeMessage:
    """
    ## Добавление пользователя в базу данных.

    ### Args:
        user (UserModel): модель пользователя.

    ### Returns:
        SomeMessage: сообщение об успешном добавлении пользователя в базу данных.
    """
    try:
        EndpointsUtils.create_user(user)
        return user_responses.get_ok_created_user
    
    except (Exception, HTTPException) as ex:
        AppExceptionsHandlers.get_exception(ex)
        raise AppExceptions.CSU
        


@router.post("/create_users", response_model=SomeMessage)
def create_users(users: ListUsersModel) -> SomeMessage:
    """
    ## Добавление пользователей в базу данных.

    ### Args:
        users (ListUsersModel): модель списка пользователей.

    ### Returns:
        SomeMessage: сообщение об успешном добавлении пользователей в базу данных.
    """
    try:
        EndpointsUtils.create_users(users)
        return user_responses.get_ok_created_userS  # сделать возврат через Pydantic модель
    
    except (Exception, HTTPException) as ex:
        AppExceptionsHandlers.get_exception(ex)
        raise AppExceptions.CSU


@router.get("/get_users", response_model=ListUsersWithIdModel)
def get_users(page: int = Query(1, ge=1), page_size: int = Query(5, ge=1)) -> ListUsersWithIdModel:
    """
    ## Получение с использованием пагинации пользователей из базы данных.

    ### Args:
        page (int): номер страницы пагинации.
        page_size (int): максимальное количество элементов на страницу.
        
    ### Returns:
        ListUsersWithIdModel: список найденных в базе данных пользователей.
    """
    try:
        return EndpointsUtils.get_users(page, page_size)
    
    except (Exception, HTTPException) as ex:
        AppExceptionsHandlers.get_exception(ex)
        raise AppExceptions.CGUE