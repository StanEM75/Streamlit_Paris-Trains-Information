import streamlit as st

# Define the title and logos for the chat interface
APP_TITLE = """<div style="text-align: center">
                <h1 style="font-size: 48px; color: #6366F1;">
                    Train Monitoring Dashboard
                </h1>
                <p>
                    <b style="font-size: 24px">
                        Powered by Streamlit
                    </b>
                </p>
            </div>
        """
LOGO_PATH = "./image/Travelers.jpeg"


def app():
    # Set the page configuration
    st.set_page_config(
        page_title="Time Series App",  
        page_icon=LOGO_PATH,  
        layout="wide",  
    )

# Run the app
if __name__ == "__main__":
    app()