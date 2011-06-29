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
>>> data['RAD_REGULATORY_PROGList']['Count']
100

>>> new_data = r.regulatory_program('sec_cit_ref_code', 'N', count=200)
>>> new_data['RAD_REGULATORY_PROGList']['Count']
190

>>> data = r.regulatory_program('cit_ref_code', '40CFR300', start=50)
>>> data['RAD_REGULATORY_PROGList']['Count']
8

>>> # Find geographic information.
... r.geo('geometric_type_code', '001')

```

### GICS

```python
>>> from epa.gics import GICS
>>> g = GICS()

>>> # List construction projects that are 91% complete.
... g.construction('complete_percent', 91)

>>> # Find all the construction projects at a specific facility.
... data = g.construction('facility_number', 190226001)
>>> data['GIC_CONSTRUCTIONList']['Count']
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

```


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
