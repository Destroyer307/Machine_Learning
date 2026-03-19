Car Price Prediction (Random Forest)

Bu projede ikinci el araba fiyatlarını tahmin etmeye çalıştım. Aynı dataset ile daha önce AdaBoost Regressor kullanmıştım ve yaklaşık %78 (0.78) doğruluk elde etmiştim.
Bu sefer Random Forest Regressor denedim ve sonuç %91 (0.91) civarına çıktı.

 Dataset

- cardekho.csv dataseti kullanıldı
- İçinde araba markası, model, km, yakıt tipi vs. var

 Yaptıklarım

- dropna() ile eksik verileri temizledim (zaten yoktu ama yine de yaptım)
- Gereksiz kolon olan "Unnamed: 0" silindi
- Aykırı değerleri biraz filtreledim:
  - Çok yüksek fiyatları kestim
  - Çok yüksek km değerlerini çıkardım
  - vehicle_age < 20 yaptım

 Feature Engineering

- Kategorik verileri ikiye ayırdım:
  - Low cardinality: one-hot encoding
    ("seller_type", "fuel_type", "transmission_type")
  - High cardinality: frequency encoding
    ("car_name", "brand", "model")

 Train-Test Split

- %75 train / %25 test olacak şekilde böldüm

 Model

RandomForestRegressor(max_depth=12)

 Sonuç

- R² Score: 0.91
- Önceki model (AdaBoost): 0.78

 Yorumum

Random Forest açık ara daha iyi sonuç verdi.
Sebebi muhtemelen:

- Daha güçlü bir model olması
- Verideki non-linear ilişkileri daha iyi yakalaması

 Genel olarak

Bu projede:

- Veri temizleme
- Encoding teknikleri
- Model karşılaştırma

gibi şeyleri pratik etmiş oldum.

Daha sonra:

- Hyperparameter tuning yapmayı
- Farklı modeller denemeyi

düşünüyorum.
