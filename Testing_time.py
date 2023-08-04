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
