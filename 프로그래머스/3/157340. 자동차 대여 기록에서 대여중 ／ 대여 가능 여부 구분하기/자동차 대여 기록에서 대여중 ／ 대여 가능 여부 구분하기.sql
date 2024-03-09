SELECT CAR_ID,
    MAX(CASE WHEN "2022-10-16" BETWEEN START_DATE AND END_DATE THEN "대여중"
    WHEN END_DATE = "2022-10-16" THEN "대여중"
    ELSE "대여 가능"
    END) AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;