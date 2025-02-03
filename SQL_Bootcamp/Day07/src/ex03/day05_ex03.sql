SELECT total_1.name, COALESCE(total_1.count, 0) + COALESCE(total_2.count, 0) AS total_count
FROM (SELECT pizzeria.name, COUNT(*) AS "count"
      FROM person_visits
               INNER JOIN pizzeria ON pizzeria.id = person_visits.pizzeria_id
      GROUP BY pizzeria.name) AS total_1
         FULL JOIN
     (SELECT pizzeria.name, COUNT(*) AS "count"
      FROM person_order
               INNER JOIN menu ON person_order.menu_id = menu.id
               INNER JOIN pizzeria ON menu.pizzeria_id = pizzeria.id
      GROUP BY pizzeria.name) AS total_2 ON total_1.name = total_2.name
ORDER BY total_count DESC, total_1.name;