from . import role
from .command import Command

class CreateNewRole (Command):

    def __init__ (self, new_role_name):
        super().__init__ ("create new role")
        self.new_role_name = new_role_name

    def run (self):
        new_role = SubRole( self.new_role_name )
        Administrator.add_role(new_role)

    def success(self):
        print ("New role <" + self.new_role_name +  "> created")


class AssignUserToRole (Command):

    def __init__(self, user, role):
        super().__init__ ("assign user to role")
        self.user = user
        self.role = role

    def run (self):
        Administrator.assign(self.role, self.user)

    def success(self):
        print ("User " + str(self.user) +  " assigned to Role " + str(self.role))
