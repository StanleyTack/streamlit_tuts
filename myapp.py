import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.386, -122.084], columns=["lat", "lon"]
)

st.map(map_data)
