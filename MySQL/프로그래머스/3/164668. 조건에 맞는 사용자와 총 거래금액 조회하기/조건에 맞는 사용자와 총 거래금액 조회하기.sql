-- 코드를 입력하세요
SELECT ugu.user_id, ugu.nickname, sum(ugb.price)
from used_goods_user as ugu
join used_goods_board as ugb on ugu.user_id = ugb.writer_id
where ugb.status = 'DONE'
group by ugu.user_id
having sum(ugb.price) >= 700000
order by sum(ugb.price);