# Stockholm Jobs RAG

Ask questions about Stockholm job ads in plain language and get answers based on real postings, with the ad IDs they came from.

Example: *"Which data analyst jobs in Stockholm ask for dbt and don't require Swedish?"*

## Why this project

I already collect job ads from Platsbanken in my [Stockholm Job Market Analyzer](LINK) pipeline. This project adds a RAG layer on top of that data.

The main focus is not the chatbot itself but checking how well it works: does retrieval find the right ads, and does the answer stick to what the ads actually say. Ads are a mix of Swedish and English, which makes retrieval harder and more interesting.

## Data

- Source: Platsbanken (JobTech API), collected by the Job Market Analyzer pipeline
- Snapshot of N job ads exported from SQLite to `data/jobs.json`
- Fields: id, headline, employer, city, published date, description
- Languages: Swedish and English, often mixed

## How it works

```
question -> embed -> find top-k similar ads -> build prompt with those ads -> LLM -> answer with ad IDs
```

## Roadmap

- [x] Export and clean job ads from SQLite
- [ ] Embeddings and semantic search (top-k)
- [ ] Prompt with retrieved ads, answers cite ad IDs
- [ ] First test: 10 questions, results table
- [ ] Hybrid search (BM25 + semantic) and metadata filters (city, date)
- [ ] Test set of 50+ questions, retrieval metrics (recall@k, MRR)
- [ ] Chunking and reranking experiments
- [ ] Agent that chooses between searching ads and running SQL stats
- [ ] Logging, tracing and deployment

## Results

Results and comparisons will be added here as the project grows.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Author

Artur - [arturmistiuk.github.io](https://arturmistiuk.github.io)