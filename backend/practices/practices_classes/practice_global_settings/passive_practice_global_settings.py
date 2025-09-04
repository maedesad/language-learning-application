from backend.practices.practices_classes.practice_global_settings.practice_global_setting import PracticeGlobalSettings

class PassivePracticeGlobalSettings(PracticeGlobalSettings):
    """Shared settings for reading and listening exercises with private attributes."""
    def __init__(self):
        super().__init__()  # Initialize difficulty_level from parent class

        # Private attributes with default values
        self.__difficult_words = 8          # Must be between 3 and 20        
        self.__final_writing_question = False
        self.__paragraphs_number = 5                # Must be between 1 and 20
        self.__dialogues_number = 14                # Must be between 2 and 40

    # ------------------- Getters and Setters -------------------

    # Get and Set difficult_words
    def get_difficult_words(self):
        return self.__difficult_words

    def set_difficult_words(self, value):
        if 3 <= value <= 20:
            self.__difficult_words = value
        else:
            raise ValueError("Difficult words must be between 3 and 20")

    # Get and Set final_writing_question
    def get_final_writing_question(self):
        return self.__final_writing_question

    def set_final_writing_question(self, value):
        if isinstance(value, bool):
            self.__final_writing_question = value
        else:
            raise ValueError("final_writing_question must be a boolean value (True/False)")

    # Get and Set paragraphs
    def get_paragraphs_number(self):
        return self.__paragraphs_number

    def set_paragraphs_number(self, value):
        if 1 <= value <= 20:
            self.__paragraphs_number = value
        else:
            raise ValueError("Paragraphs must be between 1 and 20")

    # Get and Set dialogues
    def get_dialogues_number(self):
        return self.__dialogues_number

    def set_dialogues_number(self, value):
        if 2 <= value <= 40:
            self.__dialogues_number = value
        else:
            raise ValueError("Dialogues must be between 2 and 40")