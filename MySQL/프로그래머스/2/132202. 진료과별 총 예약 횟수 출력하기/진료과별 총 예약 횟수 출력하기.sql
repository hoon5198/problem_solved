SELECT MCDP_CD as '진료과 코드',count(MCDP_CD) as '5월예약건수'
FROM appointment
where MONTH(APNT_YMD) = 5
group by MCDP_CD
order by count(mcdp_cd),mcdp_cd;