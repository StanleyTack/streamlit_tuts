import streamlit as st
import pandas as pd
import streamlit_js_eval.sje as sje
import time
import random


# Streamlit app layout and functionality.
st.title("Poop Map")
location = sje.get_geolocation()

# Initialize a DataFrame to store GPS coordinates.
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        {"lat": [37.3861, 37.4419, 37.3688], "lon": [-122.0841, -122.1430, -122.0363]}
    )

if st.button("Poop!"):
    st.session_state.clicks += 1
    # lat = 37.3861 + random.uniform(-0.025, 0.025)
    # lon = -122.0841 + random.uniform(-0.025, 0.025)
    # new_location = pd.DataFrame({"lat": [lat], "lon": [lon]})

    new_location = pd.DataFrame(
        {
            "lat": [location["coords"]["latitude"]],
            "lon": [location["coords"]["longitude"]],
        }
    )
    st.session_state.df = pd.concat(
        [st.session_state.df, new_location], axis=0, ignore_index=True
    )

# Display the interactive map and update the map center.
map_component = st.map(
    st.session_state.df,
    use_container_width=True,
)

for i in range(len(st.session_state.df)):
    st.write(
        "lat: ", st.session_state.df["lat"][i], "long: ", st.session_state.df["lon"][i]
    )
