import abc

class Creds:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Creds:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class DbCreds(Creds):
    def __init__(self, username, password, host):
        self.host = host
        super(DbCreds, self).__init__(username, password)