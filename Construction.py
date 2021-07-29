import Testing_time
import Testing_time_2
import Items
import pandas as pd
from bs4 import BeautifulSoup
import requests
from time import *
from random import *
import numpy as np
import json
import csv
#print(1+2)
#df = pd.read_csv(r"item_list.csv")
#print(df.loc[df['Item'] == 'teak_plank'])
#i = df.loc[df['Item'] == 'teak_plank']
#print(int(i['Price'] * 3))
#print(df)

def make_standard():
    #plank_id_list = [8778, 8780, 8782, 2353]
    #plank_list = Items.get_item_info(plank_id_list, response)
    #print('YO TRINITY')
    df = pd.read_csv(r"item_list.csv")
    name_list = ['oak_plank', 'teak_plank', 'mahogany_plank', 'steel_bar', 'iron_bar']

    plank_list = Items.parse_df_prices(df, name_list)
    oak_plank = plank_list[0]
    teak_plank = plank_list[1]
    mahogany_plank = plank_list[2]
    name_list = ['Oak larder', 'Mahogany table', 'Teak garden bench', 'Mounted mythical cape', 'Oak dungeon door']
    #product_id_list = [1733 for i in plank_id_list]
    actions_per_hour = 1000
    xp_each_list = [480]

    coins_per_plank = 48
    planks_per_hour_list = []
    servant_cost_list = []

    df = pd.DataFrame()
    df = Items.make_no_product(['oak_plank'], 8, 1, actions_per_hour, xp_each_list)
    planks_per_hour_list.append(actions_per_hour * 8)
    servant_cost_list.append(8 * -coins_per_plank)

    # mahogany table and gnome benches
    actions_per_hour = 1070
    xp_each_list = [840]
    df = df.append(
        Items.make_no_product(['mahogany_plank'], 6, 1, actions_per_hour, xp_each_list))
    planks_per_hour_list.append(actions_per_hour * 6)
    servant_cost_list.append(6 * -coins_per_plank)

    # teak garden bench and curved teak magic wardrobe
    actions_per_hour = 1295
    xp_each_list = [540]

    df = df.append(
        Items.make_no_product(['teak_plank'], 6, 1, actions_per_hour, xp_each_list))
    planks_per_hour_list.append(actions_per_hour * 6)
    servant_cost_list.append(6 * -coins_per_plank)

    # mythic cape
    actions_per_hour = 1162
    xp_each_list = [370]

    df = df.append(
        Items.make_no_product(['teak_plank'], 3, 1, actions_per_hour, xp_each_list))
    planks_per_hour_list.append(actions_per_hour * 3)
    servant_cost_list.append(3 * -coins_per_plank)

    # oak dungeon door
    actions_per_hour = 915
    xp_each_list = [600]

    df = df.append(
        Items.make_no_product(['oak_plank'], 10, 1, actions_per_hour, xp_each_list))
    planks_per_hour_list.append(actions_per_hour * 10)
    servant_cost_list.append(10 * -coins_per_plank)

    actions_per_hour_list = [1000, 1070, 1295, 1162, 915]
    df['Product'] = name_list

    df['Secondary Ingredient'] = ['Servant cost' for c in servant_cost_list]
    df['Secondary Ingredient Cost'] = servant_cost_list
    df['Cost'] = [df['Cost'].iloc[x] + servant_cost_list[x] for x in range(len(servant_cost_list))]
    df['GP/HR'] = [df['Cost'].iloc[x] * actions_per_hour_list[x] for x in range(len(servant_cost_list))]

    return df


def make_mahogany_homes():
    #supply_id_list = [8778, 8780, 8782, 2353]
    #supply_list = Items.get_item_info(supply_id_list, response)

    df = pd.read_csv(r"item_list.csv")

    supply_list = ['oak_plank', 'teak_plank', 'mahogany_plank', 'steel_bar', 'iron_bar']

    oak_plank = supply_list[0]
    teak_plank = supply_list[1]
    mahogany_plank = supply_list[2]
    steel_bar = supply_list[3]
    #product_id_list = [1733 for i in supply_id_list]
    name_list = ['Novice: M. homes', 'Novice Sack: M. Homes', 'Adept: M. homes', 'Adept Sack: M. Homes',
                 'Expert: M. Homes', 'Expert Sack: M. Homes']

    steel_bar_price = Items.parse_df_prices(df, ['steel_bar'])
    steel_bars_per_hour = [22, 22, 23, 23, 25, 25]

    steel_bar_cost_list = [steel_bar_price for x in range(len(steel_bars_per_hour))]

    # novice and novice plank sack
    xp_each_list = [176]
    actions_per_hour = 425
    df = Items.make_no_product(['oak_plank'], 1, 0, actions_per_hour, xp_each_list)

    xp_each_list = [178]
    actions_per_hour = 475
    df = df.append(
        Items.make_no_product(['oak_plank'], 1, 0, actions_per_hour, xp_each_list))

    # adept and adept plank sack
    xp_each_list = [277]
    actions_per_hour = 450
    df = df.append(
        Items.make_no_product(['teak_plank'], 1, 0, actions_per_hour, xp_each_list))

    xp_each_list = [290]
    actions_per_hour = 500
    df = df.append(
        Items.make_no_product(['teak_plank'], 1, 0, actions_per_hour, xp_each_list))

    # expert and expert plank sack
    xp_each_list = [380]
    actions_per_hour = 500
    df = df.append(
        Items.make_no_product(['mahogany_plank'], 1, 0, actions_per_hour, xp_each_list))

    xp_each_list = [391]
    actions_per_hour = 575
    df = df.append(
        Items.make_no_product(['mahogany_plank'], 1, 0, actions_per_hour, xp_each_list))

    actions_per_hour_list = [425, 475, 450, 500, 500, 575]
    df['Product'] = name_list

    df['Secondary Ingredient'] = ['Steel bar' for c in actions_per_hour_list]
    df['Secondary Ingredient Cost'] = [int(-steel_bar_price[0] * steel_bars_per_hour[x] / actions_per_hour_list[x]) for
                                       x in range(len(actions_per_hour_list))]
    df['Cost'] += df['Secondary Ingredient Cost']
    df['GP/HR'] = [df['Cost'].iloc[x] * actions_per_hour_list[x] for x in range(len(actions_per_hour_list))]
    # print(df)
    return df


def make_construction():
    #response = Items.get_all_items()

    df = pd.DataFrame()

    df = make_standard()
    df = df.append(make_mahogany_homes())
    return df

'''
df = make_mahogany_homes()
print(df)
'''
'''
print(df[['Product', 'Cost', 'GP/HR', 'XP/HR', 'Secondary Ingredient Cost']])
print(df[['Product', 'Base Ingredient', 'Secondary Ingredient']])
'''

#df = make_construction()
#print(make_construction())