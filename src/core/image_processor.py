import os
import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, size=(224, 224)):
        self.size = size

    #TÜRKÇE KARAKTER  OKUMA
    def load_image(self, path):
        try:
            with open(path, "rb") as f:
                file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
                image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                return image
        except Exception as e:
            print(f"HATA: Görsel okunamadı → {path}")
            return None

    def resize(self, image):
        return cv2.resize(image, self.size)

    def normalize(self, image):
        return image / 255.0

    def process(self, path):
        image = self.load_image(path)

        if image is None:
            return None

        image = self.resize(image)
        image = self.normalize(image)
        return image

    # TÜM GÖRSELLERİ İŞLE
    def process_all_images(self, input_dir, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for class_name in os.listdir(input_dir):
            input_class_path = os.path.join(input_dir, class_name)
            output_class_path = os.path.join(output_dir, class_name)

            if not os.path.exists(output_class_path):
                os.makedirs(output_class_path)

            for file in os.listdir(input_class_path):
                input_path = os.path.join(input_class_path, file)
                output_path = os.path.join(output_class_path, file)

                image = self.load_image(input_path)

                if image is None:
                    continue

                image = self.resize(image)

                #GÜVENLİ KAYDETME (encoding sorunu yok)
                success, encoded_img = cv2.imencode(".jpg", image)
                if success:
                    with open(output_path, "wb") as f:
                        encoded_img.tofile(f)

        print("Tüm görseller işlendi ✅")