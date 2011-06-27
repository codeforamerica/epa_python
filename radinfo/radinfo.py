#!/usr/bin/env python

"""Python wrapper for the EPA's RADInfo API."""

from api import API

from lookup_table import lookup_table


class RADInfo(API):
    """Python wrapper for the EPA's RADInfo API."""

    def __init__(self):
        super(RADInfo, self).__init__()
        self.base_url = 'http://iaspub.epa.gov/enviro/efservice'
        self.output_format = 'xml'
        self.lookup_table = lookup_table

    def catalog(self, table='', column=''):
        """Lookup the values available for querying."""
        lookup_table = self.lookup_table
        if table:
            if column:
                return lookup_table[table][column]
            return lookup_table[table]
        # Show what tables are available.
        return lookup_table.keys()

    def regulator_program(self, column=None, value=None, **kwargs):
        if not column and not value:
            return self.catalog('regulatory_program')
