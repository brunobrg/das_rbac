from role import Role
from role_subrole import SubRole

class Administrator(Role):

    def __init__(self,name):
        super().__init__(name)
        self.list_of_roles = []


    def create_role(self,name):
        new_role = SubRole(name)
        self.list_of_roles.append(new_role)
