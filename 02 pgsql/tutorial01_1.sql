-- create table rpt_tutorial
-- (
-- 	id serial NOT NULL,
-- 	name text,
-- 	age int,
-- 	joindate date
-- );

-- INSERT INTO rpt_tutorial (
-- 	name,age,joindate)
-- 	VALUES (
-- 		'name1', 20, '2001-07-13'
-- 	),('name2', 30, '2002-01-20');

-- update rpt_tutorial set age =33 where name = 'name2';

delete from rpt_tutorial where id =2;
select * from rpt_tutorial;
