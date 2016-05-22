from role import Role
from role_administrator import Administrator
from operation import Operation
from create_new_role import CreateNewRole
from role_subrole import SubRole

if __name__ == "__main__":
    admin = Administrator ("admin")
    oper = CreateNewRole ()

    admin.execute_command(oper)
