SELECT menu.pizza_name,
       menu.price,
       pizzeria.name AS pizzeria_name,
       person_visits.visit_date
FROM person_visits
         JOIN menu ON person_visits.pizzeria_id = menu.pizzeria_id
         JOIN person ON person_visits.person_id = person.id
         JOIN pizzeria ON person_visits.pizzeria_id = pizzeria.id
WHERE person.name = 'Kate'
  AND price >= 800
  AND price <= 1000
ORDER BY 1, 2, 3;