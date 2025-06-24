from .base import BaseRecommender
import os

class WebSeriesRecommender(BaseRecommender):
    def __init__(self, base_dir):
        artifact_dir = os.path.join(base_dir, 'artifacts', 'web_series')
        super().__init__(artifact_dir)
