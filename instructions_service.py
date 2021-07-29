class InstructionsService:
    def init(self):
        pass

    @staticmethod
    def init_instruction_body(**kwargs):
        return {
           "target_folder" : "",
           "exclude_list" : [],
           "include_list" : [],
           "instructions" : [],
        }

    def init_instruction(**kwargs):
        return {
            "instruction_type":  "", # APPLY_STRUCTURE_FOLDER / CREATE_FOLDER / CD_FOLDER / RENAME_FOLDER
            "target": "",
            "folder_struct": [
                {
                    "name": "",
                    "is_override": False
                }
            ]
        }

