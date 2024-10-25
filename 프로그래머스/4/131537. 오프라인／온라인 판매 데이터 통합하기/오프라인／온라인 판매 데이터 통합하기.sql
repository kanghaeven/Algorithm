select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from ONLINE_SALE
where SALES_DATE like '2022-03%'
union
select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT
from OFFLINE_SALE
where SALES_DATE like '2022-03%'
order by 1, 2, 3;