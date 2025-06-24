import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ----------------------------
# Utility functions
# ----------------------------
def load_artifacts(content_type):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    ARTIFACT_DIR = os.path.join(BASE_DIR, 'artifacts', content_type)

    df = pickle.load(open(os.path.join(ARTIFACT_DIR, 'data.pkl'), 'rb'))
    model = pickle.load(open(os.path.join(ARTIFACT_DIR, 'sbert_model.pkl'), 'rb'))
    index = faiss.read_index(os.path.join(ARTIFACT_DIR, 'faiss_index.index'))

    return df, model, index


def recommend(title_query, content_type='anime', top_k=10):
    df, model, index = load_artifacts(content_type)

    # Fuzzy title match (case-insensitive, partial match)
    matches = df[df['title'].str.lower().str.contains(title_query.lower())]

    if matches.empty:
        return f"❌ Title containing '{title_query}' not found in {content_type} dataset."

    idx = matches.index[0]
    query = df.loc[idx, 'tags']
    query_vec = model.encode([query], convert_to_numpy=True)
    _, I = index.search(query_vec, top_k + 1)

    columns_to_show = ['title', 'genres' if 'genres' in df.columns else 'genre', 'synopsis' if 'synopsis' in df.columns else 'summary']
    return df.iloc[I[0][1:]][columns_to_show]


# ----------------------------
# Entry Point
# ----------------------------
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Content Recommendation System")
    parser.add_argument("--type", choices=["anime", "movie", "web_series"], required=True, help="Type of content to recommend from")
    parser.add_argument("--title", required=True, help="Title to search for")
    parser.add_argument("--top_k", type=int, default=10, help="Number of recommendations")

    args = parser.parse_args()

    print(f"\n🔍 Recommendations for '{args.title}' from {args.type} dataset:\n")
    result = recommend(args.title, args.type, args.top_k)
    print(result)
