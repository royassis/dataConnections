from sqlalchemy import create_engine

from dataConnections.resources.connectors import DBResource


class SQLResource(DBResource):
    def __init__(self, name, conn_str):
        self.engine = create_engine(conn_str)
        super(SQLResource, self).__init__(name, conn_str)

    def read(self, q, *args, **kwargs):
        with self.engine.connect() as con:
            return pd.read_sql(q, con, *args, **kwargs)

