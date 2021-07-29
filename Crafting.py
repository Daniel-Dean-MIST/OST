import Items
import pandas as pd


# returns gem df
def make_gems():
    gems_per_hour = 2640
    cut_xp_list = [15, 20, 25, 50, 67.5, 85, 107.5, 137.5]
    actions_per_hour = gems_per_hour
    xp_each_list = cut_xp_list

    supply_name_list = ['uncut_opal', 'uncut_jade', 'uncut_red_topaz', 'uncut_sapphire', 'uncut_emerald', 'uncut_ruby',
                        'uncut_diamond', 'uncut_dragonstone']
    product_name_list = ['opal', 'jade', 'red_topaz', 'sapphire', 'emerald', 'diamond', 'ruby', 'dragonstone']

    df = Items.make_product(supply_name_list, product_name_list, 1, 1, actions_per_hour, xp_each_list)
    df['Product'] = 'Cut: ' + df['Product']
    return df

#print(make_gems())


# returns leather df
def make_leather():
    product_name_list = ['leather_gloves', 'leather_boots', 'leather_cowl', 'leather_vambraces', 'leather_body',
                         'leather_chaps']
    supply_name_list = ['leather' for x in range(len(product_name_list))]
    leather_xp_each_list = [13.8, 16.2, 18.5, 22, 25, 18]
    leather_per_hour = 1872
    xp_each_list = leather_xp_each_list
    actions_per_hour = leather_per_hour

    df = Items.make_product(supply_name_list, product_name_list, 1, 1, actions_per_hour, xp_each_list)
    return df


#print(make_leather())

# Finds out our battlestaff information
def make_staves():
    supply_name_list = ['battlestaff']
    supply_name_list_2 = ['water_orb', 'earth_orb', 'fire_orb', 'air_orb']
    supply_name_list = ['battlestaff' for x in range(len(supply_name_list_2))]
    product_name_list = ['water_battlestaff', 'earth_battlestaff', 'fire_battlestaff', 'air_battlestaff']
    xp_each_list = [100, 112.5, 125, 137.5]
    staves_per_hour = 2450
    actions_per_hour = staves_per_hour

    df = Items.make_double_supplies(supply_name_list, supply_name_list_2, product_name_list, 1, 1, actions_per_hour, xp_each_list)

    return df

#print(make_staves())


# Does all of our dragonhide items
def make_dragonhide_leather():
    supply_name_list = ['green_dragon_leather', 'blue_dragon_leather', 'red_dragon_leather', 'black_dragon_leather']
    product_name_list = ["green_d'hide_body", "blue_d'hide_body", "red_d'hide_body", "black_d'hide_body"]
    xp_each_list = [186, 210, 234, 258]
    bodies_per_hour = 1650
    actions_per_hour = bodies_per_hour
    df = Items.make_product(supply_name_list, product_name_list, 3, 1, actions_per_hour, xp_each_list)

    '''
    body_cost = Items.get_price(Items.get_item_info(body_id_list, response))
    leather_cost = Items.get_price(Items.get_item_info(leather_id_list, response))
    leather_cost = [x * 3 for x in leather_cost]
    '''

    return df

#print(make_dragonhide_leather()['GP/HR'])


# makes our glass items
def make_glass():
    product_name_list = ['beer_glass', 'empty_candle_lantern', 'empty_oil_lamp', 'vial', 'empty_fishbowl',
                         'unpowered_orb',
                         'lantern_lens']
    supply_name_list = ['molten_glass' for x in range(len(product_name_list))]
    xp_each_list = [17, 19, 25, 35, 42.5, 52.5, 55]

    glass_items_per_hour = 1700
    actions_per_hour = glass_items_per_hour
    df = Items.make_product(supply_name_list, product_name_list, 1, 1, actions_per_hour, xp_each_list)

    df_2 = pd.DataFrame()

    df_2['Product'] = ['Empty light orb']
    df_2['XP/HR'] = [70 * glass_items_per_hour]
    df_2['GP/HR'] = [df['Base Ingredient Cost'].iloc[0] * -glass_items_per_hour]
    df_2['Cost'] = df['Base Ingredient Cost'].iloc[0]
    df_2['Base Ingredient'] = ['Molten glass']
    df_2['Base Ingredient Cost'] = [df['Base Ingredient Cost'].iloc[0]]
    df_2['Secondary Ingredient'] = ['N/A']
    df_2['Secondary Ingredient Cost'] = [0]

    df = df.append(df_2)

    return df

#print(make_glass()['GP/HR'])


def make_bracelets():

    supply_name_list_2 = ['onion_seed','sapphire', 'emerald', 'ruby', 'diamond', 'dragonstone']
    product_name_list = ['gold_bracelet', 'sapphire_bracelet', 'emerald_bracelet', 'ruby_bracelet', 'diamond_bracelet',
                         'dragonstone_bracelet']
    supply_name_list = ['gold_bar' for x in range(len(product_name_list))]

    xp_each_list = [25, 60, 65, 90, 95, 110]
    gold_bracelets_per_hour = 1480
    actions_per_hour = gold_bracelets_per_hour

    df = Items.make_double_supplies(supply_name_list, supply_name_list_2, product_name_list, 1, 1, actions_per_hour, xp_each_list)
    return df

#print(make_bracelets())


def make_super_glass_make():
    df = pd.read_csv(r"item_list.csv")

    supply_name_list = Items.parse_df_prices(df, ['astral_rune'])
    supply_name_list_2 = Items.parse_df_prices(df, ['giant_seaweed'])
    supply_name_list_3 = Items.parse_df_prices(df, ['bucket_of_sand'])
    product_name_list = Items.parse_df_prices(df, ['molten_glass'])

    # multiply prices by quantity used or quantity made per inventory
    astral_rune_price = 2 * supply_name_list[0]
    giant_seaweed_price = 3 * supply_name_list_2[0]
    buckets_of_sand_price = 18 * supply_name_list_3[0]
    molten_glass_price = 27 * product_name_list[0]
    super_glass_makes_per_hour = 819
    # 1638 astrals in an hour

    # 2 astrals, 3 giant seaweed, and 18 buckets of sand each inventory
    # 819 inventories an hour
    df = pd.DataFrame()

    df['Product'] = ['Super Glass Make']
    df['XP/HR'] = [super_glass_makes_per_hour * 10 * 18]
    df['GP/HR'] = [super_glass_makes_per_hour * (
                molten_glass_price - astral_rune_price - giant_seaweed_price - buckets_of_sand_price)]
    df['Cost'] = [molten_glass_price - astral_rune_price - giant_seaweed_price - buckets_of_sand_price]
    df['Base Ingredient'] = ['Giant Seaweed, Buckets of Sand']
    df['Base Ingredient Cost'] = [astral_rune_price + giant_seaweed_price + buckets_of_sand_price]
    df['Secondary Ingredient'] = ['Astral rune']
    df['Secondary Ingredient Cost'] = [astral_rune_price]

    return df

#print(make_super_glass_make()[['XP/HR','GP/HR']])


def make_amethyst():

    product_name_list = ['amethyst_bolt_tips', 'amethyst_arrowtips', 'amethyst_javelin_heads', 'amethyst_dart_tip']
    supply_name_list = ['amethyst' for x in range(len(product_name_list))]
    amethyst_per_hour = 2750
    actions_per_hour = amethyst_per_hour
    xp_each_list = [60 for x in range(len(product_name_list))]

    product_quantity = [15, 15, 5, 8]

    df = Items.make_product(supply_name_list[:2], product_name_list[:2], 1, 15, actions_per_hour, xp_each_list[:2])
    df_2 = Items.make_product(supply_name_list[2:3], product_name_list[2:3], 1, 5, actions_per_hour, xp_each_list[2:3])
    df_3 = Items.make_product([supply_name_list[3]], [product_name_list[3]], 1, 8, actions_per_hour, [xp_each_list[3]])

    df = df.append(df_2)
    df = df.append(df_3)

    return df

#print(make_amethyst()[['GP/HR', 'XP/HR']])


def make_crafting():
    df = pd.DataFrame()

    df = make_gems()

    df_2 = make_leather()
    df = df.append(df_2)

    df_2 = make_staves()
    df = df.append(df_2)

    df_2 = make_dragonhide_leather()
    df = df.append(df_2)

    df_2 = make_glass()
    df = df.append(df_2)

    df_2 = make_bracelets()
    df = df.append(df_2)

    df_2 = make_super_glass_make()
    df = df.append(df_2)

    df_2 = make_amethyst()
    df = df.append(df_2)

    return df

#print(make_crafting()[['Product', 'GP/HR', 'XP/HR']])