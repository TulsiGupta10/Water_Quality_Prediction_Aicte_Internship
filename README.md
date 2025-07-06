
# 💧 Water Quality Prediction

This project aims to predict whether water is **potable** (safe to drink) or **not** based on physicochemical properties using **machine learning**. The goal is to automate water quality assessment to assist public health efforts and real-time monitoring.

---

## 📂 Project Structure

```
water-quality-prediction/
├── app.py                   # Streamlit web app for predictions
├── pollution_model.pkl      # Trained ML model
├── model_columns.pkl        # Columns used for training the model
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── output_images/           # Visual results like accuracy, confusion matrix, etc.
```

---

## 🚀 Features

- Accepts user inputs: **Year** and **Station ID**
- Predicts multiple pollutant levels (e.g., O2, NO3, NO2, etc.)
- Displays model performance: accuracy, confusion matrix, feature importance
- Streamlit web interface for easy use
- Scalable for IoT and mobile-based integration

---

## 🛠️ Technologies Used

- Python (Pandas, Scikit-learn, NumPy)
- Streamlit (Web interface)
- Joblib (Model serialization)
- Matplotlib & Seaborn (Visualizations)

---

## 📊 Dataset Description

The model is trained on water quality data containing parameters like:

- `ph`, `hardness`, `solids`, `chloramines`
- `sulfate`, `turbidity`
- Label: `potability` (0 = Not potable, 1 = Potable)

> You can update the dataset or extend with regional water quality data as needed.

---

## 🧪 How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/water-quality-prediction.git
cd water-quality-prediction
```

2. **Install Requirements**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit App**

```bash
streamlit run app.py
```

4. **View in Browser**

Go to: [http://localhost:8501](http://localhost:8501)

---

## 📈 Sample Outputs

Here are some of the visuals generated during training and evaluation:

- Confusion Matrix  
- Feature Importance  
- Accuracy Score  
- Sample Prediction
  
![Screenshot (2539)](https://github.com/user-attachments/assets/29693b81-f1b0-45e4-b3ee-96f95e11be82)


![Screenshot (2540)](https://github.com/user-attachments/assets/11a4eae1-e8ca-4595-9261-2ab084249822)


![project_output_confusion_matrix](https://github.com/user-attachments/assets/623b9431-a653-4280-a81b-e5385952bad5)


![project_output_accuracy](https://github.com/user-attachments/assets/0c89f064-2dc5-46fc-b3fd-4c833d8152d3)


![project_output_feature_importance](https://github.com/user-attachments/assets/04bd938e-c48c-4692-8544-59d846b5b966)

## 🔮 Future Scope

- Integrate with **IoT devices** for real-time monitoring
- Build a mobile app using **Flutter or React Native**
- Use **Deep Learning** for higher accuracy
- Expand to include **geographical water variations**

---

## 🤝 Contributors

- Tulsi Gupta
- Edunet Foundation / AICTE – Internship project

---



