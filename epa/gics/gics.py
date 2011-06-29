#!/usr/bin/env python

"""Python wrapper for the EPA's Grants Information and Control System API."""

from epa.envirofacts import Envirofacts

from lookup_table import lookup_table


class GICS(Envirofacts):
    """Python wrapper for the GICS API."""

    def __init__(self):
        super(GICS, self).__init__()
        self.lookup_table = lookup_table
        self.lookup_methods = ['construction']

    def action(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_ACTION', column, value, **kwargs)

    def applicant(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_APPLICANT', column, value, **kwargs)

    def assistance(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_ASST_PGM', column, value, **kwargs)

    def authority(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_AUTHORITY', column, value, **kwargs)

    def construction(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_CONSTRUCTION', column, value, **kwargs)

    def grant(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_GRANT', column, value, **kwargs)

    def grant_assistance(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_GRANT_ASST_PGM', column, value, **kwargs)

    def grant_authority(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_GRANT_AUTH', column, value, **kwargs)

    def lab_office(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_LAB_OFFICE', column, value, **kwargs)

    def milestone(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_MILESTONE', column, value, **kwargs)

    def record_type(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_RECORD_TYPE', column, value, **kwargs)

    def srf_cap(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_SRF_CAP', column, value, **kwargs)

    def status(self, column=None, value=None, **kwargs):
        return self._resolve_call('GIC_STATUS', column, value, **kwargs)
