
import importlib.util
import unittest
from unittest.mock import patch

import sys
sys.path.append('../')

from operation_execution import *


class TestOperationExecution(unittest.TestCase):


    @patch('operation_execution.input', return_value="mx1.txt")
    def test_addition(self, mock_input):
        
        operation_exe = OperationExecution(OperationExecution.mx_add, OperationExecution.load_data_from_file);
        operation_exe.execute()
        # side_effect=['First', 'Second', 'Third']
        calling_1 = mock_input()
        #calling_2 = mock_input()
        #calling_3 = mock_input()

        self.assertTrue(calling_1 == 'mx1.txt')

       #with patch("operation_execution.input", return_value ="y") as mocked_input:
       #    mocked_input.

       #input_reader.input = lambda: "mx1.txt"


if __name__ == "__main__":
    unittest.main()

