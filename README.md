# Early PPA Prediction for RTL Designs using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange)
![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning tool that predicts **Power, Performance, and Area (PPA)** metrics directly from Verilog RTL code, eliminating the need for time-consuming synthesis.

## 🚀 Key Features
- **Instant PPA Prediction**: Get area (µm²), delay (ns), and power (µW) estimates in <2 seconds
- **No Synthesis Required**: Works directly on raw Verilog code
- **Web Interface**: User-friendly GUI with code editor and file upload
- **85-92% Accuracy**: Compared to actual synthesis results (SkyWater 130nm)

## 📦 Installation
```bash
# Clone repository
git clone https://github.com/yourusername/early-ppa-prediction.git
cd early-ppa-prediction

# Install dependencies
pip install -r requirements.txt



├── models/                # Pretrained ML models
│   ├── area_model.pkl
│   ├── delay_model.pkl
│   └── vectorizer.pkl
├── app.py                 # Flask application
├── train_models.py        # Model training script
└── templates/             # Web interface
    ├── index.html
    └── style.css



### Key Features of This README:
1. **Badges** - Visual indicators for Python version, dependencies, and license
2. **Structured Sections** - Clear separation of features, installation, usage, and results
3. **Technical Transparency** - Specifics about models, accuracy, and architecture
4. **Visual Hierarchy** - Clean formatting with emojis and code blocks
5. **Reproducibility** - Precise instructions for setup and execution

To use:
1. Copy this markdown into your `README.md` file
2. Replace placeholder links/emails with your actual info
3. Add screenshots of your web interface (optional but recommended) by inserting:
```markdown
![Web Interface Demo](docs/demo-screenshot.png)
