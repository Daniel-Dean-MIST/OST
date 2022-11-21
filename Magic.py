import Items
import pandas as pd
import Crafting


def make_bolt_enchantments():
    actions_per_hour = 5500


    xp_each_list = [9, 17, 29, 37, 33, 59, 67, 78]
    
    level_list = [4, 7, 24, 27, 29, 49, 57, 68]
    
    df = Items.make_double_supplies_2(['opal_bolts'], ['cosmic_rune'], ['opal_bolts_(e)'], 10, 1, 10,
                                        actions_per_hour,
                                        [9])


    df_2 = Items.make_triple_supplies(['sapphire_bolts'], ['cosmic_rune'], ['mind_rune'], ['sapphire_bolts_(e)'], 10, 1, 1, 10,
                                        actions_per_hour,
                                        [17])
    df = df.append(df_2)

    df_2 = Items.make_double_supplies_2(['pearl_bolts'], ['cosmic_rune'], ['pearl_bolts_(e)'], 10, 1, 10,
                                      actions_per_hour,
                                      [29])
    df = df.append(df_2)

    df_2 = Items.make_triple_supplies(['emerald_bolts'], ['cosmic_rune'], ['nature_rune'], ['emerald_bolts_(e)'], 10, 1,
                                      1, 10,
                                      actions_per_hour,
                                      [37])
    df = df.append(df_2)

    df_2 = Items.make_double_supplies_2(['topaz_bolts'], ['cosmic_rune'], ['topaz_bolts_(e)'], 10, 1, 10,
                                        actions_per_hour,
                                        [33])
    df = df.append(df_2)

    df_2 = Items.make_triple_supplies(['ruby_bolts'], ['cosmic_rune'], ['blood_rune'], ['ruby_bolts_(e)'], 10, 1,
                                      1, 10,
                                      actions_per_hour,
                                      [59])
    df = df.append(df_2)
    
    df_2 = Items.make_triple_supplies(['diamond_bolts'], ['law_rune'], ['cosmic_rune'], ['diamond_bolts_(e)'], 10, 2,
                                      1, 10,
                                      actions_per_hour,
                                      [67])
    df = df.append(df_2)
    
    df_2 = Items.make_triple_supplies(['dragonstone_bolts'], ['soul_rune'], ['cosmic_rune'], ['dragonstone_bolts_(e)'], 10, 1,
                                      1, 10,
                                      actions_per_hour,
                                      [78])
    df = df.append(df_2)
    
    df['Level'] = level_list
    
    return df

#print(make_bolt_enchantments())

def make_superheat():
    xp_each_list = [53, 53, 53]
    level_list = [43, 43, 43]
    actions_per_hour = 2500

    supply_name_list = ['iron_ore', 'gold_ore', 'gold_ore']
    product_name_list = ['iron_bar', 'gold_bar', 'gold_bar']
    supply_name_list_2 = ['nature_rune', 'nature_rune', 'nature_rune']

    df = Items.make_double_supplies_2(supply_name_list, supply_name_list_2, product_name_list, 1, 1, 1,
                                      actions_per_hour, xp_each_list)

    df['Product'] = ['Superheat: iron_ore', 'superheat: gold_ore', 'superheat guantlets: gold_ore']
    df['Level'] = level_list
    return df

#print(make_superheat())

def make_camelot_teleport():
    supply_name_list = ['law_rune']
    xp_each_list = [55]
    level_list = [45]
    actions_per_hour = 1442

    df = pd.DataFrame()

    df = Items.make_no_product(supply_name_list, 1, 0, actions_per_hour, xp_each_list)

    df['Product'] = 'Camelot Teleport'
    df['Level'] = level_list

    return df

#print(make_camelot_teleport())

def make_high_alchemy():
    supply_name_list = ['rune_med_helm', 'rune_scimitar', 'rune_longsword', 'rune_full_helm', 'rune_battleaxe', 'rune_chainbody',
                        'rune_kiteshield', 'rune_platelegs', 'rune_2h_sword', 'rune_plateskirt', 'rune_platebody', 'rune_halberd']
    supply_name_list_2 = ['nature_rune' for x in range(len(supply_name_list))]
    level_list = [55 for x in supply_name_list]
    df = pd.read_csv(r"item_list.csv")
    supply_price_list = Items.parse_df_prices(df, supply_name_list)
    supply_price_list_2 = Items.parse_df_prices(df, supply_name_list_2)

    product_price_list = [11520, 15360, 19200, 21120, 24960, 30000, 32640, 38400, 38400, 38400, 39000, 38400]
    xp_each_list = [65 for x in range(len(supply_name_list))]
    actions_per_hour = 1200
    cost_list = [product_price_list[x] - supply_price_list[x] - supply_price_list_2[x] for x in range(len(supply_name_list))]

    supply_name_list = ['High Alch: ' + x for x in supply_name_list]

    df = pd.DataFrame()
    df['Product'] = supply_name_list
    df['XP/HR'] = Items.get_xp_hour(xp_each_list, actions_per_hour)
    df['GP/HR'] = Items.get_profit_hour(cost_list, actions_per_hour)
    df['Cost'] = cost_list
    df['Base Ingredient'] = supply_name_list
    df['Base Ingredient Cost'] = supply_price_list
    df['Secondary Ingredient'] = supply_name_list_2
    df['Secondary Ingredient Cost'] = supply_price_list_2
    df['Level'] = level_list
    return df


# maniacle monkeys
def make_ancients():
    df = pd.read_csv(r"item_list.csv")
    name_list = ['water_rune', 'chaos_rune', 'death_rune', 'blood_rune']
    supply_price_list = Items.parse_df_prices(df, name_list)
    water_rune_price = supply_price_list[0]
    chaos_rune_price = supply_price_list[1]
    death_rune_price = supply_price_list[2]
    blood_rune_price = supply_price_list[3]

    supply_price_list = []
    supply_name_list = []
    xp_each_list = [290, 377]
    level_list = [70, 94]
    actions_per_hour = 1085
    
    product_name_list = ['Ice Burst', 'Ice Barrage']

    rune_price = water_rune_price * 4 + chaos_rune_price * 4 + death_rune_price * 2
    supply_price_list.append(rune_price)

    rune_price = water_rune_price * 6 + blood_rune_price * 2 + death_rune_price * 4
    supply_price_list.append(rune_price)

    supply_price_list = [-i for i in supply_price_list]

    supply_name_list = ['Runes' for i in range(len(xp_each_list))]

    df = pd.DataFrame()

    df['Product'] = product_name_list
    df['XP/HR'] = Items.get_xp_hour(xp_each_list, actions_per_hour)
    df['GP/HR'] = Items.get_profit_hour(supply_price_list, actions_per_hour)
    df['Cost'] = supply_price_list
    df['Base Ingredient'] = supply_name_list
    df['Base Ingredient Cost'] = supply_price_list
    df['Secondary Ingredient'] = supply_name_list
    df['Secondary Ingredient Cost'] = [0 for i in range(len(supply_price_list))]
    df['Level'] = level_list
    return df


def bake_pie():
    supply_name_list = ['uncooked_berry_pie', 'uncooked_meat_pie', 'raw_mud_pie', 'uncooked_apple_pie',
                        'raw_garden_pie',
                        'raw_fish_pie', 'uncooked_botanical_pie', 'uncooked_mushroom_pie', 'raw_admiral_pie',
                        'uncooked_dragonfruit_pie',
                        'raw_wild_pie', 'raw_summer_pie']
    product_name_list = ['redberry_pie', 'meat_pie', 'mud_pie', 'apple_pie', 'garden_pie',
                         'fish_pie', 'botanical_pie', 'mushroom_pie', 'admiral_pie', 'dragonfruit_pie',
                         'wild_pie', 'summer_pie']
    supply_name_list_2 = ['astral_rune' for x in range(len(supply_name_list))]
    xp_each_list = [81 for i in supply_name_list]
    level_list = [65 for x in supply_name_list]
    pies_per_hour = 1200
    actions_per_hour = pies_per_hour

    df = Items.make_double_supplies_2(supply_name_list, supply_name_list_2, product_name_list, 1, 1, 1,
                                      actions_per_hour, xp_each_list)

    df['Product'] = 'Lunar: ' + df['Base Ingredient']
    df['Level'] = level_list
    return df

#print(bake_pie())

def humidify():
    supply_name_list = ['bowl', 'bucket', 'clay', 'jug', 'vial', 'waterskin(0)']
    product_name_list = ['bowl_of_water', 'bucket_of_water', 'soft_clay', 'jug_of_water', 'vial_of_water',
                         'waterskin(4)']
    supply_name_list_2 = ['astral_rune' for x in supply_name_list]

    xp_each_list = [65 for i in range(len(supply_name_list))]
    level_list = [68 for x in supply_name_list]
    humidify_per_hour = 815
    actions_per_hour = humidify_per_hour

    df = Items.make_double_supplies_2(supply_name_list, supply_name_list_2, product_name_list, 1, 1, 1,
                                      actions_per_hour, xp_each_list)

    df['Product'] = 'Humidify: ' + df['Base Ingredient']
    df['Level'] = level_list
    return df

#print(humidify())

def hunter_kit():
    supply_name_list = ['astral_rune']
    product_name_list = ['noose_wand', 'butterfly_net', 'bird_snare', 'rabbit_snare', 'teasing_stick', 'unlit_torch',
                         'box_trap', 'impling_jar']
    df = pd.read_csv(r"item_list.csv")

    supply_price_list = Items.parse_df_prices(df, supply_name_list)
    product_price_list = Items.parse_df_prices(df, product_name_list)
    product_price_list = [sum(product_price_list)]
    print(product_price_list)

    xp_each_list = [65 for i in range(len(supply_name_list))]
    level_list = [71 for x in supply_name_list]
    hunter_kits_per_hour = 742
    actions_per_hour = hunter_kits_per_hour
    cost_list = [product_price_list[0] - supply_price_list[0]]

    df = pd.DataFrame()
    df['Product'] = ['Lunar: hunter_kit']
    df['XP/HR'] = Items.get_xp_hour(xp_each_list, actions_per_hour)
    df['GP/HR'] = Items.get_profit_hour(cost_list, actions_per_hour)
    df['Cost'] = cost_list
    df['Base Ingredient'] = supply_name_list
    df['Base Ingredient Cost'] = supply_price_list
    df['Secondary Ingredient'] = ['N/A' for x in range(len(supply_price_list))]
    df['Secondary Ingredient Cost'] = [0 for i in range(len(supply_price_list))]
    df['Level'] = level_list
    return df

#print(hunter_kit())
def spin_flax():
    flax_per_hour = 1034
    supply_name_list = ['flax']
    product_name_list = ['bow_string']
    supply_name_list_2 = ['astral_rune']
    supply_name_list_3 = ['nature_rune']
    xp_each_list = [75]
    level_list = 76

    actions_per_hour = flax_per_hour

    df = Items.make_triple_supplies(supply_name_list, supply_name_list_2, supply_name_list_3, product_name_list, 5, 1, 2,
                         5, actions_per_hour, xp_each_list)

    df['Product'] = 'Lunar: ' + df['Product']
    df['Level'] = level_list
    return df

#print(spin_flax())
def super_glass_make():
    df = pd.DataFrame()
    df = Crafting.make_super_glass_make()
    df['XP/HR'] = [819 * 78]
    level_list = [77]
    df['Level'] = level_list
    return df

#print(super_glass_make())

def tan_leather():
    leather_per_hour = 1200
    supply_name_list = ['cowhide', 'cowhide', 'green_dragonhide', 'blue_dragonhide', 'red_dragonhide', 'black_dragonhide']
    product_name_list = ['leather', 'hard_leather', 'green_dragon_leather', 'blue_dragon_leather', 'red_dragon_leather',
                         'black_dragon_leather']
    supply_name_list_2 = ['nature_rune' for x in supply_name_list]
    supply_name_list_3 = ['astral_rune' for x in supply_name_list]

    xp_each_list = [81 for i in product_name_list]
    level_list = [78 for x in supply_name_list]
    actions_per_hour = leather_per_hour

    df = Items.make_triple_supplies(supply_name_list, supply_name_list_2, supply_name_list_3, product_name_list, 5, 1,
                                    2,
                                    5, actions_per_hour, xp_each_list)

    df['Product'] = 'Lunar: ' + df['Product']
    df['Level'] = level_list
    
    return df

#print(tan_leather())

def string_jewellery():
    # string jewellry
    jewellry_per_hour = 1807
    supply_name_list = ['unstrung_symbol', 'unstrung_emblem', 'gold_amulet_(u)', 'opal_amulet_(u)', 'jade_amulet_(u)',
                        'topaz_amulet_(u)', 'sapphire_amulet_(u)', 'emerald_amulet_(u)', 'ruby_amulet_(u)',
                        'diamond_amulet_(u)',
                        'dragonstone_amulet_(u)']
    product_name_list = ['holy_symbol', 'unholy_symbol', 'gold_amulet', 'opal_amulet', 'jade_amulet',
                         'topaz_amulet', 'sapphire_amulet', 'emerald_amulet', 'ruby_amulet', 'diamond_amulet',
                         'dragonstone_amulet']

    supply_name_list_2 = ['astral_rune' for x in supply_name_list]

    xp_each_list = [83 for i in supply_name_list]
    level_list = [80 for x in supply_name_list]
    actions_per_hour = jewellry_per_hour

    df = Items.make_double_supplies_2(supply_name_list, supply_name_list_2, product_name_list, 1, 2, 1,
                                      actions_per_hour, xp_each_list)

    df['Product'] = 'Lunar: ' + df['Product']
    df['Level'] = level_list
    return df

#print(string_jewellery())

def plank_make():
    planks_per_hour = 1851
    supply_name_list = ['logs', 'oak_logs', 'teak_logs', 'mahogany_logs']
    product_name_list = ['plank', 'oak_plank', 'teak_plank', 'mahogany_plank']

    supply_price_list_2 = [70, 175, 350, 1050]
    xp_each_list = [90 for i in supply_name_list]
    level_list = [86 for x in supply_name_list]
    
    df = pd.read_csv(r"item_list.csv")

    supply_price_list = Items.parse_df_prices(df, supply_name_list)
    product_price_list = Items.parse_df_prices(df, product_name_list)

    rune_price_list = Items.parse_df_prices(df, ['astral_rune', 'nature_rune'])

    cost_list = [product_price_list[x] - supply_price_list[x] - supply_price_list_2[x] - rune_price_list[0] * 2
                 - rune_price_list[1] for x in range(len(supply_name_list))]
    actions_per_hour = planks_per_hour

    df = pd.DataFrame()
    df['Product'] = ['Lunar: ' + product_name_list[x] for x in range(len(product_name_list))]
    df['XP/HR'] = Items.get_xp_hour(xp_each_list, actions_per_hour)
    df['GP/HR'] = Items.get_profit_hour(cost_list, actions_per_hour)
    df['Cost'] = cost_list
    df['Base Ingredient'] = supply_name_list
    df['Base Ingredient Cost'] = supply_price_list
    df['Secondary Ingredient'] = ['N/A' for x in range(len(supply_price_list))]
    df['Secondary Ingredient Cost'] = [0 for i in range(len(supply_price_list))]
    df['Level'] = level_list
    return df

#print(plank_make())

# returns 1 lunar magic df
def make_lunars():
    df = bake_pie()
    df_2 = humidify()
    df = df.append(df_2)

    df_2 = hunter_kit()
    df = df.append(df_2)

    df_2 = spin_flax()
    df = df.append(df_2)

    df_2 = super_glass_make()
    df = df.append(df_2)

    df_2 = tan_leather()
    df = df.append(df_2)

    df_2 = string_jewellery()
    df = df.append(df_2)

    df_2 = plank_make()
    df = df.append(df_2)
    return df


# returns one magic df
def make_magic():
    df = make_bolt_enchantments()
    df_2 = make_superheat()
    df = df.append(df_2)

    df_2 = make_camelot_teleport()
    df = df.append(df_2)

    df_2 = make_high_alchemy()
    df = df.append(df_2)

    df_2 = make_ancients()
    df = df.append(df_2)

    df_2 = make_lunars()
    df = df.append(df_2)

    return df

#print(make_magic())