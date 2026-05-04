import numpy as np
from tensorflow.keras.models import load_model
from src.core.image_processor import ImageProcessor

class PredictionService:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.processor = ImageProcessor()

        # class isimlerini manuel yaz (çok önemli)
        self.class_names = ["caretta_caretta", "chelonia_mydas"]

    def predict(self, image_path):
        image = self.processor.process(image_path)

        if image is None:
            return "Görsel okunamadı"

        image = np.expand_dims(image, axis=0)

        predictions = self.model.predict(image)
        class_index = np.argmax(predictions)

        return self.class_names[class_index]
    
    