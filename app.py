from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager, UserMixin, login_user, login_required, logout_user, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
import numpy as np
import pickle
import os
import pandas as pd

# --- App setup ---
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this in production!

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- User Model ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='farmer')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Load Model ---
MODEL_PATH = "model.pkl"
model = pickle.load(open(MODEL_PATH, 'rb')) if os.path.exists(MODEL_PATH) else None

# --- Routes ---
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists.")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Please log in.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash("Invalid credentials.")
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for("home"))

@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    if current_user.role == 'farmer':
        return render_template('predict_farmer.html', user=current_user)
    elif current_user.role == 'officer':
        return render_template('predict_officer.html', user=current_user)
    elif current_user.role == 'admin':
        return render_template('predict_admin.html', user=current_user)
    else:
        return "Unauthorized", 403

@app.route('/predict-result', methods=['POST'])
@login_required
def predict_result():
    try:
        if model is None:
            return "Model not found. Please train and save model.pkl first.", 500

        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])

        if 'soil' in request.form:
            soil = request.form['soil']
            soil_types = ['sandy', 'loamy', 'clay', 'silty', 'peaty', 'saline']
            soil_encoded = [1 if soil == s else 0 for s in soil_types]
            features = [rainfall, temperature] + soil_encoded

        elif 'humidity' in request.form and 'ndvi' in request.form and 'ph' not in request.form:
            humidity = float(request.form['humidity'])
            ndvi = float(request.form['ndvi'])
            features = [rainfall, temperature, humidity, ndvi]

        elif 'ph' in request.form and 'fertilizer' in request.form:
            humidity = float(request.form['humidity'])
            ndvi = float(request.form['ndvi'])
            ph = float(request.form['ph'])
            fertilizer = float(request.form['fertilizer'])
            features = [rainfall, temperature, humidity, ndvi, ph, fertilizer]
        else:
            return "Invalid input", 400

        final_input = np.array([features + [0]*(36 - len(features))])
        prediction = model.predict(final_input)[0]

        # --- Visualization Data ---
        df = pd.read_csv('yield_prediction_dataset.csv')
        maize_data = df[df['crop_type'].str.lower() == 'maize'].copy()
        maize_data['date_of_image'] = pd.to_datetime(maize_data['date_of_image'], dayfirst=True, errors='coerce')
        maize_data = maize_data.dropna(subset=['date_of_image'])
        maize_data['month'] = maize_data['date_of_image'].dt.month

        rainfall_groups = maize_data.groupby('rainfall')['yield'].mean().reset_index()
        rainfall_labels = rainfall_groups['rainfall'].round(2).tolist()
        rainfall_yield_values = rainfall_groups['yield'].round(2).tolist()

        monthly_stats = maize_data.groupby('month').agg({
            'yield': 'mean',
            'NDVI': 'mean',
            'temperature': 'mean'
        }).fillna(0)

        return render_template('results.html',
            prediction=round(prediction, 2),
            rainfall_labels=rainfall_labels,
            rainfall_yield_values=rainfall_yield_values,
            month_labels=monthly_stats.index.tolist(),
            monthly_yield=monthly_stats['yield'].round(2).tolist(),
            monthly_ndvi=monthly_stats['NDVI'].round(2).tolist(),
            monthly_temp=monthly_stats['temperature'].round(2).tolist()
        )
    except Exception as e:
        return f"Prediction error: {e}", 400

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f"Message from {name} ({email}): {message}")
    flash("Message sent!")
    return redirect(url_for('home'))

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("You must log in to access the system.", "warning")
    return redirect(url_for('login'))

# --- Run Server ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
