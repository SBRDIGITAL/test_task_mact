from typing import List, Type

from pydantic import BaseModel

from config.literals import AppLiterals as AL



class PydanticUtils:
    """
    ## Утилиты для работы с `Pydantic` моделями.

    Этот класс предоставляет статические методы для преобразования данных в
    списки словарей и создания экземпляров моделей `Pydantic` из данных.
    """
    
    @staticmethod
    def convert_to_list_dict(data: list, mode: AL.DictConvertModes = 'python') -> list[dict]:
        """
        ## Преобразование данных в список словарей.

        Args:
            data (list): Список объектов, которые необходимо преобразовать в словари.
            mode (AL.DictConvertModes, optional): Режим преобразования. По умолчанию 'python'.

        Raises:
            ValueError: Если произошла ошибка при преобразовании данных.

        Returns:
            list[dict]: Список словарей, представляющих объекты из входного списка.
        """       
        try:
            return [i.model_dump(mode=mode) for i in data]
        except:
            raise ValueError('Ошибка преобразования данных в список словарей.')

    @staticmethod
    def transform_data_to_model(data: List[tuple], keys: List[str], model: Type[BaseModel]) -> List[BaseModel]:
        """
        ## Преобразует данные в список экземпляров модели Pydantic.

        Args:
            data (List[tuple]): Данные для преобразования, представленные в виде списка кортежей.
            keys (List[str]): Список ключей для создания словарей из кортежей.
            model (Type[BaseModel]): Модель Pydantic, экземпляры которой будут созданы.

        Пример использования:
            get_users = user_dao.get_all_users()
            users_mapping_keys = ClassesUtils.get_attrs_names_from_class(UTM)
            result = PydanticUtils.transform_data_to_model(get_users, users_mapping_keys, UserWithIdModel)

        Returns:
            List[BaseModel]: Список экземпляров модели Pydantic, созданных на основе входных данных.
        """
        return [model(**dict(zip(keys, user))) for user in data]  # Создание списка экземпляров модели