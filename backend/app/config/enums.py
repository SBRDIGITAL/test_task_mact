from enum import Enum

class RoleEnum(Enum):
    ADMIN = 'admin'
    USER = 'user'
    
class TableNames(Enum):
    USERS = 'users'