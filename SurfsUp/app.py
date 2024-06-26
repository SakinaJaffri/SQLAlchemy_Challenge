
import datetime as dt  # For handling date and time operations.
from sqlalchemy.ext.automap import automap_base  # For reflecting database tables.
from sqlalchemy.orm import Session  # For database session management.
from sqlalchemy import create_engine, func  # For database connection and query functions.
from flask import Flask, jsonify  # For creating a Flask application and JSON serialization.



#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__) # Initializes Flask application.

# #################################################
# # Flask Routes
# #################################################
@app.route("/")
def home():  # Handles home route.
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
        )

# Defines route for precipitation data.
# Handles precipitation route.
# Queries precipitation data for last 12 months and returns JSON representation.

@app.route("/api/v1.0/precipitation")
def precipitation():

    results = session.query(Measurement.date, Measurement.prcp).\
              filter(Measurement.date > (dt.date(2017,8,23)-dt.timedelta(days=365))).all()
    
    output=[]

    for date, prcp in results:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['prcp'] = prcp
        output.append(prcp_dict)

    return jsonify(output)

# Defines route for weather stations.
# Handles stations route.
# Queries weather stations and returns their IDs as JSON list.
@app.route("/api/v1.0/stations")
def stations():

    results = session.query(Station.station).all()
    
    output=[]

    for record in results:
        output.append(record.station)

    return jsonify(output)

# Defines route for temperature observations.
# Handles temperature observations route.
# Queries temperature observations for previous year from most active station.

@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(Measurement.date, Measurement.tobs).\
              filter(Measurement.date.between('2016-01-01', '2016-12-31')).\
              filter(Measurement.station=='USC00519281').all()
    
    output= []

    for date,tobs in results:
        tobs_dict = {}
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tobs
        output.append(tobs_dict)
        
    return jsonify(output)

# Defines route for temperature stats from start date.
# Handles temperature stats route with start date.
# Queries temperature statistics (min, avg, max) from specified start date onwards.

@app.route("/api/v1.0/<start>")
def start_date(start):

    try:
        start_date = dt.datetime.strptime(start, "%Y-%m-%d")

        results = session.query(Measurement.date, func.max(Measurement.tobs),
                                func.min(Measurement.tobs),func.avg(Measurement.tobs)).\
                                group_by(Measurement.date).\
                                filter(Measurement.date >= start_date - dt.timedelta(days=1)).all()
        
        output = []
        for date, TMAX , TMIN, TAVG in results:
            start_date_dict = {}
            start_date_dict['date'] = date
            start_date_dict['TMAX '] = TMAX 
            start_date_dict['TMIN'] = TMIN
            start_date_dict['TAVG'] = TAVG
            output.append(start_date_dict)

        return jsonify(output)

    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 400

# Defines route for temperature stats in date range.
# Handles temperature stats route with date range.
# Queries temperature statistics (min, avg, max) for specified date range.

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):

    try:
        start_date = dt.datetime.strptime(start, "%Y-%m-%d")
        end_date = dt.datetime.strptime(end, "%Y-%m-%d")

        results = session.query(Measurement.date, func.max(Measurement.tobs),
                                func.min(Measurement.tobs),func.avg(Measurement.tobs)).\
                                group_by(Measurement.date).\
                                filter(Measurement.date.between(start_date - dt.timedelta(days=1), end_date)).all()
        
        output = []
        for date, TMAX , TMIN, TAVG in results:
            start_end_date_dict = {}
            start_end_date_dict['date'] = date
            start_end_date_dict['TMAX '] = TMAX 
            start_end_date_dict['TMIN'] = TMIN
            start_end_date_dict['TAVG'] = TAVG
            output.append(start_end_date_dict)

        return jsonify(output)
    
    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 400


if __name__ == "__main__":
    app.run(debug=True)
