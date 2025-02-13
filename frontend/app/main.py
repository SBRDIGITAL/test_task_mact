import sys, os

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.api.api_config import api_config, ApiConfig
from utils.requests_utils import Requester



requester = Requester(api_config)
users = requester.send_request(method='GET', router='users', endpoint='get_users')
print(f'{users=}')
print(f'{type(users)=}')