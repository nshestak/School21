UPDATE menu
SET price = price - price * 0.1
WHERE pizza_name = 'greek pizza';

-- SELECT * FROM menu
-- WHERE pizza_name = 'greek pizza'
-- ORDER BY id;