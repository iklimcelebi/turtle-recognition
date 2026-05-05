import os
import hashlib


class DatabaseService:
    def __init__(self):
        self.database = {}

    def get_hash(self, file_path):
        with open(file_path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    def build_database(self, database_path):
        self.database = {}

        for file in os.listdir(database_path):
            path = os.path.join(database_path, file)

            # sadece dosya al
            if not os.path.isfile(path):
                continue

            file_hash = self.get_hash(path)
            self.database[file_hash] = file

        print(f"✅ Database hazırlandı: {len(self.database)} kayıt")

    def find_match(self, image_path):
        query_hash = self.get_hash(image_path)

        if query_hash in self.database:
            return self.database[query_hash]
        else:
            return "Yeni kaplumbağa"