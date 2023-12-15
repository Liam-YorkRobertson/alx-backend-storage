-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN userId INT)
BEGIN
UPDATE users
SET average_weighted_score = IFNULL((SELECT SUM(corrections.score * projects.weight) / NULLIF(SUM(projects.weight), 0)
FROM corrections JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = userId), 0)
WHERE id = userId;
END$$
