from rag import answer

QUESTIONS = [
    "data analyst with SQL",
    "Python backend developer",
    "работа без знания шведского",
    "pastry chef",  # заведомо нет такой вакансии, проверка "No matching jobs found"
]

if __name__ == "__main__":
    for q in QUESTIONS:
        print("=" * 60)
        print("Q:", q)
        print(answer(q))