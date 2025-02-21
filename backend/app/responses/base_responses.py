from models.responses import SomeMessage



class ResponsesHelper:
    """ 
    ## Вспомогательный класс для генерации сообщений ответов.

    Этот класс предоставляет методы для создания сообщений ответов в стандартизированном формате.
    """
    def get_message(self, msg: str) -> SomeMessage:
        """ 
        ## Возвращает объект сообщения ответа.

        Аргументы:
            msg (str): Сообщение, которое будет включено в ответ.

        Возвращает:
            SomeMessage: Экземпляр `SomeMessage`, содержащий переданное сообщение.
        """     
        return SomeMessage(message=msg)


class UserResponses(ResponsesHelper):
    """ 
    ## Класс для обработки ответов от сервера к клиенту, связанных с ендпоинтом `users`.

    Этот класс предоставляет методы(свойства) для генерации сообщений ответов, связанных с операциями над пользователями.
    """
    
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
        ## Возвращает ответ об успешном добавлении нескольких пользователей.

        Returns:
            SomeMessage: объект ответа.
        """
        return self.get_message("Пользователи успешно добавлены в базу данных.") 



user_responses = UserResponses()