#!/usr/bin/env python

lookup_table = {
    'RAD_FACILITY': {
        'CITY_NAME':
            ('The name of the city, town, or village where a facility is '
             'located.'),
        'CONGRESSIONAL_DIST_NUM':
            ('The number that represents a Congressional District for a '
             'state within the United States.'),
        'COUNTRY_NAME':
            ('The name that represents a primary geopolitical unit of the '
             'world. The default value for RADInfo is "United States".'),
        'COUNTY_NAME':
            ('The name of U.S. county or county equivalent, as listed in '
             'FIPS Pub 6-4.'),
        'EF_PGM_SOURCE':
            ('The abbreviated name of an information management system '
             'contained in Envirofacts that may serve as a source for '
             'RADInfo data.'),
        'EPA_REGION_CODE':
            'The code that represents an EPA Region.',
        'FACILITY_REGISTRY_ID':
            ('The identification number assigned by the EPA Facility '
             'Registry System to uniquely identify a facility site.'),
        'FED_FACILITY_CODE':
            ('A code identifying whether or not a site is a Federal '
             '(U.S. Government) facility. Valid Values: "D" = Status '
             'Undetermined, "Y" = Federal Facility, "N" = Not a Federal '
             'Facility.'),
        'FRS_UPDATE_DATE':
            ('The date when RADInfo facility data is updated using the '
             'Facility Registry System.'),
        'HUC_CODE':
            ('The hydrologic unit code (HUC) that represents a geographic '
             'area representing part or all of a surface-draining basin, a '
             'combination of drainage basins, or a distinct hydrologic '
             'feature.'),
        'LOCATION_ADDRESS':
            ('The address that describes the physical (geographic) location '
             'of the front door or main entrance of a facility site, '
             'including urban-style street address or rural address.'),
        'POSTAL_CODE':
            ('The combination of the 5-digit Zone Improvement Plan (ZIP) '
             'code and the four-digit extension code (if available) that '
             'represents the geographic segment that is a subunit of the '
             'ZIP Code, assigned by the U.S. Postal Service to a geographic '
             'location to facilitate delivery, or the postal zone specific '
             'to the country, other than the U.S., where the mail is '
             'delivered.'),
        'PRIMARY_NAME':
            'The name of a facility site.',
        'RAD_CHANGE_DATE':
            ('The date when RADInfo facility data was altered by a '
             'designated RADInfo user.'),
        'RAD_SYS_ID':
            ('The non-intelligent, unique identifier assigned to a RADInfo '
             'facility or site.'),
        'SOURCE_DATA':
            ('The initial source of RADInfo information for a facility. '
             'Reconciliation with the Facility Registry System may '
             'subsequently alter some source data.'),
        'STATE_CODE':
            ('The U.S. Postal Service abbreviation that represents the '
             'state of state equivalent for the U.S. and Canada.'),
        'STATE_NAME':
            ('The name of the principal administrative subdivision of the '
             'United States.'),
        'SUPPLEMENTAL_LOCATION':
            ('The text that provides additional information about a place, '
             'including a building name with its secondary unit and number, '
             'an industrial park name, an installation name, or descriptive '
             'text where no formal address is available.'),
        'TRIBAL_LAND_CODE':
            ('Code indicating whether or not the facility is located on '
             'tribal land. Valid values: "Y" = yes; "N" = no.'),
        'TRIBAL_LAND_NAME':
            ('The name of an American Indian or Alaskan native area where '
             'the facility is located, as identified through query '
             'mechanisms available to the Envirofacts network.'),
        'URL':
            ('The URL associated with the web which provides risk data '
             'about the associated radioisotope.'),
        'URL_LINK_DESCRIPTION':
            ('A web site description identifying the type of information '
             'provided at the URL.'),
    },
    'RAD_FACILITY_TYPE': {
        'CIT_REF_CODE':
            ('The code that represents the environmental regulation with '
             'oversight of a facility. For example, the CIT_REF_CODE for a '
             'RAD NPL facility would be equal to "40CFR300".'),
        'FACILITY_TYPE':
            ('The type of facility regulated by the governing regulation. '
             'Valid Values include: '
             'NESHAPS/Underground Uranium Mine, '
             'NESHAPS/DOE RAD Facility (Non-Radon), '
             'NESHAPS/Other Federal Facility, '
             'NESHAPS/Elemental Phosphorus Plant, '
             'NESHAPS/DOE Radon, '
             'NESHAPS/Phosphogypsum Stack, '
             'NESHAPS/Disposal of Uranium Mill Tailings, '
             'NESHAPS/Operating Uranium Mill Tailings, '
             'WIPP Facility/Repository, '
             'WIPP Facility/Generator Site, '
             'RAD NPL Facility'),
        'SEC_CIT_REF_FLAG':
            ('Indicates than an additional Citation Reference Code must '
             'be used to uniquely identify this this type of facility. For '
             'example, the WIPP repository is uniquely identified as being '
             'regulated under both 40CFR191 and 40CFR194. This flag is set to '
             '"Y" when a facility has this exact combination of '
             'CIT_REF_CODE(s) associated with it. In the near term, no other '
             'combination of governing regulations will cause this flag to be '
             'set.'),
        'SUBPART_ID':
            ('Identification number assigned to the subpart of the '
             'environmental regulation with oversight of the facility.'),
    },
    'RAD_GEO_LOCATION': {
        'COORDINATE_DATA_SOURCE_CODE':
            ('The code that represents the party responsible for providing '
             'the latitude and longitude coordinates.'),
        'DATA_COLLECTION_DATE':
            'The calendar date when data were collected.',
        'EF_PGM_SOURCE':
            ('The abbreviated name of an information management system '
             'contained in Envirofacts that may serve as a source for '
             'RADInfo data.'),
        'GEOMETRIC_TYPE_CODE':
            ('The code that represents the geometric entity represented by '
             'one point or a sequence of latitude and longitude points.'),
        'HORIZONTAL_ACCURACY_MEASURE':
            ('The measure of the accuracy (in meters) of the latitude and '
             'longitude coordinates.'),
        'HORIZONTAL_COLLECT_METHOD_CODE':
            ('The code that represents the method used to determine the '
             'latitude and longitude coordinates for a point on the earth.'),
        'HORIZONTAL_REFER_DATUM_CODE':
            ('The code that represents the reference datum used in '
             'determining latitude and longitude coordinates.'),
        'LATITUDE_MEASURE':
            ('The measure of the angular distance on a meridian north or '
             'south of the equator.'),
        'LOCATION_COMMENTS_TEXT':
            ('The text that provides additional information about the '
             'geographic coordinates.'),
        'LONGITUDE_MEASURE':
            ('The measure of the angular distance on a meridian east or '
             'west of the prime meridian.'),
        'RAD_CHANGE_DATE':
            ('The date when RADInfo facility data was altered by a '
             'designated RADInfo user.'),
        'RAD_OVERRIDE':
            ('A flag indicating that the latitude and longitude coordinates '
             'for the facility in RADInfo are preferred to the designated '
             'best value coordinates in the Envirofacts Locational Reference '
             'Tables.'),
        'RAD_SYS_ID':
            ('The non-intelligent, unique identifier assigned to a RADInfo '
             'facility or site.'),
        'REFERENCE_POINT_CODE':
            ('The code that represents the place for which geographic '
             'coordinates were established.'),
        'SOURCE_MAP_SCALE_NUMBER':
            ('The number that represents the proportional distance on the '
             'ground for one unit of measure on the map or photo.'),
        'SUB_ID':
            'Identification number for the operable unit.',
        'SUB_TYPE_CODE':
            'The code for an operable unit. View a list of permitted values.',
        'VERTICAL_ACCURACY_MEASURE':
            ('The measure of the accuracy (in meters) of the vertical '
             'measure (i.e., the altitude) of a reference point.'),
        'VERTICAL_COLLECT_METHOD_CASE':
            ('The code that represents the method used to collect the '
             'vertical measure (i.e., the altitude) of a reference point.'),
        'VERTICAL_MEASURE':
            ('The measure of elevation (i.e., the altitude), in meters, '
             'above or below a reference datum.'),
        'VERTICAL_REFERENCE_DATA_CODE':
            ('The code that represents the reference datum used to '
            'determine the vertical measure (i.e., the altitude).'),
    },
    'RAD_REGULATION': {
        'CFR_PART':
            ('The Part (name/title) of the regulation related '
             'to the facility.'),
        'CRF_SECTION':
            ('The Section (name/title) of the regulation related to '
             'the facility.'),
        'CFR_SUBPART':
            ('Subpart related to the specific part of the CFR '
             '(e.g. Subpart D).'),
        'CIT_REF_CODE':
            ('The code that represents the environmental regulation with '
             'oversight of a facility. For example, the CIT_REF_CODE for a '
             'RAD NPL facility would be equal to "40CFR300".'),
        'PART_ID':
            ('The part number of the specific Code of Federal regulation '
             '(e.g. Part 60).'),
        'RAD_CHANGE_DATE':
            ('The date when RADInfo facility data was altered by a '
             'designated RADInfo user.'),
        'REG_TITLE':
            'The title (name) of the regulation related to the facility.',
        'SECTION_ID':
            ('The section number of the specific Code of Federal regulation '
             '(e.g. Part 60.489).'),
        'STATUTE':
            ('The name of the Federal statute governing the regulations '
             'related to the facility.'),
        'STAT_ACRONYM':
            ('The acronym of the Federal statute governing the regulations '
             'related to the facility.'),
        'SUBPART_ID':
            ('Identification number assigned to the subpart of the '
             'environmental regulation with oversight of the facility.'),
        'TITLE_ID':
            ('The Code of Federal Regulation number related to the '
             'regulation (e.g. 40 CFR).'),
        'URL':
            ('The URL associated with the web which provides risk data '
             'about the associated radioisotope.'),
    },
    'RAD_REGULATORY_PROG': {
        'CIT_REF_CODE':
            ('The code that represents the environmental regulation with '
             'oversight of a facility. For example, the CIT_REF_CODE for '
             'a RAD NPL facility would be equal to "40CFR300".'),
        'ENFORCEMENT_AGENCY':
            ('The Agency (or Agreement State) responsible for the '
             'implementation and enforcement of the radiation standard(s) '
             'established. In the case of 40 CFR 190, the NRC or one of the '
             '29 Agreement States is identified as the Enforcement Agency '
             'under this definition.'),
        'OPERATING_ORGANIZATION':
            ('The facility owner/operator who conducts the daily operations '
             'and submits compliance reports to the Enforcement Agency.'),
        'OVERSIGHT_AGENCY':
            ('The Agency responsible for establishing generally applicable '
             'radiation standards. In the case of 40 CFR 190, EPA is '
             'identified as the Oversight Agency under this definition.'),
        'PROG_FAC_STATUS':
            ('The status of a facility in relation to the program monitoring '
             'it. An active facility status means that the facility is '
             'currently operational or activities such as remediation are '
             'ongoing at the site/facility. An inactive facility status means '
             'the facility is no longer operational. A standby status '
             'indicates that the facility (i.e., uranium mine) is not '
             'currently operating, but has not committed to closing down its '
             'operation. An archived facility status means remediation has '
             'been completed; such facilities are no longer of regulatory '
             'concern and the information associated with them can be placed '
             'in an archive database.'),
        'PROG_FAC_TYPE':
            ('Code indicating the type of facility or complex facility that '
             'is regulated or monitored by a program. Only those facilities '
             'typecast as RAD NESHAPS Facilities and reporting under 40CFR61 '
             'are contained in the RAD_NESHAPS_FACILITY table. Similarly, '
             'only those facilities typecast as WIPP Facilites and governed '
             'under 40CFR194, or the combination of 40CFR191 and 40CFR194, '
             'are contained in the RAD_WIPP_FACILITY table, and only those '
             'facilities that must comply with 40CFR300 and typecast as RAD '
             'NPL F acilities are contained in the RAD_NPL_FACILITY table.'),
        'RAD_CHANGE_DATE':
            ('The date when RADInfo facility data was altered by a '
             'designated RADInfo user.'),
        'RAD_SYS_ID':
            ('The non-intelligent, unique identifier assigned to a RADInfo '
             'facility or site.'),
        'SEC_CIT_REF_FLAG':
            ('Indicates than an additional Citation Reference Code must '
             'be used to uniquely identify this this type of facility. For '
             'example, the WIPP repository is uniquely identified as being '
             'regulated under both 40CFR191 and 40CFR194. This flag is set to '
             '"Y" when a facility has this exact combination of '
             'CIT_REF_CODE(s) associated with it. In the near term, no other '
             'combination of governing regulations will cause this flag to be '
             'set.'),
        'SUBPART_ID':
            ('Identification number assigned to the subpart of the '
             'environmental regulation with oversight of the facility.'),
    },
}
