SELECT SUM(f1.count * f2.count)
  FROM frequency f1
  JOIN frequency f2 ON f1.term = f2.term
 WHERE f1.docid = '10080_txt_crude'
   AND f2.docid = '17035_txt_earn';
