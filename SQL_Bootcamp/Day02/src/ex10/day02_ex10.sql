SELECT person_1.name, person_2.name, person_1.address as common_address
FROM person AS person_1
         INNER JOIN person AS person_2 ON person_1.id > person_2.id AND person_1.address = person_2.address
ORDER BY 1, 2, 3