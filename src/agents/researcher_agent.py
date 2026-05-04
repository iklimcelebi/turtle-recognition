import os

class ResearcherAgent:
    def __init__(self, raw_path="data/raw"):
        self.raw_path = raw_path

    def analyze_dataset(self):
        print("🔍 Veri seti analiz ediliyor...")

        summary = {}

        for class_name in os.listdir(self.raw_path):
            class_path = os.path.join(self.raw_path, class_name)

            if os.path.isdir(class_path):
                count = len(os.listdir(class_path))
                summary[class_name] = count

        print("📊 Dataset özeti:", summary)
        return summary