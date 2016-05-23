from role import Administrator
from commands_administrator import CreateNewRole, AssignUserToRole
from session import Session
from user import User

if __name__ == "__main__":
    user = User("bruno", "12345")

    role_admin = Administrator ()
    Administrator.add_current_adm(role_admin)
    Administrator.add_privilege(role_admin, CreateNewRole)
