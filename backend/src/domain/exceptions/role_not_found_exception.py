class RoleNotFoundException(Exception):
    def __init__(self, role: str = None):
        self.role = role
        if role:
            self.message = f"Role with name '{role}' does not exist!"
        else:
            self.message = "The role was not found or does not exist!"
        super().__init__(self.message)
