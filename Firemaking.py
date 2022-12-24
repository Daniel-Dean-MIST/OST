import Items
import pandas as pd

def make_regular_logs():
    supply_name_list = ['logs', 'oak_logs', 'willow_logs', 'teak_logs', 'arctic_pine_logs', 'maple_logs',
                        'mahogany_logs',
                        'yew_logs', 'magic_logs', 'redwood_logs']
    xp_each_list = [40, 60, 90, 105, 125, 135, 157.5, 202.5, 303.8, 350]
    #print(len(supply_name_list), len(xp_each_list))
    level_list = [1, 15, 30, 35, 47, 45,
    50,
    60, 75, 90]
    actions_per_hour = 1485

    df = Items.make_no_product(supply_name_list, 1, 1, actions_per_hour, xp_each_list)
    df['Product'] = supply_name_list
    df['Level'] = level_list
    return df


#print(make_regular_logs())

def make_wintertodt():
    name_list = ['50: Wintertodt', '60: Wintertodt', '70: Wintertodt', '80: Wintertodt', '90: Wintertodt',
                 '99: Wintertodt']
    xp_hour_list = [161000, 193000, 226000, 258000, 290000, 320000]
    level_list = [50, 60, 70, 80, 90, 99]
    # 114 crates for 10 hours
    # 11.4 crates per hour
    # 36842 gp per crate on average for a maxed account
    # 420k gp / hr

    df = pd.DataFrame()

    df['Product'] = name_list
    df['XP/HR'] = xp_hour_list
    df['GP/HR'] = [300000 for x in name_list]
    df['Cost'] = [0 for x in name_list]
    df['Base Ingredient'] = ['N/A' for x in name_list]
    df['Base Ingredient Cost'] = [0 for x in name_list]
    df['Secondary Ingredient'] = ['N/A' for x in name_list]
    df['Secondary Ingredient Cost'] = [0 for x in name_list]
    df['Level'] = level_list
    return df


def make_firemaking():
    df = pd.DataFrame()

    df = make_regular_logs()
    df = df.append(make_wintertodt())
    df['Secondary Ingredient'] = ['N/A' for x in df['Secondary Ingredient']]
    df['Secondary Ingredient Cost'] = [0 for x in df['Secondary Ingredient']]
    return df


#df = make_firemaking()
#print(df)
'''
print(df[['Product', 'Cost', 'GP/HR', 'XP/HR', 'Secondary Ingredient Cost']])
print(df[['Product', 'Base Ingredient', 'Secondary Ingredient']])
'''