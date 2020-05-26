SELECT DISTINCT(CITY) FROM STATION
WHERE REVERSE(CITY) REGEXP ("^[aeiou]");

--https://www.hackerrank.com/challenges/weather-observation-station-7/problem