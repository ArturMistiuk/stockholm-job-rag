SYSTEM_PROMPT = """You are a job search assistant for Stockholm.
Answer the question using ONLY the job ads provided.
Mention the ID of every job you use, like [ID: 123].
If none of the ads fit, say "No matching jobs found."
"""


def build_prompt(question, result):
    jobs_text = ""
    for idx, row in result.iterrows():
        jobs_text += f"[ID: {idx}]\n"
        jobs_text += f"[title: {row['title']}]\n"
        jobs_text += f"[description: {row["description"][:1000]}]\n\n"

    prompt = f"""JOB ADS:
{jobs_text}
QUESTION: {question}"""

    return prompt