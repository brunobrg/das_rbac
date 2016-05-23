class User:

    users = []

    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.roles = []
        self.command_log = []
        self.__class__.users.append(self)

    def has_privilege(self, command):
        from commands_user import UserCommands

        if isinstance(command, UserCommands):
            return True
        for role in self.roles:
            if role.has_privilege(command):
                return True
        return False

    def add_command_log(self, command):
        self.command_log.append(command)

    def show_information(self):
        print("username: " + self.username)
        print("roles: ",  self.roles[0:])
        print("command log: ", self.command_log[0:])

    def __repr__(self):
        return "<Username: " + self.username + ">"


    """
        Self user commands
    """

    def call_my_information(self):
        from commands_user import ShowInformation
        ShowInformation(self).execute()



    """
        Administrator commands
    """

    def call_create_new_role(self, new_role_name):
        from commands_administrator import CreateNewRole
        CreateNewRole(new_role_name).execute()

    def call_assign_user_to_role(self, user, role):
        from commands_administrator import AssignUserToRole
        AssignUserToRole(user,role).execute()
