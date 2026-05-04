from src.services.training_service import TrainingService
from src.models.cnn_model import create_model

service = TrainingService("data/processed")
train_gen, val_gen = service.get_data_generators()

model = create_model(num_classes=train_gen.num_classes)

model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=5
)

model.save("models/classification_model.h5")

print("Model eğitildi ve kaydedildi ✅")