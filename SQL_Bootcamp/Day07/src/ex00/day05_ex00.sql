SELECT person_visits.person_id, COUNT(*) AS count_of_visits
FROM person_visits
GROUP BY person_visits.person_id
ORDER BY count_of_visits DESC, person_visits.person_id;