class IncorrectPasswordException(Exception):
    def __init__(self, username: str = None):
        self.username = username
        if username:
            self.message = f"The given password for user {username} is incorrect!"
        else:
            self.message = "The given password is incorrect!"
        super().__init__(self.message)
