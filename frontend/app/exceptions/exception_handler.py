from traceback import print_exc
from typing import Union



class AppExceptionsHandlers:
    
    @classmethod
    def get_exception(cls, exc: Union[Exception]) -> None:
        """
        ## Перенаправляет исключение в зависимости от его типа на нужный хендлер.

        Args:
            exc (Union[Exception, HTTPException]): _description_
        """        
        if isinstance(exc, Exception):
            cls.__general_exception_handler(exc)
    
    @classmethod
    def __general_exception_handler(cls, exc: Exception):
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
        
        
AXH = AppExceptionsHandlers()