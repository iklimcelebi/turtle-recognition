import numpy as np

class Similarity:

    def cosine_similarity(self, a, b):
        a = np.array(a)
        b = np.array(b)

        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))