SELECT DISTINCT f1.docid FROM frequency f1 JOIN frequency f2 ON f1.docid = f2.docid WHERE f1.term = 'transactions' AND f2.term = 'world';
