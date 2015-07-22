__author__ = 'neuro'

from bs4 import BeautifulSoup
from urllib2 import urlopen
import pprint as pp

BASE_URL = "http://www.amazon.it/gp/site-directory/ref=nav_shopall_btn"


def get_category_links(section_url):
    categories = []
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    categs = soup.find_all('div', 'popover-grouping')
    for cat in categs:
        top = cat.find('h2', 'popover-category-name').string
        subs = [sub.string for sub in cat.findAll('a', 'nav_a')]
        tmp = {
            'top_cat': top,
            'subs_cat': subs
        }
        categories.append(tmp)
    return categories


def generate_SQL(list_item):
    sql = ''
    for i in range(len(list_item)):
        list_item[i]['id'] = i
        sql = sql[:-1]
        sql += '''
          INSERT INTO auctions_db.bidplacing_category
            (id, category_name, level, parent_id)
          VALUES
            (%(id)d, '%(top_cat)s', 0, %(id)d);
            '''%list_item[i]

    sql = sql.rstrip('\n')
    with open('category_sql', 'w') as f:
        f.write(sql.encode('utf-8'))
    f.close()

if __name__ == '__main__':
    cats = get_category_links(BASE_URL)
    slq = generate_SQL(cats)
