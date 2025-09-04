from backend.practices.practices_classes.practice_global_settings.productive_practice_global_settings import ProductivePracticeGlobalSettings

class WritingPracticeGlobalSettings(ProductivePracticeGlobalSettings):
    """Global settings for Writing practice."""
    def __init__(self):
        super().__init__()  # Inherit practice_missions + difficulty_level

        # Private attribute specific to writing
        self.__paragraphs_number = 2   # Default: 2, Range: 1 to 8

    # Get and Set paragraphs_number
    def get_paragraphs_number(self):
        return self.__paragraphs_number

    def set_paragraphs_number(self, value):
        if 1 <= value <= 5:
            self.__paragraphs_number = value
        else:
            raise ValueError("Paragraphs must be between 1 and 5")

    def get_user_writing_settings(self) -> dict:
        """Return all global conversation settings as a dictionary."""
        return {
            "difficulty_level": self.get_difficulty_level(),
            "practice_missions": self.get_practice_missions(),
            "paragraphs_number": self.get_paragraphs_number()
        }       
    
    def set_user_writing_settings(self, data: dict): 
        """Restore settings from a dictionary."""        
        self.set_difficulty_level(data["difficulty_level"])        
        self.set_practice_missions(data["practice_missions"])        
        self.set_paragraphs_number(data["paragraphs_number"])     