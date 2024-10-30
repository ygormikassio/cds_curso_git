import pandas as pd
import numpy as np
import streamlit as st

def load_data():
    return pd.read_csv('data/processed/bikes_completed.csv')

def main():
    df_raw = load_data()
    
    st.dataframe(df_raw)

if __name__ == '__main__':
    main()
