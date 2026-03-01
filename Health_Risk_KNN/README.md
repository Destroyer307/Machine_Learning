# Health Risk Classification with KNN

Bu proje, sağlık verilerini kullanarak bireylerin *high_risk_flag* değerini tahmin etmek için K-Nearest Neighbors (KNN) algoritmasını kullanır.

---

## 📊 Dataset

Kullanılan özellikler:

- bmi_score
- blood_pressure_variation
- activity_level_index
- high_risk_flag (Target)

Toplam veri sayısı: 1000  
Sınıf dağılımı:
- 0 → 502
- 1 → 498

Veri dengeli bir yapıdadır.

---

## ⚙️ Kullanılan Kütüphaneler

- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn

---

## 🔎 Veri Analizi

Yapılan işlemler:

- df.head() → İlk 10 satır incelendi
- df.info() → Veri tipleri kontrol edildi
- df.describe() → İstatistiksel özet çıkarıldı
- pairplot → Değişkenler arası ilişkiler görselleştirildi
- boxenplot → Aykırı değer analizi yapıldı

---

## 🧠 Modelleme Adımları

1. Özellik (X) ve hedef (y) ayrımı
2. Train-test split (test_size=0.25, random_state=42)
3. StandardScaler ile verilerin ölçeklenmesi
4. KNN modelinin oluşturulması

Model parametreleri:

- n_neighbors = 4
- weights = "uniform"
- algorithm = "auto"
- n_jobs = -1

---

## 📈 Model Performansı

Accuracy Score: *0.956*

Confusion Matrix:

[[130   2]
 [ 10 108]]

### Sonuç

Model %95.6 doğruluk oranı ile başarılı bir performans göstermektedir.  
Yanlış sınıflandırma oranı düşüktür ve veri dengeli olduğu için accuracy metriği güvenilirdir.
