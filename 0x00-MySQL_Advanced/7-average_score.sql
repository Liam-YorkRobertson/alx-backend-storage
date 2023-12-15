-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
UPDATE users
SET average_score = IFNULL((SELECT AVG(score) FROM corrections WHERE user_id = user_id), 0) WHERE id = user_id;
END$$
