#!/usr/bin/env python

"""Unit tests for the RADInfo API."""

import unittest

from epa.radinfo import RADInfo


class TestRADInfoInit(unittest.TestCase):

    def test_default_init(self):
        r = RADInfo()
        self.assertEquals(r.base_url, 'http://iaspub.epa.gov/enviro/efservice')
        self.assertEquals(r.output_format, 'xml')
        self.assertTrue(isinstance(r.lookup_table, dict))


class TestCatalogMethod(unittest.TestCase):

    def test_empty_catalog_method(self):
        data = RADInfo().catalog()
        expected = ['regulation', 'facility_type', 'geo',
                    'regulatory_program', 'facility']
        self.assertEquals(data, expected)

    def test_incorrect_catalog_method_arg_throws_error(self):
        self.assertRaises(KeyError, RADInfo().catalog, 'should_be_error')

    def test_catalog_method_with_table_arg_returns_dict(self):
        data = RADInfo().catalog('regulation')
        self.assertTrue(isinstance(data, dict))

    def test_catalog_method_with_both_args_returns_string(self):
        data = RADInfo().catalog('regulation', 'SECTION_ID')
        expected = ('The section number of the specific Code of Federal '
                    'regulation (e.g. Part 60.489).')
        self.assertEquals(data, expected)

    def test_catalog_method_resolves_lowercase_column_names(self):
        data = RADInfo().catalog('regulation', 'section_id')
        expected = ('The section number of the specific Code of Federal '
                    'regulation (e.g. Part 60.489).')
        self.assertEquals(data, expected)


if __name__ == '__main__':
    unittest.main()
