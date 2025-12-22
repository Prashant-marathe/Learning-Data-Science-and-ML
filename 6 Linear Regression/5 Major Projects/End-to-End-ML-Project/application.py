from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Import ridge model and scaler model so our app can interact with them
model_package = pickle.load(open('models/ridge.pkl', 'rb'))
ridge_model = model_package['model']
model_accuracy = model_package['r2_score']
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

application = Flask(__name__)
app = application

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata", methods=["GET", "POST"])
def  predict_datapoint():
    if request.method == "POST":
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html', result=result[0], accuracy=model_accuracy)
    else:
        return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)