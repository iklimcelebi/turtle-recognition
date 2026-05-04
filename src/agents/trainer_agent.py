from src.services.training_service import TrainingService
from src.models.cnn_model import create_model

class TrainerAgent:
    def __init__(self, data_path="data/processed"):
        self.data_path = data_path

    def train(self):
        print("🧠 Eğitim başlıyor...")

        service = TrainingService(self.data_path)
        train_gen, val_gen = service.get_data_generators()

        model = create_model(num_classes=train_gen.num_classes)

        history = model.fit(
            train_gen,
            validation_data=val_gen,
            epochs=5
        )

        model.save("models/classification_model.h5")

        print("✅ Model eğitildi ve kaydedildi")

        return model