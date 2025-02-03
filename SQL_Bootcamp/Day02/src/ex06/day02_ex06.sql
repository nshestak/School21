SELECT menu.pizza_name, pizzeria.name
FROM person_order
         INNER JOIN person on person.id = person_order.person_id
         INNER JOIN menu on menu.id = person_order.menu_id
         INNER JOIN pizzeria on menu.pizzeria_id = pizzeria.id
WHERE person.name IN ('Denis', 'Anna')
ORDER BY menu.pizza_name, pizzeria.name;