EPA Python API wrapper
======================

Python wrapper for the multiple APIs available through the EPA's
website.

Documentation for the APIs can be found here: 
[https://www.epa.gov/enviro/envirofacts-data-service-api](https://www.epa.gov/enviro/envirofacts-data-service-api)

A chart of the API modules can be found [here](https://www.epa.gov/enviro/envirofacts-model) which shows the tables
and their foreign key relationships. 


APIs
----

### FRS

```python
>>> from epa.frs import FRS
>>> f = FRS()

>>> # General-use query function, accepts 1-3 table names to be joined.
... f.frs_query([<table>], <column>, <value>)
```

### PCS

```python
>>> from epa.pcs import PCS
>>> p = PCS()

>>> # General-use query function, accepts 1-3 table names to be joined.
... p.pcs_query(["PCS_PERMIT_FACILITY"], "CITY_CODE", "03120")

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

### TRI

```python
>>> from epa.tri import TRI
>>> t = TRI()

>>> # General-use query function, accepts 1-3 table names to be joined.
... t.tri_query([<table>], <column>, <value>)
```

The query functions accept these key parameters:<br>
operation: one of ['=', '!=', '<', '>', 'BEGINNING', 'CONTAINING'], default is '='<br>
output_format: one of ['dicts', 'xml', 'json', 'csv', 'excel'], default is 'dicts' (list of row dicts)<br>
start: starting row to output, default is 1<br>
count: max number of rows, default is 100<br>


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
