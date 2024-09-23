import uvicorn
from fastapi import FastAPI, Request, HTTPException
import requests
import logging
from my_time_series_package.my_time_series_conversion import convert_utc_to_local_hour

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.post("/arrival_time")
async def get_arrival_time(request: Request):
    try:
        # Parse the JSON request data
        data = await request.json()
        monitoring_ref = data["MonitoringRef"]
        line_ref = data["LineRef"]

        # API URL to get arrival time (replace with actual transport API URL)
        base_url = "https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring"
        headers = {
            "apiKey": "OuQIREojGU65DRhczPsANBSt0DreSkvy",  # Replace with your actual API key
            "Content-Type": "application/json"
        }
        
        # Make the API call to get the expected arrival time
        params = {
            "MonitoringRef": f"STIF:StopPoint:Q:{monitoring_ref}:",
            "LineRef": f"STIF:Line::{line_ref}:"
        }

        response = requests.get(base_url, headers=headers, params=params)

        # Log the full response for debugging
        logging.info(f"Response status: {response.status_code}")
        logging.info(f"Response content: {response.content}")

        if response.status_code == 200:
            # Try extracting data from the response
            try:
                stop_visits = response.json()['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit']
                results = []
                for visit in stop_visits:
                    destination_name = visit['MonitoredVehicleJourney']['DestinationName'][0]['value']
                    expected_arrival_time_utc = visit['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime']
                    #Apply function to get the good timezon format
                    formatted_time = convert_utc_to_local_hour(expected_arrival_time_utc)
                    results.append([
                    destination_name,
                    formatted_time
                    ])

                return results
            except KeyError as e:
                # Log if the 'Siri' key is missing
                logging.error(f"KeyError: {str(e)}")
                raise HTTPException(status_code=500, detail=f"KeyError: {str(e)}")
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

    except Exception as e:
        # Log any unexpected exceptions
        logging.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# If this script is run directly, launch the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)