import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from instructions_service import InstructionsService
import unittest

# Testing the logical objects in the system
class TestInterfaceObjects(unittest.TestCase):
    def setUp(self):
        # Objects
        # request
        # response
        pass
    
    def test_check_folder_object_properties(self):
        folder = TemplateFolderFactory.get_folder()
        self.assertEqual("name" in folder, True, "folder contains name")
        self.assertEqual(isinstance(folder["name"], str)  , True, "folder contains name")
        self.assertEqual("children" in folder, True, "folder contains folder list")
        self.assertEqual(isinstance(folder["children"], list)  , True, "folder contains name")
        self.assertEqual("exists" in folder, True, "folder contains boolean for existing")
        self.assertEqual(isinstance(folder["exists"], bool)  , True, "folder contains boolean existing")
        pass

    def test_check_request_object_properties(self):
        request = TemplateInterfaceFactory.get_request()
        self.assertEqual("name" in request, True, "request contains name")
        self.assertEqual(isinstance(request["name"], str)  , True, "request contains name")
        self.assertEqual(isinstance(request["success"], bool)  , True, "request contains boolean success")
        pass

    def test_check_response_object_properties(self):
        response = TemplateInterfaceFactory.get_response()
        self.assertEqual("name" in response, True, "response contains name")
        self.assertEqual(isinstance(response["name"], str)  , True, "response contains name") 
        self.assertEqual(isinstance(response["success"], bool)  , True, "request contains boolean success")
        pass


class TestFolderObject(unittest.TestCase):
    def setUp(self):
        # load test data
        # folder
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

if __name__ == '__main__':
    unittest.main()
