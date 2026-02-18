# Cyber Attack Detection with Logistic Regression

## Overview
This project builds a machine learning model to classify different types of cyber attacks using network traffic features. The dataset is loaded from 7_cyber_attack_data.csv and processed with Pandas and Scikit-learn.

## Features
Example input features:
- src_packet_rate  
- dst_packet_rate  
- avg_payload_size  
- connection_duration  
- tcp_flag_count  
- avg_interarrival_time  
- failed_login_attempts  
- unusual_port_activity_score  
- session_entropy  
- avg_response_delay  

Target variable:
- attack_type  

## Methods
- Train/Test Split (80/20)
- Logistic Regression
- One-vs-Rest (OvR) strategy for multi-class classification
- GridSearchCV with StratifiedKFold for hyperparameter tuning
- Evaluation using Accuracy Score, Confusion Matrix, and Classification Report

## Results
- Baseline Accuracy: ~0.79  
- Tuned Model Accuracy: ~0.78  

## Libraries Used
- pandas  
- numpy  
- scikit-learn  
- matplotlib  
- seaborn
