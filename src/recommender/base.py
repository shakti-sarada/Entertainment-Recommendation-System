import os
import pickle
import faiss
import numpy as np
from rapidfuzz import process
from config.global_paths import get_artifact_path  # Adjust import if needed
from src.utils.logger import logger  # Add logger

class BaseRecommender:
    def __init__(self, content_type):
        self.content_type = content_type
        try:
            self.artifact_dir = get_artifact_path(content_type, '')
            self.df = pickle.load(open(os.path.join(self.artifact_dir, 'data.pkl'), 'rb'))
            self.model = pickle.load(open(os.path.join(self.artifact_dir, 'sbert_model.pkl'), 'rb'))
            self.index = faiss.read_index(os.path.join(self.artifact_dir, 'faiss_index.index'))
            self.titles = self.df['title'].fillna('').str.lower().tolist()
            self.column_map = self._resolve_columns()
            logger.info(f"✅ Artifacts loaded successfully for: {content_type}")
        except Exception as e:
            logger.error(f"❌ Failed to load artifacts for {content_type}: {e}")
            raise

    def _resolve_columns(self):
        return {
            'genre': 'genres' if 'genres' in self.df.columns else 'genre',
            'synopsis': 'synopsis' if 'synopsis' in self.df.columns else 'summary'
        }

    def recommend(self, title_query, top_k=20, score_threshold=70):
        logger.info(f"🔍 Recommendation requested for: '{title_query}' in {self.content_type}")
        try:
            title_query_lower = title_query.lower()

            exact_matches = self.df[self.df['title'].str.lower() == title_query_lower]
            if not exact_matches.empty:
                idx = exact_matches.index[0]
                logger.info(f"✅ Exact match found for '{title_query}'")
            else:
                best_match, score, idx = process.extractOne(title_query_lower, self.titles)
                if score < score_threshold:
                    msg = f"❌ No close match found for '{title_query}' (best: '{best_match}', score: {score:.2f})"
                    logger.warning(msg)
                    return msg
                logger.warning(f"⚠️ Using closest match: '{best_match}' (score: {score:.2f})")

            query = self.df.loc[idx, 'tags']
            query_vec = self.model.encode([query], convert_to_numpy=True)
            _, I = self.index.search(query_vec, top_k + 1)

            recommendations = self.df.iloc[I[0][1:]][['title', self.column_map['genre'], self.column_map['synopsis']]]
            logger.info(f"✅ Recommendations generated for '{title_query}'")

            return recommendations

        except Exception as e:
            logger.error(f"❌ Error during recommendation for '{title_query}': {e}")
            return "❌ An error occurred during recommendation. Please try again."
