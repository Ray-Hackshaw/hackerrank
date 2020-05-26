SELECT DISTINCT(CITY) FROM STATION
WHERE CITY REGEXP("^[aeiou]") AND CITY REGEXP("[aeiou]$");

--REGEXP("^[aeiou].*[aeiou]$")
--More compact version

--https://www.hackerrank.com/challenges/weather-observation-station-8/problem