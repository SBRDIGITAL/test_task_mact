from typing import List

from pydantic import BaseModel

from app.config.api.endpoints_config import EndpointsConfig



# Роутеры
class AllowRouter(BaseModel):
    """ ## Модель разрешенного роутера. """
    router: EndpointsConfig.allow_routers
    
class AllowRouters(BaseModel):
    """ ## Модель разрешенных роутеров. """
    routers: List[AllowRouter]


# Ендпоинты
class AllowEndpoint(BaseModel):
    """ ## Модель разрешенного ендпоинта. """
    endpoint: EndpointsConfig.allow_endpoints

class AllowEndpoints(BaseModel):
    """ ## Модель списка разрешенных ендпоинтов. """
    endpoints: List[AllowEndpoint]