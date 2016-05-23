from abc import ABCMeta, abstractmethod
from session import Session
from datetime import datetime

class Command(metaclass=ABCMeta):

    last_id = 1;

    def __init__(self, name):
        self.command_id = self.__class__.last_id
        self.name = name
        self.executed_date = str(datetime.now())
        self.__class__.last_id += 1

    @abstractmethod
    def success():
        pass

    @abstractmethod
    def run(self):
        pass


    def execute(self):
        if self.has_privilege():
            self.success()
            self.run()    
            Session.current_user.add_command_log(self)
        else:
            self.fail()

    def has_privilege(self):
        return Session.has_privilege(self)

    def fail(self):
        print ("You can not " + self.name)


    def __repr__(self):
        return "<" + str(self.command_id) + ": " + self.name + ", date: " + self.executed_date + ">"
