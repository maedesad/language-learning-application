from backend.practices.practices_classes.practice_global_settings.practice_global_setting import PracticeGlobalSettings

class GrammarLearningGlobalSettings(PracticeGlobalSettings):
    """Shared settings for reading and listening exercises with private attributes."""
    def __init__(self):
        super().__init__()  # Initialize difficulty_level from parent class

        # Private attributes with default values             
        self.__productive_practice = False
        self.__paragraphs_number = 5                # Must be between 1 and 20
        self.__dialogues_number = 14                 # Must be between 4 and 40
        self.__grammar_questions = 12             # Must be between 5 and 30

    # ------------------- Getters and Setters -------------------
   

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
        if 4 <= value <= 40:
            self.__dialogues_number = value
        else:            
            raise ValueError("Dialogues must be between 4 and 40")
        
    # Get and Set grammar_questions
    def get_grammar_questions(self):
        return self.__grammar_questions

    def set_grammar_questions(self, value):
        if 5 <= value <= 30:
            self.__grammar_questions = value
        else:            
            raise ValueError("Questions must be between 5 and 30")   

    def get_user_grammar_learning_settings(self) -> dict:
        """Return all global conversation settings as a dictionary."""
        return {
            "difficulty_level": self.get_difficulty_level(),
            "productive_practice": self.get_productive_practice(),
            "paragraphs_number": self.get_paragraphs_number(),
            "dialogues_number": self.get_dialogues_number(),
            "grammar_questions": self.get_grammar_questions()
        }     
    
    def set_user_grammar_learning_settings(self, data: dict):
        """Restore settings from a dictionary."""        
        self.set_difficulty_level(data["difficulty_level"])        
        self.set_productive_practice(data["productive_practice"])        
        self.set_paragraphs_number(data["paragraphs_number"])        
        self.set_dialogues_number(data["dialogues_number"])        
        self.set_grammar_questions(data["grammar_questions"])        