class UserNotFoundException(Exception):
    def __init__(self, username: str = None):
        self.username = username
        if username:
            self.message = f"User with username '{username}' does not exist!"
        else:
            self.message = "The user was not found or does not exist!"
        super().__init__(self.message)
