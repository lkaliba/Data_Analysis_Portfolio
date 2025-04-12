# 📄 SQL Queries – Severe Weather Analysis

```sql
/* Create a table to store the storm data. */
CREATE TABLE severe_weather
(
  episode_id INTEGER,
  event_id INTEGER,
  state STRING,
  state_fips_code INTEGER,
  event_type STRING,
  cz_type STRING,
  cz_fips_code INTEGER,
  cz_name STRING,
  wfo STRING,
  event_begin_time DATETIME,
  event_timezone STRING,
  event_end_time DATETIME,
  injuries_direct INTEGER,
  injuries_indirect INTEGER,
  deaths_direct INTEGER,
  deaths_indirect INTEGER,
  damage_property INTEGER,
  damage_crops INTEGER,
  source STRING,
  magnitude FLOAT,
  magnitude_type STRING,
  flood_cause STRING,
  tor_f_scale STRING,
  tor_length FLOAT,
  tor_width INTEGER, 
  tor_other_wfo STRING,
  location_index INTEGER,
  event_range FLOAT,
  event_azimuth STRING,
  reference_location STRING,
  event_latitude FLOAT,
  event_longitude FLOAT,
  event_point GEOGRAPHY 
);


/* Create a staging area that points to the S3 bucket. */
CREATE OR REPLACE STAGE severe_weather
    url = 's3://severe-weather';


/* List the files in the staging area (S3). */
LIST @severe_weather;


/* Define the format of CSV files to be loaded. */
CREATE OR REPLACE FILE FORMAT csv_format
  type = csv
  field_delimiter = ','
  record_delimiter = '\n'
  skip_header = 1
  null_if = ('')
  field_optionally_enclosed_by = '\042'; 


/* Load the storm data. */
COPY INTO severe_weather
  FROM @severe_weather/severe-weather
  file_format = csv_format;

/* QUERY #1: Who were the top 5 sources of weather data? */

SELECT SOURCE, COUNT(DISTINCT EVENT_ID) AS Num_of_Events
FROM SEVERE_WEATHER
GROUP BY SOURCE
ORDER BY Num_of_Events DESC
LIMIT 5;

/* QUERY #2: What was the total property damage by state and event type? */

SELECT STATE, EVENT_TYPE, SUM(DAMAGE_PROPERTY) AS Total_Property_Damage
FROM SEVERE_WEATHER
WHERE DAMAGE_PROPERTY > 0
GROUP BY STATE, EVENT_TYPE
ORDER BY STATE, EVENT_TYPE;

/* QUERY #3: How many days did the longest event last? */

SELECT EVENT_ID, EVENT_END_TIME, EVENT_BEGIN_TIME, TIMESTAMPDIFF(DAY, EVENT_BEGIN_TIME, EVENT_END_TIME) AS Num_of_Days
FROM SEVERE_WEATHER
ORDER BY Num_of_Days DESC;

/* QUERY #4: Which event was the third storm in Abbeville County, South Carolina? */

SELECT
  STATE,
  CZ_NAME,
  EVENT_TYPE,
  EPISODE_ID,
  DENSE_RANK() OVER (
    PARTITION BY CZ_NAME
    ORDER BY EPISODE_ID
  ) AS EPISODE_SEQUENCE,
  EVENT_BEGIN_TIME
FROM
  SEVERE_WEATHER
WHERE
  CZ_TYPE = 'C'
ORDER BY
  CZ_NAME,
  EPISODE_SEQUENCE;

/* QUERY #5: What was the cumulative damage by month? */

SELECT EXTRACT(MONTH FROM EVENT_BEGIN_TIME) AS "Month", SUM(DAMAGE_PROPERTY) AS Damage,
    SUM(Damage) OVER (
    ORDER BY "Month"
    ROWS UNBOUNDED PRECEDING
    ) Cumulative_Damage
FROM SEVERE_WEATHER
GROUP BY "Month"
ORDER BY "Month";

/* QUERY #6: Which sources are major vs. minor contributors? */

SELECT SOURCE, COUNT(EVENT_ID) AS Num_of_Events,
    CASE
        WHEN Num_of_Events > 2000 THEN 'Major Source'
        ELSE 'Minor Source'
        END AS Source_Category
FROM SEVERE_WEATHER
GROUP BY SOURCE
ORDER BY SOURCE;

/* QUERY #7: Which states had the **highest storm density** (storms per sq. kilometer)? */

WITH sizes_of_states AS (
SELECT STATE_NAME, STATE_FIPS_CODE AS State_Code, ROUND((AREA_LAND_METERS / 1000000), 2) AS Area_Land_Kilometers
FROM STATE_SIZES
),

num_of_storm_events_by_state AS (
SELECT STATE_FIPS_CODE AS State_Code, COUNT(EVENT_ID) AS Num_of_Storm_Events
FROM SEVERE_WEATHER
GROUP BY State_Code
),

state_size_AND_storm_events AS (
SELECT 
s.STATE_NAME, 
n.Num_of_Storm_Events, 
s.Area_Land_Kilometers, 
ROUND((n.Num_of_Storm_Events / s.Area_Land_Kilometers), 2) AS storms_per_square_land_kilo

FROM sizes_of_states s
INNER JOIN num_of_storm_events_by_state n
ON s.State_Code = n.State_Code
ORDER BY storms_per_square_land_kilo
)
SELECT *
FROM state_size_AND_storm_events
ORDER BY storms_per_square_land_kilo DESC;

/* Which state (or territory) had the most storms per square land kilometer?  "District of Columbia" */```
