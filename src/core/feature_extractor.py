import numpy as np
from src.models.embedding_model import create_embedding_model
from src.core.image_processor import ImageProcessor

class FeatureExtractor:
    def __init__(self):
        self.model = create_embedding_model()
        self.processor = ImageProcessor()

    def get_embedding(self, image_path):
        image = self.processor.process(image_path)

        if image is None:
            return None

        image = np.expand_dims(image, axis=0)

        embedding = self.model.predict(image)[0]

        return embedding