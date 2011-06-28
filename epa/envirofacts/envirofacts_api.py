#!/usr/bin/env python

from api import API, urlopen


class Envirofacts(API):
    """Python wrapper for the EPA's Envirofacts API."""

    def __init__(self):
        super(Envirofacts, self).__init__()
        self.base_url = 'http://iaspub.epa.gov/enviro/efservice'
        self.output_format = 'xml'
        self.lookup_table = None
        self.lookup_methods = None

    def catalog(self, table='', column=''):
        """Lookup the values available for querying."""
        lookup_table = self.lookup_table
        if lookup_table is not None:
            if table:
                if column:
                    column = column.upper()
                    return lookup_table[table][column]
                return lookup_table[table]
            # Show what methods are available.
            return self.lookup_methods
        return None

    def _resolve_call(self, table, column=None, value=None, **kwargs):
        """Internal method to resolve the API wrapper call."""
        if not column:
            return self.catalog(table)
        elif not value:
            return self.catalog(table, column)
        return self.call_api(table, column, value, **kwargs)

    def call_api(self, table, column, value, **kwargs):
        """Exposed method to connect and query the EPA's API."""
        try:
            output_format = kwargs.pop('output_format')
        except KeyError:
            output_format = self.output_format
        url_list = [self.base_url, table, column, value, 'rows']
        rows_count = self._number_of_rows(**kwargs)
        url_list.append(rows_count)
        url_string = '/'.join(url_list)
        xml_data = urlopen(url_string).read()
        data = self._format_data(output_format, xml_data)
        return data

    def _number_of_rows(self, start=0, count=100, **kwargs):
        """Internal method to format the number of rows the EPA API returns."""
        first = str(start)
        last = str(start + count)
        string_format = ':'.join([first, last])
        return string_format
