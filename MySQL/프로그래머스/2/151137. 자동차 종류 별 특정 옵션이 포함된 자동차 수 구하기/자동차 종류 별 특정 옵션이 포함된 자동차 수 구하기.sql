SELECT car_type as cars ,count(car_type) as cars
FROM car_rental_company_car
WHERE options LIKE '%통풍시트%'
   OR options LIKE '%열선시트%'
   OR options LIKE '%가죽시트%'
group by car_type
order by car_type;