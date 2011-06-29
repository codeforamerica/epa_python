#!/usr/bin/env python

"""Python wrapper for the EPA's RADInfo API."""

from epa.envirofacts import Envirofacts

from lookup_table import lookup_table


class RADInfo(Envirofacts):
    """
    Python wrapper for the EPA's RADInfo API.

    >>> RADInfo().facility('city_name', 'Houston')
    """

    def __init__(self):
        super(RADInfo, self).__init__()
        self.lookup_table = lookup_table
        self.lookup_methods = ['regulation', 'facility_type', 'geo',
                               'regulatory_program', 'facility']

    def facility(self, column=None, value=None, **kwargs):
        """
        Check information related to Radiation facilities.

        >>> RADInfo().facility('state_code', 'CA')
        """
        return self._resolve_call('RAD_FACILITY', column, value, **kwargs)

    def facility_type(self, column=None, value=None, **kwargs):
        """
        Basic identifying information for a RADInfo facility, including
        the improved facility information maintained by the Facility
        Registry System (FRS). 

        >>> RADInfo().facility_type('cit_ref_code', '40CFR300')
        """
        return self._resolve_call('RAD_FACILITY_TYPE', column, value, **kwargs)

    def geo(self, column=None, value=None, **kwargs):
        """
        Locate a facility through geographic location.

        >>> RADInfo().geo('geometric_type_code', '001')
        """
        return self._resolve_call('RAD_GEO_LOCATION', column, value, **kwargs)

    def regulation(self, column=None, value=None, **kwargs):
        """
        Provides relevant information about applicable regulations.

        >>> RADInfo().regulation('title_id', 40)
        """
        return self._resolve_call('RAD_REGULATION', column, value, **kwargs)

    def regulatory_program(self, column=None, value=None, **kwargs):
        """
        Identifies the regulatory authority governing a facility, and, by
        virtue of that identification, also identifies the regulatory program
        of interest and the type of facility. 

        >>> RADInfo().regulatory_program('sec_cit_ref_flag', 'N')
        """
        return self._resolve_call('RAD_REGULATORY_PROG', column,
                                  value, **kwargs)
