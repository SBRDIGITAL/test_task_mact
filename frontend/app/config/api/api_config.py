from pydantic import ValidationError

from .endpoints_config import EndpointsConfig
from models.api_models import AllowEndpoint, AllowEndpoints, AllowRouter, AllowRouters

from ..literals import AppLiterals as AL

from exceptions.exception_handler import AXH



class ApiConfig(EndpointsConfig):
    
    def __init__(self, proto: AL.Proto, base_url: str) -> None:
        self.proto: AL.Proto = proto
        self.base_url: str = base_url
        self.__post_init()
        
    def __post_init(self) -> None:
        """ ## Запускает методы после инициализации класса. """
        try:
            self.__check_routers()
            self.__check_endpoints()
            self.__configure_url()
        
        except Exception as ex:
            AXH.get_exception(ex)
            exit()
    
    def __check_endpoints(self) -> None:
        """ ## Проверяет разрешенные ендпоинты. """
        try:
            all_endpoints = list({i for e in self.endpoints.values() for i in e.values()})
            AllowEndpoints(endpoints=[AllowEndpoint(endpoint=i) for i in all_endpoints])
            
        except ValidationError as ex:
            raise ex
        
    def __check_routers(self) -> None:
        """ ## Проверяет разрешенные роутеры. """
        try:
            AllowRouters(routers=[AllowRouter(router=i) for i in self.routers])
            
        except ValidationError as ex:
            raise ex

    def __configure_url(self) -> None:
        """ ## Конфигурация базовой `URL`. """
        self.base_url = f'{self.proto}://{self.base_url}/'
    
    def get_base_url(self) -> str:
        """ ## Возвращает базовый URL с `/`
        В формате: `http://localhost:8000/`
        """
        return self.base_url


# api_config = ApiConfig(proto='http', base_url='localhost:8000')
api_config = ApiConfig(proto='http', base_url='127.0.0.1:8000')