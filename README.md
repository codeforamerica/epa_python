EPA Python API wrapper
======================

Python wrapper for the multiple APIs available through the EPA's
website.

Documentation for the APIs can be found here: 
[https://www.epa.gov/enviro/envirofacts-data-service-api](https://www.epa.gov/enviro/envirofacts-data-service-api)


APIs
----

### PCS

```python
>>> from epa.pcs import PCS
>>> p = PCS()

>>> # Search for facilities in a city.
... p.facility('location_city', 'San Francisco')

>>> # Find a facility in a particular zipcode.
... p.facility('location_zip_code', 76108)

>>> p.pipe_schedule('discharge_num', 333, operation='>')

>>> p.pipe_schedule('npdes', 'GMG290024')

>>> p.dmr_measurement('discharge_num', '001')

>>> # Find the inspections that took place on a specific date.
... p.inspection('insp_date', '16-MAR-01')

```

Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
