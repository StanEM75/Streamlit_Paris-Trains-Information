import streamlit as st
import requests
import pandas as pd
import os

# Define the title and logos for the chat interface
APP_TITLE = """<div style="text-align: center">
                <h1 style="font-size: 48px; color: #6366F1;">
                    Find your Next Train
                </h1>
                <p>
                    <b style="font-size: 24px">
                        Powered by Streamlit
                    </b>
                </p>
            </div>
        """
LOGO_PATH = "./image/Travelers.jpeg"

# Set the page configuration
st.set_page_config(
    page_title="Trains Expected Arrival Times",  
    page_icon=LOGO_PATH,  
    layout="wide",  
)

# Import Reference Files
current_dir = os.path.dirname(__file__)

csv_path_lines = os.path.join(current_dir, 'Outputs/lines.csv')
lines = pd.read_csv(csv_path_lines)

csv_path_stops = os.path.join(current_dir, 'Outputs/stops.csv')
stops = pd.read_csv(csv_path_stops)

# Convert files from csv to arrays (dictionnaires)
line_references = lines.set_index('Name_Line')['ID_Line'].to_dict()
stops_references = stops.set_index('ArRName')['ArRId'].to_dict()

# Select a Stop
selected_stop = st.selectbox("Your stop", list(stops_references.keys()))

# Select a Line
selected_line = st.selectbox("Your line", list(line_references.keys()))

# Get the IDs for the selected values
monitoring_ref = stops_references[selected_stop]
line_ref = line_references[selected_line]

# API URL and token (if needed)
base_url = "http://localhost:8000"
endpoint = "/arrival_time"
headers = {
    "Content-Type": "application/json"
}

# Payload with the selected stop and line
payload = {
    "MonitoringRef": monitoring_ref,
    "LineRef": line_ref
}

# Button to trigger the API call
if st.button("Get Arrival Time"):
    try:
        # Make a POST request to FastAPI
        response = requests.post(
            f"{base_url}{endpoint}",
            json=payload,
            headers=headers
        )

        if response.status_code == 200:
            # Display the arrival time data from the API
            arrival_data = response.json()
            st.write(arrival_data)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"API call failed: {str(e)}")