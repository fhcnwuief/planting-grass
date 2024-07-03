-- 코드를 입력하세요
-- SELECT A.REST_ID,B.REST_NAME,B.FOOD_TYPE,B.FAVORITES,B.ADDRESS,A.SCORE
-- FROM (SELECT REST_ID, ROUND(AVG(REVIEW_SCORE),2) AS SCORE 
--       FROM REST_REVIEW
--       WHERE REST_ID IN (SELECT REST_ID FROM REST_INFO WHERE ADDRESS LIKE '%서울%')
--       GROUP BY REST_ID
--       ORDER BY REST_ID) A, REST_INFO B
-- WHERE A.REST_ID = B.REST_ID
-- ORDER BY SCORE DESC, B.FAVORITES DESC

SELECT  I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, R.SCORE
FROM    REST_INFO I, 
        (SELECT REST_ID, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
         FROM   REST_REVIEW
         GROUP BY REST_ID) R
WHERE   1=1
AND     I.REST_ID=R.REST_ID
AND     I.ADDRESS LIKE '서울%'
ORDER BY R.SCORE DESC, I.FAVORITES DESC