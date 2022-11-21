from flask import Flask
from flask import render_template, url_for, jsonify, request
import json
import Experience, Money_Makers, Training, Items, Herblore, Prayer, Crafting, Magic, Fletching, Smithing, Construction, \
    Firemaking, Cooking
import pandas as pd

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello_world():
    name = "OSTime"
    total_hours = [100, 1000, 10000]

    level = 75
    
    labels = ['Herblore', 'Prayer', 'Crafting', 'Magic', 'Fletching', 'Smithing', 'Construction', 'Firemaking',
              'Cooking']
    gp_hour = 2400000
    skill = 'Magic'

    big_list = Training.make_chart(gp_hour, 'Herblore')
    total_hours = big_list[1][:1]
    big_list = Training.make_chart(gp_hour, 'Prayer')
    total_hours += big_list[1][:1]
    big_list = Training.make_chart(gp_hour, 'Crafting')
    total_hours += big_list[1][:1]
    big_list = Training.make_chart(gp_hour, 'Magic')
    total_hours += big_list[1][:1]
    big_list = Training.make_chart(gp_hour, 'Fletching')
    total_hours += big_list[1][:1]
    big_list = Training.make_chart(gp_hour, 'Smithing')
    total_hours += big_list[1][:1]
    big_list = Training.make_chart(gp_hour, 'Construction')
    total_hours += big_list[1][:1]
    big_list = Training.make_chart(gp_hour, 'Firemaking')
    total_hours += big_list[1][:1]
    big_list = Training.make_chart(gp_hour, 'Cooking')
    total_hours += big_list[1][:1]

    colors = big_list[2]

    print(labels, total_hours)
    # print(name, total_hours, table_string, labels, colors)
    # return 'Hello, World!'
    #table_string = Training.make_table_string(1000000, 'False', username)
    table_string = Training.make_table_string(1000000, 'False', level)
    # Training.make_everything()
    return render_template('test.html', name=name, total_hours=total_hours, table_string=table_string, labels=labels,
                           colors=colors)


@app.route('/beta')
def data22():
    return 'test'


# base json everything
# read in gp hr
# json -> df to optimize for specifig gp hr
# df -> json
# display json

def big_one():
    big_one = "EDP445 On that V"
    return render_template('test.html', big_one=big_one)


@app.route('/5m', methods=['POST'])
def data():
    macro = request.form['macro']
    level = request.form['level']
    level = Training.make_level_cleanup(level)
    #username = request.form['my-username']
    #table_string = Training.make_table_string(5000000, macro, username)
    table_string = Training.make_table_string(5000000, macro, level)

    # print(my_data["Base Ingredient"]["Teak plank"])
    # e = [print(x) for x in my_data["Base Ingredient"]]
    # print(table_string)
    return table_string


@app.route('/2_5m', methods=['POST'])
def data_2():
    macro = request.form['macro']
    level = request.form['level']
    level = Training.make_level_cleanup(level)
    #table_string = Training.make_table_string(2500000, macro, username)
    table_string = Training.make_table_string(2500000, macro, level)

    return table_string


@app.route('/1m', methods=['POST'])
def data_3():
    macro = request.form['macro']
    level = request.form['level']
    level = Training.make_level_cleanup(level)
    #table_string = Training.make_table_string(1000000, macro, username)
    table_string = Training.make_table_string(1000000, macro, level)
    '''
    skill_name_list = ['Herblore', 'Prayer', 'Crafting', 'Magic', 'Fletching', 'Smithing', 'Construction', 'Firemaking', 'Cooking']
    json_list = ['Herblore.json', 'Prayer.json', 'Crafting.json', 'Magic.json', 'Fletching.json', 'Smithing.json', 'Construction.json', 'Firemaking.json', 'Cooking.json']

    i = 0

    table_string = ''

    total_hours = 0
    training_hours = 0
    money_hours = 0

    while i < len(skill_name_list):
        my_data = pd.read_json(json_list[i])

        table_string += '<tr>'
        table_string += '<td>' +  skill_name_list[i] + '</td>'
        table_string += '<td>' +  str(my_data['Product'].to_dict()[0]) + '</td>'
        table_string += '<td>' +  str(my_data['Total Hours'].to_dict()[0]) + '</td>'
        table_string += '<td>' +  str(my_data['Training Hours'].to_dict()[0]) + '</td>'
        table_string += '<td>' +  str(my_data['Money Making Hours'].to_dict()[0]) + '</td>'
        table_string += "</tr>"

        total_hours += int(my_data['Total Hours'].to_dict()[0])
        training_hours += int(my_data['Training Hours'].to_dict()[0])
        money_hours += int(my_data['Money Making Hours'].to_dict()[0])

        i += 1

    table_string += '<tr><td>Total Hours:</td><td>----</td><td>' + str(total_hours) + '</td><td>' + str(training_hours) + '</td><td>' + str(money_hours) + '</td></tr>'

    #print(my_data["Base Ingredient"]["Teak plank"])
    #e = [print(x) for x in my_data["Base Ingredient"]]
    '''
    return table_string


# cleans up the users input and returns the table string
@app.route('/titty', methods=['POST'])
def titty():
    skill_name_list = ['Herblore', 'Prayer', 'Crafting', 'Magic', 'Fletching', 'Smithing', 'Construction', 'Firemaking',
                       'Cooking']
    json_list = ['Herblore.json', 'Prayer.json', 'Crafting.json', 'Magic.json', 'Fletching.json', 'Smithing.json',
                 'Construction.json', 'Firemaking.json', 'Cooking.json']

    gp_hour = request.form['gp']
    macro = request.form['macro']
    level = request.form['level']
    level = Training.make_level_cleanup(level)
    

    price = Training.make_string_cleanup(gp_hour)
    print(level)
    try:
        table_string = Training.make_table_string(price, macro, level)
    except:
        table_string = Training.make_table_string(1000000, macro, level)
    #print(table_string)
    return table_string


# makes tables for the skill that is clicked
@app.route('/lover', methods=['POST'])
def lover():
    gp_hour = request.form['gp']
    skill = request.form['skill']
    macro = request.form['macro']
    level = request.form['level']
    
    price = Training.make_string_cleanup(gp_hour)
    level = Training.make_level_cleanup(level)

    table_string = Training.make_skill_string(price, skill, macro, level)

    # colors = 'MediumSeaGreen'
    # print('wtf')
    #print(level)
    return table_string

#returns info about ostime.gg when clicked
@app.route('/info', methods=['POST'])
def info():
    table_string = '<tr>'
    table_string += '<td>Questions and Answers</td>'
    table_string += '</tr>'
    table_string = '<tr>'
    table_string += '<td>How Does OSTime Work?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>It calculates the Total Hours required for a user to both train from 1-99 using different methods, and calculates the required amount of time it would take a user to pay off said training. Total Hours = Training Hours + Money Hours. Input the GP/HR you can make from your preffered money method, and my tool will do the rest!</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>What exactly are "Money Hours"?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>Money Hours are simply the amount of GP/HR you can make doing your preferred money making method. This is different for everyone, as everyone has different methods of making money.</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>What is the "Efficient" Column?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>How Efficient Each Training Method is Compared to the Best Training Method for Each Skill. Based off of Total Hours.</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>What does the "Macro Hours" Option do?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>It takes into account training methods that are profitable, and calculates the amount of Money Hours they would save you from having to do for another method or skill. It is similar to "Banking" Money Hours that can be "Withdrawn" for future training endevours.</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>Can you give an example of OSTime in practice?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td><img class="big_img" src="/static/img/OSTime_Example.PNG"></button></td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>Where can I find Good Money Makers?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td><a href="https://oldschool.runescape.wiki/w/Money_making_guide">The Official OSRS Money Making Wiki</a></td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>Where is the Pricing Data pulled from to Help Calculate Money Hours?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>The Official OSRS Wiki/Runelite API</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>How were Training Hours Calculated for Each Method?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>From their respective Wiki Pages and Personal Expirimentation</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>How Can I Contact You?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>You can @ me on Twitter using the Twitter Icon Up Above</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>How Often is the Data Updated?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>About Once Per Day</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>What is Your Current Road Map?</td>'
    table_string += '</tr>'
    table_string += '<tr>'
    table_string += '<td>Calculations for Profitable Training Methods, Disclaimers for Methods using Low Volume Traded Items, Adding the Runecrafting Skill, and Adding Charts</td>'
    table_string += '</tr>'
    '''
    'OSTime optimizes the best training methods for your account based off of a simple formula. \nTotal Hours = Training Hours + Money Hours to pay for the Training Hours. It does this under the assumption that you are going from 1-99 in each skill. Ie. how long it would take you to gain 13m XP doing each training method' \
                   '\n Example: In the prayer tab it would take a user who"s preferred money maker profits 1m GP/HR 37.24 hours to get 99 prayer by doing Wyrm Bones on the chaos altar. It would take the same user 38.69 hours of money making to fund this training. In total the user would spend 75.93 Total Hours split between 37.24 hours training and 38.96 hours money making to pay for the training.' \
                   + '\n This is done for all training methods listed on the site to give you the best'\
                   'training methods specific to your account. ' \
                   + 'The Efficient : Column refers to how efficient each training method is in relation to the best training method found'\
                   + 'Enter how much GP/HR you make doing your preferred money maker, and OSTime will find the most efficient methods for your account! '
    '''

    return table_string

'''
@app.route('/chart')
def chart():
    # gp_hour = request.form['gp']
    # skill = request.form['skill']

    gp_hour = 2400000
    skill = 'Herblore'

    results = Training.make_chart(gp_hour, skill)

    products = results[0]

    return [1]
'''
if __name__ =='__main__':
    app.run()