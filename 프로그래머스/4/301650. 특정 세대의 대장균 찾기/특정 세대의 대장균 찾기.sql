SELECT C.ID
FROM ECOLI_DATA AS A
JOIN ECOLI_DATA AS B ON A.ID = B.PARENT_ID AND A.PARENT_ID IS NULL
JOIN ECOLI_DATA AS C ON B.ID = C.PARENT_ID
ORDER BY 1;