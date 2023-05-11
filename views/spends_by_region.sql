CREATE OR ALTER VIEW [spends_by_country] AS
	SELECT CASE WHEN c.[country_id] = 'DE' THEN 'Exluded Information' ELSE c.[country_id] END AS [country_id], SUM([salary]) Spends 
	FROM [TRN].[hr].[employees] a
	LEFT JOIN [TRN].[hr].[departments] b 
	ON a.department_id = b.department_id
	LEFT JOIN [TRN].[hr].[locations] C
	ON b.location_id = c.location_id
	GROUP BY c.country_id
 
