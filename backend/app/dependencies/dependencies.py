from fastapi import Depends

from models.data_travel import ListUsersModel



class UserDependencies:
    
    @staticmethod
    def get_users_list(users: ListUsersModel = Depends()) -> ListUsersModel:
        """_summary_

        Args:
            users (ListUsersModel, optional): _description_. Defaults to Depends().

        Returns:
            ListUsersModel: _description_
        """        
        return users