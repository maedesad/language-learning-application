from backend.practices.practices_classes.practice_global_settings.practice_global_setting import PracticeGlobalSettings

class VocabLearningGlobalSettings(PracticeGlobalSettings):
    """Shared settings for reading and listening exercises with private attributes."""
    def __init__(self):
        super().__init__()  # Initialize difficulty_level from parent class

        # Private attributes with default values
        self.__difficult_words = 8          # Must be between 3 and 20        
        self.__productive_practice = False
        self.__paragraphs_number = 5                # Must be between 1 and 20
        self.__dialogues_number = 14  
        self.__questions_per_word = 2             # Must be between 1 and 5

    # ------------------- Getters and Setters -------------------

    # Get and Set difficult_words
    def get_difficult_words(self):
        return self.__difficult_words

    def set_difficult_words(self, value):
        if 3 <= value <= 20:
            self.__difficult_words = value
        else:
            raise ValueError("Difficult words must be between 3 and 20")

    # Get and Set productive_practice
    def get_productive_practice(self):
        return self.__productive_practice

    def set_productive_practice(self, value):
        if isinstance(value, bool):
            self.__productive_practice = value
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
        
    # Get and Set questions_per_word
    def get_questions_per_word(self):
        return self.__questions_per_word

    def set_questions_per_word(self, value):
        if 1 <= value <= 5:
            self.__questions_per_word = value
        else:
            raise ValueError("Dialogues must be between 2 and 40")    
        
    def get_user_vocab_learning_settings(self) -> dict:
        """Return all global conversation settings as a dictionary."""
        return {
            "difficulty_level": self.get_difficulty_level(),
            "productive_practice": self.get_productive_practice(),
            "questions_per_word": self.get_questions_per_word(),
            "paragraphs_number": self.get_paragraphs_number(),
            "dialogues_number": self.get_dialogues_number(),
            "difficult_words": self.get_difficult_words(),

        }  

    def set_user_vocab_learning_settings(self, data: dict):
        """Restore settings from a dictionary."""        
        self.set_difficulty_level(data["difficulty_level"])        
        self.set_productive_practice(data["productive_practice"])        
        self.set_paragraphs_number(data["paragraphs_number"])        
        self.set_dialogues_number(data["dialogues_number"])        
        self.set_questions_per_word(data["questions_per_word"])              