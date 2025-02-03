WITH t AS (
  WITH RECURSIVE _n AS (
    SELECT point1,
           point2,
           cost,
           1 AS level,
           ARRAY[point1]::bpchar[] AS path,
           FALSE AS cycle,
           ARRAY[cost] AS costs
    FROM nodes
    WHERE point1 = 'a'
    UNION
    SELECT nodes.point1,
           nodes.point2,
           nodes.cost + _n.cost AS cost,
           _n.level + 1 AS level,
           _n.path || nodes.point1 AS path,
           nodes.point1 = ANY(_n.path) AS cycle,
           _n.costs || nodes.cost AS costs
    FROM nodes
    INNER JOIN _n ON _n.point2 = nodes.point1
    AND NOT cycle
  )
  SELECT DISTINCT cost - costs[5] AS total_cost,
         path AS tour
  FROM _n
  WHERE level = 5
    AND 'a' = ANY(path)
    AND 'b' = ANY(path)
    AND 'c' = ANY(path)
    AND 'd' = ANY(path)
    AND path[1] = path[5]
  ORDER BY total_cost, tour
)
SELECT total_cost, tour
FROM t;