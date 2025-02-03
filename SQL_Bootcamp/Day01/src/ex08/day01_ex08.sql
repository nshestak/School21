SELECT _order.order_date,
       concat(name, ' (age:', age, ')') AS person_information
FROM person
         NATURAL JOIN (SELECT person_id AS id, order_date FROM person_order) AS _order
ORDER BY _order.order_date, person.name;