import json
from abc import ABC, abstractmethod
from typing import List
from backend.user.user_class import User   # Importing the User class

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

difficulty_levels_jsonpath = os.path.join(
    BASE_DIR,
    "practices_classes",
    "practices_attribute",
    "difficulty_levels.json"
)




class PracticeTopicGenerator(ABC):
    def __init__(self, user: User, json_file=difficulty_levels_jsonpath):
        self.__json_file = json_file        
        self.__suggested_topics: List[str] = [] 
        self.__user = user
        self.__difficulty_level = None   
       
    
    # -------------------
    # Getter & Setter Suggested Topics
    def get_suggested_topics(self) -> list[str]:
        return self.__suggested_topics
    
    def set_suggested_topics(self, topics: list[str]):
        self.__suggested_topics = topics
   
    # -------------------
    # Abstract method to generate topic

    class PracticeGenerator(ABC):
        @abstractmethod
        def generate_topics(self) -> List[str]:
            """Subclasses must implement how to generate a list of practice topics"""
            pass

    
    # -------------------
    # Getter & Setter Difficulty Level
    def get_difficulty_level(self):
        return self.__difficulty_level
    
    def set_difficulty_level(self, level_number: int):
        """Manually override difficulty level"""
        if isinstance(level_number, int) and 1 <= level_number <= 10:
            self.__difficulty_level = self._load_difficulty(level_number)
        else:
            raise ValueError("Level number must be between 1 and 10")
    
    # -------------------
    # Getter & Setter User
    def get_user(self):
        return self.__user
    
    def set_user(self, user: User):
        """Change user. Difficulty must be set by subclass again."""
        self.__user = user
        self.__difficulty_level = None   # Reset, subclass must re-apply

    # -------------------
    # Helper method to load difficulty level from JSON file
    def _load_difficulty(self, level_number: int):
        """Protected method: subclasses use this to fetch difficulty info"""
        try:
            with open(self.__json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                level_str = str(level_number)
                if level_str in data:
                    return {level_str: data[level_str]}
                else:
                    raise ValueError(f"Level {level_number} not found in JSON")
        except FileNotFoundError:
            raise FileNotFoundError("Difficulty levels JSON file not found!")
        
        
    
        