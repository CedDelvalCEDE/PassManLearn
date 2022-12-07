user_account = {}


def login_add(user_name: str):
    print("Enter your account data.")
    site_name = input("What's the website or the game of your account ? ")
    login_account = input("What's your name on this site ? ")
    password = input("What's your password ? ")
    slp_list = [site_name, login_account, password]
    user_account[user_name].append(slp_list)


def login_read(user_name: str):
    print(user_account[user_name])


def login_change(user_name: str):
    new_name = input("What's your new name ? ")
    user_account[new_name] = user_account[user_name]


def login_suppress(user_name: str):
    del user_account[user_name]
    main_app()


def login():
    num_match = -1
    user_name = input("What's your name ? ")
    if user_name in user_account.keys():
        while num_match != 0:
            print(
                "Welcome "
                + user_name
                + "! \n 1. Add an account \n 2. Read an account \n 3. Change an account name \n 4. "
                  "Suppress an account \n 0. exit the login"
            )
            num_match = int(input("Enter a number : "))
            match num_match:
                case 1:
                    login_add(user_name)
                case 2:
                    login_read(user_name)
                case 3:
                    login_change(user_name)
                case 4:
                    login_suppress(user_name)


def register():
    user_name = input("What's your new name ? ")
    if user_name not in user_account.keys():
        user_account[user_name] = []
    else:
        print("This name already.")


def suppress():
    user_name = input("What's the name you need to delete ? ")
    if user_name in user_account.keys():
        del user_account[user_name]
    else:
        print("This name doesn't exists.")


def main_app():
    selection: int = -1
    while selection != 0:
        print("Welcome in Passman")
        print("What can I do for you \n 1. Login \n 2. Register \n 3. Suppress \n 0. exit")
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


if __name__ == "__main__":
    main_app()
