#!/usr/bin/env python

"""Unit tests for the EPA's Envirofacts API."""

import unittest

from mock import Mock, patch

from epa.envirofacts import Envirofacts

# For mocking out urlopen and xml2dict
from epa.envirofacts import envirofacts_api
from epa.envirofacts.api import api


class TestEnvirofactsInit(unittest.TestCase):

    def test_default_init(self):
        enviro = Envirofacts()
        expected_url = 'http://iaspub.epa.gov/enviro/efservice'
        self.assertEquals(enviro.base_url, expected_url)


class TestCatalogMethod(unittest.TestCase):

    def test_catalog_method_returns_None(self):
        data = Envirofacts().catalog()
        self.assertEquals(data, None)

    def test_catalog_method_with_arg_returns_None(self):
        data = Envirofacts().catalog('test')
        self.assertEquals(data, None)


class TestCallApiMethod(unittest.TestCase):

    def setUp(self):
        envirofacts_api.urlopen = Mock()
        api.xml2dict = Mock()

    def test_call_api_method_with_test_path(self):
        Envirofacts().call_api('test', 'foo', 'bar')
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'test/foo/bar/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)

    def test_call_api_method_with_count_keyword(self):
        Envirofacts().call_api('test', 'foo', 'bar', count=200)
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'test/foo/bar/rows/0:200')
        envirofacts_api.urlopen.assert_called_with(expected_url)

    def test_call_api_method_with_start_keyword(self):
        Envirofacts().call_api('test', 'foo', 'bar', start=200)
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'test/foo/bar/rows/200:300')
        envirofacts_api.urlopen.assert_called_with(expected_url)

    def test_call_api_method_with_no_output_formatting(self):
        Envirofacts().call_api('test', 'foo', 'bar', output_format=None)
        self.assertFalse(api.xml2dict.called)


class TestNumberOfRowsMethod(unittest.TestCase):

    def test_empty_number_of_rows(self):
        rows = Envirofacts()._number_of_rows()
        self.assertEquals(rows, '0:100')

    def test_number_of_rows_with_start_keyword(self):
        rows = Envirofacts()._number_of_rows(start=900)
        self.assertEquals(rows, '900:1000')

    def test_number_of_rows_with_count_keyword(self):
        rows = Envirofacts()._number_of_rows(count=200)
        self.assertEquals(rows, '0:200')

    def test_number_of_rows_with_nonsense_keywords(self):
        rows = Envirofacts()._number_of_rows(foo='bar')
        self.assertEquals(rows, '0:100')


if __name__ == '__main__':
    unittest.main()
