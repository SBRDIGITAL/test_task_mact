from typing import Optional
from sqlalchemy import Table, MetaData

from database.models.models import models, metadata_obj



class Tables:
    """ Класс для быстрого доступа к объектам таблиц. """
    METADATA_OBJ: MetaData = metadata_obj
    user_table: Optional[Table] = models.users_table
    
    
metadata_obj: MetaData = Tables.METADATA_OBJ