from bs4 import BeautifulSoup
import requests
import pandas as pd


def gather_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    moneys = soup.find_all('td')
    return moneys


def make_money():
    moneys = gather_page('https://oldschool.runescape.wiki/w/Money_making_guide')

    activity_list = []
    gp_list = []
    all_dict = {}

    g = 0

    while g < 1346:
        activity = moneys[g].get_text().strip("\n")
        g += 1
        gps = moneys[g].get_text().replace(",", "")
        gps = float(gps)
        all_dict.update({activity: gps})
        g += 5

    df = pd.DataFrame()
    df['Activity'] = all_dict.keys()
    df['GP/HR'] = all_dict.values()

    df = df.sort_values('GP/HR', ascending=False)

    df = df.reset_index()
    df2 = df[['Activity', 'GP/HR']]

    return df2