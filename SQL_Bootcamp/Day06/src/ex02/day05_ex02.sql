SELECT person.name,
       menu.pizza_name,
       menu.price,
       ROUND(menu.price - (menu.price * person_discounts.discount/100)) as discount_price,
       pizzeria.name                                                  as pizzeria_name
FROM person_order
         INNER JOIN menu ON person_order.menu_id = menu.id
         INNER JOIN pizzeria ON pizzeria.id = menu.pizzeria_id
         INNER JOIN person_discounts
              ON person_discounts.pizzeria_id = pizzeria.id AND person_order.person_id = person_discounts.person_id
         INNER JOIN person ON person.id = person_discounts.person_id
ORDER BY person.name, menu.pizza_name;
