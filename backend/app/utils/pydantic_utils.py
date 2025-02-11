from typing import List, Type, Union

from pydantic import BaseModel

from config.literals import AppLiterals as AL



class PydanticUtils:
    
    @staticmethod
    def convert_to_list_dict(data: list, mode: AL.DictConvertModes = 'python') -> list[dict]:
        """
        ## Преобразование данных в список словарей.

        Args:
            data (list): _description_
            mode (AL.DictConvertModes, optional): _description_. Defaults to 'python'.

        Raises:
            ValueError: _description_

        Returns:
            list[dict]: _description_
        """        
        try:
            return [i.model_dump(mode=mode) for i in data]
        except:
            raise ValueError('Ошибка преобразования данных в список словарей.')

    @staticmethod
    def transform_data_to_model(data: List[tuple], keys: List[str], model: Type[BaseModel]) -> Union[BaseModel, List[BaseModel]]:
        """
        Преобразует данные в список словарей и создает список экземпляров модели Pydantic.

        Args:
            data (List[tuple]): Данные для преобразования.
            keys (List[str]): Ключи для создания словарей.
            model (Type[BaseModel]): Модель Pydantic для создания экземпляров.

        Пример использования:
            get_users = user_dao.get_all_users()
            users_mapping_keys = ClassesUtils.get_attrs_names_from_class(UTM)
            result = PydanticUtils.transform_data_to_model(get_users, users_mapping_keys, UserWithIdModel)

        Returns:
            Union[BaseModel, List[BaseModel]]: Либо список экземпляров модели Pydantic, либо один экземпляр.
        """
        instances = [model(**dict(zip(keys, user))) for user in data]  # Создание списка экземпляров модели

        if len(instances) == 1:
            return instances[0]  # Если только один объект, возвращаем его без списка
        return instances  # Возвращаем список экземпляров моделей