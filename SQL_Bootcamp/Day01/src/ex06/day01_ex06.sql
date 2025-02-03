SELECT action_date, name AS person_name
FROM person,
     (SELECT order_date AS action_date, person_id
      FROM person_order
      INTERSECT
      SELECT visit_date AS action_date, person_id
      FROM person_visits) AS name_id
WHERE name_id.person_id = person.id
ORDER BY action_date, person_name DESC;