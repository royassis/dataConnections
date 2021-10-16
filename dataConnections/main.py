from connections import csv_resource, excel_resource

df = csv_resource.read()
df2 = excel_resource.read()
print(df2)