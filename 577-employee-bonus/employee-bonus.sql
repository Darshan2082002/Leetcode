 select e.name, b.bonus 
 from Employee e 
 left join bonus b ON e.empid =b.empid
 where b.bonus<1000 OR b.bonus is NULL
 