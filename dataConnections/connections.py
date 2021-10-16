from dataConnections.config import DATA_DIR
from dataConnections.resources.connectors import CsvResource, ExcelResource
from dataConnections.resources.credentials import CredentialsResource
from dataConnections.resources.query import SQLResource

csv_file = DATA_DIR.joinpath("example.csv")
excel_file = DATA_DIR.joinpath("example.xlsx")
csv_resource = CsvResource(name="csv_file_1", filepath_or_buffer=csv_file)
excel_resource = ExcelResource(name= "excel_file1", filepath_or_buffer=excel_file,
                               credentials=CredentialsResource(name="excel-creds", password="b"))

sql_resource = SQLResource("SQL_A", 'postgresql://scott:tiger@localhost:5432/mydatabase')