from sqlalchemy import Table, Column, Integer, BigInteger, String, ForeignKey


class ColumnCreater:
    
    @staticmethod
    def get_primary_key_bigint_column(column_name: str, autoincrement: bool = True) -> Column:
        """_summary_

        Args:
            column_name (str): _description_
            autoincrement (bool): _description_

        Returns:
            Column: _description_
        """        
        return Column(column_name, BigInteger, primary_key=True, autoincrement=autoincrement)
    
    @staticmethod
    def get_string_type_column(column_name: str, max_len: int = 255) -> Column:
        """_summary_

        Args:
            column_name (str): _description_
            max_len (int, optional): _description_. Defaults to 255.

        Returns:
            Column: _description_
        """        
        return Column(column_name, String(max_len))