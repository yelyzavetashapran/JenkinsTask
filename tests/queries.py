# dbo.exluded_spends_info
dbo_exluded_spends_info_duplicates = '''SELECT COUNT(*) 
                    FROM
                        (SELECT [first_name], 
								[last_name], 
								[job_id], 
								ROW_NUMBER() OVER(partition by CONCAT([first_name],[last_name]) order by [job_id]) as row_num
						FROM [dbo].[exluded_spends_info]
						) tmp_tbl 
						WHERE row_num > 1'''


dbo_exluded_spends_info_cnt = '''SELECT 'Count of employees', count(*) cnt from [dbo].[exluded_spends_info]'''

dbo_exluded_spends_info_validation = ''' SELECT COUNT(*) 
                                            FROM [dbo].[exluded_spends_info]
                                            WHERE [salary] > 200000 or [salary] < 1000 '''



#dbo.spends_by_country

spends_by_country_count_validation = '''  SELECT COUNT(*) 
					FROM [dbo].[spends_by_country]
				'''


