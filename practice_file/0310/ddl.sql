# 항공사별 공항 MAP 관련 쿼리
SELECT 항공사코드 FROM db_air2.`비행` GROUP BY 1;

select a.항공사코드, a.출발공항코드, a.도착지공항코드, air.위도, air.경도
from db_air2.`비행` as a
join db_air2.`항공사` as air
ON (a.`출발공항코드` = air.항공사코드)
WHERE a.`항공사코드` = 'AA'
GROUP BY 2;