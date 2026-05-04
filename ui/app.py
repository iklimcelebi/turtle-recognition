import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from src.agents.predictor_agent import PredictorAgent


class TurtleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaplumbağa Tanıma Sistemi")
        self.root.geometry("500x500")

        self.predictor = PredictorAgent("models/classification_model.h5")

        self.label = tk.Label(root, text="Kaplumbağa Fotoğrafı Yükle", font=("Arial", 14))
        self.label.pack(pady=10)

        self.btn = tk.Button(root, text="Foto Seç", command=self.load_image)
        self.btn.pack(pady=10)



        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=20)

    def load_image(self):
        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        # resmi göster
        img = Image.open(file_path)
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)

        self.result_label.config(text="Analiz ediliyor...")
        self.root.update()

        self.image_label.configure(image=img)
        self.image_label.image = img

        # prediction
        result = self.predictor.run(file_path)

        text = f"Tür: {result['species']}\nKimlik: {result['identity']}"

        self.result_label.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TurtleApp(root)
    root.mainloop()