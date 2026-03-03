# Seattle Weather Classification

Bu proje, Seattle hava durumu verisini kullanarak hava durumunu (weather) tahmin etmek için Logistic Regression modeli uygular.

##  Veri Seti

Kullanılan dosya: seattle-weather.csv

Kolonlar:
- date
- precipitation
- temp_max
- temp_min
- wind
- weather (hedef değişken)

##  Kullanılan Kütüphaneler

- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn

##  Veri Ön İşleme

- weather kolonu LabelEncoder ile sayısal forma dönüştürüldü.
- date kolonu string formatından sayısal formata çevrildi.
- Eksik veri kontrolü yapıldı.
- Veriler StandardScaler ile ölçeklendirildi.
- Veri %80 eğitim, %20 test olarak bölündü.

##  Model

Model: LogisticRegression

Parametreler:
- penalty = l2
- C = 100

##  Sonuç

Test Accuracy: 0.8361774744027304
