from backend.user.user_class import User
from backend.practices.practices_classes.practice_topic_generating_context.practice_topic_generator import PracticeTopicGenerator
from backend.practices.practices_classes.practice_global_settings.individual_practice_classes.vocab_learning_global_settings import VocabLearningGlobalSettings
from backend.practices.practices_classes.practice_entry_settings.semantic_domain import SemanticDomain
from backend.practices.practices_classes.practice_entry_settings.dialogue_setting import DialogueSetting

class VocabLearningTopicGenerator(PracticeTopicGenerator, VocabLearningGlobalSettings, DialogueSetting):
    def __init__(self, user: User):
        # ------------------- Init parent classes -------------------
        PracticeTopicGenerator.__init__(self, user)
        VocabLearningGlobalSettings.__init__(self)
        DialogueSetting.__init__(self)

      # ------------------- Save user -------------------
        self.user = user   

        # ------------------- Initialize composition objects -------------------
        self.semantic_domain = SemanticDomain(user)
        

        # ------------------- Override global settings with user values -------------------
        self.set_user_settings_from_user(user)

        
    # ------------------- Helper -------------------
    def set_user_settings_from_user(self, user: User):
        """Override global settings with user-specific values."""
        self.set_difficult_words(user.vocabulary_settings.get_difficult_words())
        self.set_productive_practice(user.vocabulary_settings.get_productive_practice())
        self.set_paragraphs_number(user.vocabulary_settings.get_paragraphs_number())
        self.set_dialogues_number(user.vocabulary_settings.get_dialogues_number())
        self.set_questions_per_word(user.vocabulary_settings.get_questions_per_word())

        
        # Difficulty level specific for reading
        self.set_difficulty_level(user.vocabulary_settings.get_difficulty_level())


    # ------------------- Topic Generator -------------------
    def generate_topics(self, mode: str = "suggested") -> dict:        
        difficulty = self.get_difficulty_level()

        semantic_domain = None       
               

        # --- Semantic Domain ---
        if self.semantic_domain.is_semantic_domain_enabled():
            semantic_domain = self.semantic_domain.get_selected_semantic_domain()
       

        # Build context
        context_data = {            
            "difficulty": difficulty,
            "semantic_domain": semantic_domain,  
            "existing_vocab_categories": self.user.get_vocabulary_categories()        
        } 

        return context_data  
       
    