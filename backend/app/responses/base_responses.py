from models.responses import SomeMessage



class ResponsesHelper:
    
    def get_message(self, msg: str) -> SomeMessage:
        """
        ## Возвращает словарь с ключом и значением.

        Args:
            msg (str): значение.

        Returns:
            dict[str, str]: словарь с ключом и значением для ответа
        """        
        return SomeMessage(message=msg)


class UserResponses(ResponsesHelper):
    
    @property
    def get_ok_created_user(self) -> SomeMessage:
        """
        ## Возвращает ответ об успешном добавлении одного пользователя.

        Returns:
            SomeMessage: объект ответа.
        """
        return self.get_message("Пользователь успешно добавлен в базу данных.")
    
    @property
    def get_ok_created_userS(self) -> SomeMessage:
        """
        ## Возвращает `JSON` ответ об успешном добавлении пользователей.

        Returns:
            SomeMessage: объект ответа.
        """
        return self.get_message("Пользователи успешно добавлены в базу данных.") 



user_responses = UserResponses()