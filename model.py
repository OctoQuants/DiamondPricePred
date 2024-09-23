import pandas as pd
#from matplotlib import pyplot as plt
#import seaborn as sns
from sklearn.preprocessing import RobustScaler, StandardScaler, OneHotEncoder, OrdinalEncoder, PowerTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
import pickle
import streamlit as st

st.title("Diamond Price Prediction")

carat = st.number_input("Enter the carat value")
cut = st.text_input("Enter the cut of the diamond")
color = st.text_input("Enter the color code of the diamond")
clarity = st.text_input("Enter the clarity code")
depth = st.number_input("Enter the depth of the diamond")
table = st.number_input("Enter the table value")
x = st.number_input("Enter the length of diamond")
y = st.number_input("Enter the width of the diamond")
z = st.number_input("Enter the z of the diamond")

model_1 = pickle.load(open(r"dt.pkl","rb")) #pickle file path

if st.button("Submit"):
    result = model_1.predict([[carat,cut,color,clarity,depth,table,x,y,z]])
    st.write(f"The predicted price of the diamond is {result}")
