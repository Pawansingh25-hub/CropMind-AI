# 🌱 CropMind AI
### AI-Based Crop Disease Detection and Smart Farming Advisory System

CropMind AI is an AI-powered web application designed to help farmers identify tomato leaf diseases through image classification and receive disease management and weather-based farming advice.

## 🎯 Project Objective

The main objective of CropMind AI is to support farmers through AI-based crop disease identification and smart farming advisory.

## ✨ Key Features

- Farmer Registration and Login
- Farmer Dashboard
- Farmer Profile Management
- Tomato Leaf Image Upload
- CNN-Based Disease Prediction
- Prediction Confidence Score
- Disease Symptoms and Causes
- Prevention and Management Advice
- Prediction History
- Weather Information Integration
- Weather-Based Farming Advice
- Django Admin Panel

## 🦠 Supported Disease Classes

1. Tomato Early Blight
2. Tomato Late Blight
3. Tomato Leaf Mold
4. Tomato Healthy

## 🤖 AI Model Performance

| Metric | Result |
|---|---:|
| Total Images | 5,452 |
| Training Images | 3,815 |
| Validation Images | 818 |
| Testing Images | 819 |
| Test Accuracy | 92.06% |

Note: Accuracy is measured on a held-out PlantVillage test dataset. Real-world performance may vary.

## 🛠️ Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Django
- Database: SQLite
- Machine Learning: TensorFlow, CNN
- Image Processing: Pillow
- Dataset: PlantVillage
- Weather API: Open-Meteo

## 📁 Project Structure

```text
CropMindAI/
├── core/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── ai_predictor.py
│   ├── models.py
│   ├── views.py
│   └── weather_service.py
├── cropmind/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── class_labels.json
├── crop_disease_model.keras
├── requirements.txt
├── manage.py
├── train_model.py
├── evaluate_model.py
├── split_dataset.py
└── README.md
## ⚙️ Installation and Setup

### 1. Clone Repository

git clone https://github.com/Pawansingh25-hub/CropMind-AI.git
cd CropMind-AI

### 2. Create Virtual Environment

python -m venv venv

### 3. Activate Environment

.\venv\Scripts\Activate.ps1

### 4. Install Dependencies

python -m pip install -r requirements.txt

### 5. Configure Environment Variables

Create a .env file in the project root:

SECRET_KEY=your_django_secret_key

### 6. Run Migrations

python manage.py migrate

### 7. Start Development Server

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

## 📊 Model Evaluation

Run:

python evaluate_model.py

The script generates a classification report, confusion matrix and evaluation results.

## 🔮 Future Scope

- Support for additional crop varieties.
- Detection of more plant diseases.
- Improved real-world image validation.
- Advanced farming advisory features.
- IoT-based smart farming integration.

## 🎓 Academic Project

- Project Name: CropMind AI
- Project Type: Final Year B.Tech Project
- Domain: Artificial Intelligence, Machine Learning and Web Development
- Institution: SISTec Bhopal
- University: RGPV

## 👨‍💻 Author

**Pawan Singh**

GitHub: https://github.com/Pawansingh25-hub

---

⭐ If you find this project interesting, consider giving it a star!
