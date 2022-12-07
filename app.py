user_account = {}


def login():
    user_name = input("What's your name ?")
    if user_name in user_account.keys():
        print("Enter your account.")
        site_name = input("")
        login = input()
        password = input()
        user_account[user_name] = [site_name,login,password]


def register():
    user_name = input("What's your new name ?")
    if user_name not in user_account.keys():
        user_account[user_name] = []
    else:
        print("This name already .")


def suppress():
    user_name = input("What's the name you need to delete ?")
    if user_name in user_account.keys():
        del user_account[user_name]
    else:
        print("This name doesn't exists .")


def main_app():
    selection: int = -1
    print("Welcome in Passman")
    print("What can I do for you \n 1. Login \n 2. Register \n 3.update \n 4. Suppress")
    while selection != 0:
        selection = int(input("Enter a number : "))
        match selection:
            case 1:
                login()
            case 2:
                register()
            case 3:
                suppress()
            case 0:
                exit()
