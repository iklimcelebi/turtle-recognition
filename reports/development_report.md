# 🐢 Kaplumbağa Tanıma Sistemi - Gelişim Raporu

## Proje 
Bu projede DEKAMER veri seti kullanılarak kaplumbağa türü ve birey tanıma sistemi geliştirilmiştir.

## 1. Veri Toplama Süreci
İlk aşamada iki tür için sınırlı sayıda görüntü topladım (40 adet). DOğal olark veri sayısı modelin çalışma perforamnsını etkiler.

## 2. İlk Model (CNN)
Basit bir CNN modeli ile tür sınıflandırması yaptırdım.
Başlangıçta doğruluk oranı düşüktü (%45).

## 3. Kimlik Tanıma Problemi
İlk yaklaşımda hash tabanlı kimlik sistemi kullanıldı ancak:
- Sistemde var olan fotoğrafları kulanmama rağmen sürekli "Yeni kaplumbağa" hatası aldım. Güncellemeler Hash yöntemini kullanana kadar "yeni kaplumbağa" veya "Hata(kimlik bulunamadı)" veriyordu.

## 4. İyileştirme: Embedding Tabanlı Sistem
Hash yöntemi yerine embedding + cosine similarity kullandık son olarak.
Bu sayede görsel benzerlik üzerinden kimlik tespiti yaptırmış oldum.

## 5. Multi-Agent Yapı
Sistem 3 ajan ile modüler hale getirilmiştir:
- Researcher Agent: veri analizi
- Trainer Agent: model eğitimi
- Predictor Agent: tahmin ve kimlik doğrulama
- ChatGPT: asistan olarak kullanıldı

## 6. Son Durum
Sistem:
- Tür tahmini yapabilmektedir
- Kimlik tahmini yapabilmektedir
- Görsel tabanlı çalışmaktadır

## 7. Sonuç
%60+ doğruluk seviyesine ulaşılmıştı ve sistem çalışır durumdadır.