from backend.llm.llm_model import llm
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
import json

def generate_practices_topics(
    context_data: dict,
    exercise_type: str,
    practice_description: str,
    context_descriptions: list,
    examples: list,
    max_title_words: int = 10
):
    """
    Generate 4 exercise titles with descriptions based on context_data.
    Works for reading, listening, writing, conversation, vocab learning, grammar learning.
    """

    # --- آماده‌سازی context_data برای پرامپت ---
    formatted_context = {}
    for key, value in context_data.items():
        if isinstance(value, dict):
            formatted_context[key] = "; ".join(
                f"{k}: {v}" for k, v in value.items()
            )
        elif isinstance(value, list):
            formatted_context[key] = ", ".join(value)
        else:
            formatted_context[key] = str(value)

    # JSON string → امن برای پاس دادن
    formatted_context_str = json.dumps(
        formatted_context, indent=2, ensure_ascii=False
    )

    # --- قوانین تفسیر context_data ---
    context_rules = "\n".join(
        f"- {desc[key]}" for desc in context_descriptions for key in desc
    )

    # --- قالب مثال ---
    example_prompt_template = PromptTemplate(
        input_variables=["exerciseType", "context", "output"],
        template="Input:\nExercise Type: {exerciseType}\nContext:\n{context}\nOutput:\n{output}"
    )

    # --- پرامپت Few-Shot ---
    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt_template,
        prefix=f"""
    You are a language learning assistant.
    Generate {exercise_type} titles with a short description.

    Practice description:
    {practice_description}

    Instructions for interpreting context data:
    {context_rules}

    Each title must be <= {max_title_words} words.  
    The description should explain what the passage is about and how it relates to the context.       
    Output must be a structured JSON list of 4 items, each with 'title' and 'description'.  
    Titles must be distinct from each other, not just different phrasings of the same idea or exercise content.
    IMPORTANT:
    - The 4 items must cover clearly different scenarios, not just rephrased versions of the same idea.
    - Titles must be distinct in theme, not only in wording.
    - Avoid producing 4 variations of a same base idea for practicing.
    - Instead, generate diverse, creative contexts that combine semantic domains from different angles.

    BAD EXAMPLE (❌):
    All titles revolve around the same narrow idea:    
    "title": "Jazz on the Mountain", "description": "Discussing how jazz inspires climbers.",
    "title": "Climbing with Jazz", "description": "Exploring how jazz motivates climbers.",
    "title": "Jazz for Mountaineers", "description": "Talking about how climbers enjoy jazz.",
    "title": "The Rhythm of Climbing", "description": "Another way of saying jazz helps climbers climb."
    

    GOOD EXAMPLE (✅):
    Each title explores a unique scenario:    
    "title": "Summit Soundtrack", "description": "A mountaineer explains how listening to jazz during tough climbs helps regulate breathing and rhythm.",
    "title": "Jazz Festival at Base Camp", "description": "Campers discuss attending a jazz event while waiting for clear weather to climb.",
    "title": "Designing Climbing Gear with Jazz Aesthetics", "description": "A fashion designer merges jazz-inspired colors with mountaineering gear.",
    "title": "An Interview with a Jazz-loving Climber", "description": "A magazine interview that explores how one climber’s passion for jazz shapes his approach to the mountains."    
    """,
        suffix="Input:\nExercise Type: {{ exerciseType }}\nContext:\n{{ context }}\nOutput:",
        input_variables=["exerciseType", "context"],
        template_format="jinja2"   # 👈 این خط باعث میشه { } دیگه به str.format گیر نده
    )

    # --- جایگذاری context ---
    formatted_prompt = prompt.format(
        exerciseType=exercise_type,
        context=formatted_context_str
    )

    # --- فراخوانی مدل ---
    response = llm.invoke(formatted_prompt)
    return response.content