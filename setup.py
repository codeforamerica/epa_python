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

Python wrapper for the multiple APIs available through the EPA's website.

Documentation for the APIs can be found here: 
[https://www.epa.gov/enviro/envirofacts-data-service-api](https://www.epa.gov/enviro/envirofacts-data-service-api)


APIs
----

### PCS

    >>> from epa.pcs import PCS
    >>> p = PCS()

    >>> # Search for facilities in a city.
    ... p.facility('location_city', 'San Francisco')

    >>> # Find a facility in a particular zipcode.
    ... p.facility('location_zip_code', 76108)

    >>> # Find a sludge facility in a specific state.
    ... p.sludge('handler_state', 'NY')

    >>> p.pipe_schedule('discharge_num', 333, operation='>')

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
      version="2.0",
      description=("Python wrapper for the multiple APIs available through "
                   "the EPA's website."),
      long_description=long_description,
      keywords="epa, EPA, environment, Envirofacts",
      author="Zach Williams",
      author_email="zach@codeforamerica.org",
      url="https://github.com/codeforamerica/epa_python",
      license="BSD",
      packages=["epa", "epa.pcs", "epa.frs", "epa.envirofacts",
                "epa.envirofacts.api", "epa.envirofacts.api.xml2dict",
                "epa.tri", "epa.tests"],
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
