# 🐢 Kaplumbağa Tanıma Sistemi - Gelişim Raporu

## Proje 
Bu projede DEKAMER veri seti kullanılarak kaplumbağa türü ve kaplumbağa tanıma sistemi geliştirilmiştir.
Sistem iki temel problemi çözmektedir:
- Tür sınıflandırma
- Birey kimlik doğrulama 

## 1. Veri Toplama Süreci
İlk aşamada iki tür için sınırlı sayıda görüntü topladım (40 adet). DOğal olark veri sayısı modelin çalışma performansını etkiler.

## 2. İlk Model (CNN)
Basit bir CNN modeli ile tür sınıflandırması yaptırdım.
Başlangıçta doğruluk oranı veri azlığı ve model basitliği nedeniyle düşüktü (%45).

## 3. Kimlik Tanıma Problemi
İlk yaklaşımda hash tabanlı kimlik sistemi kullanıldı ancak:
- Sistemde var olan fotoğrafları kulanmama rağmen sürekli "Yeni kaplumbağa" hatası aldım. Güncellemeler Hash yöntemini kullanana kadar "yeni kaplumbağa" veya "Hata(kimlik bulunamadı)" veriyordu. Sorun; resim dosyalarını türkçe karakter kullanarak kaydetmemden kaynaklanıyormuş

## 4. İyileştirme, Embedding Tabanlı Sistem
fix_filenames.py isimli dosya ile türkçe karakter problemini çözdüm
Hash yöntemi yerine embedding + cosine similarity kullandık son olarak.
Bu sayede görsel benzerlik üzerinden kimlik tespiti yaptırmış oldum.

## 5. Multi-Agent Yapı
Sistem 3 ajan ile modüler hale getirilmiştir:
- Researcher Agent: veri analizi
- Trainer Agent: model eğitimi
- Predictor Agent: tahmin ve kimlik doğrulama
- Ek olarak geliştirme sürecinde:
 ChatGPT ve Gemini araçları destekleyici sistemler olarak kullandım

## 6. Son Durum
Sistem:
- Tür tahmini yapabilmektedir
- Kimlik tahmini yapabilmektedir
- Görsel tabanlı çalışmaktadır

## 7. Sonuç
Küçük veri seti ile yaptığım eğitimde %65+ doğruluk seviyesine ulaşıldı ve sistem çalışır durumdadır.
- Tür tahmini yapabilmektedir
- Kimlik doğrulama yapabilmektedir
- Görsel tabanlı çalışmaktadır

## 8. Clean Code ve SOLID 

Proje geliştirilirken Clean Code ve SOLID prensiplerine dikkat ettim.

### Single Responsibility
Her sınıf tek bir görevi yerine getirecek şekilde tasarlanmıştır:
- ImageProcessor → sadece görüntü işleme
- TrainingService → sadece model eğitimi
- PredictionService → sadece tahmin
- DatabaseService → veri yönetimi

### Open/Closed 
Sistem yeni model veya algoritmalar eklenmesine açıktır:
- src/models altında yeni model eklenebilir
- mevcut kod değiştirilmeden genişletilebilir

### Liskov Substitution 
Alt bileşenler üst bileşenlerin yerine kullanılabilir yapıdadır.

### Interface Segregation 
Sınıflar gereksiz fonksiyonlar içermeyecek şekilde ayrılmıştır.

### Dependency Injection 
Bileşenler doğrudan birbirine bağlı değildir:
- PredictorAgent → servisleri dışarıdan kullanır
- Model yolu parametre olarak verilir

---

## Clean Code Yaklaşımı
- Kod modüler hale getirilmiştir
- Tekrar eden kodlar azaltılmıştır  
- Klasör yapısı mantıklı şekilde ayrılmıştır
