#!/usr/bin/env python

"""Python wrapper for the EPA's PCS API."""

from epa.envirofacts import Envirofacts

from lookup_table import lookup_table


class PCS(Envirofacts):
    """Python wrapper for the GICS API."""

    def __init__(self):
        super(PCS, self).__init__()
        self.lookup_table = lookup_table
        self.lookup_methods = [
            'admin_penalty', 'audit', 'code_description',
            'compliance_schedule', 'compliance_violation',
            'dmr_measurement', 'enforcement_action', 'facility',
            'hearing', 'industrial_user', 'inspection', 'permit_event',
            'pipe_schedule', 'single_violation', 'sludge'
        ]

    def admin_penalty(self, column=None, value=None, **kwargs):
        """
        An enforcement action that results in levying the permit holder with a
        penalty or fine. It is used to track judicial hearing dates, penalty
        amounts, and type of administrative penalty order.

        >>> PCS().admin_penalty('enfor_action_date', '16-MAR-01')
        """
        return self._resolve_call('PCS_ADMIN_PENALTY_ORDER', column,
                                  value, **kwargs)

    def audit(self, column=None, value=None, **kwargs):
        """
        Pretreatment Compliance Inspections (PCI) or Pretreatment Audits
        collect information resulting from inspections pertaining to a Publicly
        Owned Treatment Works (POTWs) that receive pollutants from in direct
        dischargers.

        >>> PCS().audit('insp_date', '16-MAR-01')
        """
        return self._resolve_call('PCS_PCI_AUDIT', column, value, **kwargs)

    def code_description(self, column=None, value=None, **kwargs):
        """
        The Permit Compliance System (PCS) records milestones, events, and many
        other parameters in code format. To provide text descriptions that
        explain the code meanings, the PCS_CODE_DESC provide s complete
        information on all types of codes, and for each type, the text
        description of each possible code value.

        >>> PCS().code_description('code', 110)
        """
        return self._resolve_call('PCS_CODE_DESC', column, value, **kwargs)

    def compliance_schedule(self, column=None, value=None, **kwargs):
        """
        A sequence of activities with associated milestones which pertains to a
        given permit.

        >>> PCS().compliance_schedule('cmpl_schd_evt', '62099')
        """
        return self._resolve_call('PCS_CMPL_SCHD', column, value, **kwargs)

    def compliance_violation(self, column=None, value=None, **kwargs):
        """
        A compliance schedule violation reflects the non-achievement of a
        given compliance schedule event including the type of violation and ty
        pe of resolution.

        >>> PCS().compliance_violation('cs_rnc_detect_date', '16-MAR-04')
        """
        return self._resolve_call('PCS_CMPL_SCHD_VIOL', column, value, **kwargs)

    def dmr_measurement(self, column=None, value=None, **kwargs):
        """
        Measurements of effluents reported on the Discharge Monitoring Report
        (DMR). The violations are detected by comparing the measurement values
        against the corresponding effluent limit.

        >>> PCS().dmr_measurement('season_num', 2)
        """
        return self._resolve_call('PCS_DMR_MEASUREMENT', column, value, **kwargs)

    def enforcement_action(self, column=None, value=None, **kwargs):
        """
         A disciplinary action taken against a permit facility. The action may
         be applicable to one or more violations.

         >>> PCS().enforcement_action('ea_code', '09')
        """
        return self._resolve_call('PCS_ENFOR_ACTION', column, value, **kwargs)

    def effl_lim_qty(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_EFFL_LIM_QTY', column, value, **kwargs)

    def effl_lim(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_EFFL_LIM', column, value, **kwargs)

    def effl_lim_concentr(self, column=None, value=None, **kwargs):
        return self._resolve_call('PCS_EFFL_LIM_CONCENTR', column,
                                  value, **kwargs)

    def facility(self, column=None, value=None, **kwargs):
        """
        A facility that is a discharger of pollutants from one or more point
        sources into the waters of the United States.

        >>> PCS().facility('location_zip_code', '76108')
        """
        return self._resolve_call('PCS_PERMIT_FACILITY', column, value, **kwargs)

    def hearing(self, column=None, value=None, **kwargs):
        """
        An evidentiary hearing.

        >>> PCS().hearing('event_date', '23-MAY-01')
        """
        return self._resolve_call('PCS_EVIDENTIARY_HEARING_EVENT', column,
                                  value, **kwargs)

    def industrial_user(self, column=None, value=None, **kwargs):
        """
        Information from the PCI_AUDIT table pertaining to industrial users,
        i.e. the number of significant industrial users.

        >>> PCS().industrial_user('insp_date', '16-MAR-01')
        """
        return self._resolve_call('PCS_INDUSTRIAL_USER_INFO', column,
                                  value, **kwargs)

    def inspection(self, column=None, value=None, **kwargs):
        """
        An official visit to the permit facility on a periodic basis which
        consists of the following inspection types: NPDES, Biomonitoring,
        Pretreatment, and Industrial User.

        >>> PCS().inspection('insp_date', '16-MAR-01')
        """
        return self._resolve_call('PCS_INSPECTION', column, value, **kwargs)

    def permit_event(self, column=None, value=None, **kwargs):
        """
        A permit event tracks the lifecycle of a permit from issuance to
        expiration. Examples include 'Application Received' and 'Permit
        Issued', etc.

        >>> PCS().permit_event('event_actual_date', '16-MAR-04')
        """
        return self._resolve_call('PCS_PERMIT_EVENT', column, value, **kwargs)

    def pipe_schedule(self, column=None, value=None, **kwargs):
        """
        Particular discharge points at a permit facility that are governed by
        effluent limitations and monitoring and submission requirements.

        >>> PCS().pipe_schedule('state_submission_units', 'M')
        """
        return self._resolve_call('PCS_PIPE_SCHED', column, value, **kwargs)

    def single_violation(self, column=None, value=None, **kwargs):
        """
        A single event violation is a one-time event that occurred on a fixed
        date, and is associated with one permitted facility.

        >>> PCS().single_violation('single_event_viol_date', '16-MAR-01')
        """
        return self._resolve_call('PCS_SINGLE_EVENT_VIOL', column,
                                  value, **kwargs)

    def sludge(self, column=None, value=None, **kwargs):
        """
        Sludge information describes the volumn of sludge produced at a
        facility, identification information on a sludge handler, and
        classification/permitting information on a facility that handles
        sludge, such as a pretreatment POTW.

        >>> PCS().sludge('county_name', 'San Francisco')
        """
        return self._resolve_call('PCS_SLUDGE', column, value, **kwargs)
