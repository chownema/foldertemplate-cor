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
        instructions_body_dict = InstructionsService.init_instruction_body()
        self.assertEqual("exclude_list" in instructions_body_dict, # Key Exists in dict
                         True,
                         "Instruction should have an exclude list part of body")
        pass

    def test_check_include_folders(self):
        instructions_body_dict = InstructionsService.init_instruction_body()
        self.assertEqual("include_list" in instructions_body_dict, # Key Exists in dict
                         True,
                         "Instruction should have an include list part of body")
        pass

    def test_check_for_folder_struct_config(self):
        instruction_dict = InstructionsService.init_instruction()
        self.assertEqual("folder_struct" in instruction_dict, # Key Exists in dict
                         True,
                         "Instruction should have a folder Structure part in of dict")
        pass

    def test_check_for_folder_child_struct_config(self):
        # Check for folder child structure provided in the instruction dict if provided 
        pass

    def test_check_for_folder_struct_config_missing_folder_or_file(self):
        # Check for a mising folder or file according to the folder structure at an instruction point
        pass

    def test_loop_through_all_folders(self):
        # check response object has checked off the items in the list of folders given
        pass

    def test_loop_through_all_folders_children_folders(self):
        # check response object has checked off the items in the list of children folders given
        pass

    def test_loop_through_all_folders_parent_and_children_folders(self):
        # check response object has checked off the items in the list of children & parent folders given
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