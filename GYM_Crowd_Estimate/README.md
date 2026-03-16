# Gym Crowd Prediction (Machine Learning)

Bu projede bir spor salonundaki insan sayısını tahmin etmeye çalışan bir makine öğrenmesi modeli geliştirdim.  
Dataset içerisinde tarih, saat, sıcaklık, hafta içi / hafta sonu gibi özellikler bulunuyor. Amaç bu özellikleri kullanarak spor salonunda kaç kişi olacağını tahmin etmek.

## Kullanılan Kütüphaneler

- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn

## Veri Seti Özellikleri

Dataset toplam *62184 satır* ve *11 sütundan* oluşuyor.

Kullanılan bazı özellikler:

- number_people → hedef değişken (kaç kişi olduğu)
- date → tarih
- day_of_week → haftanın günü
- is_weekend → hafta sonu olup olmadığı
- is_holiday → tatil günü olup olmadığı
- temperature → sıcaklık
- is_start_of_semester → dönem başlangıcı
- is_during_semester → dönem içinde mi
- month → ay
- hour → saat

## Veri Ön İşleme

Projede veri üzerinde bazı işlemler yapıldı:

- date sütunu datetime formatına çevrildi
- yıl bilgisi çıkarıldı
- korelasyon analizi yapıldı
- timestamp sütunu model için gereksiz olduğu için kaldırıldı
- train / test split uygulandı (%75 train %25 test)
- veriler StandardScaler ile ölçeklendirildi

## Veri Analizi

Veri üzerinde bazı görselleştirmeler yaptım:

- Saatlere göre spor salonundaki kişi sayısı
- Özellikler arası korelasyon heatmap

Bu sayede hangi değişkenlerin hedef değişken ile daha ilişkili olduğunu gözlemledim.

## Kullanılan Modeller

Projede birkaç farklı regresyon modeli denedim:

- Random Forest Regressor
- KNeighbors Regressor
- Decision Tree Regressor

Modeller eğitildikten sonra performansları *R² Score* ile ölçüldü.

## Model Sonuçları

| Model | R² Score |
|------|------|
| Random Forest | ~0.924 |
| KNN | ~0.903 |
| Decision Tree | ~0.921 |

En iyi sonucu *Random Forest Regressor* verdi.

## Hyperparameter Tuning

Model performansını artırmak için RandomizedSearchCV kullandım.

Aranan bazı parametreler:

- n_estimators
- max_depth
- max_features

Tuning sonrası model performansı:

*R² Score ≈ 0.9246*

## Sonuç

Bu projede spor salonundaki insan sayısını tahmin etmek için farklı makine öğrenmesi algoritmaları denedim. Random Forest modeli diğer modellere göre daha iyi sonuç verdi. Hyperparameter tuning ile model biraz daha iyileştirildi.

## Gelecekte Yapılabilecekler

- Daha fazla feature engineering
- Zaman serisi modeli denemek
- XGBoost / LightGBM gibi modeller kullanmak
- Daha gelişmiş hiperparametre optimizasyonu
