-- 코드를 입력하세요
SELECT A.CATEGORY, SUM(B.SALES) FROM BOOK AS A
INNER
JOIN BOOK_SALES AS B
ON A.BOOK_ID = B.BOOK_ID
WHERE YEAR(B.SALES_DATE) = 2022 AND MONTH(B.SALES_DATE) = 1
GROUP BY CATEGORY
ORDER BY A.CATEGORY