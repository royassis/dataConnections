from dataConnections.resources.base import BaseResource


class CredentialsResource(BaseResource):
    def __init__(self, password):
        self.password = password


class ExcelCredentials(CredentialsResource):
    pass


class DbCredentials(CredentialsResource):
    def __init__(self, username, password, host):
        self.host = host
        self.username = username
        super(DbCredentials, self).__init__(password)
