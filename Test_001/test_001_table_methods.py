import os
import pytest
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from TestServices.Config.get_test_input import GetTestInput
from TestServices.AccessMethods.run_table_methods import RunTableMethods

# Get test cofiguration input
config = GetTestInput(__file__)

# Run method to be tested
input = RunTableMethods(config)


class TestClass:
    def test_001_initialize_table(self):
        assert input.sql_command_list[0] == config.sql_command_line

    def test_002_sql_command_list(self):
        assert len(input.sql_command_list) == len(config.customers) + 1
