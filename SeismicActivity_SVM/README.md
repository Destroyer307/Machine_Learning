# Seismic Event Detection with SVM

This project uses a Support Vector Machine (SVM) model to detect seismic events based on underground wave energy and vibration axis variation data.

## Dataset

The dataset contains 400 samples with the following columns:

- underground_wave_energy
- vibration_axis_variation
- seismic_event_detected (Target variable: 0 or 1)

Feature engineering was applied by creating:

- underground_wave_energy**2
- vibration_axis_variation**2
- underground_wave_energy * vibration_axis_variation

## Data Preprocessing

- Checked for missing values (none found)
- Split data into training and test sets (80% train, 20% test)
- Random state fixed to 42 for reproducibility

## Model

A Linear Support Vector Machine was used:

python
from sklearn.svm import SVC

model = SVC(kernel="linear")
model.fit(X_train, y_train)


## Evaluation

Metrics used:

- Accuracy
- Precision
- Recall
- F1-score
- Classification Report

The model achieved *100% accuracy* on the test set.

## Visualization

- 2D scatter plot of features
- 3D scatter plot including polynomial features
- Color-coded by seismic event detection

## Requirements

- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- plotly

Install dependencies:

bash
pip install pandas numpy seaborn matplotlib scikit-learn plotly


## How to Run

1. Place the dataset file 9-seismic_activity_svm.csv in the project directory.
2. Run the Python script or Jupyter Notebook.
3. The model will train and display evaluation metrics and visualizations.
