#!/usr/bin/env python

"""Unit tests for the RADInfo API."""

import unittest

from epa.radinfo import RADInfo

from mock import Mock

# For mocking purposes.
from epa.envirofacts import envirofacts_api
from epa.envirofacts.api import api


def mock_urlopen():
    """Reduce boilerplate setup code by mocking urlopen and xml2dict."""
    envirofacts_api.urlopen = Mock()
    api.xml2dict = Mock()


class TestRADInfoInit(unittest.TestCase):

    def test_default_init(self):
        r = RADInfo()
        self.assertEquals(r.base_url, 'http://iaspub.epa.gov/enviro/efservice')
        self.assertEquals(r.output_format, 'xml')
        self.assertTrue(isinstance(r.lookup_table, dict))


class TestRADInfoCatalogMethod(unittest.TestCase):

    def test_empty_catalog_method(self):
        data = RADInfo().catalog()
        expected = ['regulation', 'facility_type', 'geo',
                    'regulatory_program', 'facility']
        self.assertEquals(data, expected)

    def test_incorrect_catalog_method_arg_throws_error(self):
        self.assertRaises(KeyError, RADInfo().catalog, 'should_be_error')

    def test_catalog_method_with_table_arg_returns_dict(self):
        data = RADInfo().catalog('RAD_REGULATION')
        self.assertTrue(isinstance(data, dict))

    def test_catalog_method_with_both_args_returns_string(self):
        data = RADInfo().catalog('RAD_REGULATION', 'SECTION_ID')
        expected = ('The section number of the specific Code of Federal '
                    'regulation (e.g. Part 60.489).')
        self.assertEquals(data, expected)

    def test_catalog_method_resolves_lowercase_column_names(self):
        data = RADInfo().catalog('RAD_REGULATION', 'section_id')
        expected = ('The section number of the specific Code of Federal '
                    'regulation (e.g. Part 60.489).')
        self.assertEquals(data, expected)


class TestFacilityMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_facility_method(self):
        RADInfo().facility('state_code', 'TX')
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'RAD_FACILITY/STATE_CODE/TX/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestFacilityTypeMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_facility_type_method(self):
        RADInfo().facility_type('sec_cit_ref_flag', 'N')
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'RAD_FACILITY_TYPE/SEC_CIT_REF_FLAG/N/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestGeoMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_geo_method(self):
        RADInfo().geo('geometric_type_code', '001')
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'RAD_GEO_LOCATION/GEOMETRIC_TYPE_CODE/001/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestRegulationMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_regulation_method(self):
        RADInfo().regulation('title_id', 40)
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'RAD_REGULATION/TITLE_ID/40/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestRegulatoryProgramMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_regulatory_program_method(self):
        RADInfo().regulatory_program('sec_cit_ref_flag', 'N')
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'RAD_REGULATORY_PROG/SEC_CIT_REF_FLAG/N/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)
