WITH name_and_price_cte AS
         (SELECT menu.pizza_name, menu.price, pizzeria.name, pizzeria.id
          FROM menu
                   JOIN pizzeria ON pizzeria.id = menu.pizzeria_id)

SELECT P1.pizza_name, P2.name AS pizza_name_1, P1.name AS pizza_name_2, P1.price
FROM name_and_price_cte P1
         JOIN name_and_price_cte P2 ON P2.pizza_name = P1.pizza_name
WHERE P2.id > P1.id
  AND P2.price = P1.price
ORDER BY 1;