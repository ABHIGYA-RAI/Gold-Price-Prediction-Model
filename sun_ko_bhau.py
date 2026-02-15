import streamlit as slt
import pickle
import numpy as np

slt.title("Gold Price Prediction by Random Forest Regressor Model")
user_input = slt.text_area("Enter the SPX,SLV,EUR/USD,USO")
if slt.button("Predict the gold price"):
    with open('ForestRegressor.pkl','rb') as file:
        model = pickle.load(file)
    two_d = np.array([user_input.split(',')],dtype=float)
    prediction = model.predict(two_d)
    slt.header(prediction)

