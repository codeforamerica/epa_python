#!/usr/bin/env python

"""Python wrapper for the EPA's PCS API."""

from epa.envirofacts import Envirofacts

from lookup_table import lookup_table


class PCS(Envirofacts):
    """Python wrapper for the GICS API."""

    def __init__(self):
        super(PCS, self).__init__()
        self.lookup_table = lookup_table
        self.lookup_methods = []

    def admin_penalty(self, column=None, value=None, **kwargs):
        """
        An enforcement action that results in levying the permit holder with a
        penalty or fine. It is used to track judicial hearing dates, penalty
        amounts, and type of administrative penalty order.
        """
        return self._resolve_call('PCS_ADMIN_PENALTY_ORDER', column,
                                  value, **kwargs)

    def permit_event(self, column=None, value=None, **kwargs):
        """
        A permit event tracks the lifecycle of a permit from issuance to
        expiration. Examples include 'Application Received' and 'Permit
        Issued', etc.
        """
        return self._resolve_call('PCS_PERMIT_EVENT', column, value, **kwargs)

    def dmr_measurement(self, column=None, value=None, **kwargs):
        """
        Measurements of effluents reported on the Discharge Monitoring Report
        (DMR). The violations are detected by comparing the measurement values
        against the corresponding effluent limit.
        """
        return self._resolve_call('PCS_DMR_MEASUREMENT', column, value, **kwargs)

    def inspection(self, column=None, value=None, **kwargs):
        """
        An official visit to the permit facility on a periodic basis which
        consists of the following inspection types: NPDES, Biomonitoring,
        Pretreatment, and Industrial User.
        """
        return self._resolve_call('PCS_INSPECTION', column, value, **kwargs)

    def enforcement_action(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_ENFOR_ACTION', column, value, **kwargs)

    def facility(self, column=None, value=None, **kwargs):
        """Same as permit facility method."""
        return self._resolve_call('PCS_PERMIT_FACILITY', column, value, **kwargs)

    def permit_facility(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_PERMIT_FACILITY', column, value, **kwargs)

    def pci_audit(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_PCI_AUDIT', column, value, **kwargs)

    def compliance_violation(self, column=None, value=None, **kwargs):
        """
        A compliance schedule violation reflects the non-achievement of a
        given compliance schedule event including the type of violation and ty
        pe of resolution.
        """
        return self._resolve_call('PCS_CMPL_SCHD_VIOL', column, value, **kwargs)

    def effl_lim_qty(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_EFFL_LIM_QTY', column, value, **kwargs)

    def effl_lim(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_EFFL_LIM', column, value, **kwargs)

    def effl_lim_concentr(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_EFFL_LIM_CONCENTR', column,
                                  value, **kwargs)

    def single_violation(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_SINGLE_EVENT_VIOL', column,
                                  value, **kwargs)

    def sludge(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_SLUDGE', column, value, **kwargs)

    def hearing_event(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_EVIDENTIARY_HEARING_EVENT', column,
                                  value, **kwargs)

    def pipe_schedule(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_PIPE_SCHED', column, value, **kwargs)

    def compliance_schedule(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_CMPL_SCHD', column, value, **kwargs)

    def code_description(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_CODE_DESC', column, value, **kwargs)

    def industrial_user(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_INDUSTRIAL_USER_INFO', column,
                                  value, **kwargs)
