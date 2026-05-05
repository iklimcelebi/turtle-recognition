# 🐢 Kaplumbağa Tanıma Sistemi

## 📌 Proje Hakkında
Bu proje, DEKAMER veri seti kullanılarak geliştirilmiş bir yapay zeka sistemidir. Sistem iki temel görevi yerine getirir:

- Kaplumbağa türünü tahmin etmek (sınıflandırma)
- Kaplumbağa bireyini tanımak (kimlik doğrulama)

Görüntü işleme ve derin öğrenme teknikleri kullanılarak geliştirilmiştir.

---

## Sistem Özeti
Sistem birden fazla yapay zeka bileşeni ile çalışmaktadır:

- CNN tabanlı tür sınıflandırma modeli
- Embedding + cosine similarity tabanlı kimlik doğrulama sistemi
- Multi-agent mimari yapı

---

## Dosya Dizini

Proje modüler bir yapıdadır:

TURTLE-RECOGNITION/
├── config/
│   └── settings.py
├── data/
│   ├── database/
│   ├── processed/
│   │   ├── caretta_caretta/
│   │   └── chelonia_mydas/
│   └── raw/
│       ├── caretta_caretta/
│       └── chelonia_mydas/
├── models/
│   ├── classification_model.h5
│   └── embedding_model.h5
├── reports/
│   └── development_report.md
├── src/
│   ├── agents/
│   │   ├── predictor_agent.py
│   │   ├── researcher_agent.py
│   │   └── trainer_agent.py
│   ├── core/
│   │   ├── feature_extractor.py
│   │   ├── image_processor.py
│   │   └── similarity.py
│   ├── models/
│   │   ├── cnn_model.py
│   │   └── embedding_model.py
│   ├── services/
│   │   ├── database_service.py
│   │   ├── predict_identity.py
│   │   ├── prediction_service.py
│   │   └── training_service.py
│   └── utils/
│       ├── helpers.py
│       └── logger.py
├── ui/
│   └── app.py
├── fix_filenames.py
├── main.py
├── README.md
├── requirements.txt
├── test_kaplumbaga.jpg
└── train.py

---

## Ajanlar

Sistem 3 ana ajan ile çalışır:

### Researcher Agent
- Veri setini analiz eder
- Görsel dağılımını inceler

### Trainer Agent
- CNN modelini eğitir
- Tür sınıflandırma modelini oluşturur

### Predictor Agent
- Kullanıcıdan gelen görüntüyü işler
- Tür tahmini yapar
- Kimlik doğrulama gerçekleştirir

---

## Çalışma Mantığı

1. Kullanıcı bir kaplumbağa görseli yükler
2. Görsel ön işleme sürecinden geçer
3. CNN modeli ile tür tahmini yapılır
4. Görsel embedding vektörüne çevrilir
5. Database içindeki görseller ile karşılaştırılır
6. En yakın eşleşme bulunursa kimlik döndürülür
7. Eşleşme yoksa "Yeni Kaplumbağa" olarak sınıflandırılır

---

## Veri Seti
- DEKAMER veri seti kullanılmıştır
- İki tür üzerinde çalışılmıştır:
  - Caretta caretta
  - Chelonia mydas
- Her tür için sınırlı sayıda görüntü kullanılmıştır

---

## Clean Code ve SOLID Prensipleri

Bu proje, yazılım mühendisliği prensiplerine uygun olarak geliştirilmiştir.

- Modüler yapı kullanılmıştır (agent, service, core ayrımı)
- Her sınıf tek bir sorumluluğa sahiptir (Single Responsibility)
- Sistem genişletilebilir yapıdadır (Open/Closed)
- Bileşenler birbirine bağımlı değildir (Dependency Injection yaklaşımı)

Bu sayede proje:
- Okunabilir
- Sürdürülebilir
- Genişletilebilir
hale getirilmiştir.

---

## Kurulum

Gerekli kütüphaneleri yüklemek için:

```bash
pip install -r requirements.txt

Çalıştırma
    Model eğitimi:
        python train.py
    Ana sistem:
            python main.py
    Arayüz:
        python ui/app.py

Model Performansı
    Tür sınıflandırma doğruluğu: ~%60+
    Kimlik doğrulama: embedding tabanlı benzerlik sistemi


Kullanılan Teknolojiler:
    Python
    TensorFlow / Keras
    OpenCV
    NumPy
    Scikit-learn
    Tkinter (UI)


Geliştirme Süreci

    Proje geliştirilirken şu adımlar izlenmiştir:

        Veri toplama ve sınıflandırma
        Basit CNN modeli ile başlangıç
        Hash tabanlı kimlik sistemi denemesi (başarısız)
        Embedding + cosine similarity sistemine geçiş
        Multi-agent mimari tasarımı
        Sistem optimizasyonu ve modüler yapı
    
    Sonuç

        Bu proje ile:

            Görüntü tabanlı tür sınıflandırma yapılabilmiştir
            Kaplumbağa birey tanıma sistemi geliştirilmiştir
            Multi-agent yapay zeka mimarisi uygulanmıştır
            Modüler ve genişletilebilir bir sistem oluşturulmuştur


Not: Bu proje eğitim amaçlı geliştirilmiştir ve gerçek dünya uygulamalarına genişletilebilir bir altyapı sunmaktadır.