-- 코드를 입력하세요
SELECT warehouse_id,warehouse_name,address,IFNULL(freezer_yn,'N') as FREEZER_YN
FROM food_warehouse
WHERE ADDRESS like '%경기%'
ORDER BY warehouse_id asc;