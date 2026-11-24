SELECT year(ym),round(avg(pm_val1),2),round(avg(pm_val2),2)
FROM air_pollution
where location2 = '수원'
group by year(ym)
order by year(ym);