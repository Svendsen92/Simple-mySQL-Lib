from datetime import datetime
from mySQL_DatabaseLib import mySQL_DatabaseLib # type: ignore

host = "localhost"
user = "root"
database = "exampleDB"
password = "Dino1@dlgnet.dk"
tableName = "example_table"

# Create database object
db = mySQL_DatabaseLib(host=host, user=user, password=password, database=database)

# Create database if it does not already exist
db.createDatabase(database)

# Create table if it does not already exist
ColumnNames = {"inputType": "VARCHAR(20)", "value": "INT", "timeStamp": "DATETIME"}
db.createTable(tableName=tableName, columnHeaders=ColumnNames)

headerList : list = ["inputType", "value", "timeStamp"]

# Insert data
valuesTuple: tuple = ('exampleInput1', 999, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
status = db.insert(tableName=tableName, header=headerList, values=valuesTuple)
print(f"insert status = {status}")

# Update the data that was just inserted 
valuesTuple: tuple = ('new_exampleInput', 888, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
status = db.update(tableName=tableName, header=headerList, values=valuesTuple, condition="inputType = 'exampleInput1'")
print(f"update status = {status}")

# Insert new data
valuesTuple: tuple = ('exampleInput2', 777, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
status = db.insert(tableName=tableName, header=headerList, values=valuesTuple)
print(f"insert status = {status}")

# Retrive the inputType where value = 777
result = db.select(tableName=tableName, header="inputType", condition="value = 777")
print(f"select result = {result}")