def login_input(self, user=Customer1):
    with step(f"Ввод логин: {user.USERNAME}"):
        self.input(AuthLoc.USERNAME, user.USERNAME)


def pass_input(self, user=Customer1):
    with step(f"Ввод пароль: {user.PASSWORD}"):
        self.input(AuthLoc.PASSWORD, user.PASSWORD)