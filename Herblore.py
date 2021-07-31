import Items
import pandas as pd


# xp per potion
xp_each_list = [25, 37.5, 50, 50, 62.5, 67.5, 75, 80, 84, 87.5, 100, 106.3, 112.5, 117.5, 125, 142.5, 150, 157.5, 162.5,
                172.5, 155, 155, 180]
potions_per_hour = 2500

level_list = [3, 5, 12, 15, 22, 26, 30, 34, 36, 38, 45, 48, 50, 52, 55, 63, 66, 69, 72, 76, 80, 80, 81, 94]

# returns herblore df
def make_potions():
    #all potions - serum 207 and super combat potion
    supply_name_list = ['guam_potion_(unf)', 'marrentill_potion_(unf)', 'tarromin_potion_(unf)',
                        'harralander_potion_(unf)', 'harralander_potion_(unf)', 'harralander_potion_(unf)',
                        'toadflax_potion_(unf)', 'harralander_potion_(unf)', 'ranarr_potion_(unf)', 'irit_potion_(unf)',
                        'irit_potion_(unf)', 'avantoe_potion_(unf)', 'avantoe_potion_(unf)', 'avantoe_potion_(unf)',
                        'kwuarm_potion_(unf)', 'snapdragon_potion_(unf)', 'cadantine_potion_(unf)', 'lantadyme_potion_(unf)',
                        'dwarf_weed_potion_(unf)', 'lantadyme_potion_(unf)', 'cadantine_blood_potion_(unf)',
                        'cadantine_blood_potion_(unf)',
                        'toadflax_potion_(unf)', 'antifire_potion(4)',
                         'anti-venom(4)']

    supply_name_list_2 = ['eye_of_newt', 'unicorn_horn_dust', 'limpwurt_root', 'volcanic_ash', "red_spiders'_eggs",
                          'chocolate_dust',
                          "toad's_legs", 'goat_horn_dust', 'snape_grass', 'eye_of_newt', 'unicorn_horn_dust',
                          'snape_grass', 'mort_myre_fungus', 'kebbit_teeth_dust', 'limpwurt_root', "red_spiders'_eggs",
                          'white_berries',
                          'dragon_scale_dust', 'wine_of_zamorak', 'potato_cactus', 'wine_of_zamorak',
                          'potato_cactus', 'crushed_nest',
                          'crushed_superior_dragon_bones', 'torstol']

    product_name_list = ['attack_potion(3)', 'antipoison(3)', 'strength_potion(3)', 'compost_potion(3)',
                         'restore_potion(3)',
                         'energy_potion(3)', 'agility_potion(3)', 'combat_potion(3)', 'prayer_potion(3)',
                         'super_attack(3)',
                         'superantipoison(3)', 'fishing_potion(3)', 'super_energy(3)', 'hunter_potion(3)',
                         'super_strength(3)',
                         'super_restore(3)', 'super_defence(3)', 'antifire_potion(3)', 'ranging_potion(3)',
                         'magic_potion(3)',
                         'bastion_potion(3)', 'battlemage_potion(3)', 'saradomin_brew(3)',
                         'super_antifire_potion(4)', 'anti-venom+(4)']

    potions_per_hour = 2500
    xp_each_list = [25, 37.5, 50, 60, 62.5, 67.5, 80, 84, 87.5, 100, 106.3, 112.5, 117.5, 120, 125, 142.5, 150, 157.5,
                    162.5, 172.5, 155, 155, 180, 130, 125]
    actions_per_hour = potions_per_hour
    df = Items.make_double_supplies(supply_name_list, supply_name_list_2, product_name_list, 1, 1, actions_per_hour,
                                    xp_each_list)

    df_2 = Items.make_double_supplies_2(['super_energy(4)'], ['amylase_crystal'], ['stamina_potion(4)'],  1, 4, 1, actions_per_hour,
                                    [102])
    df = df.append(df_2)

    df_2 = Items.make_double_supplies_2(['antifire_potion(4)'], ['lava_scale_shard'], ['extended_antifire(4)'], 1, 4, 1,
                                        actions_per_hour,
                                        [110])
    df = df.append(df_2)

    df_2 = Items.make_double_supplies_2(['antidote++(4)'], ["zulrah's_scales"], ['anti-venom(4)'], 1, 20, 1,
                                        actions_per_hour,
                                        [120])
    df = df.append(df_2)

    df_2 = Items.make_double_supplies_2(['super_attack(4)'], ['super_strength(4)'], ['super_combat_potion(4)'], 1, 1, 1,
                                        actions_per_hour,
                                        [150])

    df_3 = Items.make_double_supplies_2(['super_defence(4)'], ['torstol'], ['super_combat_potion(4)'], 1, 1,
                                        1,
                                        actions_per_hour,
                                        [150])


    df_2['Cost'] = int((df_2['Cost'] + df_3['Cost']) / -14)
    df_2['GP/HR'] = df_2['Cost'] * 2166
    df_2['XP/HR'] = 150 * 2166
    print(df_2[['Cost', 'GP/HR', 'XP/HR']])
    df = df.append(df_2)

    df_2 = df_2 = Items.make_double_supplies_2(['super_antifire_potion(4)'], ['lava_scale_shard'], ['extended_super_antifire(4)'], 1, 4, 1,
                                        actions_per_hour,
                                        [160])
    df = df.append(df_2)

    df_2 = Items.make_double_supplies_2(['tarromin_potion_(unf)'], ['ashes'], ['onion_seed'], 1, 1, 1,
                                        actions_per_hour,
                                        [50])
    df_2['Product'] = ['serum_207']
    df = df.append(df_2)
    #stamina_potion(4), super_energy(4), amylase_crystal * 4
    #extended_antifire(4), antifire_potion(4), lava_scale_shard * 4
    #anti-venom(4), antidote++(4), zulrah's_scales * 20
    #super_combat_potion(4), super_attack(4) + supper_strength(4) + super_defence(4), torstol
    #extended_super_antifire_(4), super_antifire_potion(4), lava_scale_shard * 4
    #onion_seed (serum_207), tarromin_potion_(unf), ashes
    #print(len(supply_name_list), len(product_name_list), len(supply_name_list_2))

    return df

    '''
    for x in range(len(supply_name_list)):
        print(product_name_list[x], supply_name_list[x], supply_name_list_2[x])
        #print(supply_name_list_2[x])
        #print(product_name_list[x])
        '''

# returns a list of chemistry costs per hour
def get_chemistry_2(potion_3_list, potion_4_list, total_cost_list):
    chemistry_cost_per_hour_list = []
    chemistry = Items.get_item_info([21163])
    chemistry = Items.get_price(chemistry)
    chemistry = chemistry[0]
    additional_cost = chemistry / 5 * 0.05

    i = 0
    while i < len(potion_3_list):
        additional_profit = (potion_4_list[i] - potion_3_list[i]) * 0.05
        chemistry_profit = additional_profit - additional_cost
        new_potion = potion_4_list[i] + chemistry_profit - total_cost_list[i]
        new_potion = round(new_potion, 2) * 2500
        chemistry_cost_per_hour_list.append(new_potion)
        i += 1

    # print(chemistry_cost_per_hour_list)
    # print('additional cost: ' + str(additional_cost))
    # print('additional profit: ' + str(additional_profit))
    # print('chemistry_profit: ' + str(chemistry_profit))
    return chemistry_cost_per_hour_list


# returns our chemistry potion df
def get_chemistry(potion_3_list, potion_4_list, response):
    chemistry_cost_per_hour_list = []
    chemistry = Items.get_item_info([21163], response)
    chemistry = Items.get_price(chemistry)
    chemistry = chemistry[0]
    chemistry = 1200
    # print(chemistry)
    additional_cost = -chemistry / 5
    # print(additional_cost)
    # additional_cost *= 0.05
    # print(additional_cost)
    if chemistry == 0:
        return

    else:

        potion_4_list = Items.get_item_info(potion_4_list, response)
        potion_4_price_list = Items.get_price(potion_4_list)
        potion_4_name_list = Items.get_name(potion_4_list)
        potion_3_list = Items.get_item_info(potion_3_list, response)
        potion_3_price_list = Items.get_price(potion_3_list)

        og_df = make_potions(response)
        # og_df = og_df[3:]
        ingredient_1_price_list = og_df['Base Ingredient Cost'].to_list()
        ingredient_2_price_list = og_df['Secondary Ingredient Cost'].to_list()

        #
        # potion_4_price_list = [x + additional_cost for x in potion_4_price_list]
        price_list = [potion_4_price_list[x] - potion_3_price_list[x] for x in range(len(potion_4_list))]
        price_list = [x + additional_cost for x in price_list]
        price_list = [round(x * 0.05, 2) for x in price_list]
        potion_3_price_list = [potion_3_price_list[x] + price_list[x] for x in range(len(potion_4_list))]
        # print(price_list)

        print(len(potion_3_price_list), len(ingredient_1_price_list), len(ingredient_2_price_list))
        cost_list = [potion_3_price_list[x] - ingredient_1_price_list[x] - ingredient_2_price_list[x] for x in
                     range(len(potion_4_list))]

        df = pd.DataFrame()
        df['Product'] = potion_4_name_list
        df['XP/HR'] = [potions_per_hour * x for x in xp_each_list]
        df['GP/HR'] = [x * potions_per_hour for x in cost_list]
        df['Cost'] = cost_list
        df['Base Ingredient'] = og_df['Base Ingredient'].to_list()
        df['Base Ingredient Cost'] = og_df['Base Ingredient Cost'].to_list()
        df['Secondary Ingredient'] = og_df['Secondary Ingredient'].to_list()
        df['Secondary Ingredient Cost'] = og_df['Secondary Ingredient Cost'].to_list()

        df = make_potions(response)
        df = df[6:]
        df['Product'] = '(Chemistry) ' + df['Product']

        df = df.dropna()

        # df['Base Ingredient'] *= -1
        # print(df)
        return df


def make_herblore():
    df = make_potions()
    # df = df.append(get_chemistry(product_id_list, potion_4_list, response))

    '''
    # eliminates untraded items
    for x in df.iterrows():
        # print('EEEE')
        # print(x[1][5], x[1][7])
        if x[1][5] == 0 or x[1][7] == 0:
            # print(x[1][0], x[1][3])
            try:
                df = df.drop(x[0])
            except:
                pass
    '''
    return df

#print(make_herblore()['Cost'])
# df = get_chemistry(product_id_list, potion_4_list)
# df = make_herblore(response)
'''
#eliminates untraded items
for x in df.iterrows():
    if x[1][5] < 1:
        df = df.drop(x[0])
    #print(df)
'''

df = make_herblore()

print(df[['Product', 'GP/HR', 'XP/HR']])
# print(df[['Product', 'Base Ingredient', 'Base Ingredient Cost']])
# print(df[['Product', 'Cost', 'Base Ingredient Cost', 'Secondary Ingredient Cost']])