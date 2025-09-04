# --- descriptions for context fields ---
is_dialogue = {
    "is_dialogue": "If True → practice is like dialogue between two people. If False → practice is monologue-style (story, report, article)."
}
difficulty = {
    "difficulty": "Defines the complexity of language from range of 1 to 10. Higher difficulty = more detailed, academic, or specialized. Lower = simpler, everyday topics."
}
semantic_domain = {
    "semantic_domain": """Specifies the thematic field of the text (e.g., travel, science, daily life).
The exercises should not only address the domain in a general way, but also explore its different aspects. 
For example, if the semantic domain is 'sports', the exercises do not need to focus only on sports in general, 
but can address various dimensions such as different sports (tennis, football, swimming, golf), 
the economic impact of sports, sports clothing, sports as a global entertainment activity, 
watching sports games or even sports video games, and so on. 
'Sports' here is just an example — the model should consider multiple perspectives depending on the domain it receives."""
}
grammar_topics = {
    "grammar_topics": "The text should allow natural practice of the listed grammar structures."
}
vocab_categories = {
    "vocab_categories": """The text should incorporate themes that cover these vocabulary categories. 
If multiple diverse vocabulary categories are selected for one exercise, 
the model should make an effort to subtly and naturally connect seemingly unrelated topics, 
and generate a professional, creative title instead of simply placing unrelated categories side by side. 
For example, if the chosen categories are 'economics' and 'literature', 
the wrong approach would be: 'A discussion about economics and literature'. 
A more creative and connected approach would be: 
'A look at literary works that well reflect the living conditions of the people of their time'. 
This is just an example — the model should always find its own creative way 
to weave the selected categories together into a coherent and engaging theme."""
}

existing_vocab_categories = {
    "existing_vocab_categories": """Represents the vocabulary categories that have already been generated for the learner. 
When the model generates new vocabulary categories, it must ensure that they are clearly distinct 
from these existing ones and that the new words do not overlap with the words in the previously generated categories."""
}


passive_context_data_descriptions=[
        is_dialogue,
        difficulty,
        semantic_domain,
        grammar_topics,
        vocab_categories
]


active_context_data_descriptions=[        
        difficulty,
        semantic_domain,
        grammar_topics,
        vocab_categories
]

vocab_learning_context_data_descriptions=[        
        difficulty,
        semantic_domain,        
        existing_vocab_categories
]

grammar_learning_context_data_descriptions=[    
        is_dialogue,    
        difficulty,
        semantic_domain,
        grammar_topics,        
]