from fastapi import status
from fastapi.responses import JSONResponse



class ResponsesHelper:
    
    def get_message(self, msg: str, msg_key: str = "message") -> dict[str, str]:
        """
        ## Возвращает словарь с ключом и значением.

        Args:
            msg (str): значение.
            msg_key (str): ключ. Defaults to "message".

        Returns:
            dict[str, str]: словарь с ключом и значением для ответа
        """        
        return {msg_key: msg}


class UserResponses(ResponsesHelper):
    
    @property
    def get_ok_created_user(self) -> JSONResponse:
        """
        ## Возвращает JSON ответ об успешном добавлении одного пользователя.

        Returns:
            JSONResponse: объект ответа.
        """        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=self.get_message("Пользователь успешно добавлен в базу данных.")
        )
    
    @property
    def get_ok_created_userS(self) -> JSONResponse:
        """
        ## Возвращает JSON ответ об успешном добавлении пользователей.

        Returns:
            JSONResponse: объект ответа.
        """        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=self.get_message("Пользователи успешно добавлены в базу данных.")
        )



user_responses = UserResponses()