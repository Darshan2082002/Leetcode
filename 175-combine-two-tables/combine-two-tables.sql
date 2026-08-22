# Write your MySQL query statement below
select Person.firstName,Person.lastName,Address.city,Address.state
From Person 
LEFT Join Address
On Person.personId=Address.personId