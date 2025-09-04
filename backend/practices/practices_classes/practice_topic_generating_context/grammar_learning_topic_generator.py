from backend.user.user_class import User
from backend.practices.practices_classes.practice_topic_generating_context.practice_topic_generator import PracticeTopicGenerator
from backend.practices.practices_classes.practice_global_settings.individual_practice_classes.grammar_learning_global_settings import GrammarLearningGlobalSettings
from backend.practices.practices_classes.practice_entry_settings.semantic_domain import SemanticDomain
from backend.practices.practices_classes.practice_entry_settings.grammar_selection import GrammarSelector
from backend.practices.practices_classes.practice_entry_settings.dialogue_setting import DialogueSetting

class GrammarLearningTopicGenerator(PracticeTopicGenerator, GrammarLearningGlobalSettings, DialogueSetting):
    def __init__(self, user: User):
        # ------------------- Init parent classes -------------------
        PracticeTopicGenerator.__init__(self, user)
        GrammarLearningGlobalSettings.__init__(self)
        DialogueSetting.__init__(self)

        # ------------------- Initialize composition objects -------------------
        self.semantic_domain = SemanticDomain(user)
        self.grammar_selector = GrammarSelector(user=user, mode="learning")
        

        # ------------------- Override global settings with user values -------------------
        self.set_user_settings_from_user(user)

        
    # ------------------- Helper -------------------
    def set_user_settings_from_user(self, user: User):
        """Override global settings with user-specific values."""
        self.set_productive_practice(user.grammar_settings.get_productive_practice())
        self.set_grammar_questions(user.grammar_settings.get_grammar_questions())
        self.set_paragraphs_number(user.grammar_settings.get_paragraphs_number())
        self.set_dialogues_number(user.grammar_settings.get_dialogues_number())

        # Difficulty level specific for reading
        self.set_difficulty_level(user.grammar_settings.get_difficulty_level())



    # ------------------- Topic Generator -------------------
    def generate_topics(self, mode: str = "suggested") -> dict:
        is_dialogue = self.get_is_dialogue()
        difficulty = self.get_difficulty_level()

        semantic_domain = None
        grammar_topic = None
        

        # --- Grammar ---       
        grammar_topic = (
            self.grammar_selector.get_selected_grammar_topics()
            if mode == "custom"
            else self.grammar_selector.get_suggested_grammar_topics()
        )


        # --- Semantic Domain ---
        if self.semantic_domain.is_semantic_domain_enabled():
            semantic_domain = self.semantic_domain.get_selected_semantic_domain()


        # Build context
        context_data = {
            "is_dialogue": is_dialogue,
            "difficulty": difficulty,
            "semantic_domain": semantic_domain,
            "grammar_topic": grammar_topic,            
        } 

        return context_data  
       
    