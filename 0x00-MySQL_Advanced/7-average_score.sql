-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
UPDATE users
SET average_score = (SELECT IFNULL(SUM(score) / COUNT(DISTINCT project_id), 0) FROM corrections WHERE user_id = user_id) WHERE id = user_id;
END$$
