import abc

import pandas as pd
from sqlalchemy import create_engine

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