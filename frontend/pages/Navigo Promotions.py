import streamlit as st
import pandas as pd
import pydeck as pdk
import os

#Load data
current_dir = os.path.dirname(__file__)

csv_path_service = os.path.join(current_dir, 'Outputs/service.csv')
service = pd.read_csv(csv_path_service)

csv_path_tarif = os.path.join(current_dir, 'Outputs/tarif.csv')
tarif = pd.read_csv(csv_path_tarif)

csv_path_tarif_service = os.path.join(current_dir, 'Outputs/tarif_service.csv')
tarif_service = pd.read_csv(csv_path_tarif_service)

#Map on Paris
center_lat, center_lon = 48.8566, 2.3522

# Function to format long text for tooltips
def format_offre(offre, line_length=50):
    # Split the text into chunks of 'line_length' characters
    return '<br>'.join([offre[i:i+line_length] for i in range(0, len(offre), line_length)])

# Add a formatted 'Formatted_Offre' column to each DataFrame for the tooltip
service['Formatted_Offre'] = service['Offre'].apply(format_offre)
tarif['Formatted_Offre'] = tarif['Offre'].apply(format_offre)
tarif_service['Formatted_Offre'] = tarif_service['Offre'].apply(format_offre)

#Sidebar Parameters
st.sidebar.header("Avantage")

#Users Choices
choix = st.sidebar.selectbox(
    "Quel type d'avantage vous intéresse ?",
    ("Services", "Tarif Réduit", "Tarif Réduit + Service")
)

if choix=="Services":
    layers = [
        pdk.Layer(
            'ScatterplotLayer',
            data=service,
            get_position = '[Longitude,Latitude]',
            get_color = [255, 0, 0],
            get_radius = 100,
            pickable = True)]
    st.dataframe(service[['Nom du lieu','Adresse','Commune','Discipline','Offre']])

elif choix=="Tarif Réduit":
    layers = [
        pdk.Layer(
            'ScatterplotLayer',
            data=tarif,
            get_position = '[Longitude,Latitude]',
            get_color = [0, 255, 0],
            get_radius = 100,
            pickable = True)]
    st.dataframe(tarif[['Nom du lieu','Adresse','Commune','Discipline','Offre']])

elif choix=="Tarif Réduit + Service":
    layers = [
        pdk.Layer(
            'ScatterplotLayer',
            data=tarif_service,
            get_position = '[Longitude,Latitude]',
            get_color = [0, 0, 255],
            get_radius = 100,
            pickable = True)]
    st.dataframe(tarif_service[['Nom du lieu','Adresse','Commune','Discipline','Offre']])

#Create a map with Pydeck
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude = center_lat,
        longitude = center_lon,
        zoom = 12,
        pitch = 50
    ),
    layers = layers,
    tooltip = {
        "html": "<b>{Nom du lieu} <br/> {Adresse}<br/> {Formatted_Offre}",
        "style": {"color": "white"}
    }))