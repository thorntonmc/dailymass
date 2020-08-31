import requests
from bs4 import BeautifulSoup
from termcolor import colored, cprint

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
def print_passage(group):
    # print title
    title = group.find('h3', class_='readings__reference');
    cprint(title.get_text(), 'green');
    verses = group.find_all('span');

    for verse in verses:
        verse = verse.get_text()

        # if we have a verse number, print it in color
        if is_int(verse):
            cprint(verse.strip() + ' ', 'blue', end='')
        else:
            print(verse.strip() + ' ', end='');

    print('');

# Get daily reading html
daily="https://www.ewtn.com/catholicism/daily-readings"
r = requests.get(daily);

# parse into soup
soup = BeautifulSoup(r.text, features="html.parser")

# get all divs

reading_passage = soup.find_all('div', class_='readings__group')

for passage in reading_passage:
    print_passage(passage);



