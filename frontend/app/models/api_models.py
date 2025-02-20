from typing import List

from pydantic import BaseModel

from app.config.api.endpoints_config import EndpointsConfig



# Роутеры
class AllowRouter(BaseModel):
    """
    ## Модель разрешенного роутера.

    Этот класс представляет собой модель для одного разрешенного роутера,
    который определяется в конфигурации эндпоинтов.
    """
    router: EndpointsConfig.allow_routers
    
class AllowRouters(BaseModel):
    """
    ## Модель разрешенных роутеров.

    Этот класс представляет собой модель, содержащую список разрешенных роутеров.
    """"
    routers: List[AllowRouter]


# Ендпоинты
class AllowEndpoint(BaseModel):
    """
    ## Модель разрешенного ендпоинта.

    Этот класс представляет собой модель для одного разрешенного ендпоинта,
    который определяется в конфигурации эндпоинтов.
    """
    endpoint: EndpointsConfig.allow_endpoints

class AllowEndpoints(BaseModel):
    """
    ## Модель списка разрешенных ендпоинтов.

    Этот класс представляет собой модель, содержащую список разрешенных ендпоинтов.
    """
    endpoints: List[AllowEndpoint]