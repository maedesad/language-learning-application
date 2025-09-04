from backend.practices.practices_classes.practice_global_settings.practice_global_setting import PracticeGlobalSettings


class ProductivePracticeGlobalSettings(PracticeGlobalSettings):
    """Shared settings for conversation and writing exercises with private attributes."""
    def __init__(self):
        super().__init__()  # Initialize difficulty_level from parent class

    # Private attributes with default values               
        self.__practice_missions = False

    # Get and Set practice_missions
    def get_practice_missions(self):
        return self.__practice_missions

    def set_practice_missions(self, value):
        if isinstance(value, bool):
            self.__practice_missions = value
        else:
            raise ValueError("final_writing_question must be a boolean value (True/False)")    