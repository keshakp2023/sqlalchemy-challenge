# Import the dependencies.
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify
import pandas as pd
import datetime as dt

#################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#################################################

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


# Save references to each table

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#/api/v1.0/precipitation
@app.route("/")
def home():
    # """List of all available routes"""
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine) 

    #retrieve only the last 12 months of data

    previous_year = dt.datetime(2017,8,23) - dt.timedelta(days= 365)

    query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= previous_year).all()    
   
    session.close()

    # return jsonify(dict(query))

    prcp_dict= {}
    for date,prcp in query:
        prcp_dict[date]= prcp
    return jsonify(prcp_dict)
        
#Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine) 

    session.query(Measurement.station).distinct().count()
    most_active_stations = session.query(Measurement.station,func.count(Measurement.station)).\
                               group_by(Measurement.station).\
                               order_by(func.count(Measurement.station).desc()).all()
    
    session.close()

    return jsonify(dict(most_active_stations))

#Query the dates and temperature observations of the most-active station for the previous year of data.

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine) 

    previous_year= dt.datetime(2017,8,23) - dt.timedelta(days= 365)
    most_active = session.query(Measurement.tobs).\
                            filter(Measurement.station == 'USC00519281').\
                            filter(Measurement.date >= previous_year).all()
    session.close()
    
    temp = list(np.ravel(most_active))

    return jsonify(temp)

#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start 
@app.route("/api/v1.0/<start>")
def start_range(start):
    session = Session(engine) 

    start = dt.datetime.strptime(start, "%Y%m%d")
    start_temp_status = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
                     filter(Measurement.date>= start).all ()

    session.close()

    start_dic = {}
    for X, Y, Z in start_temp_status:
        start_dic ['min'] = X   
        start_dic ['max'] = Y
        start_dic ['avg'] = Z
    return jsonify(start_dic)


#specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

@app.route("/api/v1.0/<start>/<end>")
def start_end_range(start,end):
    session = Session(engine)

    start = dt.datetime.strptime(start, "%Y%m%d")  
    end = dt.datetime.strptime(end, "%Y%m%d") 

    start_end_temp_status = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
                     filter(Measurement.date >= start).\
                     filter(Measurement.date <= end).all()
    session.close()


    start_end_dic = {}
    for X, Y, Z in start_end_temp_status:
        start_end_dic ['min'] = X   
        start_end_dic ['max'] = Y
        start_end_dic ['avg'] = Z
    return jsonify(start_end_dic)

#################################################
# Flask Routes
#################################################
if __name__ == "__main__":
    app.run(debug=True)
