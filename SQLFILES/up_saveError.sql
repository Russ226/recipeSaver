CREATE PROCEDURE `up_saveError` (
	IN errorMessage varchar(255),
    IN className varchar(255),
    IN methodName varchar(255)
)
BEGIN
	INSERT INTO errorLog(errorMessage, className, methodName)
    values(errorMessage, className, methodName);
END
