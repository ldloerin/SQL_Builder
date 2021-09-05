import os
import sys
file_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(os.path.split(file_path)[0])
from Services.SQL_Interface.build_sql import BuildSql


class RunTableMethods():
    def __init__(self, input):
        self.customers = input.customers
        self.root = input.root
        self.__execute_workflow()

    def __execute_workflow(self):
        sql = BuildSql(self)
        sql.initialize_table()
        sql.add_table_values()
        self.sql_command_list = sql.sql_command_list
