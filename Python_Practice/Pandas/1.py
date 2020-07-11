import pandas as pd

# df = pd.read_csv('data/survey_results_public.csv', index_col = 'Respondent')
# df2 = pd.read_csv('data/survey_results_schema.csv',index_col = 'Column')

students = { "Roll": ['1207128','1207116','1207129'],
			"Name": ['Atul','Pankhuri','Akshay'],
			"Email":['gupta.atul193@gmail.com', 'pankhuriverma003@gmail.com', 'akshaygarg1693@gmail.com'],
			"KnowsPython": ["yes","no","no"],
			"Gender":['Male','Female','Male'],
			"Salary": [30000,40000,None]
			}

stud_df = pd.DataFrame(students)

# df2.sort_index(inplace=True)
# df2.reset_index(inplace=True)
rl = ['1207128','1207116']
filt =( stud_df["Name"].str.contains('k',na=False) & stud_df["Roll"].isin(rl) )

# print(stud_df[filt].loc[:,'Email'] )
print(stud_df.loc[filt,'Email']) # does the same thing as the above statement
