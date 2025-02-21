from fastapi import HTTPException, status


class HTTPExceptions:
    """
    ## Класс содержащий объекты `HTTPException` исключений приложения.
    
    Attributes:
        InternalServerError (HTTPExceptions): `500` - внутренняя ошибка сервера.
        BadRequest (HTTPExceptions): `400` - Bad Request.
        CantGetUsersError (HTTPExceptions): `500` - Ошибка при получении пользователей.
        CantSaveUsersError (HTTPExceptions): `409` - Ошибка при сохранении пользователей.
    """
    InternalServerError = HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Внутренняя ошибка сервера.'
    )
    

    BadRequest = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
    
    CantGetUsersError = HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Ошибка при получении пользователей'
    )

    CantSaveUsersError = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail='Ошибка при сохранении пользователей.'
    )