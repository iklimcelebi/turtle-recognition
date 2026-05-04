import os
import cv2



def load_image(path):
    """Görüntüyü güvenli şekilde yükler"""
    path = fix_path(path)
    image = cv2.imread(path)
    return image

def resize_image(image, size=(224, 224)):
    """Görüntüyü yeniden boyutlandırır"""
    return cv2.resize(image, size)

def get_filename(path):
    """Dosya adını uzantısız alır"""
    return os.path.splitext(os.path.basename(path))[0]