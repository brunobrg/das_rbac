from abc import ABCMeta

class Role(metaclass=ABCMeta):

    last_id = 1;

    def __init__(self, name):
        self.role_id = self.__class__.last_id
        self.name = name
        self.__class__.last_id += 1

    def execute_command (self, command):
        command.execute (self)
