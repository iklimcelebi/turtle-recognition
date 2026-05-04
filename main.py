from src.agents.researcher_agent import ResearcherAgent
from src.agents.trainer_agent import TrainerAgent
from src.agents.predictor_agent import PredictorAgent

researcher = ResearcherAgent()
researcher.analyze_dataset()


trainer = TrainerAgent()
trainer.train()

predictor = PredictorAgent("models/classification_model.h5")

result = predictor.run("test_kaplumbaga.jpg")

print("\n📌 SONUÇ")
print("Tür:", result["species"])
print("Kimlik:", result["identity"])
