#!/usr/bin/env python

"""Unit tests for the GICS Python wrapper."""

import unittest

from epa.gics import GICS
from epa.envirofacts import envirofacts_api

from test_pcs import mock_urlopen


class TestActionMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_action_method(self):
        GICS().action('action_code', 'A')
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'GIC_ACTION/ACTION_CODE/A/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestApplicantMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_default_action_method(self):
        GICS().applicant('zip_code', 94105)
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'GIC_APPLICANT/ZIP_CODE/94105/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestConstructionMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_construction_method_for_percent_complete(self):
        GICS().construction('complete_percent', 91)
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'GIC_CONSTRUCTION/COMPLETE_PERCENT/91/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestEligibleCostMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_eligible_cost_method_for_amount(self):
        GICS().eligible_cost('amount', 100000)
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'GIC_ELIGIBLE_COST/AMOUNT/100000/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestGrantMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_grant_method_for_city_name(self):
        GICS().grant('project_city_name', 'San Francisco')
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'GIC_GRANT/PROJECT_CITY_NAME/SAN%20FRANCISCO/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)


class TestMilestoneMethod(unittest.TestCase):

    def setUp(self):
        mock_urlopen()

    def test_milestone_method_for_milestone_date(self):
        GICS().milestone('milestone_date', '16-MAR-01')
        expected_url = ('http://iaspub.epa.gov/enviro/efservice/'
                        'GIC_MILESTONE/MILESTONE_DATE/16-MAR-01/rows/0:100')
        envirofacts_api.urlopen.assert_called_with(expected_url)
