
class PracticeGlobalSettings:
    """Base class for all exercise settings with shared attributes."""
    def __init__(self, difficulty_level=5):
        self.set_difficulty_level(difficulty_level)

    # -------------------
    # Getter & Setter Difficulty Level
    def get_difficulty_level(self):
        return self.difficulty_level

    def set_difficulty_level(self, value):
        if 1 <= value <= 10:
            self.difficulty_level = value
        else:
            raise ValueError("Difficulty level must be between 1 and 10")