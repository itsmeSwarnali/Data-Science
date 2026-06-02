P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).


  
set @row := 21;
select repeat(' *', @row := @row-1)
from information_schema.tables
limit 20;
