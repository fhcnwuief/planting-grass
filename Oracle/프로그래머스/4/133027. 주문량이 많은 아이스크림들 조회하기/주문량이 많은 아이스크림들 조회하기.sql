-- 코드를 입력하세요
-- SELECT  FLAVOR
--   FROM  (
--             SELECT  H.FLAVOR
--                  ,  H.TOTAL_ORDER + J.ORDER_SUM AS TOTAL_SUM
--               FROM  FIRST_HALF  H
--                  ,  (
--                         SELECT  FLAVOR
--                              ,  SUM(TOTAL_ORDER) AS ORDER_SUM
--                           FROM  JULY
--                          GROUP BY FLAVOR
--                          ORDER BY FLAVOR
--                     )           J
--              WHERE  H.FLAVOR    = J.FLAVOR
--              ORDER BY TOTAL_SUM DESC
--         )
--  WHERE  ROWNUM <= 3



SELECT FLAVOR
FROM (  SELECT A.FLAVOR, (A.TOTAL_ORDER + B.TOTAL_ORDER) AS SUM_RESULT
        FROM FIRST_HALF A LEFT OUTER JOIN ( SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
                                            FROM JULY
                                            GROUP BY FLAVOR ) B
        ON A.FLAVOR = B.FLAVOR
        
        GROUP BY A.FLAVOR, A.TOTAL_ORDER, B.TOTAL_ORDER
        ORDER BY SUM_RESULT DESC
)
WHERE ROWNUM <= 3


-- SELECT A.FLAVOR, (A.TOTAL_ORDER + B.TOTAL_ORDER) AS SUM_RESULT
-- FROM FIRST_HALF A LEFT OUTER JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
--                                   FROM JULY
--                                   GROUP BY FLAVOR) B
-- ON A.FLAVOR = B.FLAVOR
-- GROUP BY A.FLAVOR, A.TOTAL_ORDER, B.TOTAL_ORDER
-- ORDER BY SUM_RESULT DESC