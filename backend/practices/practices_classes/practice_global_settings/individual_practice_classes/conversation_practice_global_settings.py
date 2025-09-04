from backend.practices.practices_classes.practice_global_settings.productive_practice_global_settings import ProductivePracticeGlobalSettings

class ConversationPracticeGlobalSettings(ProductivePracticeGlobalSettings):
    """Global settings for Speaking practice."""
    def __init__(self):
        super().__init__()  # Inherit practice_missions + difficulty_level

        # Private attribute specific to speaking
        self.__user_dialogues_number = 4   # Default: 4, Range: 4 to 20

    # Get and Set user_dialogues_number
    def get_user_dialogues_number(self):
        return self.__user_dialogues_number

    def set_user_dialogues_number(self, value):
        if 4 <= value <= 20:
            self.__user_dialogues_number = value
        else:
            raise ValueError("User dialogues must be between 4 and 20")

    def get_user_conversation_settings(self) -> dict:
        """Return all global conversation settings as a dictionary."""
        return {
            "difficulty_level": self.get_difficulty_level(),
            "practice_missions": self.get_practice_missions(),
            "user_dialogues_number": self.get_user_dialogues_number()
        }   
    
    def set_user_conversation_settings(self, data: dict):
        """Restore settings from a dictionary."""        
        self.set_difficulty_level(data["difficulty_level"])        
        self.set_practice_missions(data["practice_missions"])        
        self.set_user_dialogues_number(data["user_dialogues_number"])        
        