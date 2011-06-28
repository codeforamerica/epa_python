#!/usr/bin/env python

"""Python wrapper for the EPA's RADInfo API."""

from epa.envirofacts import Envirofacts

from lookup_table import lookup_table


class RADInfo(Envirofacts):
    """
    Python wrapper for the EPA's RADInfo API.

    >>> RADInfo().facility('city_name', 'Dallas')
    """

    def __init__(self):
        super(RADInfo, self).__init__()
        self.lookup_table = lookup_table
        self.lookup_methods = ['regulation', 'facility_type', 'geo',
                               'regulatory_program', 'facility']

    def facility(self, column=None, value=None, **kwargs):
        return self._resolve_call('RAD_FACILITY', column, value, **kwargs)

    def facility_type(self, column=None, value=None, **kwargs):
        return self._resolve_call('RAD_FACILITY_TYPE', column, value, **kwargs)

    def geo(self, column=None, value=None, **kwargs):
        """Locate a facility through geographic location."""
        return self._resolve_call('RAD_GEO_LOCATION', column, value, **kwargs)

    def regulation(self, column=None, value=None, **kwargs):
        return self._resolve_call('RAD_REGULATION', column, value, **kwargs)

    def regulatory_program(self, column=None, value=None, **kwargs):
        return self._resolve_call('RAD_REGULATORY_PROGRAM', column,
                                  value, **kwargs)
