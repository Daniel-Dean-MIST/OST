import Items
import pandas as pd
import Testing_time_2

def make_fish():
    supply_name_list = ['raw_shrimps', 'raw_anchovies', 'raw_sardine', 'raw_salmon', 'raw_trout', 'raw_cod',
                        'raw_herring',
                        'raw_pike', 'raw_mackerel', 'raw_tuna', 'raw_bass', 'raw_swordfish', 'raw_lobster', 'raw_shark',
                        'raw_manta_ray', 'raw_sea_turtle', 'raw_dark_crab', 'raw_anglerfish', 'raw_monkfish']

    product_name_list = ['shrimps', 'anchovies', 'sardine', 'salmon', 'trout', 'cod', 'herring',
                         'pike', 'mackerel', 'tuna', 'bass', 'swordfish', 'lobster', 'shark',
                         'manta_ray', 'sea_turtle', 'dark_crab', 'anglerfish', 'monkfish']

    xp_each_list = [30, 30, 40, 90, 70, 75, 50, 80, 60, 100, 130, 140, 120, 210, 216.2, 211.3, 215, 230, 150]
    level_list = [1, 1, 1, 25, 15, 18,
    10,
    20, 10, 30, 43, 45, 40, 80,
    91, 82, 90, 84, 62, 30, 30]
    actions_per_hour = 1500
    #print(len(supply_name_list), len(product_name_list), len(xp_each_list))

    df = Items.make_product(supply_name_list, product_name_list, 1, 1, actions_per_hour, xp_each_list)


    supply_name_list = ['raw_karambwan']
    product_name_list = ['cooked_karambwan']
    xp_each_list = [190]
    actions_per_hour = 1500
    df_2 = Items.make_product(supply_name_list, product_name_list, 1, 1, actions_per_hour, xp_each_list)
    
    supply_name_list = ['raw_karambwan']
    product_name_list = ['cooked_karambwan']
    xp_each_list = [190]
    actions_per_hour = 4555
    df_3 = Items.make_product(supply_name_list, product_name_list, 1, 1, actions_per_hour, xp_each_list)
    df_3['Product'] = '1T - cooked_karambwan'
    
    df = df.append(df_2)
    
    df = df.append(df_3)
    
    
    df['Level'] = level_list
    return df

#print(make_fish())

def make_pies():
    supply_name_list = ['uncooked_berry_pie', 'uncooked_meat_pie', 'raw_mud_pie', 'uncooked_apple_pie',
                        'raw_garden_pie',
                        'raw_fish_pie', 'uncooked_botanical_pie', 'uncooked_mushroom_pie', 'raw_admiral_pie',
                        'uncooked_dragonfruit_pie',
                        'raw_wild_pie', 'raw_summer_pie']
    product_name_list = ['redberry_pie', 'meat_pie', 'mud_pie', 'apple_pie', 'garden_pie',
                         'fish_pie', 'botanical_pie', 'mushroom_pie', 'admiral_pie', 'dragonfruit_pie',
                         'wild_pie', 'summer_pie']

    xp_each_list = [78, 110, 128, 130, 138, 164, 180, 200, 210, 220, 240, 260]
    level_list = [10, 20, 29, 30,
    34,
    47, 52, 60, 70, 73,
    85, 95]
    actions_per_hour = 1500

    df = Items.make_product(supply_name_list, product_name_list, 1, 1, actions_per_hour, xp_each_list)
    df['Level'] = level_list
    return df

#print(make_pies())

def make_wine():
    supply_name_list = ['grapes']
    product_name_list = ['jug_of_wine']
    supply_name_list_2 = ['jug_of_water']
    level_list = [35]
    xp_each_list = [200]
    actions_per_hour = 2450

    df = Items.make_double_supplies(supply_name_list, supply_name_list_2, product_name_list, 1, 1, actions_per_hour, xp_each_list)
    df['Level'] = level_list
    return df

#print(make_wine())

def make_cooking():
    df = pd.DataFrame()

    df = make_fish()
    df = df.append(make_pies())
    df = df.append(make_wine())
    return df

#print(make_cooking())

# df = make_cooking()

'''
print(df[['Product', 'Cost', 'GP/HR', 'XP/HR', 'Secondary Ingredient Cost']])
print(df[['Product', 'Base Ingredient', 'Secondary Ingredient']])
'''
#print(make_cooking())