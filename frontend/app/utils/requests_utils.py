from typing import Optional
import requests

from config.literals import AppLiterals as AL

from config.api.endpoints_config import EndpointsConfig as EC
from config.api.api_config import api_config, ApiConfig

from exceptions.exception_handler import AppExceptionsHandlers as AXH



class RequesterHelpers:
    
    def __init__(self, api_config: ApiConfig):
        self.api_config: ApiConfig = api_config
    
    def __get_slash_router(self, router: EC.allow_routers) -> str:
        """ ## Возвращает роутер с `/` """
        return f"{router.replace('/', '')}/"
        
    def get_full_url_for_request(self, router: EC.allow_routers, endpoint: EC.allow_endpoints) -> str:
        """
        ## Возвращает полный URL для запроса к `API`.

        Args:
            endpoint (EndpointsConfig.allow_endpoints): ендпоинт для запроса.

        Returns:
            str: полный URL.
        """        
        return f'{self.api_config.get_base_url()}{self.__get_slash_router(router)}{endpoint}'


class Requester:
    
    def __init__(self, api_config: ApiConfig) -> None:
        """
        ## Класс для отправки запросов на `API`.

        Args:
            api_config (ApiConfig): объект конфигурации клиента `API`.
        
        Attributes:
            api_config (ApiConfig): объект конфигурации клиента `API`.
            rh (RequesterHelpers): объект класса помощника.
                    
        Пример использования:
        ```python
            api_config = ApiConfig(proto='http', base_url='127.0.0.1:8000')
            requester = Requester(api_config)
            users = requester.send_request(method='GET', router='users', endpoint='get_users')
        ```
        """        
        self.api_config: ApiConfig = api_config
        self.rh = RequesterHelpers(self.api_config)
    
    def send_request(self,
        method: AL.RequestsMethod,
        router: EC.allow_routers,
        endpoint: EC.allow_endpoints,
        data: Optional[dict] = None
    ) -> dict:
        """
        ## Отправляет запрос к `API`.

        Этот метод формирует и отправляет HTTP-запрос к указанному `API`,
        используя заданный метод, роутер и конечную точку.
        В зависимости от метода, запрос может быть `GET` или `POST`. 

        ### Args:
            method (AL.RequestsMethod): Метод HTTP-запроса, который будет использоваться. 
                Может быть `'GET'` или `'POST'`.
                
            router (EC.allow_routers): Роутер, к которому будет отправлен запрос. 
                Должен соответствовать одному из разрешенных роутеров.
                
            endpoint (EC.allow_endpoints): Конечная точка `API`, к которой будет отправлен запрос. 
                Должна соответствовать одному из разрешенных эндпоинтов.
                
            data (Optional[dict], optional): Данные, которые будут отправлены в теле запроса. 
                Используется только для `'POST'`-запросов. По умолчанию None.

        ### Returns:
            dict: Ответ от `API` в формате `JSON`, если запрос выполнен успешно.

        ### Пример использования:
        ```python
            response = requester.send_request(method='GET', router='users', endpoint='get_users')
            if response:
                print(response)
            else:
                print("Ошибка при получении данных.")
        ```

        ### Raises:
            Exception:
                В случае возникновения ошибки при выполнении запроса, будет вызван метод обработки исключений.
        """      
        try:
            url = self.rh.get_full_url_for_request(router, endpoint)
            print(f'{url=}')
            if method == 'GET':
                res = requests.get(url, json=data)
            else:
                res = requests.post(url, json=data)
            
            return res.json()
            
        except Exception as ex:
            AXH.get_exception(ex)
    

# requester = Requester(api_config)
# requester.send_request(method='GET', endpoint='get_users')