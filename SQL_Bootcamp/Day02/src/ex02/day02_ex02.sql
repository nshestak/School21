SELECT COALESCE(person.name, '-')           AS person_name,
       person_visit_by_date.visit_date AS visit_date,
       COALESCE(pizzeria.name, '-')           AS pizzeria_name
FROM (SELECT * FROM person_visits WHERE visit_date BETWEEN '2022-01-01' AND '2022-01-03') AS person_visit_by_date
         FULL JOIN person
                   ON person_visit_by_date.person_id = person.id
         FULL JOIN pizzeria
                   ON pizzeria.id = person_visit_by_date.pizzeria_id
ORDER BY person_name, visit_date, pizzeria_name;
