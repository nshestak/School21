SELECT days::DATE AS missing_date
FROM generate_series('2022-01-01', '2022-01-10', interval '1 day') AS days
         FULL JOIN
     (SELECT *
      FROM person_visits
      WHERE person_visits.person_id = 1
         OR person_visits.person_id = 2
          AND person_visits.visit_date BETWEEN '2022-01-01' AND '2022-01-10') AS date
     ON days = date.visit_date
WHERE date.person_id ISNULL
ORDER BY days;