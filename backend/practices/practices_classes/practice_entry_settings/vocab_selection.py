from backend.user.user_class import User


class VocabularySelector:
    def __init__(self, user: User):
        self.__user = user
        self.__use_vocab: bool = True

        # -------- User vocabulary data --------
        self.__vocabulary_categories: dict = user.get_vocabulary_categories()
        self.__weak_vocabulary_categories: dict = user.get_weak_vocabulary_categories()

        # -------- Selection attributes --------
        self.__selected_vocab_categories: dict = {}
        self.__suggested_vocab_categories: dict = {}


    # ------------------- Use Vocab ------------------- 
    def enable_vocab(self):
        self.__use_vocab = True

    def disable_vocab(self):
        self.__use_vocab = False

    def is_vocab_enabled(self) -> bool:
        return self.__use_vocab    



    # ------------------- Helper -------------------
    def __count_total_categories(self, categories_dict: dict) -> int:
        """Count total number of vocabulary categories (by category names)."""
        return len(categories_dict)

    # ------------------- Selected Vocabulary Categories -------------------
    def get_selected_vocab_categories(self) -> dict:
        return self.__selected_vocab_categories

    def add_selected_vocab_category(self, category: str):
        """Add a vocabulary category if it exists in user's categories and limit <= 2."""
        if self.__count_total_categories(self.__selected_vocab_categories) >= 2:
            raise ValueError("You can select at most 2 vocabulary categories.")

        if category not in self.__vocabulary_categories:
            raise ValueError("Selected vocabulary category not found in user's categories.")

        if category in self.__selected_vocab_categories:
            raise ValueError("This vocabulary category is already selected.")

        # Add category with its words
        self.__selected_vocab_categories[category] = self.__vocabulary_categories[category]

    def remove_selected_vocab_category(self, category: str):
        self.__selected_vocab_categories.pop(category, None)

    # ------------------- Suggested Vocabulary Categories -------------------
    def get_suggested_vocab_categories(self) -> dict:
        if not self.__suggested_vocab_categories:  # اگه هنوز پر نشده
            self.set_suggested_vocab_categories()
        return self.__suggested_vocab_categories

    # def set_suggested_vocab_categories(self):
    #     """Automatically pick up to 2 vocabulary categories for suggestion.
    #     Priority: weak categories -> vocabulary categories.
    #     If both empty, suggestions remain empty.
    #     """
    #     self.__suggested_vocab_categories = {}

    #     sources = [
    #         self.__weak_vocabulary_categories,
    #         self.__vocabulary_categories,
    #     ]

    #     for source in sources:
    #         if source:  # check non-empty dict
    #             for category, vocab_list in source.items():
    #                 if self.__count_total_categories(self.__suggested_vocab_categories) < 2:
    #                     self.__suggested_vocab_categories[category] = vocab_list
    #                 else:
    #                     return  # stop once we have 2 categories

    # def add_suggested_vocab_category(self, category: str):
    #     """Let user adjust suggested list manually (limit 2)."""
    #     if self.__count_total_categories(self.__suggested_vocab_categories) >= 2:
    #         raise ValueError("You can only have 2 suggested vocabulary categories.")

    #     if category not in self.__vocabulary_categories:
    #         raise ValueError("Vocabulary category not found in user's categories.")

    #     if category in self.__suggested_vocab_categories:
    #         raise ValueError("This vocabulary category is already in suggested list.")

    #     self.__suggested_vocab_categories[category] = self.__vocabulary_categories[category]

    # def remove_suggested_vocab_category(self, category: str):
    #     self.__suggested_vocab_categories.pop(category, None)

    def set_suggested_vocab_categories(self):
        """Automatically pick up to 2 vocabulary categories for suggestion.
        Priority: weak categories -> all vocabulary categories.
        """
        self.__suggested_vocab_categories = {}

        # ۱- اول از weak ها
        for category in self.__weak_vocabulary_categories:
            if category in self.__vocabulary_categories:
                if self.__count_total_categories(self.__suggested_vocab_categories) < 2:
                    self.__suggested_vocab_categories[category] = self.__vocabulary_categories[category]
                else:
                    return  # stop once we have 2

        # ۲- بعد از همه کتگوری ها
        for category, vocab_list in self.__vocabulary_categories.items():
            if category not in self.__suggested_vocab_categories:
                if self.__count_total_categories(self.__suggested_vocab_categories) < 2:
                    self.__suggested_vocab_categories[category] = vocab_list
                else:
                    return  # stop once we have 2