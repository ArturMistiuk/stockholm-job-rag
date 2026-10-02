import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer


jobs_df = pd.read_json("data/linkedin_jobs_500.json")
jobs_df["text"] = jobs_df["title"].fillna("") + " " + jobs_df["description"].fillna("")
sentences = jobs_df["text"].to_list()
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
embedings = model.encode(sentences, normalize_embeddings=True, show_progress_bar=True)
np.save("data/embeddings.npy", embedings)
print(embedings.shape)
print(embedings)
print("Size of df is same as embedings: ", len(jobs_df) == len(embedings))