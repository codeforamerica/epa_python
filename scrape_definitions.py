#!/usr/bin/env python

"""
In order to configure lookup dicts for EPA tables and columns in the fastest
way possible, it's necessary to scrape the site (you'd think the data
definitions would be more accessible, but unfortunately, they're not).
"""

import re
import json
from urllib2 import urlopen

from bs4 import BeautifulSoup as bs


def find_table_links(agency):
    """
    When given a url, this function will find all the available table names
    for that EPA dataset.
    """
    url_list = ['http://www.epa.gov/enviro/facts/', agency, '/']
    agency_url = ''.join(url_list)
    url_list.append('model.html')
    model_url  = ''.join(url_list)
    url = urlopen(model_url)
    # We'll use BeautifulSoup + lxml for parsing.
    soup = bs(url.read(), ['fast', 'lxml'])
    images = soup.find('map').findAll('area')
    href_list = (img.attrs['href'] for img in images)
    table_set = set()
    for link in href_list:
        new_soup = bs(urlopen(agency_url + link).read(), ['fast', 'lxml'])
        new_images = new_soup.find('map').findAll('area')
        table_set.update((img.attrs['href'] for img in new_images))
    return table_set


def find_definition_urls(set_of_links):
    """Find the available definition URLs for the columns in a table."""
    definition_dict = {}
    for link in set_of_links:
        if link.startswith('http://'):
            table_dict = {}
            soup = bs(urlopen(link).read(), ['fast', 'lxml'])
            unordered_list = soup.find('div', {'id': 'main'}).findAll('ul')[-1]
            for li in unordered_list.findAll('li'):
                a = li.findChild('a')
                table_dict.update({a.string: a.attrs['href']})
            link_name = re.sub('.*p_table_name=(\w+)&p_topic.*', r'\1',
                               link).upper()
            definition_dict.update({link_name: table_dict})
    return definition_dict

def create_agency(agency):
    """Create an agency text file of definitions."""
    links = find_table_links(agency)
    definition_dict = find_definition_urls(links)
    with open(agency + '.txt', 'w') as f:
        f.write(str(definition_dict))

def loop_through_agency(agency):
    with open(agency + '.txt') as f:
        data = eval(f.read())
    for table in data:
        for column in data[table]:
            value_link = data[table][column]
            data[table][column] = grab_definition(value_link)
    data = json.dumps(data)
    with open(agency + '_values.json', 'w') as f:
        f.write(str(data))


def grab_definition(url):
    if url.startswith('//'):
        url = 'http:' + url
    soup = bs(urlopen(url).read(), ['fast', 'lxml'])
    try:
        bold = soup.findAll('b')[1]
        value = bold.next.next.strip('\n\n')
    except IndexError:
        print url
    except TypeError:
        print url
    else:
        return value
    return url


def main():
    agency = 'cerclis'
    #create_agency(agency)
    loop_through_agency(agency)

if __name__ == '__main__':
    main()
