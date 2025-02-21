from typing import Optional
from sqlalchemy import Table

from database.models.models import models, metadata_obj



class Tables:
    """ ## Класс для быстрого доступа к объектам таблиц. """
    user_table: Optional[Table] = models.users_table