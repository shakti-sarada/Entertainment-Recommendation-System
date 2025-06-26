from .base import BaseRecommender
import os

class AnimeRecommender(BaseRecommender):
    def __init__(self, base_dir):
        artifact_dir = os.path.join(base_dir, 'artifacts', 'anime')
        super().__init__(artifact_dir)
