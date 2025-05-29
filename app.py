from flask import Flask, render_template, request, jsonify
import joblib
from utilsweb import extract_features_from_verilog

app = Flask(__name__)

# Load models
area_model = joblib.load("models/area_model.pkl")
delay_model = joblib.load("models/delay_model.pkl")
power_model = joblib.load("models/power_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    code = request.form['code']
    try:
        features = extract_features_from_verilog(code)
        area = float(area_model.predict(features)[0])
        delay = float(delay_model.predict(features)[0])
        power = float(power_model.predict(features)[0])
        return jsonify({
            "area": round(area, 2),
            "delay": round(delay, 2),
            "power": round(power, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
