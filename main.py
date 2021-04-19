import pandas as pd
import abc
from sqlalchemy import create_engine


class ResourceNameExistsException(Exception):
    pass

class Creds:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class DbCreds(Creds):
    def __init__(self, username, password, host):
        self.host = host
        super(DbCreds, self).__init__(username, password)


class ConnectionResource(abc.ABC):
    def __init__(self, name, creds=None):
        self.name = name
        self.creds = creds

    @abc.abstractmethod
    def read(self):
        pass


class FileResources(ConnectionResource):
    def __init__(self, name, filepath_or_buffer, creds=None, *args, **kwargs):
        self.filepath_or_buffer = filepath_or_buffer
        super().__init__(name, creds=creds, *args, **kwargs)

    @abc.abstractmethod
    def read(self):
        pass


class DBResources(ConnectionResource):
    def __init__(self, name, conn_str):
        self.conn_str = conn_str
        super().__init__(name)

    @abc.abstractmethod
    def read(self):
        pass


class SQLResources(DBResources):
    def __init__(self, name, conn_str):
        self.engine = create_engine(conn_str)
        super(SQLResources, self).__init__(name, conn_str)

    def read(self, q, *args, **kwargs):
        with self.engine.connect() as con:
            return pd.read_sql(q, con, *args, **kwargs)


class CsvResources(FileResources):

    def read(self, *args, **kwargs):
        return pd.read_csv(self.filepath_or_buffer, *args, **kwargs)


class ExcelResources(FileResources):

    def read(self, *args, **kwargs):
        return pd.read_excel(self.filepath_or_buffer, *args, **kwargs)


class ConnectionHandler:
    def __init__(self):
        self.resources = dict()

    def add_resource(self, resource):
        if self.resources.get(resource.name):
            raise ResourceNameExistsException()

        self.resources[resource.name] = resource
        self.__dict__.update({resource.name: resource})

    def __getitem__(self, key):
        return self.resources[key]


csv_resource = CsvResources("filea", "path", creds = Creds("a","b"))
excel_resource = ExcelResources("fileb", "path")
sql_resource = SQLResources("SQL_A", 'postgresql://scott:tiger@localhost:5432/mydatabase')

conn_handler = ConnectionHandler()

conn_handler.add_resource(csv_resource)
conn_handler.add_resource(excel_resource)
conn_handler.add_resource(sql_resource)

print(conn_handler.filea)
