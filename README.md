# Streamlit Project - Paris Navigo TravelPass Offers

![Project Image](https://c0.lestechnophiles.com/www.numerama.com/wp-content/uploads/2024/05/navigo-metro-2-1024x576.jpg?avif=1&key=55b16b38)

Access the application here: https://appparis-trains-information-kntvzmzt34povglrzbbept.streamlit.app/Navigo_Promotions

## 🚀 Introduction

In Paris, there is a monthly pass that provides access to all public transportation in the city. It is called Navigo Pass.<br><br>
Partnerships exist with Parisian stores and cultural venues to offer special deals to Navigo Pass holders.<br><br>
These deals include both discounts and dedicated services.<br><br>
One of the goals of this project is to showcase to Navigo subscribers all the promotions they can access.<br><br>
The other objective is to give access to the expected arrival times for the next trains of the Parisian metro.

## 🛠️ Technos Used

- **Python**
- **Streamlit**
- **Pandas**
- **FastAPI**

## 🔑 Data Preparation : API_Request.ipynb
- Import Subway Lines Referential and the list of Subway Stops in Paris.
- Keep only the metro lines.
- Do the same for the stops, and keep only the ones in Paris.

## 🔑 Backend

1. **my_time_series_package**
- Creation of a function that converts a datetime value into the proper format.
- Also convert the time to be sure it is a Parisian time.

2. **main.py**
- Create the endpoint of the API.
- We need one endpoint, called arrival_time. It will guide the process through the API to know which information pick.
- The two informations we need to get is the destination_name, which corresponds to the direction of the train, and the expect arrival time at the selected station.

## 🔑 Frontend

1. **Home.py**
- Main page of the Streamlit app.

2. **Navigo Promotions.py**
- Center the map of the Streamlit App on Paris.
- Create Select Boxes to allow the user to select a type of advantage.
- Select the dataframe corresponding to this advantage.

3. **Next Trains.py**
- Create Select Boxes to allow the user to select a line and a stop.
- Request the API and the endpoint arrival time.

