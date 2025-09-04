import json
from backend.user.user_class import User
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
all_grammar_jsonpath = os.path.join(
    BASE_DIR,
    "practices_classes",
    "practice_entry_settings",
    "all-grammars.json"
)

class GrammarSelector:
    def __init__(self, user: User, mode: str = "practice", grammar_json_path: str = all_grammar_jsonpath):
        if mode not in ["practice", "learning"]:
            raise ValueError("Mode must be 'practice' or 'learning'")
        self.mode = mode
        self.__user = user
        self.__all_grammars: dict = self.__load_all_grammars(grammar_json_path)
        self.__use_grammar: bool = True

        # -------- User grammar data --------
        self.__learned_grammar = user.get_learned_grammar()
        self.__next_grammar = user.get_next_grammar()
        self.__weak_grammar = user.get_weak_grammar()
        self.__unlearned_needed_grammar = user.get_unlearned_needed_grammar()

        # -------- Selection attributes --------
        self.__selected_grammar_topics: dict = {}
        self.__suggested_grammar_topics: dict = {}

    # ------------------- Use Grammar ------------------- 
    def enable_grammar(self):
        self.__use_grammar = True

    def disable_grammar(self):
        self.__use_grammar = False

    def is_grammar_enabled(self) -> bool:
        return self.__use_grammar    

    # ------------------- JSON Loader -------------------
    def __load_all_grammars(self, path: str) -> dict:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Grammar JSON file not found!")

    def get_all_grammars(self) -> dict:
        return self.__all_grammars

    # ------------------- Helper -------------------
    def __count_total_grammars(self, topics_dict: dict) -> int:
        """Count total number of grammar items across all groups."""
        return sum(len(items) for items in topics_dict.values())

    # ------------------- Selected Grammar Topics -------------------
    def get_selected_grammar_topics(self) -> dict:
        return self.__selected_grammar_topics

    def add_selected_grammar_topic(self, group: str, grammar_id: str):
        """Add a grammar topic based on mode restrictions."""
        limit = 2 if self.mode == "practice" else 1
        if self.__count_total_grammars(self.__selected_grammar_topics) >= limit:
            raise ValueError(f"You can select at most {limit} grammar topic(s).")

        if group in self.__all_grammars and grammar_id in self.__all_grammars[group]:
            # حالت learning: بررسی نشده باشد
            if self.mode == "learning" and group in self.__learned_grammar and grammar_id in self.__learned_grammar[group]:
                raise ValueError("You cannot select a grammar that is already learned in learning mode.")

            if group in self.__selected_grammar_topics and grammar_id in self.__selected_grammar_topics[group]:
                raise ValueError("This grammar topic is already selected.")

            if group not in self.__selected_grammar_topics:
                self.__selected_grammar_topics[group] = {}

            self.__selected_grammar_topics[group][grammar_id] = self.__all_grammars[group][grammar_id]
        else:
            raise ValueError("Selected grammar topic not found in all grammars.")

    def remove_selected_grammar_topic(self, group: str, grammar_id: str):
        if group in self.__selected_grammar_topics:
            self.__selected_grammar_topics[group].pop(grammar_id, None)
            if not self.__selected_grammar_topics[group]:
                self.__selected_grammar_topics.pop(group)

    # ------------------- Suggested Grammar Topics -------------------
    def get_suggested_grammar_topics(self) -> dict:
        if not self.__suggested_grammar_topics:  # اگر هنوز پر نشده
            self.set_suggested_grammar_topics()
        return self.__suggested_grammar_topics

    def set_suggested_grammar_topics(self):
        """Automatically pick grammar topics based on mode."""
        self.__suggested_grammar_topics = {}
        limit = 2 if self.mode == "practice" else 1

        if self.mode == "learning":
            source = self.__next_grammar
            # تنها گرامر بعدی را پیشنهاد بده
            for group, items in source.items():
                for grammar_id, desc in items.items():
                    self.__suggested_grammar_topics[group] = {grammar_id: desc}
                    return
        else:
            sources = [self.__weak_grammar, self.__unlearned_needed_grammar, self.__learned_grammar, self.__next_grammar]
            for source in sources:
                if source:  # check non-empty dict
                    for group, items in source.items():
                        for grammar_id, desc in items.items() if isinstance(items, dict) else []:
                            if self.__count_total_grammars(self.__suggested_grammar_topics) < limit:
                                if group not in self.__suggested_grammar_topics:
                                    self.__suggested_grammar_topics[group] = {}
                                self.__suggested_grammar_topics[group][grammar_id] = desc
                            else:
                                return  # stop once limit reached

    def add_suggested_grammar_topic(self, group: str, grammar_id: str):
        """Let user adjust suggested list manually."""
        limit = 2 if self.mode == "practice" else 1
        if self.__count_total_grammars(self.__suggested_grammar_topics) >= limit:
            raise ValueError(f"You can only have {limit} suggested grammar topic(s).")

        if group in self.__all_grammars and grammar_id in self.__all_grammars[group]:
            if self.mode == "learning" and group in self.__learned_grammar and grammar_id in self.__learned_grammar[group]:
                raise ValueError("Cannot suggest a grammar that is already learned in learning mode.")

            if group in self.__suggested_grammar_topics and grammar_id in self.__suggested_grammar_topics[group]:
                raise ValueError("This grammar topic is already in suggested list.")

            if group not in self.__suggested_grammar_topics:
                self.__suggested_grammar_topics[group] = {}
            self.__suggested_grammar_topics[group][grammar_id] = self.__all_grammars[group][grammar_id]
        else:
            raise ValueError("Grammar topic not found in all grammars.")

    def remove_suggested_grammar_topic(self, group: str, grammar_id: str):
        if group in self.__suggested_grammar_topics:
            self.__suggested_grammar_topics[group].pop(grammar_id, None)
            if not self.__suggested_grammar_topics[group]:
                self.__suggested_grammar_topics.pop(group)
