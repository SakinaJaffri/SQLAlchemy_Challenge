# SQLAlchemy Challenge

![Hawaii Climate](https://github.com/SakinaJaffri/SQLAlchemy_Challenge/assets/146900226/443dc487-b0a8-40bd-a85c-0ad91c5afe63)

## Introduction

Planning a vacation to Honolulu, Hawaii? Understanding the climate is essential for your trip! This project focuses on analyzing climate data in Honolulu using **Python** and **SQLAlchemy** to provide insights into the region’s weather patterns. It also includes building a Flask API to easily access the climate data.

## Part 1: Climate Data Analysis and Exploration

The goal of this section is to conduct climate analysis using **SQLAlchemy**, **Pandas**, and **Matplotlib**.

### Steps Performed:
- **Precipitation Analysis**: 
  - Retrieved the last 12 months of precipitation data and visualized it using Matplotlib.
  - Displayed summary statistics for the precipitation data.
  
- **Station Analysis**:
  - Calculated the total number of weather stations.
  - Identified the most active weather stations.
  - Extracted and visualized temperature observations from the most active station for the previous year.

## Part 2: Building a Climate Data API

Using the findings from Part 1, a **Flask** API was created to make climate data accessible. The following routes were developed:

- **`/`**: Home page displaying available API routes.
- **`/api/v1.0/precipitation`**: Returns a JSON of precipitation data for the last 12 months.
- **`/api/v1.0/stations`**: Returns a JSON list of weather stations.
- **`/api/v1.0/tobs`**: Returns temperature observations for the previous year from the most active station.
- **`/api/v1.0/<start>`** and **`/api/v1.0/<start>/<end>`**: Returns JSON-formatted min, max, and average temperatures for a specified date range.

## Usage

1. Clone the repository to your local machine.
2. Ensure that **Python**, **Flask**, **SQLAlchemy**, and other dependencies are installed.
3. Run the Flask application by executing `python app.py`.
4. Access the available routes through your browser or API client to retrieve climate data.

## Conclusion

With this Flask API and climate analysis, you can explore the weather patterns of Honolulu, Hawaii, and make informed decisions for your next trip. 🏖️🌞

---

## Technologies Used:
- Python
- SQLAlchemy
- Pandas
- Matplotlib
- Flask
