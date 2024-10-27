select i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, round(avg(r.REVIEW_SCORE), 2) as SCORE 
from rest_info as i
join REST_REVIEW as r
on i.rest_id = r.rest_id
where ADDRESS like '서울%'
group by rest_name
order by score desc, favorites desc;