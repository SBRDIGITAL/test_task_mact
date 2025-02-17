from typing import Literal


class EndpointsConfig:
    """
    ## Конфигурация разрешенных ендпоинтов. 
    
    Attributes:
        routers (list[str]): все существующие роутеры.
        endpoints (dict[str, dict[str, str]]): все существующие ендпоинты распределенные по роутерам.
        
        allow_routers: разрешенные роутеры.
        allow_endpoints: разрешенные ендпоинты.
    """
    routers = ["users"]
    endpoints = {
        "users": {  # роутер пользователей
            "create_users": "create_users",
            "get_users": "get_users",
        },
        # "admins": {
        #     "admin": "test-admin"
        # }
    }
    allow_routers = Literal["users"]
    allow_endpoints = Literal["create_users", "get_users",
        # "test-admin"
    ]