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