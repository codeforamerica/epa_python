EPA Python API wrapper
======================

Python wrapper for the multiple APIs available through the EPA's
website.

Documentation for the APIs can be found here: 
[http://www.epa.gov/enviro/facts/ef_restful.html](http://www.epa.gov/enviro/facts/ef_restful.html)


APIs
----

### RADInfo

```python
>>> from epa.radinfo import RADInfo

>>> r = RADInfo()

>>> # Find information on a facility in a certain city.
... r.facility('city_name', 'Berkeley')
{'data': {'about': 'Berkeley's Radiation Facility'}}

>>> # Find all the radiation facilities in Texas.
... r.facility('state_code', 'TX')
{'all': {'seven': 'Texas facilities'}}

>>> r.regulation('part_id', 61)

>>> r.regulation('title_id', 40)

>>> # Search for the CIT_REF_CODE of a RAD NPL facility.
... r.regulation('cit_ref_code', '40CFR300')

>>> # An empty method returns a dict of available columns.
... r.facility_type()

>>> # A method call without a value returns info about that column.
... r.facility_type('cit_ref_code')
```


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
