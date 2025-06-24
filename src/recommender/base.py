import os
import pickle
import faiss
import numpy as np
from rapidfuzz import process
from config.global_paths import get_artifact_path  # Adjust import if needed

class BaseRecommender:
    def __init__(self, content_type):
        self.artifact_dir = get_artifact_path(content_type, '')
        self.df = pickle.load(open(os.path.join(self.artifact_dir, 'data.pkl'), 'rb'))
        self.model = pickle.load(open(os.path.join(self.artifact_dir, 'sbert_model.pkl'), 'rb'))
        self.index = faiss.read_index(os.path.join(self.artifact_dir, 'faiss_index.index'))

        self.titles = self.df['title'].fillna('').str.lower().tolist()
        self.column_map = self._resolve_columns()

    def _resolve_columns(self):
        return {
            'genre': 'genres' if 'genres' in self.df.columns else 'genre',
            'synopsis': 'synopsis' if 'synopsis' in self.df.columns else 'summary'
        }

    def recommend(self, title_query, top_k=20, score_threshold=70):
        title_query_lower = title_query.lower()

        exact_matches = self.df[self.df['title'].str.lower() == title_query_lower]
        if not exact_matches.empty:
            idx = exact_matches.index[0]
        else:
            best_match, score, idx = process.extractOne(title_query_lower, self.titles)
            if score < score_threshold:
                return f"❌ No close match found for '{title_query}' (best: '{best_match}', score: {score:.2f})"
            print(f"⚠️ Using closest match: '{best_match}' (score: {score:.2f})")

        query = self.df.loc[idx, 'tags']
        query_vec = self.model.encode([query], convert_to_numpy=True)
        _, I = self.index.search(query_vec, top_k + 1)

        return self.df.iloc[I[0][1:]][['title', self.column_map['genre'], self.column_map['synopsis']]]
