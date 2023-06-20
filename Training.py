import pandas as pd
import json
import Experience, Money_Makers, Items, Herblore, Prayer, Crafting, Magic, Fletching, Smithing, Construction, \
    Firemaking, Cooking
import time

player_level = 1

# finds how many hours the user needs to make money
# finds how many hours the user needs to train using the method
# finds the total amount of hours to reach their goal :)
def optimize_training(df, money_df, needed_exp):
    df2 = df

    df2['Money Making Activity'] = money_df['Activity']

    # how many hours our user needs to train
    total_training_hours = round(needed_exp / df['XP/HR'], 2)

    df2['Training Hours'] = total_training_hours

    # how much money we need to fund their desired level
    df2['GP/XP'] = df2['GP/HR'] / df2['XP/HR']
    training_cost = -round(needed_exp * df2['GP/XP'] / 1000000, 2)
    df2['Training Cost'] = training_cost

    # df2['Training Cost'] = training_cost

    money_hours_list = []
    # for every methods training cost
    for t_method in df2['Training Cost']:
        # finds how many hours it would take to pay for the method for every money making method
        money_hours = 1 * t_method * 1000000 / money_df['GP/HR'][0]
        # money_hours = -1 * t_method * 1000000 / money_df['GP/HR'][0]
        money_hours = round(money_hours, 2)
        # if the method doesn't loose any money, then we set the money making hours = 0.
        if money_hours < 0:
            money_hours = 0
        # adds our money making hours to a list
        money_hours_list.append(money_hours)

    df2['Money Making Hours'] = money_hours_list
    df2['Total Hours'] = df2['Training Hours'] + df2['Money Making Hours']

    # Sorts our df based off of Total Hours
    df2 = df2.sort_values('Total Hours')
    df2 = df2.reset_index()

    # How Efficient Each Method is Compared to the best Method
    efficiency_list = df2['Total Hours'].iloc[0] / df2['Total Hours']

    # Used to display our efficiency more cleanly
    formatted_efficiency_list = []

    for ef in efficiency_list:
        f_ef = str(round(ef * 100.00, 2)) + '%'
        formatted_efficiency_list.append(f_ef)

    df2['Efficiency'] = formatted_efficiency_list

    return df2

#for non-macro hours
def optimize_training_2(df, money_hr, player_level):
    #print(player_xp)

    if player_level < 1 or player_level > 99:
        player_level = 75
    #player_xp = int(player_xp)
    #gets the base level to xp df
    level_xp_df = Experience.get_level_xp_df()
    player_xp= level_xp_df['Xp'].loc[player_level]
    
    #if a player is level 99 then we assume they are going for 200m exp
    #else we assume they are going for 99
    if player_level == 99:
        needed_exp = 200000000
    else:
        needed_exp = level_xp_df['Xp'].loc[99] - int(player_xp)

    df2 = df

    # how many hours our user needs to train
    total_training_hours = round(needed_exp / df['XP/HR'], 2)

    df2['Training Hours'] = total_training_hours

    # how much money we need to fund their desired level
    df2['GP/XP'] = df2['GP/HR'] / df2['XP/HR']
    training_cost = -round(needed_exp * df2['GP/XP'] / 1000000, 2)
    df2['Training Cost'] = training_cost

    # df2['Training Cost'] = training_cost

    money_hours_list = []
    # for every methods training cost
    for t_method in df2['Training Cost']:
        # finds how many hours it would take to pay for the method for every money making method
        money_hours = 1 * t_method * 1000000 / money_hr
        # money_hours = -1 * t_method * 1000000 / money_hr
        money_hours = round(money_hours, 2)
        # if the method doesn't loose any money, then we set the money making hours = 0.
        if money_hours < 0:
            money_hours = 0
        # adds our money making hours to a list
        money_hours_list.append(money_hours)

    df2['Money Making Hours'] = money_hours_list
    df2['Total Hours'] = df2['Training Hours'] + df2['Money Making Hours']
    df2['Achievable XP/HR'] = round(needed_exp / df['Total Hours'], 2)

    # Sorts our df based off of Total Hours
    df2 = df2.sort_values('Total Hours')
    df2 = df2.reset_index()

    # How Efficient Each Method is Compared to the best Method
    efficiency_list = df2['Total Hours'].iloc[0] / df2['Total Hours']

    # Used to display our efficiency more cleanly
    formatted_efficiency_list = []

    for ef in efficiency_list:
        f_ef = str(round(ef * 100.00, 2)) + '%'
        formatted_efficiency_list.append(f_ef)

    df2['Efficiency'] = formatted_efficiency_list
    
    df2 = df2[df2['Level'] <= player_level]
    df2 = df2.reset_index(drop=True)
    
    return df2

#for macro hours
def optimize_training_3(df, money_hr, player_level):

    #print(player_xp)

    if player_level < 1 or player_level > 99:
        player_level = 75
    #player_xp = int(player_xp)
    #gets the base level to xp df
    level_xp_df = Experience.get_level_xp_df()
    player_xp= level_xp_df['Xp'].loc[player_level]
    
    #if a player is level 99 then we assume they are going for 200m exp
    #else we assume they are going for 99
    if player_level == 99:
        needed_exp = 200000000
    else:
        needed_exp = level_xp_df['Xp'].loc[99] - int(player_xp)

    df2 = df

    print(player_level)
    
    # how many hours our user needs to train
    total_training_hours = round(needed_exp / df['XP/HR'], 2)

    df2['Training Hours'] = total_training_hours

    # how much money we need to fund their desired level
    df2['GP/XP'] = df2['GP/HR'] / df2['XP/HR']
    training_cost = -round(needed_exp * df2['GP/XP'] / 1000000, 2)
    df2['Training Cost'] = training_cost

    # df2['Training Cost'] = training_cost

    money_hours_list = []
    # for every methods training cost
    for t_method in df2['Training Cost']:
        # finds how many hours it would take to pay for the method for every money making method
        money_hours = 1 * t_method * 1000000 / money_hr
        # money_hours = -1 * t_method * 1000000 / money_hr
        money_hours = round(money_hours, 2)
        # if the method doesn't loose any money, then we set the money making hours = 0.
        #if money_hours < 0:
        #    money_hours = 0
        # adds our money making hours to a list
        money_hours_list.append(money_hours)

    df2['Money Making Hours'] = money_hours_list
    df2['Total Hours'] = df2['Training Hours'] + df2['Money Making Hours']

    #print(df2['Total Hours'])

    # Sorts our df based off of Total Hours
    df2 = df2.sort_values('Total Hours')
    df2 = df2.reset_index()

    # How Efficient Each Method is Compared to the best Method
    efficiency_list = df2['Total Hours'].iloc[0] / df2['Total Hours']
    df3 = df2

    #saves our total hours from df3 before it gets changed
    temp_total_list = df3['Total Hours'].to_list()

    #if our total hours is - then we make it positive in df3 to make an accuracte efficiency metric
    if df3['Total Hours'].iloc[0] < 0:

        df3['Total Hours'] -= df3['Total Hours'].iloc[0] * 2
        efficiency_list = df3['Total Hours'].iloc[0] / df3['Total Hours']

    # Used to display our efficiency more cleanly
    formatted_efficiency_list = []
    for ef in  efficiency_list:
        f_ef = str(round(ef * 100.00, 2)) + '%'


        formatted_efficiency_list.append(f_ef)

    df2['Efficiency'] = formatted_efficiency_list
    df2['Total Hours'] = temp_total_list
    df2['Achievable XP/HR'] = round(needed_exp / df2['Total Hours'], 2)

    #making positive xp/hr
    achieve_list = df2['Achievable XP/HR'].to_list()
    temp_list = []

    for x in achieve_list:
        if x <= 0:
            x *= -1
        temp_list.append(x)
    
    df2['Achievable XP/HR'] = temp_list

    df2 = df2[df2['Level'] <= player_level]
    df2 = df2.reset_index(drop=True)

    return df2

# gets all of our prices and returns optimized df's
def make_all_skills():
    #response = Items.get_all_items()
    df_list = []
    # 0. herb
    # 1. prayer
    # 2. crafting
    # 3. magic
    # 4. fletch
    # 5. smith
    # 6. construct
    # 7. firemake
    # 8. cook

    herb_df = Herblore.make_herblore()
    prayer_df = Prayer.make_prayer()
    craft_df = Crafting.make_crafting()
    magic_df = Magic.make_magic()
    fletch_df = Fletching.make_fletching()
    smith_df = Smithing.make_smithing()
    construct_df = Construction.make_construction()
    firemake_df = Firemaking.make_firemaking()
    cook_df = Cooking.make_cooking()
    df_list.append(herb_df)

    df_list.append(prayer_df)
    df_list.append(craft_df)
    df_list.append(magic_df)
    df_list.append(fletch_df)
    df_list.append(smith_df)
    df_list.append(construct_df)
    df_list.append(firemake_df)
    df_list.append(cook_df)

    df_list = [x.reset_index() for x in df_list]

    return df_list


# optimizes all of our skills
def optimize_all(df_list, gold_per_hour, macro, player_level):
    skill_list = ['Herblore', 'Prayer', 'Crafting', 'Magic', 'Fletching', 'Smithing', 'Construction', 'Firemaking', 'Cooking']
    level_df = pd.DataFrame()
    optimized_df_list = []
            
    i = 0
    while i < len(skill_list):
        if macro == 'true':

            optimized_df_list.append(optimize_training_3(df_list[i], gold_per_hour, player_level))

        else:

            optimized_df_list.append(optimize_training_2(df_list[i], gold_per_hour, player_level))
        i += 1
    return optimized_df_list


# jsons all of our optimized lists
def json_all(df_list, number):
    df_list[0].to_json(r'C:\Users\Daniel\Documents\Scripts\OST\flask\Herblore_' + str(number) + '.json')
    df_list[1].to_json(r'C:\Users\Daniel\Documents\Scripts\OST\flask\Prayer_' + str(number) + '.json')
    df_list[2].to_json(r'C:\Users\Daniel\Documents\Scripts\OST\flask\Crafting_' + str(number) + '.json')
    df_list[3].to_json(r'C:\Users\Daniel\Documents\Scripts\OST\flask\Magic_' + str(number) + '.json')
    df_list[4].to_json(r'C:\Users\Daniel\Documents\Scripts\OST\flask\Fletching_' + str(number) + '.json')
    df_list[5].to_json(r'C:\Users\Daniel\Documents\Scripts\OST\flask\Smithing_' + str(number) + '.json')
    df_list[6].to_json(r'C:\Users\Daniel\Documents\Scripts\OST\flask\Construction_' + str(number) + '.json')
    df_list[7].to_json(r'C:\Users\Daniel\Documents\Scripts\OST\flask\Firemaking_' + str(number) + '.json')
    df_list[8].to_json(r'C:\Users\Daniel\Documents\Scripts\OST\flask\Cooking_' + str(number) + '.json')


# json all base dfs
def json_all_base(df_list):
    df_list[0].to_json(r'Herblore.json')
    df_list[1].to_json(r'Prayer.json')
    df_list[2].to_json(r'Crafting.json')
    df_list[3].to_json(r'Magic.json')
    df_list[4].to_json(r'Fletching.json')
    df_list[5].to_json(r'Smithing.json')
    df_list[6].to_json(r'Construction.json')
    df_list[7].to_json(r'Firemaking.json')
    df_list[8].to_json(r'Cooking.json')


# makes all of our base price dfs
# makes all of our optimized dfs based off of gp
# puts all of our df data into json files
# calls itself again every 10 minutes
def make_everything():
    #player_df = Experience.get_player_level_df(username)
    Items.make_csv()
    df_list = make_all_skills()
    
    json_all_base(df_list)

    #times_updated += 1
    #print(times_updated)
    #time.sleep(5)

    #make_everything(times_updated)
    print('OSTime has been updated baby')
    return

# turns all jsons into df
# turns df information into table_string
# returns table_string
def make_table_string(price, macro, player_level):
    skill_name_list = ['Herblore', 'Prayer', 'Crafting', 'Magic', 'Fletching', 'Smithing', 'Construction', 'Firemaking',
                       'Cooking']
    id_list_2 = ['herblore2', 'prayer2', 'crafting2', 'magic2', 'fletching2', 'smithing2', 'construction2', 'firemaking2',
                       'cooking2']
        
    json_list = ['Herblore.json', 'Prayer.json', 'Crafting.json', 'Magic.json', 'Fletching.json', 'Smithing.json',
                 'Construction.json', 'Firemaking.json', 'Cooking.json']
    img_list = ['Herblore_Icon.PNG', 'Prayer_Icon.PNG', 'Crafting_Icon.PNG', 'Magic_Icon.PNG', 'Fletching_Icon.PNG',
                'Smithing_Icon.PNG', 'Construction_Icon.PNG', 'Firemaking_Icon.PNG', 'Cooking_Icon.PNG']
    
    id_list = ['herblore', 'prayer', 'crafting', 'magic', 'fletching', 'smithing', 'construction', 'firemaking',
               'cooking']

    all_data = [pd.read_json(x) for x in json_list]
    #time.sleep(5)
    #print(all_data)
    all_data = optimize_all(all_data, price, macro, player_level)
    all_data = [x.drop(x.columns[[0, 1]], axis=1) for x in all_data]
    # print(all_data)
    i = 0

    table_string = ''

    total_hours = 0
    training_hours = 0
    money_hours = 0
    achievable_xp_hr = 0

    while i < len(skill_name_list):
        my_data = all_data[i]
        # print(table_string)
        table_string += '<tr>'
        table_string += '<td class="custo">' + skill_name_list[
            i] + '</td>' + '<td><button class="Yo" id="' + id_list_2[i] + '"><img src="/static/img/' + img_list[
                            i] + '"></button></td>'
        table_string += '<td>' + str(my_data['Product'].to_dict()[0]) + '</td>'
        table_string += '<td>' + str(round(my_data['Total Hours'].to_dict()[0], 2)) + '</td>'
        table_string += '<td>' + str(round(my_data['Training Hours'].to_dict()[0], 2)) + '</td>'
        table_string += '<td>' + str(round(my_data['Money Making Hours'].to_dict()[0], 2)) + '</td>'
        table_string += '<td>' + str(round(my_data['Achievable XP/HR'].to_dict()[0] / 1000, 2)) + 'k</td>'
        table_string += "</tr>"

        total_hours += int(my_data['Total Hours'].to_dict()[0])
        training_hours += int(my_data['Training Hours'].to_dict()[0])
        money_hours += int(my_data['Money Making Hours'].to_dict()[0])
        achievable_xp_hr += int(my_data['Money Making Hours'].to_dict()[0])

        i += 1

    table_string += '<tr><td>Total Hours:</td><td><button class="Yoe"><img src="/static/img/Experience_Icon.PNG"</button></td><td>----</td><td>' + str(
        total_hours) + '</td><td>' + str(training_hours) + '</td><td>' + str(money_hours) + '</td>' + str(achievable_xp_hr) + '</td><td>'

    # print(my_data["Base Ingredient"]["Teak plank"])
    # e = [print(x) for x in my_data["Base Ingredient"]]

    return table_string

#makes table string for each skill
def make_skill_string(price, skill, checked, player_level):
    #player_level = 55
    all_data = str(skill) + '.json'
    all_data = pd.read_json(all_data)

    if checked == 'true':
        print('Hey')
        try:
            all_data = optimize_training_3(all_data, price, player_level)
        except:
            all_data = optimize_training_3(all_data, 1000000, 1)

    else:
        try:
            all_data = optimize_training_2(all_data, price, player_level)
        except:
            all_data = optimize_training_2(all_data, 1000000, 1)
    all_data = all_data.drop(all_data.columns[[0, 1]], axis=1)
    # print(all_data[['Product', 'Total Hours', 'Training Hours', 'Money Making Hours']])
    # print(all_data)

    product_list = all_data['Product'].to_list()
    my_data = all_data

    i = 0

    table_string = ''

    while i < len(product_list):
        # print(table_string)
        table_string += '<tr>'
        table_string += '<td><button class="Yoe" id="herblore"><img src="/static/img/' + skill + '_Icon.PNG"></button></td>' + '<td class="custo">' + str(
            i + 1) + '</td>'
        table_string += '<td>' + str(my_data['Product'].to_dict()[i]) + '</td>'
        table_string += '<td>' + str(round(my_data['Total Hours'].to_dict()[i], 2)) + '</td>'
        table_string += '<td>' + str(round(my_data['Training Hours'].to_dict()[i], 2)) + '</td>'
        table_string += '<td>' + str(round(my_data['Money Making Hours'].to_dict()[i], 2)) + '</td>'
        table_string += '<td>' + str(round(my_data['Achievable XP/HR'].to_dict()[i] / 1000, 2)) + 'k</td>'
        table_string += '<td>' + my_data['Efficiency'].to_dict()[i] + ' : Efficient</td>'
        table_string += "</tr>"

        i += 1

    return table_string

#gets the gp_hr and cleans it up
def make_string_cleanup(gp_hour):
    times_updated = 0
    if gp_hour == 'Titty Boi 223':
        print('A J is Amazing')

        try:
            make_everything()
            print('Done')
            return
        except:
            print('1776!')

    price = gp_hour

    is_dot = False

    if '.' in price:
        is_dot = True

    try:
        price = price.replace(' ', '')
    except:
        pass

    try:
        price = price.replace(',', '')
    except:
        pass

    try:
        price = price.replace('.', '')

    except:
        pass

    try:
        price = price.replace('k', '000')
    except:
        pass

    try:
        price = price.replace('m', '000000')
    except:
        pass

    try:
        price = price.replace('b', '000000000')
    except:
        pass

    if is_dot:
        try:
            price = price[:len(price) - 1]
        except:
            pass

    try:
        price = int(price)
    except:
        price = 1000000

    if price < 1:
        price = 1000000

    if price > 2000000000:
        price = 2000000000

    print(price)

    return price

#if the player's level isn't a valid level
#we set it to 75 by default
def make_level_cleanup(player_level):
    xp_level_df = Experience.get_level_xp_df()
    
    try:
        int(player_level)
    except:
        return 75
    
    if int(player_level) > 0 and int(player_level) < 100:
        return int(player_level)
    
    elif int(player_level) >= 99:
        return int(99)

    else:
        player_level = 75
    return player_level

#cleans up our gp_hour and our player level
#returns gp at [0]
#returns level at [1]
def get_total_cleanup(gp_hour, player_level):
    gp = make_string_cleanup(gp_hour)
    player_level = make_level_cleanup(player_level)
    
    combined_list = []
    combined_list.append(gp)
    combined_list.append(player_level)
    
    return combined_list

# returns total hours from df
def make_chart(price, skill, player_level):
    all_data = str(skill) + '.json'
    print(all_data)
    all_data = pd.read_json(all_data)
    all_data = optimize_training_2(all_data, price, player_level)
    all_data = all_data.drop(all_data.columns[[0, 1]], axis=1)

    total_hours = all_data['Total Hours'].to_list()
    products = all_data['Product'].to_list()

    color_list = ['MediumSeaGreen', '#007bff', 'LightPink', 'SlateBlue', 'IndianRed', 'MediumSeaGreen', '#007bff',
                  'LightPink', 'SlateBlue', ]

    big_list = [products, total_hours, color_list]
    return big_list


'''
print('How Much Money do You Make in an Hour? ')
money_hour = input()
money_hour = int(money_hour)
'''
# money_df = Money_Makers.make_money()
# herb_df = Herblore.make_herblore()
# prayer_df = Prayer.make_prayer()
# craft_df = Crafting.make_crafting()
# magic_df = Magic.make_magic()
# fletch_df = Fletching.make_fletching()
# df = optimize_training(craft_df, money_df, 13034431)
# smith_df = Smithing.make_smithing()
# construct_df = Construction.make_construction()
# firemake_df = Firemaking.make_firemaking()
# cook_df = Cooking.make_cooking()

# df = pd.DataFrame()
# df = optimize_training_2(construct_df, money_hour, 13034431)
# print(df[['Product', 'Total Hours', 'Training Hours', 'Money Making Hours', 'Efficiency']])
# print(df[['Product', 'Cost', 'GP/HR', 'XP/HR']])

# money_df.to_json (r'C:\Users\Daniel\Documents\Scripts\OST\flask\Money.json')


# df = optimize_training_2(prayer_df, money_hour, 13034431)
# print(df[['Product', 'Total Hours', 'Training Hours', 'Money Making Hours', 'Efficiency']])
# print(df[['Product', 'Cost', 'GP/HR', 'XP/HR']])

'''
df_list = make_all_skills()
optimized_list = optimize_all(df_list, 1400000)
for x in optimized_list:
    print(x[['Product', 'Total Hours', 'Training Hours', 'Money Making Hours', 'Efficiency']])
    # print(x[['Product', 'Cost', 'GP/HR', 'XP/HR']])
    # print(x[['Product', 'Base Ingredient', 'Secondary Ingredient']])
    # print(x[['Product', 'Cost', 'Base Ingredient Cost', 'Secondary Ingredient Cost']])
# json_all_base(df_list)


make_everything(0)
'''
#Items.make_csv()

#make_everything()