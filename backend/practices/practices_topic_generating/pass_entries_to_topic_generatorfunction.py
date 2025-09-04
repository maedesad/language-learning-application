from typing import Any, Dict, List
from backend.practices.practices_topic_generating.practices_topic_generator_function import generate_practices_topics
from backend.practices.practices_topic_generating.topic_output_example import topic_output_examples

def pass_entries_to_topic_generator(
    context_data: Dict[str, Any],
    practice_type: str,
    practice_description: str,
    context_descriptions: List[Dict[str, str]],
    output_example: Dict[str, Any] = topic_output_examples,
    max_title_words: int = 10,
):
    """
    Build a strict lookup key according to your rules and call generate_practices_topics.
    - practice_type: e.g. "reading_practice" (must match keys in output_example)
    - The function checks ONLY for the Python None in context_data for
      'semantic_domain' and 'vocab_categories'.
    - If the constructed key is not present in output_example -> KeyError.
    """

    semantic_val = context_data.get("semantic_domain")
    vocab_val = context_data.get("vocab_categories")
    is_dialogue = bool(context_data.get("is_dialogue", False))

    key = None

    # ---------- Reading / Listening ----------
    if practice_type in ["reading_practice", "listening_practice"]:
        if semantic_val is None and vocab_val is not None:
            sec2 = "vocab_categories"
        elif vocab_val is None and semantic_val is not None:
            sec2 = "semantic_domain"
        elif semantic_val is not None and vocab_val is not None:
            sec2 = "semantic_domain"  # default priority
        else:
            raise ValueError(
                "For reading/listening practice both 'semantic_domain' and 'vocab_categories' are None. "
                "Provide at least one of them."
            )

        sec3 = "dialogue" if is_dialogue else "monologue"
        key = f"{practice_type}_{sec2}_{sec3}"

    # ---------- Writing / Conversation ----------
    elif practice_type in ["writing_practice", "conversation_practice"]:
        if semantic_val is None and vocab_val is not None:
            sec2 = "vocab_categories"
        elif vocab_val is None and semantic_val is not None:
            sec2 = "semantic_domain"
        elif semantic_val is not None and vocab_val is not None:
            sec2 = "semantic_domain"  # default priority
        else:
            raise ValueError(
                "For writing/conversation practice both 'semantic_domain' and 'vocab_categories' are None. "
                "Provide at least one of them."
            )

        key = f"{practice_type}_{sec2}"

    # ---------- Grammar Learning ----------
    elif practice_type == "grammar_learning":
        sec2 = "dialogue" if is_dialogue else "monologue"
        key = f"{practice_type}_{sec2}"

    # ---------- Vocab Learning ----------
    elif practice_type == "vocab_learning":
        key = practice_type

    else:
        raise ValueError(f"Unsupported practice_type: '{practice_type}'")

    # strict lookup
    if key not in output_example:
        raise KeyError(f"Example key '{key}' not found in output_example. No fallback is attempted.")

    examples_for_llm = output_example[key]

    # call generator (assumes generate_practices_topics is defined)
    topics = generate_practices_topics(
        context_data=context_data,
        exercise_type=practice_type,
        practice_description=practice_description,
        context_descriptions=context_descriptions,
        examples=examples_for_llm,
        max_title_words=max_title_words,
    )

    return topics
