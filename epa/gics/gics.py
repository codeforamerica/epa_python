#!/usr/bin/env python

"""Python wrapper for the EPA's Grants Information and Control System API."""

from epa.envirofacts import Envirofacts

from lookup_table import lookup_table


class GICS(Envirofacts):
    """Python wrapper for the GICS API."""

    def __init__(self):
        super(GICS, self).__init__()
        self.lookup_table = lookup_table
        self.lookup_methods = [
            'action', 'applicant', 'assistance', 'authority',
            'construction', 'eligible_cost', 'grant', 'grant_assistance',
            'grant_authority', 'lab_office', 'milestone', 'record_type',
            'srf_cap', 'status'
        ]

    def action(self, column=None, value=None, **kwargs):
        """
        The underlying GICS table provides codes and descriptions
        identifying the current status or disposition of a grant project.

        >>> GICS().action('action_code', 'A')
        """
        return self._resolve_call('GIC_ACTION', column, value, **kwargs)

    def applicant(self, column=None, value=None, **kwargs):
        """
        Find the applicant information for a grant.

        >>> GICS().applicant('zip_code', 94105)
        """
        return self._resolve_call('GIC_APPLICANT', column, value, **kwargs)

    def assistance(self, column=None, value=None, **kwargs):
        """
        Provides the Catalog of Federal Domestic Assistance (CFDA) codes and
        names.
        """
        return self._resolve_call('GIC_ASST_PGM', column, value, **kwargs)

    def authority(self, column=None, value=None, **kwargs):
        """Provides codes and associated authorizing statutes."""
        return self._resolve_call('GIC_AUTHORITY', column, value, **kwargs)

    def construction(self, column=None, value=None, **kwargs):
        """
        Identifies monetary, descriptive, and milestone information for
        Wastewater Treatment construction grants.

        >>> GICS().construction('complete_percent', 91)
        """
        return self._resolve_call('GIC_CONSTRUCTION', column, value, **kwargs)

    def eligible_cost(self, column=None, value=None, **kwargs):
        """
        The assistance dollar amounts by eligible cost category.

        >>> GICS().eligible_cost('amount', 100000)
        """
        return self._resolve_call('GIC_ELIGIBLE_COST', column, value, **kwargs)

    def grant(self, column=None, value=None, **kwargs):
        """
        Provides various award, project, and grant personnel information.

        >>> GICS().grant('project_city_name', 'San Francisco')
        """
        return self._resolve_call('GIC_GRANT', column, value, **kwargs)

    def grant_assistance(self, column=None, value=None, **kwargs):
        """Many-to-many table connecting grants and assistance."""
        return self._resolve_call('GIC_GRANT_ASST_PGM', column, value, **kwargs)

    def grant_authority(self, column=None, value=None, **kwargs):
        """Many-to-many table connecting grants and authority."""
        return self._resolve_call('GIC_GRANT_AUTH', column, value, **kwargs)

    def lab_office(self, column=None, value=None, **kwargs):
        """Abbreviations, names, and locations of labratories and offices."""
        return self._resolve_call('GIC_LAB_OFFICE', column, value, **kwargs)

    def milestone(self, column=None, value=None, **kwargs):
        """
        Status codes and related dates of certain grants,

        >>> GICS().milestone('milestone_date', '16-MAR-01')
        """
        return self._resolve_call('GIC_MILESTONE', column, value, **kwargs)

    def record_type(self, column=None, value=None, **kwargs):
        """
        Codes and descriptions indicating whether an award is for a new
        project or for the continuation of a currently funded one.

        >>> GICS().record_type('record_type_code', 'A')
        """
        return self._resolve_call('GIC_RECORD_TYPE', column, value, **kwargs)

    def srf_cap(self, column=None, value=None, **kwargs):
        """
        Fiscal dollar amounts for State Revolving Fund Capitalization
        Grants.

        >>> GICS().srf_cap('grant_number', '340001900')
        """
        return self._resolve_call('GIC_SRF_CAP', column, value, **kwargs)

    def status(self, column=None, value=None, **kwargs):
        """
        Provides codes and descriptions of project milestones.

        >>> GICS().status('status_code', 'AF')
        """
        return self._resolve_call('GIC_STATUS', column, value, **kwargs)
