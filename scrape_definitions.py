#!/usr/bin/env python

"""
In order to configure lookup dicts for EPA tables and columns in the fastest
way possible, it's necessary to scrape the site (you'd think the data
definitions would be more accessible, but unfortunately, they're not).

This is a second attempt at making an adequate scraper -- but instead of using
the alpha version of `BeautifulSoup 4`, it uses the `lxml` module to scrape the
EPA sites.
"""

import re
import json
from urllib2 import urlopen, HTTPError

import lxml.html as lh


class Scraper(object):
    """
    A web scraper that grabs table and column definitions for the multiple
    EPA APIs.
    """

    def __init__(self, agency=None, page='model.html'):
        if agency.startswith('http://'):
            # Then it's a full link.
            self.model_url = agency
        else:
            url_list = ['http://www.epa.gov/enviro/facts/', agency, '/']
            self.agency_url = ''.join(url_list)
            url_list.append(page)
            self.model_url = ''.join(url_list)
        self.agency = agency

    def find_table_links(self):
        """
        When given a url, this function will find all the available table names
        for that EPA dataset.
        """
        html = urlopen(self.model_url).read()
        doc = lh.fromstring(html)
        href_list = [area.attrib['href'] for area in doc.cssselect('map area')]
        tables = self._inception_table_links(href_list)
        return tables

    def _inception_table_links(self, href_list):
        """
        Sometimes the EPA likes to nest their models and tables -- model within
        a model within a model -- so this internal method tries to clear all
        that up.
        """
        tables = set()
        for link in href_list:
            if not link.startswith('http://'):
                link = self.agency_url + link
            html = urlopen(link).read()
            doc = lh.fromstring(html)
            area = doc.cssselect('map area')
            if area:
                # Then this is a model containing models.
                tables.update((a.attrib['href'] for a in area))
            else:
                # The link is a table without additional models.
                tables.update(link)
        return tables

    def find_definition_urls(self, set_of_links):
        """Find the available definition URLs for the columns in a table."""
        definition_dict = {}
        re_link_name = re.compile('.*p_table_name=(\w+)&p_topic.*')
        for link in set_of_links:
            if link.startswith('http://'):
                table_dict = {}
                html = urlopen(link).read()
                doc = lh.fromstring(html)
                unordered_list = doc.cssselect('#main ul')[-1]
                for li in unordered_list.iterchildren():
                    a = li.find('a')
                    table_dict.update({a.text: a.attrib['href']})
                link_name = re_link_name.sub(r'\1', link).upper()
                definition_dict.update({link_name: table_dict})
        return definition_dict

    def create_agency(self):
        """Create an agency text file of definitions."""
        agency = self.agency
        links = self.find_table_links()
        definition_dict = self.find_definition_urls(links)
        with open(agency + '.txt', 'w') as f:
            f.write(str(definition_dict))

    def loop_through_agency(self):
        """Loop through an agency to grab the definitions for its tables."""
        agency = self.agency
        with open(agency + '.txt') as f:
            data = eval(f.read())
        for table in data:
            for column in data[table]:
                value_link = data[table][column]
                data[table][column] = self.grab_definition(value_link)
        data = json.dumps(data)
        with open(agency + '_values.json', 'w') as f:
            f.write(str(data))

    def grab_definition(self, url):
        """
        Grab the column definition of a table from the EPA using a combination
        of regular expressions and lxml.
        """
        re_description = re.compile('Description:(.+?\\n)')
        re_table_name = re.compile("(\w+ Table.+)")
        if url.startswith('//'):
            url = 'http:' + url
        elif url.startswith('/'):
            url = 'http://www.epa.gov' + url
        try:
            html = urlopen(url).read()
            doc = lh.fromstring(html)
            main = doc.cssselect('#main')[0]
            text = main.text_content()
            definition = re_description.search(text).group(1).strip()
        except (AttributeError, IndexError, TypeError, HTTPError):
            print url
        else:
            value = re_table_name.sub('', definition)
            return value
        return url


def main():
    scraper = Scraper('cerclis')
    scraper.create_agency()
    scraper.loop_through_agency()


if __name__ == '__main__':
    main()
