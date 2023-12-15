-- SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month

CREATE VIEW need_meeting AS SELECT name FROM students WHERE score < 80 AND IFNULL(students.last_meeting, '1970-01-01') < DATE_ADD(NOW(), INTERVAL -1 MONTH);
