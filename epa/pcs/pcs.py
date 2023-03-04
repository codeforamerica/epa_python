#!/usr/bin/env python

from epa.envirofacts import Envirofacts

from .table_lookup import table_lookup
from .table_column_lookup import table_column_lookup
from .column_table_lookup import column_table_lookup


class PCS(Envirofacts):
    """Python wrapper for the EPA's PCS API."""

    def __init__(self):
        super(PCS, self).__init__()
        self.table_lookup = table_lookup
        self.table_column_lookup = table_column_lookup
        self.column_table_lookup = column_table_lookup

    def pcs_query(self, table_lst, column=None, value=None, **kwargs):
        """
        General-purpose PCS query function allowing queries on 1-3 tables.
        """
        if not table_lst or len(table_lst) > 3:
            raise ValueError("table_lst must contain 1-3 table names")
        return self._resolve_call(table_lst, column, value, **kwargs)

    def audit(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_PCI_AUDIT'], column, value, **kwargs)

    def code_description(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_CODE_DESC'], column, value, **kwargs)

    def compliance_schedule(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_CMPL_SCHD'], column, value, **kwargs)

    def compliance_violation(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_CMPL_SCHD_VIOL'], column, value, **kwargs)

    def dmr_measurement(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_DMR_MEASUREMENT'], column, value, **kwargs)

    def effl_lim_qty(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_EFFL_LIM_QTY'], column, value, **kwargs)

    def effl_lim(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_EFFL_LIM'], column, value, **kwargs)

    def effl_lim_concentr(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_EFFL_LIM_CONCENTR'], column,
                                  value, **kwargs)

    def facility(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_PERMIT_FACILITY'], column, value, **kwargs)

    def hearing(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_EVIDENTIARY_HEARING_EVENT'], column,
                                  value, **kwargs)

    def industrial_user(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_INDUSTRIAL_USER_INFO'], column,
                                  value, **kwargs)

    def inspection(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_INSPECTION'], column, value, **kwargs)

    def permit_event(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_PERMIT_EVENT'], column, value, **kwargs)

    def pipe_schedule(self, column=None, value=None, **kwargs):
        return self._resolve_call(['PCS_PIPE_SCHED'], column, value, **kwargs)
