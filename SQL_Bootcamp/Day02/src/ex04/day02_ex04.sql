SELECT menu.pizza_name, pizzeria.name, menu.price
FROM menu
         INNER JOIN pizzeria on menu.pizzeria_id = pizzeria.id
WHERE pizza_name IN ('mushroom pizza', 'pepperoni pizza')
ORDER BY pizza_name, name;