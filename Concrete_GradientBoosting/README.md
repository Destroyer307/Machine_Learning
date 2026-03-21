# Gradient Boosting ile Beton Dayanımı Tahmini

## Proje
Bu projede beton verisi kullanarak "Strength" değerini tahmin etmeye çalıştım.  
Model olarak Gradient Boosting kullandım.

## Veri
Veri setinde şu özellikler var:
- Cement
- Blast Furnace Slag
- Fly Ash
- Water
- Superplasticizer
- Coarse Aggregate
- Fine Aggregate
- Age
- Strength (hedef)

Toplam:
- 1030 satır
- 9 sütun

## Veri Durumu
- Veri temiz (eksik değer yok)
- df.isnull().sum() sonucu tamamen 0

## Model
Kullandığım model:
GradientBoostingRegressor

Başlangıç parametreleri:
- n_estimators = 100
- learning_rate = 0.2
- max_depth = 5

## Eğitim
Veriyi şu şekilde böldüm:
- %75 train
- %25 test

## Sonuç
Modelin R² skoru:
0.92

## Hiperparametre Optimizasyonu
RandomizedSearchCV kullandım.

Denediğim parametreler:
- n_estimators: [100,120,180,200]
- loss: ["squared_error","absolute_error","huber","quantile"]
- max_depth: [3,4,5]
- learning_rate: [0.1,0.2]

## En İyi Parametreler
- n_estimators: 100
- max_depth: 4
- loss: squared_error
- learning_rate: 0.2

Yeni R² skoru:
0.925

## Amaç
Bu projedeki ana amacım:
Gradient Boosting algoritmasının parametrelerinin modeli nasıl etkilediğini anlamak ve en iyi sonucu elde etmek.
