SELECT C.ClientNum,C.ClientName,C.ConsltNum,E.LastName,E.FirstName
FROM Client C
INNER JOIN Consultant E
ON C.ConsltNum=E.ConsltNum