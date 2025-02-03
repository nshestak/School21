SELECT
    (SELECT person.name FROM person WHERE id = po.person_id) AS NAME
FROM
    person_order po
WHERE
    (menu_id = 13 OR menu_id = 14 OR menu_id = 18)
AND
    order_date = '2022-01-07';