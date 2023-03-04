#!/usr/bin/env python

"""
In order to configure lookup dicts for EPA tables and columns in the fastest
way possible, it's necessary to scrape the site (you'd think the data
definitions would be more accessible, but unfortunately, they're not).
"""

import requests
from bs4 import BeautifulSoup
import pprint

# URL of top system page. See: https://www.epa.gov/enviro/envirofacts-model
# This is the PCS base page:
base_url = 'https://www.epa.gov/enviro/pcs-icis-model'

# table name -> description
table_lookup = {}

# table_name -> { column_name -> description }
table_column_lookup = {}

# column_name -> [table_name]
column_table_lookup = {}


def column_page(page_url, in_table_name, in_col_name):
    print("Table/Column:", in_table_name, in_col_name)
    response = requests.get(page_url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    prefix = "Column Name: "
    prefix_len = len(prefix)
    col_name = None
    for header in soup.find_all('h1'):
        if header is not None and header.string.strip().startswith(prefix):
            col_name = header.string.strip()[prefix_len:]
            break
    if not col_name:
        return
    if col_name != in_col_name:
        print("ERROR: column name does not match expected")

    string_gen = soup.strings
    for string in string_gen:
        if "Description:" in string:
            description = next(string_gen).strip()
            table_column_lookup[in_table_name][col_name] = description
            break

    if col_name not in column_table_lookup.keys():
        column_table_lookup[col_name] = [in_table_name]
    elif in_table_name not in column_table_lookup[col_name]:
        column_table_lookup[col_name].append(in_table_name)


def table_page(page_url):
    response = requests.get(page_url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    prefix = "Table Name: "
    prefix_len = len(prefix)
    table_name = None
    for header in soup.find_all('h1'):
        if header is not None and header.string.strip().startswith(prefix):
            table_name = header.string.strip()[prefix_len:]
            break
    if not table_name:
        return
    if table_name in table_lookup.keys():
        return
    print("Table:", table_name)

    string_gen = soup.strings
    for string in string_gen:
        if "Description:" in string:
            description = next(string_gen).strip()
            table_lookup[table_name] = description
            break

    if table_name not in table_column_lookup.keys():
        table_column_lookup[table_name] = {}

    for a in soup.find_all('a'):
        col_url = a.get('href')
        col_name = a.string
        if not col_url.startswith("https:"):
            col_url = "https:" + col_url
        if col_url is not None and "column_name" in col_url:
            column_page(col_url, table_name, col_name)


def node_page(node_url):
    response = requests.get(node_url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    map_tags = soup.find_all('map')
    area_tags = soup.find_all('area')

    for map in map_tags:
        for area in area_tags:
            if area.parent == map:
                url = area['href']
                if not url.startswith("https://"):
                    url = "https://www.epa.gov" + url
                if "node" in url:
                    node_page(url)
                elif "table_name" in url:
                    table_page(url)


node_page(base_url)

with open("table_lookup.py", "w") as fp:
    fp.write("table_lookup = \\\n")
    pprint.pprint(table_lookup, stream=fp, width=120)
with open("table_column_lookup.py", "w") as fp:
    fp.write("table_column_lookup = \\\n")
    pprint.pprint(table_column_lookup, stream=fp, width=120)
with open("column_table_lookup.py", "w") as fp:
    fp.write("column_table_lookup = \\\n")
    pprint.pprint(column_table_lookup, stream=fp, width=120)
