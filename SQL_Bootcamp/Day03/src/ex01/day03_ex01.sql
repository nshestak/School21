SELECT menu.id
FROM menu
WHERE NOT EXISTS
    (SELECT menu_id FROM person_order WHERE menu_id = menu.id)
ORDER BY 1;