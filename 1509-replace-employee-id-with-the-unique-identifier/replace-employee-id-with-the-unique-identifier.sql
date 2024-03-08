# Write your MySQL query statement below
SELECT e.name, em.unique_id
FROM Employees e LEFT JOIN EmployeeUNI em ON e.id = em.id