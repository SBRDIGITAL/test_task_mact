from dao.user_dao import user_dao
from database.mapping.mapping_imports import UTM
from models.users import ListUsersWithIdModel, UserWithIdModel, ListUsersModel, UserModel

from utils.pydantic_utils import PydanticUtils
from utils.classes_utils import ClassesUtils



class EndpointsUtils:
    """ ## Утилиты для работы с конечными точками. """
    
    @staticmethod
    def create_user(user: UserModel) -> None:
        """
        ## Добавление одного пользователя в базу данных.

        Args:
            user (UserModel): `Pydantic` модель пользователя.
        """        
        user_dao.insert_user(**user.model_dump())
    
    @staticmethod
    def create_users(users: ListUsersModel) -> None:
        """
        ## Добавление пользователей в базу данных.
        
        Args:
            users (ListUsersModel): `Pydantic` модель списка пользователей.
        """
        
        user_dao.insert_users(PydanticUtils.convert_to_list_dict(users.users))
    
    @classmethod
    def get_all_users(cls) -> ListUsersWithIdModel:
        """
        ## Получение всех пользователей из базы данных.

        Returns:
            ListUsersWithIdModel: `Pydantic` модель список найденных пользователей.
        """        
        get_users = user_dao.get_all_users()
        users_mapping_keys = ClassesUtils.get_attrs_names_from_class(UTM)
        result = PydanticUtils.transform_data_to_model(get_users, users_mapping_keys, UserWithIdModel)
        return ListUsersWithIdModel(total_count=len(result), users=result)

    @classmethod
    def get_users(cls, page: int, page_size: int):
        """
        ## Получение пользователей из базы данных с пагинацией.

        Args:
            page (int): номер страницы пагинации.
            page_size (int): максимальное количество элементов на страницу.
        
        Returns:
            ListUsersWithIdModel: пользователи для текущей страницы.
        """
        all_users = cls.get_all_users()
        start_index = (page - 1) * page_size  # Вычисляем начальный и конечный индексы для среза
        end_index = start_index + page_size
        paginated_users = all_users.users[start_index:end_index]
        return ListUsersWithIdModel(total_count=len(paginated_users), users=paginated_users)