#!/usr/bin/env python
"""
Author: Zach Williams, <zach AT codeforamerica DOT org>

Copyright (c) 2011, Code for America. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer. Redistributions in binary form
must reproduce the above copyright notice, this list of conditions and the
following disclaimer in the documentation and/or other materials provided with
the distribution. Neither the name of Code for America nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission. THIS SOFTWARE IS PROVIDED
BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
EPA Python API wrapper
======================

Python wrapper for the multiple APIs available through the EPA's
website.

Documentation for the APIs can be found here: 
[http://www.epa.gov/enviro/facts/ef_restful.html](http://www.epa.gov/enviro/facts/ef_restful.html)


APIs
----

### RADInfo

    >>> from epa.radinfo import RADInfo
    >>> r = RADInfo()

    >>> # An empty method returns a dict of available columns.
    ... r.facility_type()

    >>> # A method call without a value returns info about that column.
    ... r.facility_type('cit_ref_code')

    >>> # Find information on a facility in a certain city.
    ... r.facility('city_name', 'Berkeley')
    {'data': {'about': "Berkeley's Radiation Facility"}}

    >>> # Find all the radiation facilities in Texas.
    ... r.facility('state_code', 'TX')
    {'all': {'seven': 'Texas facilities'}}

    >>> # Integer values are converted to strings automatically.
    ... r.regulation('part_id', 61)

    >>> r.regulation('title_id', '40')

    >>> # Search for the CIT_REF_CODE of a RAD NPL facility.
    ... r.regulation('cit_ref_code', '40CFR300')

    >>> data = r.regulatory_program('sec_cit_ref_flag', 'N')
    >>> data['Count']
    100

    >>> new_data = r.regulatory_program('sec_cit_ref_code', 'N', count=200)
    >>> new_data['Count']
    190

    >>> data = r.regulatory_program('cit_ref_code', '40CFR300', start=50)
    >>> data['Count']
    8

    >>> # Find geographic information.
    ... r.geo('geometric_type_code', '001')


### GICS

    >>> from epa.gics import GICS
    >>> g = GICS()

    >>> # List construction projects that are 91% complete.
    ... g.construction('complete_percent', 91)

    >>> # Find all the construction projects at a specific facility.
    ... data = g.construction('facility_number', 190226001)
    >>> data['Count']
    8

    >>> # Search for a specific grant's milestones.
    ... g.milestone('grant_number', 190709130)

    >>> # Find all ADMIN COMPLETE milestones.
    ... g.milestone('milestone_type', 'ADMIN COMPLETE')

    >>> # Search for milestones on a specific DD-MON-YY date.
    ... g.milestone('milestone_date', '16-MAR-01')

    >>> # Find descriptions for a status code.
    ... g.status('status_code', 'AF')

    >>> # Find grants on a specific date.
    ... g.grant('award_accept_date', '12-MAR-01')

    >>> # Find grants for a specific city.
    ... g.grant('projecty_city_name', 'San Francisco')

    >>> # Search the GICS API's grants for a specific state.
    ... g.grant('project_state_code', 'TX', count=500)

    >>> # Find an applicant in a specific zipcode.
    ... g.applicant('zip_code', 94105)


### PCS

    >>> from epa.pcs import PCS
    >>> p = PCS()

    >>> # Search for facilities in a city.
    ... p.facility('location_city', 'San Francisco')

    >>> # Find a facility in a particular zipcode.
    ... p.facility('location_zip_code', 76108)

    >>> # Find a sludge facility in a specific state.
    ... p.sludge('handler_state', 'NY')

    >>> p.pipe_schedule('discharge_num', 333)

    >>> p.pipe_schedule('npdes', 'GMG290024')

    >>> p.dmr_measurement('discharge_num', '001')

    >>> # Find the inspections that took place on a specific date.
    ... p.inspection('insp_date', '16-MAR-01')

    >>> p.enforcement_action('ea_code', '09')


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
"""

setup(name="epa",
      version="1.0",
      description=("Python wrapper for the multiple APIs available through "
                   "the EPA's website."),
      long_description=long_description,
      keywords="epa, EPA, environment",
      author="Zach Williams",
      author_email="zach@codeforamerica.org",
      url="https://github.com/codeforamerica/epa_python",
      license="BSD",
      packages=["epa"],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                  ],
      test_suite="test.py",
      tests_require=["mock", "Mock"])
