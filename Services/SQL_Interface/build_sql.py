import os
import sqlite3


class BuildSql():
    def __init__(self, input):
        self.customers = input.customers
        self.root = input.root
        self.database_file = os.path.join(self.root, 'Database', 'Customers.db')
    
    def execute_workflow(self):
        self.__remove_database()
        self.__connect_database()
        self.initialize_table()
        self.add_table_values()
        self.__close_connection()


    def __remove_database(self):
        if os.path.exists(self.database_file):
            os.remove(self.database_file)

    def __connect_database(self):
        self.connection = sqlite3.connect(self.database_file)
        self.c = self.connection.cursor()

    def initialize_table(self):
        sql_command = "CREATE TABLE Customers ("
        sql_command += "CustomerID, "
        sql_command += "CustomerName, "
        sql_command += "ContactName, "
        sql_command += "Address, "
        sql_command += "City, "
        sql_command += "PostalCode, "
        sql_command += "Country"
        sql_command += ")"
        try:
            self.c.execute(sql_command)
        except Exception as e:
            print(e)
            print('Database connection not available during test')
        self.sql_command_list = [sql_command]

    def add_table_values(self):
        for key, value in self.customers.items():
            sql_command = "INSERT INTO Customers VALUES ("
            sql_command += "'" + value["CustomerID"] + "', "
            sql_command += "'" + value["CustomerName"] + "', "
            sql_command += "'" + value["ContactName"] + "', "
            sql_command += "'" + value["Address"] + "', "
            sql_command += "'" + value["City"] + "', "
            sql_command += "'" + value["PostalCode"] + "', "
            sql_command += "'" + value["Country"] + "')"
            try:
                self.c.execute(sql_command)
            except Exception as e:
                print(e)
                print('Database connection not available during test')
            self.sql_command_list.append(sql_command)

    def __close_connection(self):
        # self.c.execute("SELECT * FROM Customers")
        # print(self.c.fetchall())
        self.connection.close()
