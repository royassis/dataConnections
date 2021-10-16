

from dataConnections.resources.connectors import SQLResources, CsvResources, ExcelResources
from dataConnections.resources.credentials import Creds
from dataConnections.resources.handlers import ConnectionHandler

csv_resource = CsvResources("filea", "path", creds = Creds("a", "b"))
excel_resource = ExcelResources("fileb", "path")
sql_resource = SQLResources("SQL_A", 'postgresql://scott:tiger@localhost:5432/mydatabase')

conn_handler = ConnectionHandler()

conn_handler.add_resource(csv_resource)
conn_handler.add_resource(excel_resource)
conn_handler.add_resource(sql_resource)

print(conn_handler.filea)
