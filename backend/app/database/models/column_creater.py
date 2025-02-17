from sqlalchemy import Table, Column, Integer, BigInteger, String, ForeignKey



class ColumnCreater:
    
    @staticmethod
    def get_primary_key_int_column(column_name: str) -> Column[Integer]:
        """
        # Создаёт поле с типом данных `BigInteger` и `primary_key=True`.
        ## Автоинкремент для `sqlite3` срабатывает только если `INTEGER PRIMARY KEY` без `autoincrement=True`.

        Args:
            column_name (str): наименование поля.

        Returns:
            Column[Integer]: колонка с типом данных `Integer`.
        """        
        return Column(column_name, Integer, primary_key=True)
    
    @staticmethod
    def get_primary_key_bigint_column(column_name: str, autoincrement: bool = True) -> Column[BigInteger]:
        """
        ## Создаёт поле с типом данных `BigInteger` и `primary_key=True`.

        Args:
            column_name (str): наименование поля.
            autoincrement (bool): автоинкремент. Defaults to True.

        Returns:
            Column[BigInteger]: колонка с типом данных `BigInteger`.
        """        
        return Column(column_name, BigInteger, primary_key=True, autoincrement=autoincrement)
    
    @staticmethod
    def get_string_type_column(name: str, max_len: int = 255, nullable: bool = False, unique: bool = False) -> Column:
        """
        ## Создаёт поле с типом данных `String`.

        Args:
            name (str): наименование поля.
            max_len (Optional[int]): максимальное кол-во символов. Defaults to 255.
            nullable (bool): может быть пустым, если `True`. Defaults to False.

        Returns:
            Column: _description_
        """        
        return Column(name, String(max_len), nullable=nullable, unique=unique)