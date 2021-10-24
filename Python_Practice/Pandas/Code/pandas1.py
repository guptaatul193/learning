import os
import json
import pandas as pd

# Data directory path
data_path = os.path.join('..','Data','')
stud_path = os.path.join(data_path,'StudentInfo.csv')
branch_path = os.path.join(data_path,'Branch.csv')
hod_path = os.path.join(data_path,'HOD.csv')
academics_path = os.path.join(data_path,'Academics.csv')

# Indexing tables
data_ind = {0:'All', 1:'stud_df', 2:'branch_df', 3:'hod_df', 4:'academics_df'}

# Global variables to store data
stud_df = None
branch_df = None
hod_df = None
academics_df = None

# Load CSV data into dataframes
def loadData():
    global stud_df
    # stud_df = pd.read_csv(stud_path).set_index(['RollNumber'])
    stud_df = pd.read_csv(stud_path)
    global branch_df
    # branch_df = pd.read_csv(branch_path).set_index(['BranchCd'])
    branch_df = pd.read_csv(branch_path)
    global hod_df
    # hod_df = pd.read_csv(hod_path).set_index(['HodId'])
    hod_df = pd.read_csv(hod_path)
    global academics_df
    academics_df = pd.read_csv(academics_path)

def saveData():
    stud_df.to_csv(stud_path)
    branch_df.to_csv(branch_path)
    hod_df.to_csv(hod_path)
    academics_df.to_csv(academics_path)

def showData( choice=0 ):
    if not choice:
        print(stud_df)
        print(branch_df)
        print(hod_df)
        print(academics_df)
        print('\n')
    else:
        eval('print('+ data_ind[choice] +', end="\\n\\n")')

loadData()
# showData()

# Get student Name and Branch Name
print("Get student Name and Branch Name - ")
Name_BranchName = stud_df.merge( branch_df, how="left", left_on="BranchCd", right_on="BranchCd")
print( Name_BranchName.loc[:,["Name","BranchName"]], end="\n\n")

# Get student Name, Branch Name, HOD Name, Semester and Pass/Fail status - all ordered by Name
print('Get student Name, Branch Name, HOD Name, Semester and Pass/Fail status - all ordered by Name and Semester')
withHOD = Name_BranchName.merge( hod_df, how="left", left_on="HodId", right_on="HodId" )
withPassFlag =  withHOD.merge( academics_df, how="left", left_on="RollNumber", right_on="RollNumber" )
print( withPassFlag.loc[:,["Name","BranchName","HodName", "Semester", "PassFlag"]].sort_values(by=["Name","Semester"]) )
