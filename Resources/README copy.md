# Module 10 Challenge

## Part 1: Analyze and Explore the Climate Data (using a jupyter notebook)

[Module 10 SQL Alchemy Challenge Assistance Video Part 1](https://zoom.us/rec/play/Cut4rS_M1-KVNk1rFGEjfVnrTelPl7scdSDK6sWrzqDW7EhrhA9tP_NUHOSGp0BJfEDcC_iC6XvrzTj9.DA1b5QpcIPlo0i2K?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2FMklUCSgH-AVcGk1YfLF8MljpkMNiD_QMyep3YYu5HcFvQvqWhPsNmi1ssPkn9m2U.zRctHRu8hTdKL1E-)

Use Python and SQLAlchemy to do a basic climate analysis and data exploration of a SQLite climate database. Specifically, use SQLAlchemy ORM queries, Pandas, and Matplotlib to complete the following steps:

* Use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete a climate analysis and data exploration.

* Use the SQLAlchemy create_engine() function to connect to the SQLite database.

* Use the SQLAlchemy automap_base() function to reflect tables (in SQLite) into classes (in Juypter Notebook), and then save references to the classes named station and measurement.

* Link Python to the database by creating a SQLAlchemy session.
  
* Close session at the end of the notebook.

### Perform Precipitation Analysis
1. Find the most recent date in the dataset.

2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data. HINT: Don’t pass the date as a variable to your query.
   
3. Select only the "date" and "prcp" values.

4. Load the query results into a Pandas DataFrame. Explicitly set the column names.

5. Sort the DataFrame values by "date".

6. Plot the results by using the DataFrame plot method, as the following image shows:

![Precipitation in inches for 2016-1017](./Images/precipitation.jpg)

7. Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis
1. Design a query to calculate the total number of stations in the dataset.

2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

    * List the stations and observation counts in descending order. Hint: use the func.count function in your query.
    * Answer the following question: which station id has the greatest number of observations? 
  
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query. Hint: use functions such as func.min, func.max, and func.avg in your query.
   
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
    * Filter by the station that has the greatest number of observations.
    * Query the previous 12 months of TOBS data for that station.
    * Plot the results as a histogram with bins=12, as the following image shows:

![Station Temperature Analysis](./Images/station-histogram.jpg)

5. Close session.
   
## Part 2: Design Your Climate App (using VS Code)

[Module 10 SQL Alchemy Challenge Assistance Video Part 2](https://zoom.us/rec/play/tSyd_AajwuA1SyFkFej9LAUv6tsng2AnTIAvxe56hw9GFE7eGqqNvMnTiCrs7MqLYl8CmiJqqnUrKYyj.b0ZTo7jILUPNzisB?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2Fz3dmRDIFqXJnDu0A2iSwpGh9u_CdCeUvPrzgq6cDkcwiNrIHvf87noAS2fuWxMyb.PutUtXfD4JXd1TCs)

design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

1. / Start at the homepage and List all the available routes.

2. /api/v1.0/precipitation

   * Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

   * Return the JSON representation of your dictionary.

3. /api/v1.0/stations

    * Return a JSON list of stations from the dataset.

4. /api/v1.0/tobs

    * Query the dates and temperature observations of the most-active station for the previous year of data.

    * Return a JSON list of temperature observations for the previous year.

5. /api/v1.0/<start> and /api/v1.0/<start>/<end>

    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

    * For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

    * For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
    * Hints:
      * Join the station and measurement tables for some of the queries.
      * Use the Flask jsonify function to convert your API data to a valid JSON response object.

#### References
[Link to Bootcampspot Instructions for Module 10 Challenge](https://courses.bootcampspot.com/courses/3285/assignments/52213?module_item_id=936335)

[Link to Class Repository: Module 10 Challenge](https://unc.bootcampcontent.com/UNC-Coding-Boot-Camp/UNC-VIRT-DATA-PT-03-2023-U-LOLC/-/tree/main/10-Advanced-SQL/Module_10_Challenge)

[SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)

[Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/)

[Flask: A minimal applicaiton](https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application)

