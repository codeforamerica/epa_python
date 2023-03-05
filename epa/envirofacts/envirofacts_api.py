#!/usr/bin/env python

"""
All of the EPA's Envirofacts APIs follow the exact same structure -- a base
URL, followed by a path that includes the table name, column name, and value.
This module should be imported and built off of -- since it has methods to
handle calling the EPA in that way.
"""

from urllib.parse import quote

from .api import API, urlopen


class Envirofacts(API):
    """Python wrapper for the EPA's Envirofacts API."""

    def __init__(self):
        super(Envirofacts, self).__init__()
        self.base_url = 'https://data.epa.gov/efservice'
        self.operations = ['=', '!=', '<', '>', 'BEGINNING', 'CONTAINING']
        self.default_operation = '='
        self.output_formats = ['dicts', 'xml', 'json', 'csv', 'excel']
        self.default_output_format = 'dicts'
        self.table_lookup = None
        self.table_column_lookup = None
        self.column_table_lookup = None

    def catalog(self, table='', column=''):
        """Lookup the values available for querying."""
        if table:
            if not self.table_lookup or not self.table_column_lookup:
                return None
            table = table.upper()
            if table not in self.table_lookup.keys():
                # raise ValueError("unknown table: {}".format(table))
                return None
        if column:
            if not self.column_table_lookup:
                return None
            column = column.upper()
            if column not in self.column_table_lookup.keys():
                # raise ValueError("unknown column: {}".format(column))
                return None
        if table and column:
            if column not in self.table_column_lookup[table].keys():
                # raise ValueError(f"table {table} has no column {column}")
                return None
            return self.table_column_lookup[table][column]  # get column description
        elif table:
            return self.table_lookup[table]  # get table description
        elif column:
            return self.column_table_lookup[column]  # get list of tables that contain this column
        return None

    def _resolve_call(self, table_lst, column='', value='', **kwargs):
        """Internal method to resolve the API wrapper call."""
        if not column:
            return self.catalog(table_lst[0])
        elif not value:
            return self.catalog(table_lst[0], column)
        # We have the tables, column, and value. Now we need to
        # ensure they're all strings and uppercase.
        column = column.upper()
        value = str(value).upper()
        data = self.call_api(table_lst, column, value, **kwargs)
        return data

    def call_api(self, table_lst, column, value, **kwargs):
        """Exposed method to connect and query the EPA's API."""
        if type(table_lst) == str:
            # A list of tables is expected, but handle a string
            table_lst = [table_lst]

        try:
            output_format = kwargs.pop('output_format')
            if output_format:
                output_format = output_format.lower()
        except KeyError:
            output_format = self.default_output_format
        if output_format not in self.output_formats:
            raise ValueError("illegal output format: {}".format(output_format))
        # if dict, request json then convert it
        convert_to_dict = (output_format == 'dicts')
        if convert_to_dict:
            output_format = 'json'

        try:
            op = kwargs.pop('operation')
            if op:
                op = op.upper()
        except KeyError:
            op = self.default_operation
        if op not in self.operations:
            raise ValueError("illegal operation: {}".format(op))

        url_list = [self.base_url, table_lst[0], column, quote(op), quote(value)]
        url_list.extend(table_lst[1:])
        rows_count = self._number_of_rows(**kwargs)
        url_list.append(rows_count)
        url_list.append(output_format)
        url_string = '/'.join(url_list)
        data = urlopen(url_string).read()
        if convert_to_dict:
            data = self._format_data(output_format, data)
        return data

    @staticmethod
    def _number_of_rows(start=0, count=100, **kwargs):
        """Internal method to format the number of rows the EPA API returns."""
        first = str(start)
        last = str(start + count - 1)
        string_format = f"rows/{first}:{last}"
        return string_format
