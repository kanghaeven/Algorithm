SELECT PRODUCT_CODE, PRICE * SUM(sales_amount) SALES FROM PRODUCT P
JOIN OFFLINE_SALE O
ON P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY 2 DESC, 1;