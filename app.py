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
    table_string = Training.make_table_string(1000000)
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


@app.route('/5m')
def data():
    table_string = Training.make_table_string(5000000)

    # print(my_data["Base Ingredient"]["Teak plank"])
    # e = [print(x) for x in my_data["Base Ingredient"]]
    # print(table_string)
    return table_string


@app.route('/2_5m')
def data_2():
    table_string = Training.make_table_string(2500000)

    return table_string


@app.route('/1m')
def data_3():
    table_string = Training.make_table_string(1000000)
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

    price = Training.make_string_cleanup(gp_hour)

    table_string = Training.make_table_string(price)

    return table_string


# makes tables for the skill that is clicked
@app.route('/lover', methods=['POST'])
def lover():
    gp_hour = request.form['gp']
    skill = request.form['skill']

    price = Training.make_string_cleanup(gp_hour)

    table_string = Training.make_skill_string(price, skill)

    # colors = 'MediumSeaGreen'
    # print('wtf')
    return table_string


@app.route('/chart')
def chart():
    # gp_hour = request.form['gp']
    # skill = request.form['skill']

    gp_hour = 2400000
    skill = 'Herblore'

    results = Training.make_chart(gp_hour, skill)

    products = results[0]

    return [1]

if __name__ =='__main__':
    app.run()