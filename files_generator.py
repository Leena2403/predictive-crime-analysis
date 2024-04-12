import pandas as pd

df = pd.read_csv('Datasets/FIR_Details_Data.csv')
ar = pd.read_csv('Datasets/AccusedData (1).csv')

years = df['Year'].unique()
crimeno = df['Crime_No'].unique()
firno = df['FIRNo'].unique()

arrestid = ar['Arr_ID'].unique()
districts = df['District_Name'].unique()
unitid = df['Unit_ID'].unique()
crimehead = df['CrimeHead_Name'].unique()
crimegroup = df['CrimeGroup_Name'].unique()

unit_name = df['UnitName'].unique()
beatname = df['Beat_Name'].unique()

# with open ('data/years.txt','w') as file:
#     for year in years:
#         file.write(f'{year}\n')

# with open('data/Districts.txt','w') as file:
#     for district in districts:
#         file.write(f'{district}\n')

# with open('data/crimehead.txt','w') as file:
#     for crime in crimehead:
#         file.write(f'{crime}\n')

with open('data/beatname.txt','w') as file:
    for beat in beatname:
        file.write(f'{beat}\n')

# with open('data/unitname.txt','w') as file:
#     for unit in unit_name:
#         file.write(f'{unit}\n')

# with open('data/crimegroup.txt','w') as file:
#     for crime in crimegroup:
#         file.write(f'{crime}\n')

# with open('data/crimesno.txt','w') as file:
#     for crime in crimeno:
#         file.write(f'{crime}\n')

# with open('data/arrested.txt','w') as file:
#     for arrest in arrestid:
#         file.write(f"{arrest}\n")

# with open('data/fir.txt','w') as file:
#     for fir in firno:
#         file.write(f"{fir}\n")

# with open('data/unitid.txt','w') as file:
#     for unit in unitid:
#         file.write(f'{unit}\n')