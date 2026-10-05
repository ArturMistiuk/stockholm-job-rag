import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from config import MODEL_EMB_NAME, JOBS_PATH, EMBEDDINGS_PATH


if __name__ == "__main__":
    model = SentenceTransformer(MODEL_EMB_NAME)

    jobs_df = pd.read_json(JOBS_PATH)
    jobs_df["text"] = jobs_df["title"].fillna("") + " " + jobs_df["description"].fillna("")

    sentences = jobs_df["text"].to_list()

    embeddings = model.encode(sentences, normalize_embeddings=True, show_progress_bar=True)

    assert len(jobs_df) == len(embeddings), "jobs and embeddings are out of sync"

    np.save(EMBEDDINGS_PATH, embeddings)
