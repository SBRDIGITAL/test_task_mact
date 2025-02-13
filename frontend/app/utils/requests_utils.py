from typing import Optional
import requests

from config.literals import AppLiterals as AL

from config.api.endpoints_config import EndpointsConfig as EC
from config.api.api_config import api_config, ApiConfig

from models.api_models import AllowEndpoint
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
    
    def __init__(self, api_config: ApiConfig):
        self.api_config: ApiConfig = api_config
        self.rh = RequesterHelpers(self.api_config)
    
    def send_request(self,
        method: AL.RequestsMethod,
        router: EC.allow_routers,
        endpoint: EC.allow_endpoints,
        data: Optional[dict] = None
    ) -> Optional[dict]:
        """
        ## _summary_

        Args:
            method (AL.RequestsMethod): _description_
            router (EC.allow_routers): _description_
            endpoint (EC.allow_endpoints): _description_
            data (Optional[dict], optional): _description_. Defaults to None.

        Returns:
            Optional[dict]: _description_
        """        
        try:
            url = self.rh.get_full_url_for_request(router, endpoint)
            print(f'{url=}')
            if method == 'GET':
                res = requests.get(url, json=data)
            else:
                res = requests.post(url, json=data)
            
            return res.json() if res else None
            
        except Exception as ex:
            AXH.get_exception(ex)
    

# requester = Requester(api_config)
# requester.send_request(method='GET', endpoint='get_users')