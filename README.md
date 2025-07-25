# 🌾 CropYield360 - AI-Powered Crop Yield Prediction System

**CropYield360** is an AI-powered web platform built with Flask that predicts maize yield in Trans Nzoia, Kenya. It uses machine learning, NDVI data, and role-based access to offer tailored prediction forms for farmers, officers, and admins.

## 🚀 Features

* ✅ Maize yield prediction using a trained `RandomForestRegressor`
* ✅ Role-based login for:

  * Farmers (simplified input form)
  * Agricultural Officers (intermediate data input)
  * Admins (full data control)
* ✅ Secure user authentication (Login/Register)
* ✅ Contact form integration
* ✅ Dynamic, interactive graphs using **Chart.js**
* ✅ Visual insights: Rainfall vs Yield, Temperature vs Yield, NDVI trends
* ✅ Professional UI with background image, sticky navbar, and responsive layout

---

## 📁 Project Structure

```
project-root/
│
├── app.py                      # Main Flask app
├── model.pkl                   # Trained ML model
├── yield_prediction_dataset.csv # Dataset used for training and graphs
├── requirements.txt            # Dependencies
│
├── instance/
│   └── database.sqlite         # SQLite DB (user auth)
│
├── static/
│   └── css/
│       ├── index.css           # Landing page styles
│       ├── predict.css         # Predict form styles
│
├── templates/
│   ├── index.html              # Landing page
│   ├── login.html              # Login form
│   ├── register.html           # Register form
│   ├── dashboard.html          # Role-based dashboard
│   ├── predict_farmer.html     # Farmer form
│   ├── predict_officer.html    # Officer form
│   ├── predict_admin.html      # Admin form
│   ├── result.html             # Prediction result + charts
```

---

## ⚙️ Setup Instructions

### 1. Clone and Install

```bash
git clone https://github.com/faithFey/Ai-crop-yield-prediction-project.git
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the App

```bash
python app.py
```

Visit: `http://127.0.0.1:5000`

---

## 🧠 Machine Learning Model

* Model: `RandomForestRegressor`
* Features: Rainfall, Temperature, Soil Type, NDVI, Humidity, pH, Fertilizer
* Trained on: NDVI-satellite + agronomic data (`yield_prediction_dataset.csv`)
* Maize-only filtering applied

---

## 📊 Charts & Insights

The app generates visual analysis after prediction:

* 📈 Rainfall vs Yield (Maize only)
* 📈 Temperature vs Yield
* 🌿 NDVI Trends by Month
* 📆 Monthly Yield Distribution

Powered by **Chart.js** (dynamic rendering with data passed via Jinja2).

---

## 👥 User Roles

| Role    | Access                                 |
| ------- | -------------------------------------- |
| Farmer  | Input rainfall, temperature, soil type |
| Officer | + humidity, NDVI                       |
| Admin   | + pH, fertilizer usage                 |

---

## 📨 Contact / Support

Use the contact form on the landing page or email `faithnasimiyuu@gmail.com`.

---

## 🛡️ Security & Notes

* DO NOT use this setup in production as-is.
* Use HTTPS, input validation, rate limiting, and secure DB in production.

---
## 🚀 Live Deployment

This project is successfully deployed and hosted on **Render**, making it accessible to users worldwide.

### 🔗 Live Web App  
[👉 Visit CropYield360 on Render](https://cropyield360.onrender.com)  

### 💡 Features Available Online
- 🌾 **Role-Based Login System** for Farmers, Officers, and Admins
- 📈 **AI-Powered Maize Yield Prediction**
- 📊 **Interactive Charts for Rainfall, NDVI, and Yield Trends**
- 📬 **Contact Form** for users and visitors
- 📄 **Secure Authentication & Dynamic Dashboards**

### 🛠️ Hosted On:
- **Platform:** [Render](https://render.com)  
- **Backend:** Flask + SQLite  
- **Frontend:** HTML, CSS, Chart.js  
- **Model:** Trained using Scikit-learn (RandomForestRegressor)

---
## 📌 License

This project is open-source and licensed under MIT.

---

## 🙏 Acknowledgements

* Trans Nzoia agriculture stakeholders
* Google Earth Engine (NDVI data)
* Flask, Scikit-learn, Chart.js
