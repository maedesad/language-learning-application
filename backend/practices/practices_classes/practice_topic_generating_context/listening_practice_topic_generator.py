from backend.user.user_class import User
from backend.practices.practices_classes.practice_topic_generating_context.practice_topic_generator import PracticeTopicGenerator
from backend.practices.practices_classes.practice_global_settings.individual_practice_classes.listening_practice_global_settings import ListeningPracticeGlobalSettings
from backend.practices.practices_classes.practice_entry_settings.semantic_domain import SemanticDomain
from backend.practices.practices_classes.practice_entry_settings.grammar_selection import GrammarSelector
from backend.practices.practices_classes.practice_entry_settings.vocab_selection import VocabularySelector
from backend.practices.practices_classes.practice_entry_settings.dialogue_setting import DialogueSetting

class ListeningPracticeTopicGenerator(PracticeTopicGenerator, ListeningPracticeGlobalSettings, DialogueSetting):
    def __init__(self, user: User):
        # ------------------- Init parent classes -------------------
        PracticeTopicGenerator.__init__(self, user)
        ListeningPracticeGlobalSettings.__init__(self)
        DialogueSetting.__init__(self)

        # ------------------- Initialize composition objects -------------------
        self.semantic_domain = SemanticDomain(user)
        self.grammar_selector = GrammarSelector(user)
        self.vocab_selector = VocabularySelector(user)

        # ------------------- Override global settings with user values -------------------
        self.set_user_settings_from_user(user)

        
    # ------------------- Helper -------------------
    def set_user_settings_from_user(self, user: User):
        """Override global settings with user-specific values."""
        self.set_difficult_words(user.listening_settings.get_difficult_words())
        self.set_final_writing_question(user.listening_settings.get_final_writing_question())
        self.set_paragraphs_number(user.listening_settings.get_paragraphs_number())
        self.set_dialogues_number(user.listening_settings.get_dialogues_number())

        # Difficulty level specific for reading
        self.set_difficulty_level(user.listening_settings.get_difficulty_level())

    # ------------------- Topic Generator -------------------
    def generate_topics(self, mode: str = "suggested") -> dict:
        is_dialogue = self.get_is_dialogue()
        difficulty = self.get_difficulty_level()

        semantic_domain = None
        grammar_topics = None
        vocab_categories = None

        # --- Grammar ---
        if self.grammar_selector.is_grammar_enabled():
            grammar_topics = (
                self.grammar_selector.get_selected_grammar_topics()
                if mode == "custom"
                else self.grammar_selector.get_suggested_grammar_topics()
            )

        # --- Vocab ---
        if self.vocab_selector.is_vocab_enabled():
            vocab_categories = (
                self.vocab_selector.get_selected_vocab_categories()
                if mode == "custom"
                else self.vocab_selector.get_suggested_vocab_categories()
            )

        # --- Semantic Domain ---
        if self.semantic_domain.is_semantic_domain_enabled():
            semantic_domain = self.semantic_domain.get_selected_semantic_domain()

        # Constraint: cannot have vocab and semantic domain at same time
        if semantic_domain and vocab_categories:
            raise ValueError("Cannot use both semantic domain and vocabulary categories at the same time.")

        # Build context
        context_data = {
            "is_dialogue": is_dialogue,
            "difficulty": difficulty,
            "semantic_domain": semantic_domain,
            "grammar_topics": grammar_topics,
            "vocab_categories": vocab_categories,
        } 

        return context_data  
       
    