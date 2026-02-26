# Iris Dataset - SVM Classification

Bu projede Iris veri seti kullanılarak Support Vector Machine (SVM) algoritması ile sınıflandırma yapılmıştır.

## Kullanılan Kütüphaneler

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Veri Seti

- Toplam 150 örnek
- Özellikler:
  - SepalLengthCm
  - SepalWidthCm
  - PetalLengthCm
  - PetalWidthCm
- Hedef değişken: Species

## Yapılan İşlemler

1. CSV dosyası pandas ile okundu.
2. Özellikler (X) ve hedef değişken (y) ayrıldı.
3. Veri %70 eğitim, %30 test olacak şekilde bölündü.
4. LabelEncoder ile hedef değişken sayısal hale getirildi.
5. SVC modeli oluşturuldu ve eğitildi.
6. Test verisi üzerinde tahmin yapıldı.
7. Accuracy hesaplandı.

## Sonuç

Accuracy: 1.0

Model test verisi üzerinde %100 doğruluk elde etmiştir.
