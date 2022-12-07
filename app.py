user_account = {}


def login_add(user_name: str):
    print("Enter your account data.")
    site_name = input("What's the website or the game of your account ? ")
    login_account = input("What's your name on this site ? ")
    password = input("What's your password ? ")
    user_account[user_name] = [site_name, login_account, password]


def login():
    user_name = input("What's your name ?")
    if user_name in user_account.keys():
        print('Welcome ' + user_name + '! \n 1. Add an account \n 2. Read an account \n 3. Change an account \n 4. '
                                       'Suppress an account \n 0. exit the login')
        num_match = input("Enter a number")
        while num_match != 0:
            match num_match:
                case 1:
                    login_add(user_name)
                case 2:
                    login_read()
                case 3:
                    login_change()
                case 4:
                    login_suppress()




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
    print("What can I do for you \n 1. Login \n 2. Register \n 3.Suppress \n 0. exit")
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
