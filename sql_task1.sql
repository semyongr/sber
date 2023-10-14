DECLARE @period INT, @date DATE

SET @date = GETDATE()
SET @period = 100;
 
WHILE @period > 0
    BEGIN
	PRINT @date
        SET @period = @period - 1
        SET @date = DATEADD(day, RAND()*(7-2)+2, @date)
    END;


