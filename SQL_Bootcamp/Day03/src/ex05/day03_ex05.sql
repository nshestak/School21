SELECT pizzeria.name AS pizzeria_name
FROM person_visits
         FULL JOIN person_order ON person_order.order_date = person_visits.visit_date
         JOIN person ON person.id = person_visits.person_id
         JOIN pizzeria ON pizzeria.id = person_visits.pizzeria_id
WHERE person.name = 'Andrey'
  AND person_order.id IS NULL
ORDER BY pizzeria_name;
