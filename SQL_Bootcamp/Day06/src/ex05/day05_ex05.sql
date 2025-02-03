COMMENT ON TABLE person_discounts IS 'Discounts for persons';
COMMENT ON COLUMN person_discounts.id IS 'Primary key';
COMMENT ON COLUMN person_discounts.person_id IS 'The identifier of the person in the order';
COMMENT ON COLUMN person_discounts.pizzeria_id IS 'The identifier of the pizzeria where the order was placed';
COMMENT ON COLUMN person_discounts.discount IS 'Discount value is calculated based on the number of orders';