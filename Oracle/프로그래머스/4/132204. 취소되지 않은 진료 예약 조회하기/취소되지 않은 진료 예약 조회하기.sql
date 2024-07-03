-- 코드를 입력하세요
-- SELECT T.APNT_NO, P.PT_NAME, T.PT_NO, T.MCDP_CD, T.DR_NAME, 
--                         TO_CHAR(T.APNT_YMD,'YYYY-MM-DD HH24:MI:SS.FF') AS APNT_YMD
-- FROM PATIENT P (SELECT A.APNT_NO, D.MCDP_CD, D.DR_NAME,A.APNT_YMD,A.PT_NO,A.APNT_CNCL_YN
--                 FROM APPOINTMENT A JOIN DOCTOR D
--                 ON A.MDDR_ID = D.DR_ID 
--                 WHERE TO_CHAR(A.APNT_YMD,'YYYYMMDD') = '20220413') T
-- WHERE P.PT_NO = T.PT_NO AND T.MCDP_CD = 'CS' AND T.APNT_CNCL_YN = 'N'
-- ORDER BY T.APNT_YMD


SELECT P.APNT_NO, P.PT_NAME, P.PT_NO, MCDP_CD, D.DR_NAME, P.APNT_YMD
FROM
(
    SELECT P.PT_NO, P.PT_NAME, A.MDDR_ID, A.APNT_NO, A.APNT_YMD, A.APNT_CNCL_YN
    FROM PATIENT P
    JOIN APPOINTMENT A
    ON P.PT_NO = A.PT_NO
    WHERE A.MCDP_CD = 'CS'
) P
JOIN DOCTOR D 
ON  P.MDDR_ID = D.DR_ID
WHERE P.APNT_YMD BETWEEN TO_DATE('2022-4-13','YYYY-MM-DD') AND TO_DATE('2022-4-14','YYYY-MM-DD') 
AND P.APNT_CNCL_YN = 'N'
ORDER BY APNT_YMD ASC;