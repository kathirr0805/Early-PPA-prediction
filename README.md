# Early PPA Prediction for RTL Designs using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange)
![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning tool that predicts **Power, Performance, and Area (PPA)** metrics directly from Verilog RTL code, eliminating the need for time-consuming synthesis.

## 🚀 Features

- 🔍 Predicts **Area**, **Delay**, and **Power** from Verilog code
- 🧠 Uses **Random Forest Regression** with **TF-IDF** vectorized RTL features
- 🌐 Web UI built using **Flask**
- 💾 Pretrained ML models provided (`.pkl`)
- ⚙️ Easily deployable on **Render**, **Replit**, or locally
- 🧩 No ML or synthesis knowledge needed to use
## 📦 Installation

---

## 📊 Machine Learning Techniques Used

- **TF-IDF Vectorization**: For feature extraction from Verilog code
- **Random Forest Regression**: Trained separately to predict:
  - Area
  - Delay
  - Power

Models were trained on a custom RTL dataset with real synthesis values.

---

## 🛠️ Requirements

- Python 3.8+
- Flask
- scikit-learn
- joblib
- numpy
- Git LFS (for large model files)

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/kathirr0805/ppa.git
cd ppa

# 2. (Optional) Setup virtual env
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 4. Run the app
python app.py
