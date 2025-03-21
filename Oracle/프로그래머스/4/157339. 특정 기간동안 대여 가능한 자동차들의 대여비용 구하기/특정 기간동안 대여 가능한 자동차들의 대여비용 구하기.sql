-- 코드를 입력하세요
-- SELECT CAR_ID, CAR_TYPE, DAILY_FEE FROM CAR_RENTAL_COMPANY_CAR
-- WHERE CAR_TYPE IN ('세단','SUV')

-- -- 2022년 11월1일부터 2022년 11월 30일까지 대여 가능
-- SELECT *
-- FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- WHERE CAR_ID IN ( SELECT CAR_ID FROM CAR_RENTAL_COMPANY_CAR WHERE CAR_TYPE IN ('세단','SUV'))
-- AND TO_CHAR(END_DATE,'YYYY-MM-DD') < '2022-11-01' OR TO_CHAR(START_DATE,'YYYY-MM-DD') > '2022-11-30'
-- ORDER BY CAR_ID

-- SELECT * FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
-- WHERE CAR_TYPE IN ('세단','SUV')

-- SELECT CAR_ID, CAR_TYPE,DAILY_FEE * (1 - DISCOUNT_RATE * 0.01) * 30 AS FEE
-- FROM (
--     SELECT A.CAR_ID, A.CAR_TYPE, A.DAILY_FEE, B.DURATION_TYPE, B.DISCOUNT_RATE
--     FROM CAR_RENTAL_COMPANY_CAR A, CAR_RENTAL_COMPANY_DISCOUNT_PLAN B
--     WHERE A.CAR_TYPE = B.CAR_TYPE AND A.CAR_TYPE IN ('세단','SUV') AND B.DURATION_TYPE LIKE '30%'
--     AND A.CAR_ID IN (SELECT CAR_ID
--                         FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
--                         WHERE TO_CHAR(END_DATE,'YYYY-MM-DD') < '2022-11-01' 
--                         OR TO_CHAR(START_DATE,'YYYY-MM-DD') > '2022-11-30')
-- )
-- WHERE DAILY_FEE * (1 - DISCOUNT_RATE * 0.01) * 30 BETWEEN 500000 AND 2000000
-- ORDER BY CAR_TYPE, CAR_ID DESC



-- SELECT CAR_ID, CAR_TYPE, DAILY_FEE FROM CAR_RENTAL_COMPANY_CAR
-- WHERE CAR_TYPE IN ('세단','SUV') AND CAR_ID IN (SELECT DISTINCT CAR_ID
--                                                 FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
--                                                 WHERE CAR_ID IN ( SELECT CAR_ID
--                                                                   FROM CAR_RENTAL_COMPANY_CAR
--                                                                  WHERE CAR_TYPE IN ('세단','SUV'))
--                                                                     AND TO_CHAR(END_DATE,'YYYY-MM-DD') < '2022-11-01' 
--                                                                     OR TO_CHAR(START_DATE,'YYYY-MM-DD') > '2022-11-30'
--                                             )

SELECT  B.CAR_ID, A.CAR_TYPE, B.DAILY_FEE * (1 - A.DISCOUNT_RATE * 0.01) * 30 AS FEE
FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN A 

LEFT OUTER JOIN 

CAR_RENTAL_COMPANY_CAR B 

ON A.CAR_TYPE = B.CAR_TYPE

WHERE  A.CAR_TYPE IN ('세단','SUV') AND A.DURATION_TYPE = '30일 이상'
AND B.CAR_ID IN (SELECT CAR_ID 
               FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
               WHERE CAR_ID NOT IN ( SELECT  A.CAR_ID
                                          FROM  CAR_RENTAL_COMPANY_CAR              A
                                             ,  CAR_RENTAL_COMPANY_RENTAL_HISTORY   B
                                         WHERE  A.CAR_ID = B.CAR_ID
                                           AND  A.CAR_TYPE IN ('세단', 'SUV')
                                           AND  TO_CHAR(B.END_DATE, 'YYYYMMDD') >= '20221101'
                                           AND  TO_CHAR(B.START_DATE, 'YYYYMMDD') < '20221201'
                                    )
                 )
AND B.DAILY_FEE * (1 - A.DISCOUNT_RATE * 0.01) * 30 BETWEEN 500000 AND 2000000
ORDER BY FEE DESC, A.CAR_TYPE, B.CAR_ID DESC