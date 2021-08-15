import pandas as pd
from bs4 import BeautifulSoup
import requests
from time import *
from random import *
import numpy as np
import json
import csv

#takes an item name and finds its market price
def gather_price(item_name):
		url = 'https://oldschool.runescape.wiki/w/' + item_name
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')
		content = soup.find('span', {'class':'infobox-quantity'})
		try:
			content = int(content.find('span').get_text().replace(',', ''))
		except:
			print(item_name)
		#content = soup.find_all('span')
		#content = soup.get_attribute_list('id')
		sleep(uniform(0.0, 3.0))
		return content

def gather_heads(item_name):
	url = 'https://oldschool.runescape.wiki/w/' + item_name
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	content = soup.find('span', {'class': 'infobox-quantity-replace'})
	try:
		content = int(content.find('span').get_text().replace(',', ''))
	except:
		pass
	try:
		content = content.get_text().replace(',', '')
		content = int(content.get_text())
	except:
		pass
	# content = soup.find_all('span')
	# content = soup.get_attribute_list('id')
	sleep(uniform(0.0, 3.0))
	return content

#returns a list of all item names
def get_name_list():
	name_list = ['oak_plank', 'teak_plank', 'mahogany_plank', 'steel_bar']
	return name_list

#gets information from the runelite osrs wiki api
def get_runelite_info():
	#url = 'https://prices.runescape.wiki/api/v1/osrs/mapping'
	#url = 'https://prices.runescape.wiki/api/v1/osrs/latest'
	url = 'https://oldschool.runescape.wiki/w/Module:GEPrices/data'
	headers = {
		'User' : 'DannyD',
		'Email' : 'danieldean549@gmail.com',
		'Purpose' : 'Making an optimization site for training skills. Requires item prices as an input.'
	}
	response = requests.get(url, headers=headers)

	return response

def get_item_info(id_list, response):
	info_list = [response['data'][str(x)] for x in id_list]
	return info_list

def get_item_price(id_list, response):
	price_list = [response['data'][str(x)]['high'] for x in id_list]
	return price_list

id_list = [960, 8778, 8780, 8782]

#response = get_runelite_info()
#print(response)
#info_list = get_item_info(info_list)
#print(info_list)
#print(get_item_price(id_list, response))
#print(info_list['data']['2'])



"""
name_list = ['oak_plank', 'teak_plank', 'mahogany_plank', 'steel_bar', 'iron_bar',
			 'raw_shrimp', 'raw_anchovies', 'raw_sardine', 'raw_salmon', 'raw_trout', 'raw_cod', 'raw_herring',
			 'raw_pike', 'raw_mackerel', 'raw_tuna', 'raw_bass', 'raw_swordfish', 'raw_lobster', 'raw_shark',
			 'raw_manta_ray', 'raw_sea_turtle', 'raw_dark_crab', 'raw_anglerfish', 'raw_monkfish', 'raw_karambwan',
			 'shrimps', 'anchovies', 'sardine', 'salmon', 'trout', 'cod', 'herring',
			 'pike', 'mackerel', 'tuna', 'bass', 'swordfish', 'lobster', 'shark',
			 'manta_ray', 'sea_turtle', 'dark_crab', 'anglerfish', 'monkfish', 'cooked_karambwan',
			 'uncut_opal', 'uncut_jade', 'uncut_red_topaz', 'uncut_sapphire', 'uncut_emerald', 'uncut_ruby',
			 'uncut_diamond', 'uncut_dragonstone',
			 'opal', 'jade', 'red_topaz', 'sapphire', 'emerald', 'ruby', 'diamond', 'dragonstone']



'''
#construction
supply_name_list = ['oak_plank', 'teak_plank', 'mahogany_plank', 'steel_bar']
supply_price_list = [gather_price(x) for x in supply_name_list]
'''

'''
#cooking
supply_name_list = ['raw_shrimp', 'raw_anchovies', 'raw_sardine', 'raw_salmon', 'raw_trout', 'raw_cod', 'raw_herring',
					 'raw_pike', 'raw_mackerel', 'raw_tuna', 'raw_bass', 'raw_swordfish', 'raw_lobster', 'raw_shark',
					 'raw_manta_ray', 'raw_sea_turtle', 'raw_dark_crab', 'raw_anglerfish', 'raw_monkfish']
product_name_list = ['shrimps', 'anchovies', 'sardine', 'salmon', 'trout', 'cod', 'herring',
					 'pike', 'mackerel', 'tuna', 'bass', 'swordfish', 'lobster', 'shark',
					 'manta_ray', 'sea_turtle', 'dark_crab', 'anglerfish', 'monkfish']
'''
'''
#pies
supply_name_list = ['uncooked_berry_pie', 'uncooked_meat_pie', 'raw_mud_pie', 'uncooked_apple_pie',
                        'raw_garden_pie',
                        'raw_fish_pie', 'uncooked_botanical_pie', 'uncooked_mushroom_pie', 'raw_admiral_pie',
                        'uncooked_dragonfruit_pie',
                        'raw_wild_pie', 'raw_summer_pie']
product_name_list = ['redberry_pie', 'meat_pie', 'mud_pie', 'apple_pie', 'garden_pie',
					 'fish_pie', 'botanical_pie', 'mushroom_pie', 'admiral_pie', 'dragonfruit_pie',
					 'wild_pie', 'summer_pie']
'''
#wine
supply_name_list = ['grapes']
product_name_list = ['jug_of_wine']
supply_name_list_2 = ['jug_of_water']

'''
#crafting
#gems
supply_name_list = ['uncut_opal', 'uncut_jade', 'uncut_red_topaz', 'uncut_sapphire', 'uncut_emerald',
					'uncut_diamond', 'uncut_dragonstone']
product_name_list = ['opal', 'jade', 'red_topaz', 'sapphire', 'emerald', 'diamond', 'dragonstone']
'''

#leather
supply_name_list = ['leather']
product_name_list = ['leather_gloves', 'leather_boots', 'leather_cowl', 'leather_vambraces', 'leather_body', 'leather_chaps']

name_list = name_list + supply_name_list + product_name_list

#wool
supply_name_list = ['wool']
product_name_list = ['ball_of_wool']

name_list = name_list + supply_name_list + product_name_list


#battlestaves
supply_name_list = ['battlestaff', 'water_orb', 'earth_orb', 'fire_orb', 'air_orb', ]
product_name_list = ['water_battlestaff', 'earth_battlestaff', 'fire_battlestaff', 'air_battlestaff']

name_list = name_list + supply_name_list + product_name_list


#dragon leather
supply_name_list = ['green_dragon_leather', 'blue_dragon_leather', 'red_dragon_leather', 'black_dragon_leather']
product_name_list = ["green_d'hide_body", "blue_d'hide_body", "red_d'hide_body", "black_d'hide_body"]

name_list = name_list + supply_name_list + product_name_list


#glass
supply_name_list = ['molten_glass']
product_name_list = ['beer_glass', 'empty_candle_lantern', 'empty_oil_lamp', 'vial', 'empty_fishbowl', 'unpowered_orb',
					 'lantern_lens']
#light_orb = ['empty_light_orb']

name_list = name_list + supply_name_list + product_name_list


#bracelets
supply_name_list = ['gold_bar']
supply_name_list_2 = ['sapphire', 'emerald', 'ruby', 'diamond', 'dragonstone']
product_name_list = ['gold_bracelet', 'sapphire_bracelet', 'emerald_bracelet', 'ruby_bracelet', 'diamond_bracelet',
					 'dragonstone_bracelet']
name_list = name_list + supply_name_list + product_name_list


#super_glass_make
supply_name_list = ['astral_rune']
supply_name_list_2 = ['giant_seaweed']
supply_name_list_3 = ['buckets_of_sand']
product_name_list = ['molten_glass']
name_list = name_list + supply_name_list + product_name_list + supply_name_list_2 + supply_name_list_3

#print(supply_name_list, [gather_price(x) for x in supply_name_list])
#print(product_name_list, [gather_price(x) for x in product_name_list])


#amethyst
supply_name_list = ['amethyst']
product_name_list = ['amethyst_bolt_tips', 'amethyst_arrowtips', 'amethyst_javelin_heads', 'amethyst_dart_tip']

name_list = name_list + supply_name_list + product_name_list


#firemaking
supply_name_list = ['logs', 'oak_logs', 'willow_logs', 'teak_logs', 'arctic_pine_logs', 'maple_logs', 'mahogany_logs',
					'yew_logs', 'magic_logs', 'redwood_logs']
name_list = name_list + supply_name_list

#fletching
#darts
supply_name_list = ['bronze_dart_tip', 'iron_dart_tip', 'steel_dart_tip', 'mithril_dart_tip', 'adamant_dart_tip',
					'rune_dart_tip', 'dragon_dart_tip', 'amethyst_dart_tip']
supply_name_list_2  = ['feather']
product_name_list = ['bronze_dart', 'iron_dart', 'steel_dart', 'mithril_dart', 'adamant_dart',
					 'rune_dart', 'dragon_dart', 'amethyst_dart']

name_list = name_list + supply_name_list + product_name_list + supply_name_list_2


#arrows
supply_name_list = ['arrow_shaft', 'feather', 'headless_arrow']
supply_name_list_2  = ['bronze_arrowtips', 'iron_arrowtips', 'steel_arrowtips', 'mithril_arrowtips',
					   'broad_arrowtips', 'adamant_arrowtips', 'rune_arrowtips', 'amethyst_arrowtips', 'dragon_arrowtips']
product_name_list = ['headless_arrow','bronze_arrow', 'iron_arrow', 'steel_arrow', 'mithril_arrow', 'adamant_arrow',
					 'rune_arrow', 'amethyst_arrow', 'dragon_arrow']

name_list = name_list + supply_name_list + product_name_list + supply_name_list_2

#bows
supply_name_list = ['logs', 'oak_logs', 'willow_logs', 'maple_logs', 'yew_logs', 'magic_logs', 'bowstring']
product_name_list = ['shortbow', 'longbow', 'oak_shortbow', 'oak_longbow', 'willow_shortbow', 'willow_longbow',
					 'maple_shortbow', 'maple_longbow', 'yew_shortbow', 'yew_longbow', 'magic_shortbow', 'magic_longbow']

name_list = name_list + supply_name_list + product_name_list

#cut bows
product_name_list = ['shortbow_(u)', 'longbow_(u)', 'oak_shortbow_(u)', 'oak_longbow_(u)', 'willow_shortbow_(u)', 'willow_longbow_(u)',
                         'maple_shortbow_(u)', 'maple_longbow_(u)', 'yew_shortbow_(u)', 'yew_longbow_(u)', 'magic_shortbow_(u)',
                         'magic_longbow_(u)']

#battlestaves
supply_name_list = ['celastrus_bark']
product_name_list = ['battlestaff']

name_list = name_list + supply_name_list + product_name_list


#redwood_shields
supply_name_list = ['redwood_logs']
product_name_list = ['redwood_shield']

name_list = name_list + supply_name_list + product_name_list


#herblore
supply_name_list = ['guam_potion_(unf)', 'marrentill_potion_(unf)', 'tarromin_potion_(unf)', 'harralander_potion_(unf)',
					'ranarr_potion_(unf)', 'toadflax_potion_(unf)', 'irit_potion_(unf)', 'avantoe_potion_(unf)',
					'kwuarm_potion_(unf)', 'snapdragon_potion_(unf)', 'cadantine_potion_(unf)', 'lantadyme_potion_(unf)',
					'dwarf_weed_potion_(unf)', 'torstrol_potion_(unf)', 'amulet_of_chemistry']
product_name_list = ['attack_potion_(3)', 'antipoison_(3)', 'strength_potion_(3)', 'compost_potion_(3)', 'restore_potion_(3)',
					 'energy_potion_(3)', 'agility_potion_(3)', 'combat_potion_(3)', 'prayer_potion_(3)', 'super_attack_(3)',
					 'superantipoison_(3)', 'fishing_potion_(3)', 'super_energy_(3)', 'hunter_potion_(3)', 'super_strength_(3)',
					 'super_restore_(3)', 'super_defence_(3)', 'antifire_potion_(3)', 'ranging_potion_(3)', 'magic_potion_(3)',
					 'stamina_potion_(4)', 'bastion_potion_(3)', 'battlemage_potion_(3)', 'saradomin_brew_(3)', 'extended_antifire_(4)',
					 'anti-venom_(4)', 'super_combat_potion_(4)', 'anti-venom+(4)', 'extended_super_antifire_(4)']

supply_name_list_2 = ['eye_of_newt', 'unicorn_horn_dust', 'limpwurt_root', 'volcanic_ash', "red_spiders'_eggs", 'chocolate_dust',
					  "toad's_legs", 'goat_horn_dust', 'snape_grass', 'mort_myre_fungus', 'kebbit_teeth_dust', 'white_berries',
					  'dragon_scale_dust', 'wine_of_zamorak', 'potato_cactus', 'amylase_crystal', 'crushed_nest', 'lava_scale_shard',
					  "zulrah's_scales", 'torstol', 'crushed_superior_dragon_bones']
product_name_list_2 = ['attack_potion_(4)', 'antipoison_(4)', 'strength_potion_(4)', 'compost_potion_(4)', 'restore_potion_(4)',
					 'energy_potion_(4)', 'agility_potion_(4)', 'combat_potion_(4)', 'prayer_potion_(4)', 'super_attack_(4)',
					 'superantipoison_(4)', 'fishing_potion_(4)', 'super_energy_(4)', 'hunter_potion_(4)', 'super_strength_(4)',
					 'super_restore_(4)', 'super_defence_(4)', 'antifire_potion_(4)', 'ranging_potion_(4)', 'magic_potion_(4)',
					 'stamina_potion_(4)', 'bastion_potion_(4)', 'battlemage_potion_(4)', 'saradomin_brew_(4)', 'extended_antifire_(4)',
					 'anti-venom_(4)', 'super_combat_potion_(4)', 'anti-venom+(4)', 'extended_super_antifire_(4)']

name_list = name_list + supply_name_list + product_name_list + supply_name_list_2 + product_name_list_2


#magic
#bolt_enchantment
supply_name_list = ['air_rune', 'water_rune', 'earth_rune', 'fire_rune', 'cosmic_rune', 'mind_rune', 'nature_rune',
					'blood_rune', 'law_rune', 'chaos_rune', 'death_rune', 'astral_rune', 'body_rune', 'soul_rune']
supply_name_list_2 = ['opal_bolts', 'sapphire_bolts', 'pearl_bolts', 'emerald_bolts', 'red_topaz_bolts', 'ruby_bolts']
product_name_list = [x + '_(e)' for x in supply_name_list_2]

name_list = name_list + supply_name_list + product_name_list + supply_name_list_2


#superheat
supply_name_list = ['iron_ore']
product_name_list = ['iron_bar']

name_list = name_list + supply_name_list + product_name_list


#bake_pie
supply_name_list = ['uncooked_berry_pie', 'uncooked_meat_pie', 'raw_mud_pie', 'uncooked_apple_pie', 'raw_garden_pie',
					'raw_fish_pie', 'uncooked_botanical_pie', 'uncooked_mushroom_pie', 'raw_admiral_pie', 'uncooked_dragonfruit_pie',
					'raw_wild_pie', 'raw_summer_pie']
product_name_list = ['redberry_pie', 'meat_pie', 'mud_pie', 'apple_pie', 'garden_pie',
					'fish_pie', 'botanical_pie', 'mushroom_pie', 'admiral_pie', 'dragonfruit_pie',
					'wild_pie', 'summer_pie']
name_list = name_list + supply_name_list + product_name_list


#humidify
supply_name_list = ['bowl', 'bucket', 'clay', 'jug', 'vial', 'waterskin(0)']
product_name_list = ['bowl_of_water', 'bucket_of_water', 'soft_clay', 'jug_of_water', 'vial_of_water', 'waterskin(4)']

name_list = name_list + supply_name_list + product_name_list


#hunter_kit
product_name_list = ['noose_wand', 'butterfly_net', 'bird_snare', 'rabbit_snare', 'teasing_stick', 'unlit_torch',
					 'box_trap', 'impling_jar']
name_list = name_list  + product_name_list

#spin_flax
supply_name_list = ['flax']
product_name_list = ['bowstring']
name_list = name_list + supply_name_list + product_name_list


#tan_leather
supply_name_list = ['cowhide', 'green_dragonhide', 'blue_dragonhide', 'red_dragonhide', 'black_dragonhide']
product_name_list = ['leather', 'hard_leather', 'green_dragon_leather', 'blue_dragon_leather', 'red_dragon_leather',
					 'black_dragon_leather']
name_list = name_list + supply_name_list + product_name_list


#string_jewellery
supply_name_list = ['unstrung_symbol', 'unstrung_emblem', 'gold_amulet_(u)', 'opal_amulet_(u)', 'jade_amulet_(u)',
					'topaz_amulet_(u)', 'sapphire_amulet_(u)', 'emerald_amulet_(u)', 'ruby_amulet_(u)', 'diamond_amulet_(u)',
					'dragonstone_amulet_(u)']
product_name_list = ['holy_symbol', 'unholy_symbol', 'gold_amulet', 'opal_amulet', 'jade_amulet',
					'topaz_amulet', 'sapphire_amulet', 'emerald_amulet', 'ruby_amulet', 'diamond_amulet',
					'dragonstone_amulet']
name_list = name_list + supply_name_list + product_name_list


#prayer
#ensouled_heads
supply_name_list = ['ensouled_goblin_head#item', 'ensouled_monkey_head#item', 'ensouled_imp_head#item', 'ensouled_minotaur_head#item',
					'ensouled_scorpion_head#item', 'ensouled_bear_head#item', 'ensouled_unicorn_head#item', 'ensouled_dog_head#item',
					'ensouled_chaos_druid_head#item', 'ensouled_ogre_head#item', 'ensouled_elf_head#item', 'ensouled_troll_head#item',
					'ensouled_horror_head#item', 'ensouled_kalphite_head#item', 'ensouled_dagannoth_head#item', 'ensouled_bloodveld_head#item',
					'ensouled_tzhaar_head#item', 'ensouled_demon_head#item', 'ensouled_aviansie_head#item', 'ensouled_abyssal_head#item',
					'ensouled_dragon_head#item']
print('head_time')
price_list = [gather_heads(x) for x in name_list]
df_2 = {'Item': supply_name_list, 'Price':price_list}
df_2 = pd.DataFrame(df_2)

#bones
supply_name_list = ['bones', 'wolf_bones', 'burnt_bones', 'monkey_bones', 'bat_bones', 'big_bones', 'jogre_bones', 'zogre_bones',
					'shaikahan_bones', 'babydragon_bones', 'wyrm_bones', 'wyvern_bones', 'dragon_bones', 'drake_bones', 'fayrg_bones',
					'lava_dragon_bones', 'raurg_bones', 'hydra_bones', 'dagganoth_bones', 'ourg_bones', 'superior_dragon_bones']
name_list = name_list + supply_name_list


#smithing
#blast_furnace
supply_name_list = ['iron_ore', 'coal', 'mithril_ore', 'adamant_ore', 'runite_ore', 'gold_ore']
product_name_list = ['iron_bar', 'steel_bar', 'mithril_bar', 'adamant_bar', 'runite_bar', 'gold_bar']
name_list = name_list + supply_name_list + product_name_list


#dart_tips
product_name_list = ['bronze_dart_tips', 'iron_dart_tips', 'steel_dart_tips', 'mithril_dart_tips', 'adamant_dart_tips',
					 'rune_dart_tips']
name_list = name_list + product_name_list


#armor
product_name_list = ['steel_platebody', 'mithril_platelegs', 'mithril_plateskirt', 'mithril_platebody', 'adamant_platebody',
					 'rune_platelegs', 'rune_plateskirt', 'rune_2h_sword']

name_list = name_list + product_name_list

#cannonballs
product_name_list = ['cannonballs']
name_list = name_list + product_name_list

'''
name_list = ['oak_plank', 'teak_plank', 'mahogany_plank', 'steel_bar', 'iron_bar',
			 'raw_shrimp', 'raw_anchovies', 'raw_sardine', 'raw_salmon', 'raw_trout', 'raw_cod', 'raw_herring',
			 'raw_pike', 'raw_mackerel', 'raw_tuna', 'raw_bass', 'raw_swordfish', 'raw_lobster', 'raw_shark',
			 'raw_manta_ray', 'raw_sea_turtle', 'raw_dark_crab', 'raw_anglerfish', 'raw_monkfish', 'raw_karambwan',
			 'shrimps', 'anchovies', 'sardine', 'salmon', 'trout', 'cod', 'herring',
			 'pike', 'mackerel', 'tuna', 'bass', 'swordfish', 'lobster', 'shark',
			 'manta_ray', 'sea_turtle', 'dark_crab', 'anglerfish', 'monkfish', 'cooked_karambwan',
			 'uncut_opal', 'uncut_jade', 'uncut_red_topaz', 'uncut_sapphire', 'uncut_emerald', 'uncut_ruby',
			 'uncut_diamond', 'uncut_dragonstone',
			 'opal', 'jade', 'red_topaz', 'sapphire', 'emerald', 'ruby', 'diamond', 'dragonstone']
'''

print(len(name_list))
temp_df = pd.DataFrame()
temp_df['Names'] = name_list
temp_df = temp_df.drop_duplicates()
name_list = temp_df['Names'].to_list()
print(len(name_list))
price_list = [gather_price(x) for x in name_list]
df = {'Item': name_list, 'Price':price_list}
df = pd.DataFrame(df)
df = df.append(df_2)
df.to_csv(r'item_list.csv', index=False)
"""

#df = pd.read_csv(r"item_list.csv")
#print(df.loc[df['Item'] == 'teak_plank'])
#i = df.loc[df['Item'] == 'teak_plank']
#print(int(i['Price'] * 3))

#takes a name list and returns a list of df prices
def parse_df_prices(df, name_list):
    name_list = [int(df.loc[df['Item'] == n]['Price']) for n in name_list]
    return name_list

#name_list = ['oak_plank', 'teak_plank', 'mahogany_plank', 'steel_bar', 'iron_bar']
#print(parse_df_prices(df, name_list))

#df = json.loads(r'C:\Users\Daniel\Documents\Scripts\OST\flask\item_list.json')
#print(json.dumps(df, indent=4))
#print(supply_name_list, [gather_price(x) for x in supply_name_list])
#print(product_name_list, [gather_price(x) for x in product_name_list])
#print(supply_name_list_2, [gather_price(x) for x in supply_name_list_2])
#print(supply_name_list_3, [gather_price(x) for x in supply_name_list_3])
#print(product_name_list_2, [gather_price(x) for x in product_name_list_2])
#content = gather_price('https://oldschool.runescape.wiki/w/Coal')
#content = gather_price('Cooked_karambwan')
#print(content)
'''
import numpy as np
def powerup(i):
	if i==1:
		return 1
	else:
		return np.square(i) + powerup(i-1)

print(powerup(4))

print(max(21, 14))
'''
'''
j = 1
k = 2

for i in range(3):
	j += k
	k += j
print(k)

strings = ['a', 'bc', 'def', 'ghij']
output = ''
for x in strings:
	if len(x) % 2 == 0:
		continue
	output += x
print(output)
'''