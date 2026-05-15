CREATE DATABASE hospital;
USE hospital;

CREATE TABLE patients (
    patient_id  INT PRIMARY KEY,
    name        VARCHAR(50),
    age         INT,
    gender      VARCHAR(10),
    city        VARCHAR(50)
);

CREATE TABLE staff (
    staff_id    INT PRIMARY KEY,
    name        VARCHAR(50),
    role        VARCHAR(30),
    shift       VARCHAR(20),
    dept        VARCHAR(30)
);

CREATE TABLE er_visits (
    visit_id        INT PRIMARY KEY,
    patient_id      INT,
    staff_id        INT,
    checkin_time    DATETIME,
    discharge_time  DATETIME,
    severity        VARCHAR(20),
    status          VARCHAR(20)
);

USE hospital;

INSERT INTO patients VALUES
(1,'Aarav Shah',34,'Male','Mumbai'),(2,'Priya Nair',28,'Female','Pune'),
(3,'Rohit Verma',45,'Male','Delhi'),(4,'Sneha Iyer',52,'Female','Mumbai'),
(5,'Karan Mehta',23,'Male','Bangalore'),(6,'Anjali Singh',38,'Female','Chennai'),
(7,'Dev Patel',61,'Male','Hyderabad'),(8,'Meera Joshi',29,'Female','Mumbai'),
(9,'Arjun Rao',47,'Male','Pune'),(10,'Fatima Khan',33,'Female','Delhi'),
(11,'Vikram Bose',55,'Male','Mumbai'),(12,'Pooja Gupta',41,'Female','Chennai'),
(13,'Sameer Das',26,'Male','Bangalore'),(14,'Nisha Reddy',36,'Female','Hyderabad'),
(15,'Rahul Sharma',49,'Male','Mumbai'),(16,'Kavya Menon',31,'Female','Pune'),
(17,'Aditya Kumar',58,'Male','Delhi'),(18,'Riya Desai',24,'Female','Mumbai'),
(19,'Manish Tiwari',43,'Male','Chennai'),(20,'Deepa Pillai',67,'Female','Bangalore');

INSERT INTO staff VALUES
(1,'Dr. Sharma','Doctor','Morning','Emergency'),
(2,'Dr. Patel','Doctor','Evening','Emergency'),
(3,'Dr. Iyer','Doctor','Night','Emergency'),
(4,'Nurse Priya','Nurse','Morning','Emergency'),
(5,'Nurse Rahul','Nurse','Evening','Emergency'),
(6,'Nurse Anjali','Nurse','Night','Emergency'),
(7,'Dr. Mehta','Doctor','Morning','Cardiology'),
(8,'Dr. Reddy','Doctor','Evening','Cardiology'),
(9,'Nurse Deepa','Nurse','Morning','Cardiology'),
(10,'Nurse Vikram','Nurse','Night','Emergency');

INSERT INTO er_visits VALUES
(1,1,1,'2024-01-05 08:10:00','2024-01-05 09:45:00','High','Discharged'),
(2,2,4,'2024-01-05 08:30:00','2024-01-05 11:00:00','Medium','Discharged'),
(3,3,1,'2024-01-05 09:00:00','2024-01-05 10:30:00','Low','Discharged'),
(4,4,2,'2024-01-05 14:00:00','2024-01-05 16:30:00','High','Admitted'),
(5,5,5,'2024-01-05 15:00:00','2024-01-05 17:00:00','Medium','Discharged'),
(6,6,2,'2024-01-05 16:00:00','2024-01-05 18:45:00','High','Admitted'),
(7,7,3,'2024-01-06 22:00:00','2024-01-07 01:30:00','High','Admitted'),
(8,8,6,'2024-01-06 23:00:00','2024-01-07 02:00:00','Medium','Discharged'),
(9,9,3,'2024-01-07 00:00:00','2024-01-07 02:30:00','Low','Discharged'),
(10,10,1,'2024-01-07 08:00:00','2024-01-07 09:00:00','Low','Discharged'),
(11,11,4,'2024-01-07 09:00:00','2024-01-07 11:30:00','High','Admitted'),
(12,12,5,'2024-01-07 14:00:00','2024-01-07 15:30:00','Medium','Discharged'),
(13,13,2,'2024-01-08 14:30:00','2024-01-08 17:00:00','High','Admitted'),
(14,14,6,'2024-01-08 23:30:00','2024-01-09 02:00:00','Medium','Discharged'),
(15,15,3,'2024-01-09 01:00:00','2024-01-09 04:30:00','High','Admitted'),
(16,16,1,'2024-01-09 08:30:00','2024-01-09 09:30:00','Low','Discharged'),
(17,17,7,'2024-01-09 09:00:00','2024-01-09 11:00:00','Medium','Discharged'),
(18,18,4,'2024-01-09 10:00:00','2024-01-09 13:00:00','High','Admitted'),
(19,19,8,'2024-01-10 14:00:00','2024-01-10 16:00:00','Medium','Discharged'),
(20,20,9,'2024-01-10 15:00:00','2024-01-10 17:30:00','Low','Discharged');

INSERT INTO er_visits VALUES
(21,1,2,'2024-01-10 16:00:00','2024-01-10 19:00:00','High','Admitted'),
(22,3,5,'2024-01-11 08:00:00','2024-01-11 09:30:00','Low','Discharged'),
(23,5,1,'2024-01-11 09:30:00','2024-01-11 11:00:00','Medium','Discharged'),
(24,7,3,'2024-01-11 22:00:00','2024-01-12 02:00:00','High','Admitted'),
(25,9,6,'2024-01-12 00:00:00','2024-01-12 03:00:00','Medium','Discharged'),
(26,11,4,'2024-01-12 08:30:00','2024-01-12 10:00:00','High','Admitted'),
(27,13,2,'2024-01-12 14:00:00','2024-01-12 16:30:00','Medium','Discharged'),
(28,15,1,'2024-01-13 08:00:00','2024-01-13 09:00:00','Low','Discharged'),
(29,17,5,'2024-01-13 15:00:00','2024-01-13 17:30:00','High','Admitted'),
(30,19,3,'2024-01-13 23:00:00','2024-01-14 01:30:00','Medium','Discharged'),
(31,2,1,'2024-01-14 08:00:00','2024-01-14 09:30:00','Low','Discharged'),
(32,4,4,'2024-01-14 09:00:00','2024-01-14 12:00:00','High','Admitted'),
(33,6,2,'2024-01-14 14:00:00','2024-01-14 16:00:00','Medium','Discharged'),
(34,8,6,'2024-01-14 23:00:00','2024-01-15 01:00:00','High','Admitted'),
(35,10,3,'2024-01-15 00:30:00','2024-01-15 02:30:00','Low','Discharged'),
(36,12,5,'2024-01-15 08:00:00','2024-01-15 10:30:00','Medium','Discharged'),
(37,14,1,'2024-01-15 09:30:00','2024-01-15 11:00:00','High','Admitted'),
(38,16,4,'2024-01-15 14:00:00','2024-01-15 16:00:00','Low','Discharged'),
(39,18,2,'2024-01-15 15:00:00','2024-01-15 18:00:00','High','Admitted'),
(40,20,6,'2024-01-15 22:00:00','2024-01-16 01:00:00','Medium','Discharged'),
(41,1,3,'2024-01-16 08:00:00','2024-01-16 10:00:00','High','Admitted'),
(42,3,5,'2024-01-16 09:00:00','2024-01-16 11:30:00','Medium','Discharged'),
(43,5,1,'2024-01-16 14:00:00','2024-01-16 15:30:00','Low','Discharged'),
(44,7,4,'2024-01-16 15:00:00','2024-01-16 18:00:00','High','Admitted'),
(45,9,2,'2024-01-17 08:00:00','2024-01-17 09:30:00','Medium','Discharged'),
(46,11,6,'2024-01-17 09:00:00','2024-01-17 12:00:00','High','Admitted'),
(47,13,3,'2024-01-17 22:00:00','2024-01-18 01:00:00','Medium','Discharged'),
(48,15,5,'2024-01-17 23:00:00','2024-01-18 02:30:00','High','Admitted'),
(49,17,1,'2024-01-18 08:30:00','2024-01-18 10:00:00','Low','Discharged'),
(50,19,4,'2024-01-18 14:00:00','2024-01-18 16:30:00','Medium','Discharged');

-- query to count total visits for each severity level. Sort by count highest first.
select count(visit_id) as total_count ,severity from er_visits group by severity order by total_count desc;

-- Average treatment time per severity
select round(avg(timestampdiff(minute,checkin_time,discharge_time)),2) as time_difference,severity from er_visits
 group by severity order by time_difference desc;

-- write a query to show only the staff members who handled more than 5 visits. Show staff_id and total_visits.
select count(visit_id) as visit_count,staff_id from er_visits group by staff_id having visit_count >5;

--  Write the same query but show staff name and role instead of staff_id.
select count(e.visit_id) as visit_count , s.name,s.role from er_visits e
 left join staff s on e.staff_id = s.staff_id group by e.staff_id having visit_count >5;
 
 -- Peak hours analysis
 select count(visit_id) as total_visit , hour(checkin_time) as hours from er_visits group by hours order by total_visit desc;
 
 -- Shifts that exceed capacity
 select s.shift,round(avg(timestampdiff(minute,e.checkin_time,e.discharge_time))) as treat_time
 from staff s left join er_visits e on s.staff_id = e.staff_id group by s.shift having treat_time >120 ;
 
 -- Patient admission rate by city
 select p.city, count(*) as total_visit,count(case when e.status = "Admitted" then 1 end) as total_admission,
 round(count(case when e.status = "Admitted" then 1 end) *100/count(*),2) as admission_percent
 from patients p left join er_visits e on p.patient_id = e.patient_id group by p.city having total_visit>2