#!/usr/bin/env python

"""Unit tests for the EPA's Envirofacts API."""

import unittest

from epa.envirofacts import Envirofacts


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


if __name__ == '__main__':
    unittest.main()
