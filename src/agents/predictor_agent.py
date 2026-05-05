from src.services.prediction_service import PredictionService
from src.services.predict_identity import IdentityService


class PredictorAgent:
    def __init__(self, model_path):
        self.predictor = PredictionService(model_path)

        # SADECE HASH SİSTEMİ
        self.identity = IdentityService("data/database")

    def run(self, image_path):
        print("🔎 Tahmin yapılıyor...")

        # Tür tahmini
        species = self.predictor.predict(image_path)

        # Kimlik (HASH)
        try:
            identity = self.identity.identify(image_path)
        except Exception as e:
            print("❌ Kimlik hatası:", e)
            identity = "Yeni kaplumbağa"

        return {
            "species": species,
            "identity": identity
        }
    

    