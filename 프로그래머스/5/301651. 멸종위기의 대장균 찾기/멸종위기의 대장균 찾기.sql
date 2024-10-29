WITH RECURSIVE CTE AS (
    SELECT ID, PARENT_ID, 1 AS G
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION
    
    SELECT E.ID, E.PARENT_ID, C.G+1
    FROM ECOLI_DATA AS E
    JOIN CTE AS C
    ON E.PARENT_ID = C.ID
)

SELECT COUNT(A.G) AS COUNT, A.G AS GENERATION
FROM CTE AS A
LEFT JOIN CTE AS B
ON A.ID = B.PARENT_ID
WHERE B.G IS NULL
GROUP BY A.G
ORDER BY 2;