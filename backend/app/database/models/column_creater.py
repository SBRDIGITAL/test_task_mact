from sqlalchemy import Table, Column, Integer, BigInteger, String, ForeignKey


class ColumnCreater:
    
    @staticmethod
    def get_primary_key_int_column(column_name: str) -> Column[BigInteger]:
        """
        # Создаёт поле с типом данных `BigInteger` и `primary_key=True`.
        ## Автоинкремент для `sqlite3` срабатывает только если `INTEGER PRIMARY KEY` без `autoincrement=True`.

        Args:
            column_name (str): _description_

        Returns:
            Column[BigInteger]: _description_
        """        
        return Column(column_name, Integer, primary_key=True)
    
    @staticmethod
    def get_primary_key_bigint_column(column_name: str, autoincrement: bool = True) -> Column[BigInteger]:
        """
        ## Создаёт поле с типом данных `BigInteger` и `primary_key=True`.

        Args:
            column_name (str): _description_
            autoincrement (bool): _description_

        Returns:
            Column[BigInteger]: _description_
        """        
        return Column(column_name, BigInteger, primary_key=True, autoincrement=autoincrement)
    
    @staticmethod
    def get_string_type_column(name: str, max_len: int = 255, nullable: bool = False, unique: bool = False) -> Column:
        """_summary_

        Args:
            name (str): _description_
            max_len (Optional[int]): _description_. Defaults to 255.
            nullable (bool): _description_. Defaults to False.

        Returns:
            Column: _description_
        """        
        return Column(name, String(max_len), nullable=nullable, unique=unique)