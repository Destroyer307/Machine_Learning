# Indian Liver Patient Dataset (ILPD) - Logistic Regression

Bu proje, Indian Liver Patient Dataset (ILPD) kullanılarak karaciğer hastalığı sınıflandırması yapmaktadır.

##  Kullanılan Teknolojiler
- Python
- Pandas, NumPy
- Seaborn, Matplotlib
- Scikit-learn

##  Veri Ön İşleme
- Eksik veriler temizlendi (dropna)
- gender değişkeni LabelEncoder ile sayısallaştırıldı
- Aykırı değer filtrelemesi yapıldı (ag_ratio, albumin)
- Özellikler ve hedef değişken ayrıldı (X, y)
- Veriler train_test_split ile %80-%20 bölündü
- StandardScaler ile ölçeklendirme uygulandı

##  Model
- Logistic Regression
- GridSearchCV ile hiperparametre optimizasyonu
  - penalty: l1, l2, elasticnet
  - C değerleri farklı kombinasyonlar
  - 5-fold cross validation

##  Sonuç
Test doğruluk oranı:


Accuracy: 0.7017


##  Çalıştırma
1. Gerekli kütüphaneleri yükleyin:
   
   pip install pandas numpy seaborn matplotlib scikit-learn
   
2. Notebook dosyasını çalıştırın.

Karaciğer hastalığı sınıflandırması için temel bir makine öğrenmesi uygulamasıdır.
