import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput
from Services.Output.write_dockerfile import WriteDockerfile
from Services.SQL_Interface.build_sql import BuildSql


class BuildSqlDatabase(GetInput):
    def execute_workflow(self):
        self.__main()
        self.__create_dockerfile()

    def __main(self):
        self.root = os.path.split(os.path.dirname(__file__))[0]
        self.sql_command_list = BuildSql(self).sql_command_list

    def __create_dockerfile(self):
        self.root_path = os.path.dirname(self.code_path)
        WriteDockerfile(self)


my_code = BuildSqlDatabase(__file__)
my_code.execute_workflow()
