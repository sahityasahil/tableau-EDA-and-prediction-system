# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 05:55:44 2023

@author: sahit
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('D:/FOA/trained_model.sav', 'rb'))

# creating a function for prediction

def trade_prediction(input_data):
    
    input_data = (5221,1000.0,2.0)

    # changing the input data into numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Product Exported'
    else:
      return 'Product Imported'
  
    
def main():
     # giving a title
     st.title('Trade Prediction Web Application')
      
     # Getting the input from the user
     trade_usd = st.text_input('Trade in US Dollars')
     weight_kg = st.text_input('Weight in Kilograms')
     quantity = st.text_input('Quantity')
      
     #code for prediction
     trade1 = ''
      
     #creating a button
     if st.button('Trade Result'):
         trade1 = trade_prediction([trade_usd, weight_kg, quantity])
          
         st.success(trade1)
    
if __name__ == '__main__':
    main()