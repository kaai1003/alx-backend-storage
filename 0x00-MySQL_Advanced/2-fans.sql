-- ranks country origins of bands
-- ordered by the number of (non-unique) fans
SELECT origin, SUM(FANS) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY SUM(fans) DESC;
