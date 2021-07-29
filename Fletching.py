import Items
import pandas as pd


def make_darts():
    supply_name_list = ['bronze_dart_tip', 'iron_dart_tip', 'steel_dart_tip', 'mithril_dart_tip', 'adamant_dart_tip',
                        'rune_dart_tip', 'dragon_dart_tip', 'amethyst_dart_tip']
    supply_name_list_2 = ['feather' for x in range(len(supply_name_list))]
    product_name_list = ['bronze_dart', 'iron_dart', 'steel_dart', 'mithril_dart', 'adamant_dart',
                         'rune_dart', 'dragon_dart', 'amethyst_dart']
    xp_each_list = [1.8, 3.8, 7.5, 11.2, 15, 18.8, 25, 21]
    actions_per_hour = 126000
    # 25 darts per game tick average

    df = Items.make_double_supplies(supply_name_list, supply_name_list_2, product_name_list, 10, 10, actions_per_hour,
                                    xp_each_list)
    return df

def make_arrows():
    supply_name_list_2 = ['bronze_arrowtips', 'iron_arrowtips', 'steel_arrowtips', 'mithril_arrowtips',
                          'broad_arrowheads', 'adamant_arrowtips', 'rune_arrowtips', 'amethyst_arrowtips',
                          'dragon_arrowtips']
    product_name_list = ['bronze_arrow', 'iron_arrow', 'steel_arrow', 'mithril_arrow',
                         'onion_seed', 'adamant_arrow',
                         'rune_arrow', 'amethyst_arrow', 'dragon_arrow']
    supply_name_list = ['headless_arrow' for x in range(len(supply_name_list_2))]

    xp_each_list = [1.3, 2.5, 5, 7.5, 10, 10, 12.5, 13.5, 15]
    actions_per_hour = 45000

    #headless arrow
    df = Items.make_double_supplies(['arrow_shaft'], ['feather'], ['headless_arrow'], 15, 15, actions_per_hour,
                                    [1])

    df_2 = Items.make_double_supplies(supply_name_list, supply_name_list_2, product_name_list, 15, 15,
                                    actions_per_hour,
                                    xp_each_list)

    df = df.append(df_2)
    product_name_list = ['headless_arrow', 'bronze_arrow', 'iron_arrow', 'steel_arrow', 'mithril_arrow',
                         'broad_arrow', 'adamant_arrow',
                         'rune_arrow', 'amethyst_arrow', 'dragon_arrow']

    df['Product'] = product_name_list
    return df


def cut_bows():
    supply_name_list = ['logs', 'logs', 'oak_logs', 'oak_logs', 'willow_logs', 'willow_logs', 'maple_logs', 'maple_logs',
                        'yew_logs', 'yew_logs', 'magic_logs', 'magic_logs']
    product_name_list = ['shortbow_(u)', 'longbow_(u)', 'oak_shortbow_(u)', 'oak_longbow_(u)', 'willow_shortbow_(u)', 'willow_longbow_(u)',
                         'maple_shortbow_(u)', 'maple_longbow_(u)', 'yew_shortbow_(u)', 'yew_longbow_(u)', 'magic_shortbow_(u)',
                         'magic_longbow_(u)']
    xp_each_list = [5, 10, 16.5, 25, 33.33, 41.5, 50, 58.3, 67.5, 75, 83.3, 91.5]
    actions_per_hour = 1700

    df = Items.make_product(supply_name_list, product_name_list, 1, 1, actions_per_hour, xp_each_list)
    df['Product'] = 'Cut: ' + df['Product']
    return df

def string_bows():
    supply_name_list = ['logs', 'logs', 'oak_logs', 'oak_logs', 'willow_logs', 'willow_logs', 'maple_logs',
                        'maple_logs',
                        'yew_logs', 'yew_logs', 'magic_logs', 'magic_logs']
    product_name_list = ['shortbow', 'longbow', 'oak_shortbow', 'oak_longbow', 'willow_shortbow', 'willow_longbow',
                         'maple_shortbow', 'maple_longbow', 'yew_shortbow', 'yew_longbow', 'magic_shortbow',
                         'magic_longbow']
    supply_name_list_2 = ['bow_string' for x in range(len(product_name_list))]
    xp_each_list = [5, 10, 16.5, 25, 33.33, 41.5, 50, 58.3, 67.5, 75, 83.3, 91.5]
    actions_per_hour = 2450

    df = Items.make_double_supplies(supply_name_list, supply_name_list_2, product_name_list, 15, 15,
                                    actions_per_hour,
                                    xp_each_list)
    df['Product'] = 'String: ' + df['Product']
    return df

def make_battlestaves():
    supply_name_list = ['celastrus_bark']
    product_name_list = ['battlestaff']
    xp_each_list = [80]
    actions_per_hour = 1700

    df = Items.make_product(supply_name_list, product_name_list, 1, 1, actions_per_hour, xp_each_list)
    return df

def make_redwood_shields():
    supply_name_list = ['redwood_logs']
    product_name_list = ['redwood_shield']
    xp_each_list = [92]
    actions_per_hour = 1826

    df = Items.make_product(supply_name_list, product_name_list, 2, 1, actions_per_hour, xp_each_list)
    return df


def make_fletching():
    df = pd.DataFrame()

    df = make_darts()
    df_2 = make_arrows()
    df = df.append(df_2)

    df_2 = cut_bows()
    df = df.append(df_2)

    df_2 = string_bows()
    df = df.append(df_2)

    df_2 = make_battlestaves()
    df = df.append(df_2)

    df_2 = make_redwood_shields()
    df = df.append(df_2)

    return df

'''
df = make_fletching()
print(df)

print(df[['Product', 'Cost', 'GP/HR', 'XP/HR', 'Secondary Ingredient Cost']])
print(df[['Product', 'Base Ingredient', 'Secondary Ingredient']])
'''