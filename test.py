import pandas as pd 

df = pd.DataFrame() 

charnumlist = ['5','s2','ree']
id_list = ['Ko','Po','Do']

df['ID'] = id_list
df['V'] = charnumlist

mask = df['V'].str.isnumeric()

new_df = df[mask]

print(new_df)