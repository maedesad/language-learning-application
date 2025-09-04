from backend.practices.practices_classes.practice_global_settings.individual_practice_classes import (
    ReadingPracticeGlobalSettings,
    ListeningPracticeGlobalSettings,
    WritingPracticeGlobalSettings,
    ConversationPracticeGlobalSettings,
    VocabLearningGlobalSettings,
    GrammarLearningGlobalSettings
)

class User:
    """User profile with global practice settings, vocabulary categories, and grammar progress."""

    def __init__(self, username: str, userID: str, semantic_domains: list[str]):
        self.__username = username
        self.__userID = userID
        self.__semantic_domains = semantic_domains  # ["sport", "economy", ...]

        # ---------------- Practice settings (default objects from previous classes) ----------------
        self.reading_settings = ReadingPracticeGlobalSettings()
        self.listening_settings = ListeningPracticeGlobalSettings()
        self.writing_settings = WritingPracticeGlobalSettings()
        self.conversation_settings = ConversationPracticeGlobalSettings()
        self.vocabulary_settings = VocabLearningGlobalSettings()
        self.grammar_settings = GrammarLearningGlobalSettings()

        # ---------------- Vocabulary attributes ----------------
        self.__vocabulary_categories = {}  # {"Art": [...], "Kitchen": [...]}
        self.__weak_vocabulary_categories = []  # ["Art"]
        self.__suggested_vocabulary_categories = []  # ["express feelings", ...]

        self.__weak_words = []  # ["plate", "cup", "pan"]

        # ---------------- Grammar attributes ----------------
        self.__learned_grammar = {}  
        # {"Present and past": {"1":"Present continuous (I am doing)", ...}}

        self.__next_grammar = {}  
        # {"Present and past": {"16": "Past perfect continuous (I had been doing)"}}

        self.__week_grammar = {}  
        # {"Present and past": {"3": "Present continuous and present simple 1 (I am doing and I do)", "5": "Past simple (I did)"}}

        self.__unlearned_needed_grammar = {}  
        # {"Modals": {"29": "might", "24": "must"}}

    # ---------------- Getters ----------------
    def get_username(self):
        return self.__username

    def get_userID(self):
        return self.__userID

    def get_semantic_domains(self):
        return self.__semantic_domains

    def get_vocabulary_categories(self):
        return self.__vocabulary_categories

    def get_weak_vocabulary_categories(self):
        return self.__weak_vocabulary_categories

    def get_suggested_vocabulary_categories(self):
        return self.__suggested_vocabulary_categories

    def get_weak_words(self):
        return self.__weak_words

    def get_learned_grammar(self):
        return self.__learned_grammar

    def get_next_grammar(self):
        return self.__next_grammar

    def get_weak_grammar(self):
        return self.__week_grammar

    def get_unlearned_needed_grammar(self):
        return self.__unlearned_needed_grammar

    # ---------------- Mutators (examples) ----------------
    def add_vocabulary_category(self, category_name: str, words: list[str]):
        self.__vocabulary_categories[category_name] = words

    def add_learned_grammar(self, group: str, grammar_id: str, grammar_desc: str):
        if group not in self.__learned_grammar:
            self.__learned_grammar[group] = {}
        self.__learned_grammar[group][grammar_id] = grammar_desc

    def set_next_grammar(self, group: str, grammar_id: str, grammar_desc: str):
        # فقط یک مورد نگه می‌دارد، قبلی را حذف می‌کند
        self.__next_grammar = {grammar_id: grammar_desc}

    def add_week_grammar(self, group: str, grammar_id: str, grammar_desc: str):
        if group not in self.__week_grammar:
            self.__week_grammar[group] = {}
        self.__week_grammar[group][grammar_id] = grammar_desc

    def add_unlearned_needed_grammar(self, group: str, grammar_id: str, grammar_desc: str):
        if group not in self.__unlearned_needed_grammar:
            self.__unlearned_needed_grammar[group] = {}
        self.__unlearned_needed_grammar[group][grammar_id] = grammar_desc
    
    def add_weak_vocabulary_category(self, category_name: str):
        if category_name not in self.__weak_vocabulary_categories:
            self.__weak_vocabulary_categories.append(category_name)

    def add_suggested_vocabulary_category(self, category_name: str):
        if category_name not in self.__suggested_vocabulary_categories:
            self.__suggested_vocabulary_categories.append(category_name)

    def add_weak_word(self, word: str):
        if word not in self.__weak_words:
            self.__weak_words.append(word)