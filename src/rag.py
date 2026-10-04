import anthropic
from search import search
from prompt import build_prompt, SYSTEM_PROMPT
from config import ANTHROPIC_API_KEY, MODEL_ANTHROPIC


client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def answer(question):
    result = search(question)
    prompt = build_prompt(question=question, result=result)
    response = client.messages.create(
        model=MODEL_ANTHROPIC,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    text = "".join(block.text for block in response.content if block.type == "text")

    return text