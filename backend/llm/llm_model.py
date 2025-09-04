from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",   
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    #temperature=0.9,   # پیش‌فرض 0.7 هست
    #top_p=0.95
)

