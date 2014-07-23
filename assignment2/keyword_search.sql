SELECT MAX(sim) FROM (
SELECT f1.docid, SUM(f1.count * f2.count) as sim
  FROM (SELECT docid, term, count
          FROM frequency
         UNION
        SELECT 'q' as docid, 'washington' as term, 1 as count
         UNION
        SELECT 'q' as docid, 'taxes' as term, 1 as count
         UNION
        SELECT 'q' as docid, 'treasury' as term, 1 as count
       ) f1
  JOIN (SELECT docid, term, count
          FROM frequency
         UNION
        SELECT 'q' as docid, 'washington' as term, 1 as count
         UNION
        SELECT 'q' as docid, 'taxes' as term, 1 as count
         UNION
        SELECT 'q' as docid, 'treasury' as term, 1 as count
       ) f2 ON f1.term = f2.term
 WHERE f2.docid = 'q'
 GROUP BY f1.docid
) x;
