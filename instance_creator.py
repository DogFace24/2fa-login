class Details():

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f"{self.username}, {self.password}"


