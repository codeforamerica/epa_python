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

    >>> # Find information on a facility in a certain city.
    ... r.facility('city_name', 'Berkeley')
    {'data': {'about': 'Berkeley's Radiation Facility'}}

    >>> # Find all the radiation facilities in Texas.
    ... r.facility('state_code', 'TX')
    {'all': {'seven': 'Texas facilities'}}


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
