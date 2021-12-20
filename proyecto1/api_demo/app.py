from flask import Flask, jsonify, request
import pandas as pd

import config as cfg
import pipeline_predict as pp

app = Flask(__name__)

@app.route("/saludar")
def saludar():
    return jsonify({"username": "prengsen"})

#ruta para predecir.
@app.route("/predecir", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    dataframe = pd.json_normalize(json_data)
    data = dataframe

    #cambiar nombre X1stFlrSF y X2ndFlrSF
    data = data[cfg.FEATURES]
    data['MSSubClass'] = data['MSSubClass'].astype('O')
    data['GarageCars'] = data['GarageCars'].astype('O')
    data['BsmtFullBath'] = data['BsmtFullBath'].astype('O')
    resultado = pp.predict(data)
    print(resultado)
    return jsonify({"Prediccion": resultado})