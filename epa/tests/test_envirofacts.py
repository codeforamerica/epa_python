#!/usr/bin/env python

"""Unit tests for the EPA's Envirofacts API."""

import unittest

from mock import Mock

from epa.envirofacts import Envirofacts

# For mocking out urlopen and xml2dict
from epa.envirofacts import envirofacts_api
from epa.envirofacts.api import api


class TestEnvirofactsInit(unittest.TestCase):

    def test_default_init(self):
        enviro = Envirofacts()
        expected_url = 'https://data.epa.gov/efservice'
        self.assertEqual(enviro.base_url, expected_url)


class TestCatalogMethod(unittest.TestCase):

    def test_catalog_method_returns_None(self):
        data = Envirofacts().catalog()
        self.assertEqual(data, None)

    def test_catalog_method_with_arg_returns_None(self):
        data = Envirofacts().catalog('test')
        self.assertEqual(data, None)

    def test_catalog_lookup(self):
        table_lookup = {"TABLE_A": "Table A", "TABLE_B": "Table B"}
        table_column_lookup = {"TABLE_A": {"COLUMN_A": "Column A"}, "TABLE_B": {"COLUMN_B": "Column B"}}
        column_table_lookup = {"COLUMN_A": ["TABLE_A"], "COLUMN_B": ["TABLE_B"]}
        enviro = Envirofacts()
        enviro.table_lookup = table_lookup
        enviro.table_column_lookup = table_column_lookup
        enviro.column_table_lookup = column_table_lookup
        self.assertEqual("Table A", enviro.catalog('table_A'))
        self.assertEqual("Column A", enviro.catalog('table_A', 'column_A'))
        self.assertEqual(None, enviro.catalog('table_A', 'column_B'))
        self.assertEqual(["TABLE_A"], enviro.catalog(column='COLUMN_A'))


class TestCallApiMethod(unittest.TestCase):

    def setUp(self):
        envirofacts_api.urlopen = Mock()
        api.xml2dict = Mock()

    def test_call_api_method_with_test_path(self):
        Envirofacts().call_api('test', 'foo', 'bar')
        expected_url = ('https://data.epa.gov/efservice/'
                        'test/foo/=/bar/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)

    def test_call_api_method_with_count_keyword(self):
        Envirofacts().call_api('test', 'foo', 'bar', count=200)
        expected_url = ('https://data.epa.gov/efservice/'
                        'test/foo/=/bar/rows/0:200')
        envirofacts_api.urlopen.assert_called_with(expected_url)

    def test_call_api_method_with_operation_keyword(self):
        Envirofacts().call_api('test', 'foo', 'bar', operation='>')
        expected_url = ('https://data.epa.gov/efservice/'
                        'test/foo/>/bar/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)

    def test_call_api_method_with_start_keyword(self):
        Envirofacts().call_api('test', 'foo', 'bar', start=200)
        expected_url = ('https://data.epa.gov/efservice/'
                        'test/foo/=/bar/rows/200:300')
        envirofacts_api.urlopen.assert_called_with(expected_url)

    def test_call_api_method_with_no_output_formatting(self):
        Envirofacts().call_api('test', 'foo', 'bar', output_format=None)
        self.assertFalse(api.xml2dict.called)


class TestResolveCallMethod(unittest.TestCase):

    def setUp(self):
        envirofacts_api.urlopen = Mock()
        api.xml2dict = Mock()

    def test_resolve_call_with_one_arg_returns_None(self):
        data = Envirofacts()._resolve_call('test')
        self.assertEqual(data, None)

    def test_resolve_call_with_two_args_returns_None(self):
        data = Envirofacts()._resolve_call('test', 'foo')
        self.assertEqual(data, None)

    def test_resolve_call_uses_urlopen_when_passed_three_args(self):
        Envirofacts()._resolve_call('test', 'foo', 'bar')
        self.assertTrue(envirofacts_api.urlopen.called)


class TestNumberOfRowsMethod(unittest.TestCase):

    def test_empty_number_of_rows(self):
        rows = Envirofacts()._number_of_rows()
        self.assertEqual(rows, 'rows/0:100')

    def test_number_of_rows_with_start_keyword(self):
        rows = Envirofacts()._number_of_rows(start=900)
        self.assertEqual(rows, 'rows/900:1000')

    def test_number_of_rows_with_count_keyword(self):
        rows = Envirofacts()._number_of_rows(count=200)
        self.assertEqual(rows, 'rows/0:200')

    def test_number_of_rows_with_nonsense_keywords(self):
        rows = Envirofacts()._number_of_rows(foo='bar')
        self.assertEqual(rows, 'rows/0:100')
