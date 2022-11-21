import Items
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_level_xp_df():
    df = pd.DataFrame()
    
    level_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
    56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
    74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91,
    92, 93, 94, 95, 96, 97, 98, 99]
    
    experience_list = [0, 0, 83, 174, 276, 388, 512, 650, 801, 969, 1154, 1358, 1584,
    1833, 2107, 2411, 2746, 3115, 3523, 3973, 4470, 5018, 5624, 6291, 7028, 7842,
    8740, 9730, 10824, 12031, 13363, 14833, 16456, 18247, 20224, 22406, 24815, 27473,
    30408, 33648, 37224, 41171, 45529, 50339, 55649, 61512,
    67983, 75127, 83014, 91721, 101333, 111945, 123660,
    136594, 150872, 166636, 184040, 203254, 224466, 247886,
    273742, 302288, 333804, 368599, 407015, 449428, 496254,
    547953, 605032, 668051, 737627, 814445, 899257, 992895,
    1096278, 1210421, 1336443, 1475581, 1629200, 1798808,
    1986068, 2192818, 2421087, 2673114, 2951373, 3258594,
    3597792, 3972294, 4385776, 4842295, 5346332, 5902831,
    6517253, 7195629, 7944614, 8771558, 9684577, 10692629,
    11805606, 13034431]

    df['Level'] = level_list
    df['Xp'] = experience_list
    return df

def get_hiscores(player_name):
  url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=' + str(player_name)
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  return soup

#takes in soup
#returns a df of skills, their rank, their level, and their xp
def get_levels(soup):
  skill_list = ['Attack', 'Defence', 'Strength', 'Hitpoints', 'Ranged', 'Prayer', 'Magic', 'Cooking', 'Woodcutting', 'Fletching', 'Fishing', 'Firemaking', 'Crafting', 'Smithing', 'Mining', 'Herblore', 'Agility', 'Theiving', 'Slayer', 'Farming', 'Runecraft', 'Hunter', 'Construction']

  df = pd.DataFrame()

  mega_list = []
  mega_list_2 = []

  rank_list = []
  level_list = []
  xp_list = []

  soup = soup.get_text()
  x_string = ''

  #makes our soup a list
  #appends each list entry into mega_list
  for x in soup:
    if x != ',':
      x_string += x
    else:
      mega_list.append(x_string)
      x_string = ''
    
  for x in mega_list:
    x = x.split('\n')
    for y in x:
      mega_list_2.append(y)

  mega_list = mega_list_2

  rank_list = get_list_item(mega_list, 0)
  level_list = get_list_item(mega_list, 1)
  xp_list = get_list_item(mega_list, 2)

  df['Skill'] = skill_list
  df['Rank'] = rank_list
  df['Level'] = level_list
  df['Xp'] = xp_list
  
  df = df.set_index('Skill')
  
  return df

#takes in a list and index
#returns a list of items in that specific index
def get_list_item(mega_list, item_index):
  index_list = []

  mod_number = 0

  i = 0
  counter = 0

  while i < len(mega_list):
    if counter == 3:
      counter = 0
    if counter == item_index:
      index_list.append(mega_list[i])
    
    counter += 1
    i += 1

  index_list = index_list[1:24]
  return index_list

#takes in a username and returns a df of skill, rank, level, and Xp
def get_player_level_df(username):
    
    soup = get_hiscores(username)
    df = get_levels(soup)
    return df
