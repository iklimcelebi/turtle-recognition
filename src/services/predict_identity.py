import os
import hashlib


class IdentityService:
    def __init__(self, database_path="data/database"):
        self.database_path = database_path
        self.database = self.load_database()

    def get_hash(self, file_path):
        with open(file_path, "rb") as f:
            file_bytes = f.read()
            return hashlib.md5(file_bytes).hexdigest()

    def load_database(self):
        db = {}

        for file in os.listdir(self.database_path):
            path = os.path.join(self.database_path, file)

            if not os.path.isfile(path):
                continue

            file_hash = self.get_hash(path)
            db[file_hash] = file

        print(f"✅ Database hash yüklendi: {len(db)} kayıt")

        return db

    def identify(self, image_path):
        query_hash = self.get_hash(image_path)

        if query_hash in self.database:
            return self.database[query_hash]
        else:
            return "Yeni kaplumbağa"
        


        