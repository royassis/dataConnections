from dataConnections.resources.connectors import CsvResource, ExcelResource
from dataConnections.resources.credentials import CredentialsResource
from dataConnections.resources.handlers import ConnectionHandler
from dataConnections.resources.query import SQLResource

from config import DATA_DIR

csv_file = DATA_DIR.joinpath("example.csv")
csv_resource = CsvResource(name="csv_connection_1", filepath_or_buffer=csv_file)
excel_resource = ExcelResource(name= "fileb", filepath_or_buffer="path",
                               creds=CredentialsResource(name="a", password="b"))

sql_resource = SQLResource("SQL_A", 'postgresql://scott:tiger@localhost:5432/mydatabase')

conn_handler = ConnectionHandler()

conn_handler.add_resource(csv_resource)
conn_handler.add_resource(excel_resource)
conn_handler.add_resource(sql_resource)

print(conn_handler.filea)
