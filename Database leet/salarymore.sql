# Write your MySQL query statement below
SELECT e.name AS EMployee
FROM Employee e
JOIN Employee m ON e.managerID = m.id
WHERE e.salary > m.salary;
