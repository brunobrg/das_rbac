from user import User

class Session:

    current_user = None

    @classmethod
    def login(cls, username, password):
        for user in User.users:
            if user.username == username and user.password == password:
                cls.current_user = user
                return "Welcome " + cls.current_user.username


        return "invalid username or password."

    @classmethod
    def has_privilege(cls, command):
        if cls.current_user == None:
            print("There is no current user. Please, log into the system")
        else:
            return cls.current_user.has_privilege(command)
