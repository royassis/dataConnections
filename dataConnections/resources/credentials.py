from dataConnections.resources.base import BaseResource


class CredentialsResource(BaseResource):
    def __init__(self, password, *args, **kwargs):
        self.password = password
        super(CredentialsResource, self).__init__(*args, **kwargs)


class ExcelCredentials(CredentialsResource):
    pass


class DbCredentials(CredentialsResource):
    def __init__(self, username, host, *args, **kwargs):
        self.host = host
        self.username = username
        super(DbCredentials, self).__init__(*args, **kwargs)
