#!/usr/bin/env python

"""Python wrapper for the EPA's RADInfo API."""

from epa.envirofacts import Envirofacts

from lookup_table import lookup_table


class RADInfo(Envirofacts):
    """Python wrapper for the EPA's RADInfo API."""

    def __init__(self):
        super(RADInfo, self).__init__()
        self.lookup_table = lookup_table

    def facility(self, column=None, value=None, **kwargs):
        return self._resolve_call('regulation', column, value, **kwargs)

    def facility_type(self, column=None, value=None, **kwargs):
        return self._resolve_call('facility_type', column, value, **kwargs)

    def geo(self, column=None, value=None, **kwargs):
        """Locate a facility through geographic location."""
        return self._resolve_call('geo', column, value, **kwargs)

    def regulation(self, column=None, value=None, **kwargs):
        return self._resolve_call('regulation', column, value, **kwargs)

    def regulatory_program(self, column=None, value=None, **kwargs):
        return self._resolve_call('regulatory_program', column,
                                  value, **kwargs)
