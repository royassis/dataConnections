import abc
from pathlib import Path

import pandas as pd

from dataConnections.resources.base import BaseResource


class ConnectionResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(ConnectionResource, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def read(self):
        pass


class FileResource(ConnectionResource):
    def __init__(self, filepath_or_buffer, *args, **kwargs):
        self.filepath_or_buffer = Path(filepath_or_buffer)
        super().__init__(*args, **kwargs)

    @abc.abstractmethod
    def read(self):
        pass


class DBResource(ConnectionResource):
    def __init__(self, name, conn_str):
        self.conn_str = conn_str
        super().__init__(name)

    @abc.abstractmethod
    def read(self):
        pass


class CsvResource(FileResource):

    def read(self, *args, **kwargs):
        return pd.read_csv(self.filepath_or_buffer, *args, **kwargs)


class ExcelResource(FileResource):
    def __init__(self, filepath_or_buffer, credentials, *args, **kwargs):
        super(ExcelResource, self).__init__(filepath_or_buffer, *args, **kwargs)
        self.credentials = credentials

    def read(self, *args, **kwargs):
        return pd.read_excel(self.filepath_or_buffer, *args, **kwargs)
