import pandas as pd
from bs4 import BeautifulSoup
import requests
from time import *
from random import *
import numpy as np
import json
import csv

#gets information from the runelite osrs wiki api
def get_runelite_info():
	#url = 'https://prices.runescape.wiki/api/v1/osrs/mapping'
	#url = 'https://prices.runescape.wiki/api/v1/osrs/latest'
	#url = 'https://oldschool.runescape.wiki/w/Module:GEPrices/data'
	#url = 'https://oldschool.runescape.wiki/w/Module:GEPrices/data.json'
	#url = 'https://prices.runescape.wiki/api/v1/osrs/latest'
	url = 'https://oldschool.runescape.wiki/?title=Module:GEPrices/data.json&action=raw&ctype=application%2Fjson'
		
	headers = {
	'User' : 'DannyD',
	'Email' : 'danieldean549@gmail.com',
	'Purpose' : 'Making an optimization site for training skills. Requires item prices as an input. Ostime.gg'
	}
	response = requests.get(url)
	#response = requests.get(url, headers=headers)
	print(response)
	return response

#scrapes all item prices and formats them in a friendly way
def get_all_info():
	page = get_runelite_info()
	soup = BeautifulSoup(page.content, 'html.parser')

	content = soup.getText()
	content = content.replace('{', '')
	content = content.replace('}', '')
	content = content.replace('"', '')
	content = content.lower()
	return content

#splits all of the items information into a name_list and formats it further
def get_all_names(content):
    big_list = content.split(',')
    small_list = [b.split(':') for b in big_list]
    small_list = small_list[2:]
    name_list = [s[0].strip() for s in small_list]
    name_list = [str(n).lower() for n in name_list]
    name_list = [n.replace(' ', '_') for n in name_list]
    return name_list

#splits all of the items information into a price_list and formats it further
def get_all_prices(content):
	big_list = content.split(',')
	small_list = [b.split(':') for b in big_list]
	small_list = small_list[2:]
	price_list = [int(s[1].strip()) for s in small_list]
	return price_list

#makes a dataframe out of our name_list and price_list and then saves it to an item_list csv file
def make_csv():
    all_info = get_all_info()
    #print(all_info)
    sleep(1)
    name_list = get_all_names(all_info)
    #print(name_list)
    sleep(1)
    price_list = get_all_prices(all_info)
    #print(price_list)
    sleep(1)
    #print(name_list, price_list)

    df = {'Item': name_list,
          'Price': price_list}
    df = pd.DataFrame(df)
    df.to_csv(r'item_list.csv', index=False)
    #print(df)
    return

# returns a list of xps per hour
def get_xp_hour(xp_each_list, actions_per_hour):
    xp_hour_list = []

    i = 0
    while i < len(xp_each_list):
        xp_hour = xp_each_list[i] * actions_per_hour
        xp_hour_list.append(xp_hour)
        i += 1

    # print(xp_hour_list)
    return (xp_hour_list)


# finds the profit per hour for each method
def get_profit_hour(total_cost_list, actions_per_hour):
    profit_per_hour_list = []

    i = 0
    while i < len(total_cost_list):
        profit_per_hour = 0
        profit_per_hour = int(total_cost_list[i]) * int(actions_per_hour)
        profit_per_hour_list.append(profit_per_hour)
        i += 1
    # print(profit_per_hour_list)
    return (profit_per_hour_list)

#takes a name list and returns a list of df prices
def parse_df_prices(df, name_list):
    #print(df)
    #name_list = ['Oak_plank', 'Teak_plank', 'Mahogany_plank', 'Steel_bar', 'Iron_bar']
    #print(name_list)
    name_list = [df.loc[df['Item'] == n]['Price'] for n in name_list]
    #print(name_list)
    name_list = [int(n) for n in name_list]
    #print(name_list)
    return name_list

#prints our our mispelled item names
def find_mispelled_item(name_list):
    df = pd.read_csv(r"item_list.csv")
    for x in range(len(name_list)):
        try:
            parse_df_prices(df, [name_list[x]])
        except:
            print(name_list[x])
    return

# lets us put in variable number of supply and products
def make_no_product(supply_list, supply_quantity, product_quantity, actions_per_hour, xp_each_list):

    df = pd.read_csv(r"item_list.csv")
    #print('Supply List: ',supply_list)
    supply_price_list = parse_df_prices(df, supply_list)
    supply_name_list = supply_list

    product_price_list = [0 for x in range(len(supply_price_list))]
    product_name_list = []
    '''
    pairs_of_six = len(product_name_list) / 6
    pairs_of_six = int(pairs_of_six - 1)
    for x in range(pairs_of_six):
        supply_price_list += supply_price_list[:6]
        supply_name_list += supply_name_list[:6]
        xp_each_list += xp_each_list[:6]
    '''

    cost_list = [product_price_list[x] * product_quantity - supply_price_list[x] * supply_quantity for x in
                 range(len(supply_name_list))]

    df = pd.DataFrame()
    df['Product'] = product_name_list
    df['XP/HR'] = get_xp_hour(xp_each_list, actions_per_hour)
    df['GP/HR'] = get_profit_hour(cost_list, actions_per_hour)
    df['Cost'] = cost_list
    df['Base Ingredient'] = supply_name_list
    df['Base Ingredient Cost'] = supply_price_list
    df['Secondary Ingredient'] = ['N/A' for i in range(len(supply_price_list))]
    df['Secondary Ingredient Cost'] = [0 for i in range(len(supply_price_list))]

    return df

# takes supply and product list
def make_product(supply_list, product_list, supply_quantity, product_quantity, actions_per_hour, xp_each_list):

    df = pd.read_csv(r"item_list.csv")
    #print('Supply List: ',supply_list)
    supply_price_list = parse_df_prices(df, supply_list)
    supply_name_list = supply_list

    product_price_list = parse_df_prices(df, product_list)
    product_name_list = product_list
    '''
    pairs_of_six = len(product_name_list) / 6
    pairs_of_six = int(pairs_of_six - 1)
    for x in range(pairs_of_six):
        supply_price_list += supply_price_list[:6]
        supply_name_list += supply_name_list[:6]
        xp_each_list += xp_each_list[:6]
    '''
    cost_list = [product_price_list[x] * product_quantity - supply_price_list[x] * supply_quantity for x in
                 range(len(supply_name_list))]

    df = pd.DataFrame()
    df['Product'] = product_name_list
    df['XP/HR'] = get_xp_hour(xp_each_list, actions_per_hour)
    df['GP/HR'] = get_profit_hour(cost_list, actions_per_hour)
    df['Cost'] = cost_list
    df['Base Ingredient'] = supply_name_list
    df['Base Ingredient Cost'] = supply_price_list
    df['Secondary Ingredient'] = ['N/A' for i in range(len(supply_price_list))]
    df['Secondary Ingredient Cost'] = [0 for i in range(len(supply_price_list))]

    return df

# takes supply and product list
def make_double_supplies(supply_list, supply_list_2, product_list, supply_quantity, product_quantity, actions_per_hour, xp_each_list):

    df = pd.read_csv(r"item_list.csv")
    #print('Supply List: ',supply_list)
    supply_price_list = parse_df_prices(df, supply_list)
    supply_name_list = supply_list
    supply_price_list_2 = parse_df_prices(df, supply_list_2)
    supply_name_list_2 = supply_list_2

    product_price_list = parse_df_prices(df, product_list)
    product_name_list = product_list
    '''
    pairs_of_six = len(product_name_list) / 6
    pairs_of_six = int(pairs_of_six - 1)
    for x in range(pairs_of_six):
        supply_price_list += supply_price_list[:6]
        supply_name_list += supply_name_list[:6]
        xp_each_list += xp_each_list[:6]
    '''
    cost_list = [product_price_list[x] * product_quantity - (supply_price_list[x] + supply_price_list_2[x]) * supply_quantity for x in
                 range(len(supply_name_list))]

    df = pd.DataFrame()
    df['Product'] = product_name_list
    df['XP/HR'] = get_xp_hour(xp_each_list, actions_per_hour)
    df['GP/HR'] = get_profit_hour(cost_list, actions_per_hour)
    df['Cost'] = cost_list
    df['Base Ingredient'] = supply_name_list
    df['Base Ingredient Cost'] = supply_price_list
    df['Secondary Ingredient'] = supply_name_list_2
    df['Secondary Ingredient Cost'] = supply_price_list_2

    return df

# takes in both supply quantites
def make_double_supplies_2(supply_list, supply_list_2, product_list, supply_quantity, supply_quantity_2, product_quantity, actions_per_hour, xp_each_list):

    df = pd.read_csv(r"item_list.csv")
    #print('Supply List: ',supply_list)
    supply_price_list = parse_df_prices(df, supply_list)
    supply_name_list = supply_list
    supply_price_list_2 = parse_df_prices(df, supply_list_2)
    supply_name_list_2 = supply_list_2

    product_price_list = parse_df_prices(df, product_list)
    product_name_list = product_list
    '''
    pairs_of_six = len(product_name_list) / 6
    pairs_of_six = int(pairs_of_six - 1)
    for x in range(pairs_of_six):
        supply_price_list += supply_price_list[:6]
        supply_name_list += supply_name_list[:6]
        xp_each_list += xp_each_list[:6]
    '''
    cost_list = [product_price_list[x] * product_quantity - supply_price_list[x] * supply_quantity - supply_price_list_2[x] * supply_quantity_2 for x in
                 range(len(supply_name_list))]

    df = pd.DataFrame()
    df['Product'] = product_name_list
    df['XP/HR'] = get_xp_hour(xp_each_list, actions_per_hour)
    df['GP/HR'] = get_profit_hour(cost_list, actions_per_hour)
    df['Cost'] = cost_list
    df['Base Ingredient'] = supply_name_list
    df['Base Ingredient Cost'] = supply_price_list
    df['Secondary Ingredient'] = supply_name_list_2
    df['Secondary Ingredient Cost'] = supply_price_list_2

    return df

# takes supply and product list
def make_triple_supplies(supply_list, supply_list_2, supply_list_3, product_list, supply_quantity, supply_quantity_2, supply_quantity_3,
                         product_quantity, actions_per_hour, xp_each_list):

    df = pd.read_csv(r"item_list.csv")
    #print('Supply List: ',supply_list)
    supply_price_list = parse_df_prices(df, supply_list)
    supply_name_list = supply_list
    supply_price_list_2 = parse_df_prices(df, supply_list_2)
    supply_name_list_2 = supply_list_2
    supply_price_list_3 = parse_df_prices(df, supply_list_3)
    supply_name_list_3 = supply_list_3

    product_price_list = parse_df_prices(df, product_list)
    product_name_list = product_list
    '''
    pairs_of_six = len(product_name_list) / 6
    pairs_of_six = int(pairs_of_six - 1)
    for x in range(pairs_of_six):
        supply_price_list += supply_price_list[:6]
        supply_name_list += supply_name_list[:6]
        xp_each_list += xp_each_list[:6]
    '''
    cost_list = [(product_price_list[x] * product_quantity - supply_price_list[x] * supply_quantity - supply_price_list_2[x] * supply_quantity_2
                  - supply_price_list_3[x] * supply_quantity_3) for x in range(len(supply_name_list))]

    df = pd.DataFrame()
    df['Product'] = product_name_list
    df['XP/HR'] = get_xp_hour(xp_each_list, actions_per_hour)
    df['GP/HR'] = get_profit_hour(cost_list, actions_per_hour)
    df['Cost'] = cost_list
    df['Base Ingredient'] = supply_name_list
    df['Base Ingredient Cost'] = supply_price_list
    df['Secondary Ingredient'] = supply_name_list_2
    df['Secondary Ingredient Cost'] = supply_price_list_2

    return df

#make_csv()

get_all_info()