-- Session #1
BEGIN;
-- Session #2
BEGIN;
-- Session #1
UPDATE pizzeria SET rating = 3 WHERE id = 1;
-- Session #2
UPDATE pizzeria SET rating = 2 WHERE id = 2;
-- Session #1
UPDATE pizzeria SET rating = 3 WHERE id = 2;
-- Session #2
UPDATE pizzeria SET rating = 2 WHERE id = 1;
-- Session #1
COMMIT;ERROR: deadlock detected
-- Session #2
COMMIT;
-- Session #1
SELECT * FROM pizzeria;
-- Session #2
SELECT * FROM pizzeria;