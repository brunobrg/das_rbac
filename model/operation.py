from abc import ABCMeta, abstractmethod

class Operation(metaclass=ABCMeta):

    last_id = 0;

    def __init__(self, name):
        self.operation_id = self.__class__.last_id
        self.name = name
        self.__class__.last_id += 1

    @abstractmethod
    def execute(self):
        pass
