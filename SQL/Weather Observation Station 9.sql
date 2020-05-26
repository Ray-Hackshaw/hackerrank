SELECT DISTINCT(CITY) FROM STATION
WHERE CITY NOT REGEXP("^[aeiou]");

--Definitely a way to do this with proper regex OR using consonants list instead?
--https://www.hackerrank.com/challenges/weather-observation-station-9/problem