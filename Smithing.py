import Items
import pandas as pd


# makes 1 set of bars
def make_bars():

    supply_name_list = ['iron_ore', 'iron_ore', 'mithril_ore', 'adamantite_ore', 'runite_ore', 'gold_ore', 'gold_ore']
    supply_name_list_2 = ['coal' for x in supply_name_list]
    product_name_list = ['iron_bar', 'steel_bar', 'mithril_bar', 'adamantite_bar', 'runite_bar', 'gold_bar', 'gold_bar']
    xp_each_list = [12.5, 17.5, 30, 37.5, 50, 22.5, 56.2]
    bars_per_hour_list = [6000, 5400, 3600, 2700, 2150, 6000, 6400]

    #iron
    df = Items.make_double_supplies_2([supply_name_list[0]], [supply_name_list_2[0]], [product_name_list[0]], 1, 0, 1, bars_per_hour_list[0], [xp_each_list[0]])


    #steel
    df_2 = Items.make_double_supplies_2([supply_name_list[1]], [supply_name_list_2[1]], [product_name_list[1]], 1, 1, 1, bars_per_hour_list[1], [xp_each_list[1]])
    df = df.append(df_2)

    #mithril
    df_2 = Items.make_double_supplies_2([supply_name_list[2]], [supply_name_list_2[2]], [product_name_list[2]], 1, 2, 1, bars_per_hour_list[2], [xp_each_list[2]])
    df = df.append(df_2)

    #adamant
    df_2 = Items.make_double_supplies_2([supply_name_list[3]], [supply_name_list_2[3]], [product_name_list[3]], 1, 3, 1, bars_per_hour_list[3], [xp_each_list[3]])
    df = df.append(df_2)

    #rune
    df_2 = Items.make_double_supplies_2([supply_name_list[4]], [supply_name_list_2[4]], [product_name_list[4]], 1, 4, 1, bars_per_hour_list[4], [xp_each_list[4]])
    df = df.append(df_2)

    #gold bar
    df_2 = Items.make_double_supplies_2([supply_name_list[5]], [supply_name_list_2[5]], [product_name_list[5]], 1, 0, 1,
                                        bars_per_hour_list[5], [xp_each_list[5]])
    df = df.append(df_2)
    df['Product'] = 'B.F: ' + df['Product']
    #gold bar gauntlets
    df_2 = Items.make_double_supplies_2([supply_name_list[6]], [supply_name_list_2[6]], [product_name_list[6]], 1, 0, 1,
                                        bars_per_hour_list[6], [xp_each_list[6]])
    df_2['Product'] = ['B.F. Gauntlets: Gold Bar']
    df = df.append(df_2)
    return df

#print(make_bars()['GP/HR'])


def make_darts():
    supply_name_list = ['bronze_bar', 'iron_bar', 'steel_bar', 'mithril_bar', 'adamantite_bar', 'runite_bar']
    product_name_list = ['bronze_dart_tip', 'iron_dart_tip', 'steel_dart_tip', 'mithril_dart_tip',
                         'adamant_dart_tip',
                         'rune_dart_tip']

    #Items.find_mispelled_item(product_name_list)
    xp_each_list = [1.25, 2.5, 3.75, 5, 6.25, 7.5]
    actions_per_hour = 950

    df = Items.make_product(supply_name_list, product_name_list, 1, 10, actions_per_hour, xp_each_list)

    return df

#print(make_darts())

# lets us put in variable number of supply and products
def make_armor():
    product_name_list = ['steel_platebody', 'mithril_platelegs', 'mithril_plateskirt', 'mithril_platebody',
                         'adamant_platebody',
                         'rune_platelegs', 'rune_plateskirt', 'rune_2h_sword']
    supply_name_list = ['steel_bar', 'mithril_bar', 'mithril_bar', 'mithril_bar', 'adamantite_bar', 'runite_bar',
                        'runite_bar', 'runite_bar']

    supply_quantity_list = [5, 3, 3, 5, 5, 3, 3, 3]
    product_quantity_list = [1 for x in supply_quantity_list]
    actions_per_hour = 1112
    xp_each_list = [187.5, 150, 150, 250, 312.5, 225, 225, 225]
    df_list = [Items.make_product([supply_name_list[x]], [product_name_list[x]], supply_quantity_list[x], product_quantity_list[x], actions_per_hour, [xp_each_list[x]])
               for x in range(len(product_name_list))]

    #print(df_list)
    df = pd.DataFrame()
    df = df.append(df_list[0])
    df = df.append(df_list[1])
    df = df.append(df_list[2])
    df = df.append(df_list[3])
    df = df.append(df_list[4])
    df = df.append(df_list[5])
    df = df.append(df_list[6])
    df = df.append(df_list[7])
    return df


def make_cannonballs():
    supply_name_list = ['steel_bar']
    product_name_list = ['cannonball']
    xp_each_list = [25.6]
    actions_per_hour = 540

    df = Items.make_product(supply_name_list, product_name_list, 1, 4, actions_per_hour, xp_each_list)

    return df

#print(make_cannonballs())

def make_smithing():
    df = make_bars()
    df = df.append(make_darts())
    df = df.append(make_armor())
    df = df.append(make_cannonballs())

    return df

# df = make_cannonballs()

#print(make_smithing())

# print(df[['Product', 'Cost', 'GP/HR', 'XP/HR']])
# print(df[['Product', 'Base Ingredient', 'Secondary Ingredient']])