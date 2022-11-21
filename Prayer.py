import Items
import pandas as pd

# print(str(body_rune_price) + ' ' + str(nature_rune_price) + ' ' + str(soul_rune_price) + ' ' + str(blood_rune_price))


# makes our ensouled head dataframe
def make_heads():
    monsters_per_hour = 220
    xp_each_list_2 = [130, 182, 286, 364, 454, 480, 494, 520, 584, 650, 716, 754, 780, 832, 884, 936, 1040, 1104, 1170,
                      1234, 1300, 1560]

    rune_list = ['body_rune', 'nature_rune', 'soul_rune', 'blood_rune']

    df = pd.read_csv(r"item_list.csv")

    rune_price_list = Items.parse_df_prices(df, rune_list)

    body_rune_price = rune_price_list[0]
    nature_rune_price = rune_price_list[1]
    soul_rune_price = rune_price_list[2]
    blood_rune_price = rune_price_list[3]

    head_list = ['ensouled_goblin_head', 'ensouled_monkey_head', 'ensouled_imp_head', 'ensouled_minotaur_head',
					'ensouled_scorpion_head', 'ensouled_bear_head', 'ensouled_unicorn_head', 'ensouled_dog_head',
					'ensouled_chaos_druid_head', 'ensouled_giant_head', 'ensouled_ogre_head', 'ensouled_elf_head', 'ensouled_troll_head',
					'ensouled_horror_head', 'ensouled_kalphite_head', 'ensouled_dagannoth_head', 'ensouled_bloodveld_head',
					'ensouled_tzhaar_head', 'ensouled_demon_head', 'ensouled_aviansie_head', 'ensouled_abyssal_head',
					'ensouled_dragon_head']
    
    supply_1_list = []
    supply_1_price_list = []
    supply_1_name_list = []

    supply_2_price_list = []
    # gets our info for our ensouled heads
    #supply_1_list = Items.get_item_info(head_id_list, response)
    supply_1_price_list = Items.parse_df_prices(df, head_list)
    supply_1_name_list = head_list

    rune_price = int(body_rune_price) * 2 + int(nature_rune_price) * 1
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 3 + int(nature_rune_price) * 1
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 3 + int(nature_rune_price) * 2
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 4 + int(nature_rune_price) * 2
    supply_2_price_list.append(rune_price)

    rune_price = int(nature_rune_price) * 1 + int(soul_rune_price) * 1
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 1 + int(nature_rune_price) * 1 + int(soul_rune_price) * 1
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 2 + int(nature_rune_price) * 1 + int(soul_rune_price) * 1
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 2 + int(nature_rune_price) * 2 + int(soul_rune_price) * 1
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 3 + int(nature_rune_price) * 2 + int(soul_rune_price) * 1
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 4 + int(nature_rune_price) * 2 + int(soul_rune_price) * 1
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 4 + int(nature_rune_price) * 3 + int(soul_rune_price) * 1
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 2 + int(nature_rune_price) * 2 + int(soul_rune_price) * 2
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 3 + int(nature_rune_price) * 2 + int(soul_rune_price) * 2
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 4 + int(nature_rune_price) * 2 + int(soul_rune_price) * 2
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 4 + int(nature_rune_price) * 3 + int(soul_rune_price) * 2
    supply_2_price_list.append(rune_price)

    rune_price = int(body_rune_price) * 4 + int(nature_rune_price) * 3 + int(soul_rune_price) * 3
    supply_2_price_list.append(rune_price)

    rune_price = int(blood_rune_price) * 1 + int(nature_rune_price) * 2 + int(soul_rune_price) * 2
    supply_2_price_list.append(rune_price)

    rune_price = int(blood_rune_price) * 1 + int(nature_rune_price) * 3 + int(soul_rune_price) * 2
    supply_2_price_list.append(rune_price)

    rune_price = int(blood_rune_price) * 1 + int(nature_rune_price) * 4 + int(soul_rune_price) * 2
    supply_2_price_list.append(rune_price)

    rune_price = int(blood_rune_price) * 1 + int(nature_rune_price) * 4 + int(soul_rune_price) * 3
    supply_2_price_list.append(rune_price)

    rune_price = int(blood_rune_price) * 1 + int(nature_rune_price) * 4 + int(soul_rune_price) * 4
    supply_2_price_list.append(rune_price)

    rune_price = int(blood_rune_price) * 2 + int(nature_rune_price) * 4 + int(soul_rune_price) * 4
    supply_2_price_list.append(rune_price)

    # gets our total_cost
    total_cost_list = []

    i = 0

    while i < len(supply_2_price_list):
        total_cost = int(supply_2_price_list[i]) + int(supply_1_price_list[i])
        total_cost_list.append(-total_cost)

        i += 1

    specialty_profit_per_hour_list = Items.get_profit_hour(total_cost_list, monsters_per_hour)

    df = pd.DataFrame()

    df['Product'] = supply_1_name_list
    df['XP/HR'] = Items.get_xp_hour(xp_each_list_2, monsters_per_hour)
    df['GP/HR'] = specialty_profit_per_hour_list
    df['Cost'] = total_cost_list
    df['Base Ingredient'] = supply_1_name_list
    supply_1_price_list = [-x for x in supply_1_price_list]
    df['Base Ingredient Cost'] = supply_1_price_list
    df['Secondary Ingredient'] = supply_1_name_list
    df['Secondary Ingredient Cost'] = supply_1_price_list

    # eliminates untraded items
    for x in df.iterrows():
        if x[1][5] == 0:
            # print(x[1][5])
            df = df.drop(x[0])
            
    return df

#print(make_heads())

# print(Items.get_xp_hour(xp_each_list, gilded_per_hour))
# print(Items.get_xp_hour(xp_each_list, chaos_per_hour))

def make_prayer():
    level_list = []
    gilded_per_hour = 2550
    chaos_per_hour = 2000
    xp_each_list = [15.7, 15.7, 15.7, 17.5, 18.5, 52.5, 52.5, 78.7, 87.5, 105, 175, 252, 252, 280, 294, 297.5, 336, 385,
                    437.5, 490, 525]
    
    supply_name_list = ['bones', 'wolf_bones', 'burnt_bones', 'monkey_bones', 'bat_bones', 'big_bones', 'jogre_bones',
                        'zogre_bones',
                        'shaikahan_bones', 'babydragon_bones', 'wyrm_bones', 'wyvern_bones', 'dragon_bones',
                        'drake_bones', 'fayrg_bones',
                        'lava_dragon_bones', 'raurg_bones', 'hydra_bones', 'dagannoth_bones', 'ourg_bones',
                        'superior_dragon_bones']


    df = Items.make_no_product(supply_name_list, 1, 0, chaos_per_hour, xp_each_list)
    df['Product'] = '(Chaos): ' + df['Base Ingredient']

    df['Cost'] /= 2
    df['GP/HR'] /= 2

    df_2 = Items.make_no_product(supply_name_list, 1, 0, gilded_per_hour, xp_each_list)
    df_2['Product'] = '(Gilded): ' + df_2['Base Ingredient']
    df = df.append(df_2)

    #df['Secondary Ingredient'] = ['N/A' for x in range(len(df['Cost']))]
    #df['Secondary Ingredient Cost'] = [0 for x in range(len(df['Cost']))]

    # print(df)

    df = df.append(make_heads())
    level_list = [1 for x in df['Product']]
    df['Level'] = level_list
    return df

#print(make_prayer())

# response = Items.get_all_items()
# df = make_prayer(response)
# print(df[['Product', 'GP/HR', 'XP/HR']])
# print(df[['Product', 'Cost', 'Base Ingredient', 'Base Ingredient Cost']])
# df = make_heads()
# print(df[['Product', 'GP/HR', 'XP/HR']])

# print(make_prayer()[['Product', 'GP/HR', 'XP/HR']])

#print(make_prayer())