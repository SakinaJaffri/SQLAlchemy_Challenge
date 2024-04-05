# SQLAlchemy_Challenge
![image](https://github.com/SakinaJaffri/SQLAlchemy_Challenge/assets/146900226/443dc487-b0a8-40bd-a85c-0ad91c5afe63)

## Introduction

Planning a vacation in Honolulu, Hawaii? Understanding the climate can be crucial for a memorable trip. This README outlines the steps taken to conduct a climate analysis of the area using Python and SQLAlchemy.

## Part 1: Analyze and Explore the Climate Data

In this section, the goal is to perform basic climate analysis and data exploration using Python, SQLAlchemy ORM queries, Pandas, and Matplotlib. Here's what was done:

### Precipitation Analysis

- Retrieve the previous 12 months of precipitation data.
- Load the data into a Pandas DataFrame and plot the results.
- Print summary statistics for the precipitation data.

### Station Analysis

- Calculate the total number of stations in the dataset.
- Identify the most active stations based on observation counts.
- Retrieve temperature data for the most active station for the previous year.
- Plot the temperature observations as a histogram.

## Part 2: Designing My Climate App

With the initial analysis completed, the next step is to design a Flask API based on the developed queries. Here are the routes created:

- **`"/"`**: Start at the homepage, listing all available routes.
- **`"/api/v1.0/precipitation"`**: Convert the precipitation analysis results into a JSON representation.
- **`"/api/v1.0/stations"`**: Return a JSON list of weather stations.
- **`"/api/v1.0/tobs"`**: Query temperature observations for the previous year from the most active station and return as JSON.
- **`"/api/v1.0/<start>"` and `"/api/v1.0/<start>/<end>"`**: Return JSON-formatted temperature statistics (min, avg, max) for a specified date or date range.

## Usage

- Clone this repository to your local machine.
- Ensure you have Python, Flask, and the required dependencies installed.
- Run the Flask application using `python app.py`.
- Access the routes mentioned above to retrieve climate data.

Now, with this information at hand, enjoy planning your vacation in beautiful Honolulu, Hawaii! 🏝️🌞
