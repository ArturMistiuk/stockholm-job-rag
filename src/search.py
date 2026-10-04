import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from config import MODEL_EMB_NAME, JOBS_PATH, EMBEDDINGS_PATH

model = SentenceTransformer(MODEL_EMB_NAME)
embedings = np.load(EMBEDDINGS_PATH)

jobs_df = pd.read_json(JOBS_PATH)

assert len(jobs_df) == len(embedings), "jobs and embeddings are out of sync"


def search(query, k=5):
    query_embeding = model.encode(query, normalize_embeddings=True)
    scores = embedings @ query_embeding
    top_k_indices = np.argsort(scores)[::-1][:k]

    results = jobs_df.iloc[top_k_indices].copy()
    results["score"] = scores[top_k_indices]
    return results

if __name__ == "__main__":
    print(search("data analyst SQL")[["title", "score"]])