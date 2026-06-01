Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. 
Truncate your answer to  decimal places.


select cast(round(max(LAT_N),4) as decimal(10,4)) from STATION WHERE LAT_N<137.2345;
