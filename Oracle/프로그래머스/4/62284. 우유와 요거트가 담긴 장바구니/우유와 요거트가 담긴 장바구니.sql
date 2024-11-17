-- 코드를 입력하세요
SELECT CART_ID
FROM (
        SELECT CART_ID, COUNT(CART_ID)
        FROM (
                SELECT CART_ID, NAME
                FROM CART_PRODUCTS
                WHERE NAME = 'Milk'

                UNION

                SELECT CART_ID, NAME
                FROM CART_PRODUCTS
                WHERE NAME = 'Yogurt'
            )
        GROUP BY CART_ID
        HAVING COUNT(CART_ID) = 2
)
ORDER BY CART_ID





-- SELECT CART_ID, COUNT(CART_ID)
-- FROM (
--     SELECT CART_ID, NAME
--     FROM CART_PRODUCTS
--     WHERE NAME = 'Milk'

--     UNION

--     SELECT CART_ID, NAME
--     FROM CART_PRODUCTS
--     WHERE NAME = 'Yogurt'
-- )
-- GROUP BY CART_ID
-- HAVING COUNT(CART_ID) = 2



-- SELECT CART_ID, NAME
-- FROM CART_PRODUCTS
-- WHERE NAME = 'Milk'

-- UNION

-- SELECT CART_ID, NAME
-- FROM CART_PRODUCTS
-- WHERE NAME = 'Yogurt'