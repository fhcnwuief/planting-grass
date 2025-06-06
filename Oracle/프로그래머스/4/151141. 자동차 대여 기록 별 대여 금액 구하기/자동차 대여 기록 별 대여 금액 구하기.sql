-- 코드를 입력하세요

-- SELECT * FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
-- WHERE CAR_TYPE = '트럭'

-- SELECT * FROM CAR_RENTAL_COMPANY_CAR
-- WHERE CAR_TYPE = '트럭'

-- SELECT HISTORY_ID, CAR_ID, TO_CHAR(START_DATE,'YYYY-MM-DD') START_DATE, TO_CHAR(END_DATE,'YYYY-MM-DD') END_DATE,
-- TO_NUMBER(END_DATE - START_DATE) + 1 DURATE
-- FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
-- WHERE CAR_ID IN (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_CAR WHERE CAR_TYPE = '트럭')

-- SELECT HISTORY_ID, CASE WHEN DURATE >= 7 THEN DAILY_FEE * 0.05 * DURATE
--                      WHEN DURATE >= 30 THEN DAILY_FEE * 0.08 * DURATE
--                      WHEN DURATE >= 90 THEN DAILY_FEE * 0.15 * DURATE
--                     ELSE DAILY_FEE * DURATE END AS FEE
-- FROM (
-- SELECT A.CAR_ID, A.CAR_TYPE, A.DAILY_FEE, B.HISTORY_ID,
-- TO_NUMBER(B.END_DATE - B.START_DATE) + 1 DURATE
-- FROM CAR_RENTAL_COMPANY_CAR A, CAR_RENTAL_COMPANY_RENTAL_HISTORY B
-- WHERE A.CAR_ID = B.CAR_ID AND A.CAR_TYPE = '트럭'
--     )
-- ORDER BY FEE DESC, HISTORY_ID DESC

-- SELECT CAR_TYPE, DISCOUNT_RATE * 0.01 DISCOUNT_RATE , REGEXP_REPLACE(DURATION_TYPE, '[^0-9]') AS NEW_DURATION_TYPE
-- FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
-- WHERE CAR_TYPE = '트럭'



SELECT 
    HISTORY_ID, 
    CASE 
        WHEN DURATE >= 90 THEN DAILY_FEE * 0.85 * DURATE  -- 15% 할인
        WHEN DURATE >= 30 THEN DAILY_FEE * 0.92 * DURATE  -- 8% 할인
        WHEN DURATE >= 7 THEN DAILY_FEE * 0.95 * DURATE   -- 5% 할인
        ELSE DAILY_FEE * DURATE 
    END AS FEE
FROM (
    SELECT 
        A.CAR_ID, 
        A.CAR_TYPE, 
        A.DAILY_FEE, 
        B.HISTORY_ID,
        (B.END_DATE - B.START_DATE) + 1 AS DURATE
    FROM 
        CAR_RENTAL_COMPANY_CAR A, 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY B
    WHERE 
        A.CAR_ID = B.CAR_ID 
        AND A.CAR_TYPE = '트럭'
)
ORDER BY 
    FEE DESC, 
    HISTORY_ID DESC;