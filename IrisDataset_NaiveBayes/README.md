# Iris Classification with Gaussian Naive Bayes

Bu projede Iris veri seti kullanılarak çiçek türleri sınıflandırılmıştır.
Model olarak Gaussian Naive Bayes algoritması kullanılmıştır.

## Kullanılan Kütüphaneler

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Veri Seti

Veri setinde 3 farklı iris türü bulunmaktadır:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

Toplam 150 gözlem vardır (her sınıftan 50 adet).

Özellikler:
- SepalLengthCm
- SepalWidthCm
- PetalLengthCm
- PetalWidthCm

## Veri Ön İşleme

- "Id" sütunu kaldırıldı.
- "Species" sütunu LabelEncoder ile sayısal değerlere dönüştürüldü.
- Veriler %70 eğitim, %30 test olacak şekilde ayrıldı.
- StandardScaler ile özellikler ölçeklendirildi.

## Model

Gaussian Naive Bayes modeli kullanıldı.

Model eğitimi:
gnb.fit(X_train, y_train)

Tahmin:
y_pred = gnb.predict(X_test)

## Sonuçlar

Accuracy:
0.9777

Confusion Matrix:
[[19  0  0]
 [ 0 12  1]
 [ 0  0 13]]

Model yaklaşık %97 doğruluk oranı elde etmiştir.
