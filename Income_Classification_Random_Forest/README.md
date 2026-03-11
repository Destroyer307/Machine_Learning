Income Classification - Random Forest

Bu projede bir kişinin yıllık gelirinin 50K'dan fazla mı yoksa az mı olduğunu tahmin eden bir makine öğrenmesi modeli geliştirdim. Bunun için Random Forest Classifier kullandım ve modelin en iyi parametrelerini bulmak için GridSearchCV uyguladım.

Dataset

Kullanılan veri seti: income_evaluation.csv

Dataset içinde bulunan bazı özellikler:

- age
- workclass
- finalweight
- education
- education_num
- marital_status
- occupation
- relationship
- race
- sex
- capital_gain
- capital_loss
- hours_per_week
- native_country
- income (target)

Amaç:
"income" değişkenini tahmin etmek.
(">50K" veya "<=50K")

Yapılan İşlemler

Projede veri üzerinde şu adımlar uygulandı:

1. Veri Yükleme

Dataset pandas kullanılarak içeri alındı.

2. Kolon Düzenleme

Dataset içindeki bazı kolon isimleri daha okunabilir olacak şekilde değiştirildi.

3. Eksik Veriler

Eksik değerler kontrol edildi ve kategorik kolonlarda mode (en sık görülen değer) ile dolduruldu.

4. Encoding

- Target değişkeni için LabelEncoder
- Kategorik değişkenler için OneHotEncoder

kullanıldı.

5. Train Test Split

Veri:

- %75 eğitim
- %25 test

olacak şekilde ayrıldı.

6. Model

Kullanılan model:

RandomForestClassifier

7. Hyperparameter Tuning

Model için GridSearchCV ile şu parametreler denendi:

max_depth = [5, 8, 20]
max_features = ["sqrt", "log2", 5]
n_estimators = [10, 100, 1000]

En İyi Parametreler

GridSearch sonucunda bulunan en iyi parametreler:

max_depth = 20
max_features = "sqrt"
n_estimators = 1000

Model Performansı

Test verisi üzerinde elde edilen accuracy:

Accuracy = 0.8673

Yani model yaklaşık %86 doğruluk ile tahmin yapabiliyor.

Kullanılan Kütüphaneler

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Amaç

Bu proje temel olarak şu konuları pratik etmek için yapılmıştır:

- veri ön işleme
- kategorik veri encoding
- Random Forest kullanımı
- GridSearch ile hyperparameter tuning
