from backend.practices.practices_classes.practice_global_settings.passive_practice_global_settings import PassivePracticeGlobalSettings

class ReadingPracticeGlobalSettings(PassivePracticeGlobalSettings):
    """Global settings for Reading practice (inherits from PassivePracticeGlobalSettings)."""
    def get_user_reading_settings(self) -> dict:
        """Return all global conversation settings as a dictionary."""
        return {
            "difficulty_level": self.get_difficulty_level(),
            "final_writing_question": self.get_final_writing_question(),
            "paragraphs_number": self.get_paragraphs_number(),
            "dialogues_number": self.get_dialogues_number(),
            "difficult_words": self.get_difficult_words(),

        }
    
    def set_user_reading_settings(self, data: dict):
        """Restore settings from a dictionary."""        
        self.set_difficulty_level(data["difficulty_level"])        
        self.set_final_writing_question(data["final_writing_question"])        
        self.set_paragraphs_number(data["paragraphs_number"])        
        self.set_dialogues_number(data["dialogues_number"])        
        self.set_difficult_words(data["difficult_words"])