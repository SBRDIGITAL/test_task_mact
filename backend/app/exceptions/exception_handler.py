from traceback import print_exc

from typing import Union

from fastapi import HTTPException
from fastapi.responses import JSONResponse



class AppExceptionsHandlers:
    
    @classmethod
    def get_exception(cls, exc: Union[Exception, HTTPException]) -> None:
        """
        ## Перенаправляет исключение в зависимости от его типа на нужный хендлер.

        Args:
            exc (Union[Exception, HTTPException]): _description_
        """        
        if isinstance(exc, HTTPException):
            cls.__http_exception_handler(exc)
        else:
            cls.__general_exception_handler(exc)
    
    @classmethod
    def __general_exception_handler(cls, exc: Exception) -> JSONResponse:
        """
        ## Обработчик общих исключений.

        Этот метод обрабатывает все необработанные исключения, возникающие в приложении. 
        Он логирует информацию об исключении и возвращает общий ответ с сообщением об ошибке.

        Args:
            exc (Exception): Исключение, которое было выброшено в процессе обработки запроса.

        Returns:
            JSONResponse: Ответ с кодом состояния 500 и сообщением о внутренней ошибке сервера.
        """
        print_exc()

    @classmethod
    def __http_exception_handler(cls, exc: HTTPException) -> JSONResponse:
        """
        ## Обработчик HTTP исключений.

        Этот метод обрабатывает исключения типа HTTPException, которые могут возникнуть
        в приложении. 
        Он логирует информацию об исключении и возвращает ответ с соответствующим
        кодом состояния и сообщением.

        Args:
            exc (HTTPException): Исключение, которое было выброшено в процессе обработки запроса, 
                содержащее информацию о статусе и сообщении.

        Returns:
            JSONResponse: Ответ с кодом состояния, установленным в исключении,
            и сообщением об ошибке.
        """
        print_exc()