from abc import ABCMeta
from .singleton import Singleton

class Role(metaclass=ABCMeta):

    last_id = 1;

    def __init__(self, name):
        self.role_id = self.__class__.last_id
        self.name = name
        self.privileges = []
        self.__class__.last_id += 1

    def execute (self, command):
        command.execute ()

    def has_privilege (self, command):
        for privilege in self.privileges:
            if isinstance(command, privilege):
                return True
        return False

    def __repr__(self):
        return "<" + str(self.role_id) + ": " + self.name + ">"


class Administrator(Role):

    current_adm = None

    def __init__(self):
        super().__init__("administrator")
        self.list_of_roles = []

    @classmethod
    def add_privilege(cls, role, command):
        role.privileges.append(command)

    @classmethod
    def assign(cls, role, user):
        user.roles.append(role)

    @classmethod
    def add_current_adm(cls, adm):
        cls.current_adm = adm

    @classmethod
    def add_role(cls, role):
        cls.current_adm.list_of_roles.append(role)


class SubRole(Role):

    def __init__(self,name):
        super().__init__(name)
