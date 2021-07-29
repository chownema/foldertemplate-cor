import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from instructions_service import InstructionsService
import unittest

class TestFolder(unittest.TestCase):
    def setUp(self):
        # load test data
        pass

    def test_check_exclude_folders(self):
        pass

    def test_check_include_folders(self):
        pass
    def test_check_for_folder_struct_config(self):
        instructions_body_dict = InstructionsService.init_instruction_body()
        instruction_dict = InstructionsService.init_instruction()
        # print(instructions_body_dict)
        self.assertEqual(bool(instruction_dict["folder_struct"]), # Is not Empty
                         True,
                         "Instruction should have a folder Structure part in body")
        # self.assertEqual(,,"")
        pass

    def test_check_for_folder_child_struct_config(self):
        pass

    def test_check_for_folder_struct_config_missing_info(self):
        pass

    def test_loop_through_all_folders(self):
        pass

    def test_loop_through_all_folders_children_folders(self):
        pass

    def test_loop_through_all_folders_parent_and_children_folders(self):
        pass

    def test_existence_of_folder(self):
        pass

    def test_existence_of_file(self):
        pass

    def test_existence_of_file(self):
        pass


class TestCreateLogic(unittest.TestCase):
    def setUp(self):
        # load test data
        pass

    def test_create_missing_folder(self):
        pass

    def test_create_missing_(self):
        pass

if __name__ == '__main__':
    unittest.main()
