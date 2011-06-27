#!/usr/bin/env python

"""Python wrapper for the EPA's RADInfo API."""

from api import API


class RADInfo(API):
    """Python wrapper for the EPA's RADInfo API."""

    def __init__(self):
        super(RADInfo, self).__init__()
        self.base_url = 'http://iaspub.epa.gov/enviro/efservice'
        self.output_format = 'xml'

    def catalog(self, table):
        pass

    def regulator_program(self, column=None, value=None, **kwargs):
        if not column and not value:
            return self.catalog('regulatory_program')
