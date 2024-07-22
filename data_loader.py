import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris

class DataLoader():
    
    # Load CSV data from uploaded file
    @st.cache_data
    def load_csv(file):
        csv = pd.read_csv(file)
        return csv

    # Load example data set
    def load_data():
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['target'] = iris.target
        return df