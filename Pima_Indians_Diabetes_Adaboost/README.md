Diabetes Prediction (AdaBoost)

Bu projede amacım bir diyabet veri seti üzerinde makine öğrenmesi algoritmaları kullanarak tahmin yapmaktı. Veri setini temizleyip modeli eğitip sonuçları değerlendirdim.

Kullandığım Kütüphaneler

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Veri Seti

- Toplam: 768 satır, 9 sütun
- Hedef değişken: Outcome (0 = sağlıklı, 1 = diyabet)

Yaptığım İşlemler

1. Veri Analizi

- "df.head()", "df.info()" ile veriyi inceledim
- Eksik veri yok gibi gözüküyor ama bazı sütunlarda 0 değerleri aslında eksik veri

2. Veri Temizleme

- Şu sütunlarda 0 değerleri NaN yaptım:
  - Glucose, BloodPressure, SkinThickness, Insulin, BMI
- Sadece train setine göre median hesapladım (data leakage olmaması için)
- Sonra hem train hem test setine uyguladım

3. Veri Bölme

train_test_split(test_size=0.2, random_state=42)

4. Ölçeklendirme

- StandardScaler kullandım

5. Model

- AdaBoostClassifier kullandım

İlk başta default model:

- Accuracy ≈ 0.75

6. Hyperparameter Tuning

GridSearchCV ile denedim:

params = {
    "n_estimators": [50,80,100,150,500],
    "learning_rate": [0.1,1,10,20,100]
}

En iyi parametreler:

{'learning_rate': 1, 'n_estimators': 100}

7. Sonuçlar

- Accuracy: 0.77

Classification Report

- Class 0:
  - precision: 0.83
  - recall: 0.81
- Class 1:
  - precision: 0.67
  - recall: 0.71

Confusion Matrix

[[80 19]
 [16 39]]

Kısa Yorum

Model fena değil ama özellikle class 1 (diyabet) tahmininde biraz daha geliştirilebilir. Daha farklı modeller veya feature engineering ile artırılabilir.
