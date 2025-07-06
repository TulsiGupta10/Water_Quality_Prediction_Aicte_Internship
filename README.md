
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

All are located in the `output_images/` folder.

---

## 🔮 Future Scope

- Integrate with **IoT devices** for real-time monitoring
- Build a mobile app using **Flutter or React Native**
- Use **Deep Learning** for higher accuracy
- Expand to include **geographical water variations**

---

## 🤝 Contributors

- **Your Name** – Project Developer  
- Edunet Foundation / AICTE – Project Template

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).


