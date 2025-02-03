WITH menu_id_cte AS (SELECT *
                     FROM menu
                     WHERE NOT EXISTS
                                   (SELECT menu_id FROM person_order WHERE menu_id = menu.id))
SELECT menu_id_cte.pizza_name, menu_id_cte.price, pizzeria.name AS pizzeria_name
FROM menu_id_cte
    INNER JOIN pizzeria ON menu_id_cte.pizzeria_id = pizzeria.id
ORDER BY pizza_name, price;