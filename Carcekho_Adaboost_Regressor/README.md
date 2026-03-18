 Car Price Prediction (AdaBoost)

Bu projede ikinci el araç fiyatlarını tahmin etmeye çalıştım. Dataset olarak cardekho.csv kullandım ve model olarak AdaBoost Regressor tercih ettim.



 Projede Neler Yaptım?

- Dataset’i okudum ve inceledim ("df.head(), df.info()")
- Gereksiz kolonları sildim ("Unnamed: 0")
- Hatalı verileri temizledim
  - "seats > 0" filtresi
  - Aykırı değerleri çıkardım (çok yüksek price ve km)
- Duplicate verileri sildim
- Veriyi görselleştirdim
  - Scatter plot (age vs price, km vs price)
  - Boxplot (fuel type, transmission)



 Feature Analysis

- "vehicle_age" arttıkça fiyat düşüyor
- "max_power" ve "engine" arttıkça fiyat artıyor
- "fuel_type" ve "transmission_type" önemli etkili



 Feature Engineering

Categorical verileri ikiye ayırdım:

- One-Hot Encoding
  
  - seller_type
  - fuel_type
  - transmission_type

- Frequency Encoding
  
  - brand
  - model
  - car_name

Train ve test için ayrı ayrı düzgün encoding yaptım (data leakage olmaması için).



 Model

Kullandığım model:

AdaBoostRegressor(n_estimators=150)

Modeli eğittim ve test ettim.



 Sonuç

R2 Score: 0.7767

Bence fena değil, ama geliştirilebilir.



 Notlar

- Outlier temizlemek performansı ciddi artırdı
- Encoding kısmı en kritik yerlerden biri
- Daha iyi sonuç için:
  - Hyperparameter tuning (GridSearch)
  - Farklı modeller (XGBoost, RandomForest) denenebilir



 Genel Yorum

Bu proje sayesinde:

- Veri temizleme
- Feature engineering
- Model eğitme

konularını baya pekiştirdim.



 Kullanım

pip install pandas numpy seaborn matplotlib scikit-learn

Notebook u çalıştır yeterli.

