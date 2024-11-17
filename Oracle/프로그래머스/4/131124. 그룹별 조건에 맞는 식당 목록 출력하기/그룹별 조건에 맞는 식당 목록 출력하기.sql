-- 코드를 입력하세요

-- SELECT A.MEMBER_NAME, B.REVIEW_TEXT, TO_CHAR(B.REVIEW_DATE,'YYYY-MM-DD') AS REVIEW_DATE
-- FROM (SELECT MEMBER_NAME,MEMBER_ID 
--       FROM MEMBER_PROFILE
--       WHERE MEMBER_ID IN (SELECT MEMBER_ID 
--                           FROM REST_REVIEW
--                           GROUP BY MEMBER_ID 
--                           HAVING COUNT(MEMBER_ID) = (SELECT DISTINCT COUNT 
--                                                      FROM (SELECT MEMBER_ID, COUNT(MEMBER_ID) AS COUNT
--                                                            FROM REST_REVIEW
--                                                            GROUP BY MEMBER_ID
--                                                            ORDER BY COUNT DESC)
--                                                      WHERE ROWNUM = 1))) A 
--         LEFT OUTER JOIN REST_REVIEW B ON A.MEMBER_ID = B.MEMBER_ID
-- ORDER BY REVIEW_DATE, REVIEW_TEXT


-- 빈도수 많은 멤버 이름..!
-- SELECT MEMBER_NAME
-- FROM MEMBER_PROFILE
-- WHERE MEMBER_ID IN (SELECT MEMBER_ID FROM REST_REVIEW
-- GROUP BY MEMBER_ID
-- HAVING COUNT(MEMBER_ID) = ( SELECT DISTINCT COUNT FROM ( SELECT MEMBER_ID, COUNT(MEMBER_ID) AS COUNT
--                                                         FROM REST_REVIEW
--                                                         GROUP BY MEMBER_ID
--                                                         ORDER BY COUNT DESC)
--                             WHERE ROWNUM = 1))

-- 빈도수와 해당 빈도수에 해당하는 MEMBER_ID
-- SELECT MEMBER_ID , COUNT(MEMBER_ID) AS CNT_MEMB
-- SELECT MEMBER_ID
-- FROM REST_REVIEW
-- GROUP BY MEMBER_ID
-- HAVING COUNT(MEMBER_ID) = ( SELECT DISTINCT COUNT FROM ( SELECT MEMBER_ID, COUNT(MEMBER_ID) AS COUNT
--                                                         FROM REST_REVIEW
--                                                         GROUP BY MEMBER_ID
--                                                         ORDER BY COUNT DESC)
--                             WHERE ROWNUM = 1)


-- SELECT DISTINCT COUNT
-- FROM (
--     SELECT MEMBER_ID, COUNT(MEMBER_ID) AS COUNT
--     FROM REST_REVIEW
--     GROUP BY MEMBER_ID
--     ORDER BY COUNT DESC
-- )
-- WHERE ROWNUM = 1


-- 각 멤버별 등장 횟수
-- SELECT MEMBER_ID, COUNT(MEMBER_ID) AS COUNT
-- FROM REST_REVIEW
-- GROUP BY MEMBER_ID
-- ORDER BY COUNT DESC

SELECT MP.MEMBER_NAME, RR.REVIEW_TEXT, TO_CHAR(RR.REVIEW_DATE, 'YYYY-MM-DD') AS REVIEW_DATE
FROM REST_REVIEW RR
JOIN MEMBER_PROFILE MP ON RR.MEMBER_ID = MP.MEMBER_ID
WHERE RR.MEMBER_ID = (
    SELECT MEMBER_ID
    FROM (
        SELECT MEMBER_ID
        FROM REST_REVIEW
        GROUP BY MEMBER_ID
        ORDER BY COUNT(*) DESC
    )
    WHERE ROWNUM = 1
)
ORDER BY RR.REVIEW_DATE ASC, RR.REVIEW_TEXT ASC;