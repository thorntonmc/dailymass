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
    cprint(title.get_text() + '\n', 'green');
    verses = group.find_all('span');

    for verse in verses:
        verse = verse.get_text()
        verse = verse.strip()

        # if we have a verse number, print it in color
        if is_int(verse):
            cprint(verse + '.', 'blue', end='')
        else:
            verse = verse.split()
            counter = 0;
            for word in verse:
                word_len = len(word)

                if counter + word_len > 80:
                    print('\n', end='')
                    print(word + ' ', end='')
                    counter = word_len
                else:
                    print(word + ' ', end='')
                    counter += word_len

                if (counter > 80):
                    print('\n', end='')
                    counter = 0
            print(' ')


    print('\n');

def main():
    # Get daily reading html
    daily="https://www.ewtn.com/catholicism/daily-readings"
    r = requests.get(daily);

    # parse into soup
    soup = BeautifulSoup(r.text, features="html.parser")

    # get all divs

    reading_passage = soup.find_all('div', class_='readings__group')

    for passage in reading_passage:
        print_passage(passage);

if __name__ == "__main__":
    main()

