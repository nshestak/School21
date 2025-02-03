SELECT person.name
FROM person
         INNER JOIN person_order ON person.id = person_order.person_id
         INNER JOIN menu ON person_order.menu_id = menu.id
WHERE person.gender = 'male'
  AND pizza_name IN ('mushroom pizza', 'pepperoni pizza')
  AND person.address IN ('Moscow', 'Samara')
ORDER BY name DESC;