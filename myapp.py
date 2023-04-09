import streamlit as st
import pandas as pd
import streamlit_js_eval.sje as sje
import time

# Initialize an empty DataFrame to store GPS coordinates.
coords_df = pd.DataFrame(
    {"lat": [37.3861, 37.4419, 37.3688], "lon": [-122.0841, -122.1430, -122.0363]}
)

# Streamlit app layout and functionality.
st.title("Poop Map")
location = sje.get_geolocation()

if st.button("Poop!"):
    while location is None:
        st.write("waiting for location")
        time.sleep(100)

    new_location = {
        "lat": location["coords"]["latitude"],
        "lon": location["coords"]["longitude"],
    }
    coords_df.append(new_location, ignore_index=True)
    st.write(
        "lat:",
        location["coords"]["latitude"],
        ", lon: ",
        location["coords"]["longitude"],
    )

# Display the interactive map and update the map center.
map_component = st.map(
    coords_df,
    use_container_width=True,
)
