#!/usr/bin/env python

"""Unit tests for the RADInfo API."""

import unittest

from mock import Mock

from epa.pcs import PCS

# For mocking purposes.
from epa.envirofacts import envirofacts_api
from epa.envirofacts.api import api


def mock_urlopen():
    """Reduce boilerplate setup code by mocking urlopen and xml2dict."""
    envirofacts_api.urlopen = Mock()
    api.xml2dict = Mock()


class TestPcsQuery(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_query_method(self):
        PCS().pcs_query(['PCS_PIPE_SCHED', 'PCS_PCI_AUDIT', 'PCS_PERMIT_FACILITY'], 'NPDES', '16-MAR-01',
                        operation='>')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_PIPE_SCHED/NPDES/>/16-MAR-01/PCS_PCI_AUDIT/PCS_PERMIT_FACILITY/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestAuditMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_audit_method(self):
        PCS().audit('insp_date', '16-MAR-01')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_PCI_AUDIT/INSP_DATE/=/16-MAR-01/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestCodeDescriptionMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_code_description_method(self):
        PCS().code_description('code', 110)
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_CODE_DESC/CODE/=/110/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestComplianceScheduleMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_compliance_schedule_method(self):
        PCS().compliance_schedule('cmpl_schd_evt', '62099')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_CMPL_SCHD/CMPL_SCHD_EVT/=/62099/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestComplianceViolationMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_compliance_violation_method(self):
        PCS().compliance_violation('cs_rnc_detect_date', '16-MAR-04')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_CMPL_SCHD_VIOL/CS_RNC_DETECT_DATE/=/16-MAR-04/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestDmrMeasurementMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_dmr_measurement_method(self):
        PCS().dmr_measurement('season_num', 2)
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_DMR_MEASUREMENT/SEASON_NUM/=/2/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestPCSFacilityMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_facility_method(self):
        PCS().facility('location_zip_code', '76108')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_PERMIT_FACILITY/LOCATION_ZIP_CODE/=/76108/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestHearingMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_hearing_method(self):
        PCS().hearing('event_date', '23-MAY-01')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_EVIDENTIARY_HEARING_EVENT/EVENT_DATE/=/23-MAY-01/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestIndustrialUserMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_industrial_user_method(self):
        PCS().industrial_user('insp_date', '16-MAR-01')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_INDUSTRIAL_USER_INFO/INSP_DATE/=/16-MAR-01/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestInspectionMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_inspection_method(self):
        PCS().inspection('insp_date', '16-MAR-01')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_INSPECTION/INSP_DATE/=/16-MAR-01/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestPermitEventMethod(unittest.TestCase):

    def setUp(self):
       mock_urlopen()

    def test_default_permit_event_method(self):
        PCS().permit_event('event_actual_date', '16-MAR-04')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_PERMIT_EVENT/EVENT_ACTUAL_DATE/=/16-MAR-04/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestPipeScheduleMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_pipe_schedule_method(self):
        PCS().pipe_schedule('state_submission_units', 'M')
        expected_url = ('https://data.epa.gov/efservice/'
                        'PCS_PIPE_SCHED/STATE_SUBMISSION_UNITS/=/M/'
                        'rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)
