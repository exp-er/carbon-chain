import streamlit as st
import pandas as pd

def foot():
    df=pd.read_csv("./Base/footprint.csv")
    st.write(df)
    st.caption("Calculation using footprint and average price")
def cred():
    df=pd.read_csv("./Base/credit.csv")
    st.caption("Calculation using offset cost and offsetting currently(made-up values)")
    st.write(df)
def ratio():
    df=pd.read_csv("./Base/ratio.csv")
    st.write(df)
    st.caption("calculating ratio based on offsetting, average profit, and carbon footprint")