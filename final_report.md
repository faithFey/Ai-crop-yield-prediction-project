# AI-Powered Crop Yield Prediction System

**Developer: Faith Wafula  • Institution: PLP Academy, Kenya**

---

## 1. Introduction

In Trans Nzoia County, maize farming is the backbone of food security and livelihoods. However, yield forecasting remains unreliable due to climate variability and lack of smart tools. This project introduces **CropYield360**, an AI-powered web application that predicts maize yield using environmental and satellite data.

---

## 2. Objectives

* Build a machine learning model for maize yield prediction.
* Develop a user-friendly Flask web app with role-based access (Farmer, Officer, Admin).
* Visualize yield trends through interactive charts (rainfall, NDVI, temperature).
* Deploy and test the system for real-world use.

---

## 3. Methodology

### Dataset

* Source: yield\_prediction\_dataset.csv (1,625 records)
* Features: NDVI, rainfall, temperature, soil moisture, soil type, crop type, yield

### Tools & Technologies

* **Backend:** Flask, Flask-Login, Flask-SQLAlchemy
* **ML Model:** RandomForestRegressor via scikit-learn
* **Frontend:** HTML, CSS, Chart.js, Jinja templates
* **Database:** SQLite
* **Deployment:** Render
* **Version Control:** GitHub

### Machine Learning Pipeline

* Data preprocessing (cleaning, encoding, feature selection)
* Train/test split
* RandomForestRegressor training
* Model saved as `model.pkl`

---

## 4. System Architecture

* Users register/login with a role (Farmer, Officer, Admin)
* Prediction forms differ based on role (farmer: soil; officer: NDVI/humidity; admin: full form)
* Predictions sent to model and output visualized in `results.html`
* Graphs shown using Chart.js and passed via Jinja context

```
User → Flask Form → Model Input → Prediction → Chart.js Output
```

---

## 5. Testing & Validation

### Unit Testing

* Tested model with dummy data (36 features)
* Confirmed correct shape and prediction output

### Integration Testing

* Used Postman to submit POST requests to `/predict-result`
* Verified session handling, form input validation, prediction logic

### User Testing

* Verified flow: Register → Login → Predict → View graphs
* Forms worked per role; outputs visually accurate

---

## 6. Results

* System accurately predicts yield (rounded tons per hectare)
* Graphs generated:

  * Rainfall vs Yield
  * Monthly Yield Trends
  * NDVI Seasonal Variation
  * Temperature vs Yield

### Screenshots

* \[![Landing page](<static/images/landing screenshot.png>)]
* \[![Prediction page](<static/images/prediction screenshot.png>)]
* \[![Results page](<static/images/results screenshot.png>)]

---

## 7. Deployment

* **Hosted On:** [Render](https://render.com)
* **Live App:** \[https://cropyield360.onrender.com]
* **GitHub:** [https://github.com/faithFey/Ai-crop-yield-prediction-project](https://github.com/faithFey/Ai-crop-yield-prediction-project)

---

## 8. Conclusion & Future Work

This project provides a practical, smart tool for maize farmers in Trans Nzoia. It supports better planning, improves food security, and fosters tech adoption in agriculture.

### Future Improvements:

* Add SMS or WhatsApp yield reports
* Mobile-first responsive design
* Integrate satellite NDVI APIs (e.g., SentinelHub)
* Store historical prediction logs for analysis

---

## 9. References

* scikit-learn documentation: [https://scikit-learn.org](https://scikit-learn.org)
* Flask documentation: [https://flask.palletsprojects.com](https://flask.palletsprojects.com)
* Dataset: Provided in local CSV
* Render: [https://render.com](https://render.com)
* Chart.js: [https://www.chartjs.org](https://www.chartjs.org)

---

*Prepared for PLP Academy Final Project Submission.*
