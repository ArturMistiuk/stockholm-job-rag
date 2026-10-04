import anthropic
from search import search
from prompt import build_prompt
from config import ANTHROPIC_API_KEY


client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def answer(question):
    result = search(question)
    prompt = build_prompt(question=question, result=result)
    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=2000,
        system="You are job searching helper in Stockholm",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    