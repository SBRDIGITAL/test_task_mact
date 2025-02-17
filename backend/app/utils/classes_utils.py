

class ClassesUtils:

    @staticmethod
    def get_attrs_names_from_class(obj) -> list[str]:
        """
        ## Получение словаря с данными о таблице.

        Args:
            table (Table): SQLAlchemy объект таблицы.

        Returns:
            dict: Словарь с данными о таблице.
        """
        return [value for key, value in obj.__dict__.items() if not key.startswith("__")]