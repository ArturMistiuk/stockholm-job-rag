# Stockholm Jobs RAG

Ask questions about Stockholm job ads in plain language and get answers based on real postings, with the ad IDs they came from.

Example: *"Which data analyst jobs in Stockholm ask for dbt and don't require Swedish?"*

**Status:** semantic search over job ads works. The LLM answer step is next.

## Why this project

I already collect job ads in my [Stockholm Job Market Analyzer](LINK) pipeline. This project adds a RAG layer on top of that data.

The main focus is not the chatbot itself but checking how well it works: does retrieval find the right ads, and does the answer stick to what the ads actually say. Ads are a mix of Swedish and English, which makes retrieval harder and more interesting.

## Data

- Source: LinkedIn job ads for Stockholm, collected by the Job Market Analyzer pipeline
- Snapshot: 500 ads published 2026-06-27 to 2026-09-28, stored in `data/linkedin_jobs_500.json`
- Roles: data analyst, data scientist, machine learning, data engineer, AI engineer, business and product analyst
- Fields: `id`, `title`, `employer`, `occupation`, `municipality`, `published_date`, `work_mode`, `language`, `source_url`, `description`, `skills`
- Languages: 364 English and 136 Swedish ads, often mixed

## How it works

```
question -> embed -> find top-k similar ads -> build prompt with those ads -> LLM -> answer with ad IDs
```

Implemented so far:

- `src/embed.py` embeds `title + description` for every ad with the multilingual model `paraphrase-multilingual-MiniLM-L12-v2` and saves normalized vectors to `data/embeddings.npy`
- `src/search.py` embeds the query and returns the top-k ads by cosine similarity
- `notebooks/search_check.ipynb` runs manual checks of search results on sample queries

## Roadmap

- [x] Export and clean job ads
- [x] Embeddings and semantic search (top-k)
- [ ] Prompt with retrieved ads, answers cite ad IDs
- [ ] First test: 10 questions, results table
- [ ] Hybrid search (BM25 + semantic) and metadata filters (work mode, language, date)
- [ ] Test set of 50+ questions, retrieval metrics (recall@k, MRR)
- [ ] Chunking and reranking experiments
- [ ] Agent that chooses between searching ads and running SQL stats
- [ ] Logging, tracing and deployment

## Results

Results and comparisons will be added here as the project grows.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install sentence-transformers pandas numpy
```

## Usage

```bash
python src/embed.py     # build data/embeddings.npy (re-run after the data changes)
python src/search.py    # run a sample query
```

From Python, with `src` on the path:

```python
from search import search
search("data analyst SQL Python", k=5)[["title", "employer", "score"]]
```

## Author

Artur - [arturmistiuk.github.io](https://arturmistiuk.github.io)
