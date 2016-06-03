from . import command

class UserCommands(Command):
    def __init__ (self, name):
        super().__init__ (name)

class ShowInformation (UserCommands):

    def __init__ (self, user):
        super().__init__ ("show information")
        self.user = user

    def run (self):
        self.user.show_information()

    def success(self):
        print ("Showing user information...")
