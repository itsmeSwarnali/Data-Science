Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. 
Your result cannot contain duplicates.



select distinct city from station where upper(left(city,1)) not in ('A', 'E', 'I', 'O', 'U') AND 
upper(right(city,1)) not in ('A', 'E', 'I', 'O', 'U');
