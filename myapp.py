import streamlit as st
import pandas as pd
import streamlit_js_eval as sje

# Initialize an empty DataFrame to store GPS coordinates.
coords_df = pd.DataFrame(
    {"lat": [37.3861, 37.4419, 37.3688], "lon": [-122.0841, -122.1430, -122.0363]}
)

# Streamlit app layout and functionality.
st.title("Poop Map")

if st.button("Poop!"):
    location = sje.get_geolocation()
    if location is None:
        st.write("no location found")
    elif location is not None:
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
