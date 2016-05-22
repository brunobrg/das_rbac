from operation import Operation
from role_subrole import SubRole
class CreateNewRole (Operation):

    def __init__ (self):
        super().__init__ ("create new role")

    def execute (self, role):
        self.create_new_role (role)

    def create_new_role(self,role):
        new_role = SubRole("qualquer nome")
        role.list_of_roles.append(new_role)
