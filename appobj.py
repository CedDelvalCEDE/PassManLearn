class SignPaper:

    def __init__(self, user_name: str, password: str):
        self.user_name = {'username': user_name}
        self.password = {'password': password}
        self.AccountVault = AccountVault(user_name)

    def change(self, decision: int, used_string: str):
        match decision:
            case 1:
                self.user_name = used_string
            case 2:
                self.password = used_string


class AccountVault:

    def __init__(self, user_name: str, user_account_site: str = 'empty', user_account_name: str = 'empty',
                 user_account_password: str = 'empty'):
        self.user_name: str = 'empty_string'
        self.user_account_site = []
        self.user_account_name = []
        self.user_account_password = []

    def change(self, decision: int, used_string: str):
        match decision:
            case 1:
                self.user_account_site = used_string
            case 2:
                self.user_account_name = used_string
            case 3:
                self.user_account_password = used_string

    def deleteV(self, decision: int, used_string: str):
        match decision: