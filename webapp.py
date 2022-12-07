# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import pickle
import streamlit as st

st.set_page_config(page_title="Football Team Division Prediction Web App")

# loading the saved models
logiRegModel = pickle.load(open('logiRegModel.sav', 'rb'))
#randomForesModel = pickle.load(open('randomForesModel.sav', 'rb'))
gaussModel = pickle.load(open('gaussModel.sav', 'rb'))
knnModel = pickle.load(open('knnModel.sav', 'rb'))
treeModel = pickle.load(open('treeModel.sav', 'rb'))

def footballTeamDivisionPrediction(input_data): 
    input_data_as_nparray = np.asarray(input_data)  #pd.DataFrame(data=input_data, columns=['HS','AS','HST','AST','HY','AY','HR','AR','HF','AF','FTHG','FTAG','FTR','HTR','HTHG','HTAG','HC','AC','IWA','IWD','IWH', 'B365H', 'B365D', 'B365A'])
    input_data_reshaped = input_data_as_nparray.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)

    return prediction

def traingModelSelection(inputModel):
    if inputModel == "Logistic Regression":
        return logiRegModel
    elif inputModel == "Gaussian":
        return gaussModel
    elif inputModel == "KNN":
        return knnModel
    elif inputModel == "Decision Tree":
        return treeModel
    
if __name__ == '__main__':
    #giving a title
    st.title('Football Team Division Prediction Web App')
    
    model_options = ['Logistic Regression', 'Gaussian', 'KNN', 'Decision Tree']
    chosenModel = st.selectbox("Select your Training Model:", options=model_options)
    
    #getting the input data from the user
    HS = st.slider("Home Team Shots: ")
    AS = st.slider("Away Team Shots: ")
    HST = st.slider("Home Team Shots on Target: ")
    AST = st.slider("Away Team Shots on Target: ")
    HY = st.slider("Home Team Yellow Cards: ")
    AY = st.slider("Away Team Yellow Cards: ")
    HR = st.slider("Home Team Red Cards: ")
    AR = st.slider("Away Team Red Cards: ")
    HF = st.slider("Home Team Fouls Committed: ")
    AF = st.slider("Away Team Fouls Committed: ")
    FTHG = st.slider("Full Time Home Team Goals: ")
    FTAG = st.slider("Full Time Away Team Goals: ")
    FTR = st.slider("Full Time Result: ")
    HTR = st.slider("Half Time Result: ")
    HTHG = st.slider("Half Time Home Team Goals: ")
    HTAG = st.slider("Half Time Away Team Goals: ")
    HC = st.slider("Home Team Corners: ")
    AC = st.slider("Away Team Corners: ")
    IWA = st.slider("Interwetten away win odds")
    IWD = st.slider("Interwetten draw odds")
    IWH = st.slider("Interwetten home win odds")
    B365H = st.slider("Bet365 home win odds")
    B365D = st.slider("Bet365 draw odds")
    B365A = st.slider("Bet365 away win odds")

    #code for Prediction
    loaded_model = traingModelSelection(chosenModel)

    predicted_division = ''
    predicted_value = footballTeamDivisionPrediction([HS,AS,HST,AST,HY,AY,HR,AR,HF,AF,FTHG,FTAG,FTR,HTR,HTHG,HTAG,HC,AC,IWA,IWD,IWH, B365H, B365D, B365A])

    # creating a button for Prediction
    if st.button('Team Division Prediction'):
        if predicted_value > 0:
            predicted_division = predicted_value
        else:
            predicted_division = 'An error occured'
        st.success('The football teams predicted division: {0}'.format(predicted_division))