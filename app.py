# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:46:06 2023

@author: Aishwarya
"""

import pickle
import streamlit as st


load = open('model.pkl','rb')
model = pickle.load(load)

def predict(SL,SW,PL,PW):
    prediction = model.predict([[SL,SW,PL,PW]])
    return prediction

def main():
    st.title('Iris Flower Species :earth_africa:')
    
    SL = st.number_input('Sepal length :')
    SW = st.number_input('Sepal width :')
    PL = st.number_input('Petal Length :')
    PW = st.number_input('Petal Width :')
    
    if st.button('Predict'):
        result = predict(SL,SW,PL,PW)
        st.success('The flower is: {} '.format(result))
        

if __name__ == '__main__':
    main()