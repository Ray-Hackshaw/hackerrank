SELECT DISTINCT CITY FROM STATION
WHERE CITY NOT REGEXP("^[aeiou].*[aeiou]$");


--Opted for cleaner regex expression this time round.
--https://www.hackerrank.com/challenges/weather-observation-station-11/problem