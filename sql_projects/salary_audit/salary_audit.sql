CREATE DATABASE sql_practice;
USE sql_practice;

CREATE TABLE departments (
  dept_id   INT PRIMARY KEY,
  dept_name VARCHAR(50),
  location  VARCHAR(50)
);

CREATE TABLE employees (
  emp_id     INT PRIMARY KEY,
  name       VARCHAR(50),
  dept_id    INT,
  salary     DECIMAL(10,2),
  hire_date  DATE,
  job_title  VARCHAR(50),
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

INSERT INTO departments VALUES
(1, 'Engineering',  'Mumbai'),
(2, 'Marketing',    'Delhi'),
(3, 'HR',           'Mumbai'),
(4, 'Finance',      'Bangalore'),
(5, 'Sales',        'Mumbai');

INSERT INTO employees VALUES
(101, 'Aisha Sharma',    1, 95000,  '2020-03-15', 'Senior Engineer'),
(102, 'Rohan Mehta',     2, 62000,  '2021-07-01', 'Marketing Analyst'),
(103, 'Priya Nair',      1, 78000,  '2019-11-20', 'Engineer'),
(104, 'Karan Patel',     3, 45000,  '2022-01-10', 'HR Executive'),
(105, 'Sneha Gupta',     4, 88000,  '2020-06-25', 'Finance Manager'),
(106, 'Dev Joshi',       1, 102000, '2018-08-05', 'Lead Engineer'),
(107, 'Meera Iyer',      2, 58000,  '2023-02-14', 'Marketing Executive'),
(108, 'Arjun Singh',     5, 51000,  '2021-09-30', 'Sales Executive'),
(109, 'Fatima Khan',     4, 74000,  '2019-04-17', 'Finance Analyst'),
(110, 'Vikram Rao',      3, 47000,  '2022-11-08', 'HR Analyst'),
(111, 'Ananya Das',      1, 89000,  '2020-12-01', 'Senior Engineer'),
(112, 'Ravi Kulkarni',   5, 63000,  '2021-03-22', 'Sales Manager'),
(113, 'Pooja Verma',     2, 71000,  '2018-05-30', 'Marketing Manager'),
(114, 'Sameer Bose',     NULL, 55000,'2023-07-19', 'Contractor'),
(115, 'Nisha Reddy',     1, 67000,  '2022-08-14', 'Engineer');

select name,job_title,salary from employees where salary > 70000 order by salary desc;

-- find the average salary per department
select dept_id, round(avg(salary),2) as avg_salary from employees group by dept_id order by avg_salary desc;

-- JOIN the department name in
select d.dept_id, d.dept_name,round(avg(e.salary),2) as avg_salary from departments d left join employees e on d.dept_id = e.dept_id group by d.dept_id order by avg_salary desc;

-- RANK employees by salary within each department
select name, dept_id, salary,rank() over(partition by dept_id order by salary desc) as salary_rank from employees;

-- RANK vs DENSE_RANK
select name, dept_id,salary ,dense_rank() over (partition by dept_id order by salary desc) as salary_normal,
rank() over (partition by dept_id order by salary desc) as salary_dense from employees;

-- Find only the TOP earner from each department

with ranked as(
select name,dept_id,salary, rank() over (partition by dept_id order by salary desc) as salary_rank from employees
) select * from ranked where salary_rank = 1; 

-- COALESCE to clean NULL

select e.name,e.salary,coalesce(d.dept_name,"no department") as department from employees e left join departments d on e.dept_id = d.dept_id;
select e.name,e.salary,case 
when e.salary>=90000 then "high"
when e.salary>=60000 then "mid"
else "low" 
end as salalry_tier,coalesce(d.dept_name,"no department") as department from employees e left join departments d on e.dept_id = d.dept_id;