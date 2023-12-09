CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  department VARCHAR(50),
  salary DECIMAL(10, 2)
);


CREATE TABLE departments (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  location VARCHAR(50)
);


INSERT INTO employees (first_name, last_name, department, salary)
VALUES
  ('Prince', 'Doe', 'Sales', 5000),
  ('Mikk', 'Smith', 'HR', 6000),
  ('Sanjana', 'Johnson', 'Finance', 7000),
  ('Dolly', 'Brown', 'Marketing', 5500),
  ('Paresh', 'Wilson', 'IT', 6500);


INSERT INTO departments (name, location)
VALUES
  ('Sales', 'New York'),
  ('HR', 'London'),
  ('Finance', 'San Francisco'),
  ('Marketing', 'Paris'),
  ('IT', 'Tokyo');
 
select * from employees;
select * from departments;