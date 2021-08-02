class InstructionsService:
    def init(self):
        pass

    @staticmethod
    def init_instruction_body(**kwargs):
        return { **{
           "target_folder" : "",
           "exclude_list" : [],
           "include_list" : [],
           "instructions" : [],
        }, **kwargs } # Merge

    def init_instruction(**kwargs):
        return { **{
            "instruction_type":  "", # APPLY_STRUCTURE_FOLDER / CREATE_FOLDER / CD_FOLDER / RENAME_FOLDER
            "target": "",
            "folder_struct": [
                # {
                #     "name": "",
                #     "is_override": False,
                #     "is_child_structure": False,
                #     "is_parent_structure": False
                # }
            ]
        }, **kwargs }

    def init_folder_structure(**kwargs):
        return { **{
            "name": "",
            "is_override": False,
            "is_child_structure": False,
            "is_parent_structure": False
        }, **kwargs}
