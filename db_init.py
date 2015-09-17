from django.db import IntegrityError
from bs4 import BeautifulSoup
from urllib2 import urlopen
import pprint as pp
import json
import sys
import os
import argparse
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction_men.settings')
from bidplacing.models import Category

__author__ = 'neuro'

AMAZON = "http://www.amazon.it/gp/site-directory/ref=nav_shopall_btn"


def create_categories_file(section_url):
    categories = []
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    div = soup.find_all('div', 'popover-grouping')
    for cat in div:
        top = cat.find('h2', 'popover-category-name').string
        subs = [sub.string for sub in cat.findAll('a', 'nav_a')]
        tmp = {
            'top_cat': top,
            'subs_cat': subs
        }
        categories.append(tmp)
    with open('categories.json', 'w') as f:
        f.write(json.dumps(cats))
    f.close()
    return categories


def save_categories():
    cats = None
    with open('categories.json', 'r') as f:
        categories = json.load(f)
    f.close()
    for cat in categories:
        c = Category.create(cat['top_cat'], None, 0)
        c.save()
        for sub in cat['subs_cat']:
            s = Category.create(sub, c, 1)
            try:
                s.save()
            except IntegrityError:
                pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Script for db init using data\
        by amazon')

    parser.add_argument('--amazon', '-a',
                        dest='amazon',
                        action='store_true',
                        help='if true scrape data from amazon and store it\
                        in a JSON file',
                        required=False)

    parser.add_argument('--categories', '-c',
                        dest='cat',
                        action='store_true',
                        help='create the category table, expecting an empty \
                        table',
                        required=False)

    namespace = parser.parse_args()

    if namespace.amazon:
        cats =      (AMAZON)
        sys.exit(0)
    if namespace.cat:
        save_categories
        sys.exit(0)
