SELECT (CASE WHEN p.id = pv.person_id THEN p.name ELSE 'unknown' END ) AS person_name,
        (CASE WHEN pz.id = pv.pizzeria_id THEN pz.name ELSE 'unknown' END ) AS pizzeria_name
FROM person p,pizzeria pz,(SELECT person_id, pizzeria_id FROM person_visits WHERE visit_date >= '2022-01-07' AND visit_date <= '2022-01-09') AS pv
WHERE pz.id = pv.pizzeria_id AND p.id = pv.person_id
ORDER BY person_name, pizzeria_name DESC;
