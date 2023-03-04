table_column_lookup = \
{'FRS_AFFILIATION': {'AFFILIATION_TYPE': 'The name that describes the capacity or function that an organization or '
                                         'individual serves for a facility site. \n'
                                         'Allowable Values (examples):\n'
                                         'Organization                          Individual \n'
                                         'Legally Responsible Entity        Report Certifier \n'
                                         'Legal Operator                       Regulatory Contact \n'
                                         'Waste Treater                       Public Contact \n'
                                         'Waste Handler                       Technical Contact \n'
                                         'Land Owner                          Owner \n'
                                         'Parent Corporation                 Operator \n'
                                         'Owner/Operator',
                     'AFFILIATION_UIN': 'A system generated number that uniquely identifies an affiliation record.',
                     'CONTACT_UIN': 'A system generated number that uniquely identifies an individual person.',
                     'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                    'corresponding information was first posted to the database.',
                     'END_DATE': 'The date on which the affiliation between the facility site and the organization '
                                 'and/or individual person ended (YYYYMMDD).',
                     'LAST_REPORTED_DATE': 'The most recent date the corresponding affiliation data was reported to '
                                           'the Source of Data.',
                     'MAIL_UIN': 'A system generated number that uniquely identifies a mailing address.',
                     'ORG_UIN': 'A system generated number that uniquely identifies an organization.',
                     'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information management '
                                      'system for an environmental program.',
                     'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an information '
                                   'management system that represents a facility site, waste site, operable unit, or '
                                   'other feature tracked by that Environmental Information System.',
                     'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                                   'Internet.',
                     'REGISTRY_ID': 'The identification number assigned by the EPA Facility Registry System to '
                                    'uniquely identify a facility site.',
                     'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
                     'SOURCE_OF_DATA': 'The source of the associated affiliation data.',
                     'START_DATE': 'The date on which the affiliation between the facility site and the organization '
                                   'and/or individual person began (YYYYMMDD).',
                     'SUP_INTEREST_ID': 'A system generated number that uniquely identifies a supplemental interest '
                                        'record.',
                     'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time '
                                    'the corresponding information was updated in the database.',
                     'USER_ID': 'The user ID of the person who entered the data or the method by which the data was '
                                'entered into the system.'},
 'FRS_AGENCY_REF': {'FEDERAL_AGENCY_CODE': 'The Federal Agency/Bureau code. The five-character code consists of a '
                                           'letter followed by four numbers. There are four possible letters that can '
                                           "occupy the first character position: 'C' for Civilian Federal Agency; 'D' "
                                           "for Department of Defense; 'E' for Department of Energy; 'X' for Unknown. "
                                           'The second and third characters represent the agency code, while the '
                                           'fourth and fifth characters represent the bureau code.',
                    'FEDERAL_AGENCY_NAME': 'The Federal Agency/Bureau name.'},
 'FRS_ALTERNATIVE_ID': {'ALTERNATIVE_ID': 'An alternative identification number maintained by an information '
                                          'management system for an environmental program.',
                        'ALTERNATIVE_ID_TYPE': 'The type of alternative identification number (for example, STATE '
                                               'PERMIT NUMBER), or the abbreviated name of the environmental '
                                               'information system that references the alternative identification '
                                               'number (for example, TRIS, PCS).',
                        'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                       'corresponding information was first posted to the database.',
                        'FIPS_CODE': 'The code that represents the county or county equivalent and the state or state '
                                     'equivalent of the United States.',
                        'LAST_REPORTED_DATE': 'The most recent date the corresponding alternative identification data '
                                              'was reported to the Source of Data.',
                        'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information management '
                                         'system for an environmental program.',
                        'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an '
                                      'information management system that represents a facility site, waste site, '
                                      'operable unit, or other feature tracked by that Environmental Information '
                                      'System.',
                        'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                                      'Internet.',
                        'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
                        'SOURCE_OF_DATA': 'The source of the associated alternative identification data.',
                        'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and '
                                       'time the corresponding information was updated in the database.',
                        'USER_ID': 'The user ID of the person who entered the data or the method by which the data was '
                                   'entered into the system.'},
 'FRS_ALT_NAME': {'ALTERNATIVE_NAME': 'An alternative, historic or program specific name for the facility site.',
                  'ALTERNATIVE_NAME_TYPE': 'The type of the alternative, historical, or program-specific name for the '
                                           'facility site (e.g., primary, legal, historical, local).',
                  'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                 'corresponding information was first posted to the database.',
                  'LAST_REPORTED_DATE': 'The most recent date the corresponding alternative name data was reported to '
                                        'the Source of Data.',
                  'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information management system '
                                   'for an environmental program.',
                  'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an information '
                                'management system that represents a facility site, waste site, operable unit, or '
                                'other feature tracked by that Environmental Information System.',
                  'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                                'Internet.',
                  'REGISTRY_ID': 'The identification number assigned by the EPA Facility Registry System to uniquely '
                                 'identify a facility site.',
                  'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
                  'SOURCE_OF_DATA': 'The source of the associated alternative name data.',
                  'STD_ALT_NAME': 'The alternative name after a set of standardization rules are applied for '
                                  'comparison purposes.  The rules include removing special characters and certain '
                                  'words (e.g., "/", "Inc.") and replacing abbreviated words with standardized '
                                  'equivalents (e.g., "Assoc" becomes "Association").',
                  'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time the '
                                 'corresponding information was updated in the database.',
                  'USER_ID': 'The user ID of the person who entered the data or the method by which the data was '
                             'entered into the system.'},
 'FRS_CODE_DESCRIPTION': {'CODE_DESCRIPTION': 'The meaning of the data code.',
                          'CODE_TYPE': 'The type of data code (e.g., data quality, SIC, NAICS).',
                          'CODE_VALUE': 'The value of the data code.'},
 'FRS_CONTACT': {'ALTERNATE_PHONE': 'An alternate telephone number for an individual person.',
                 'CONTACT_UIN': 'A system generated number that uniquely identifies an individual person.',
                 'CREATE_DATE': 'A system-generated value that represents the calendar date and time the corresponding '
                                'information was first posted to the database.',
                 'DIVISION_NAME': 'The name of a division or a department of a company.',
                 'EMAIL_ADDRESS': 'The text that describes an electronic mail address of an individual person.',
                 'FAX_NUMBER': 'The telephone number to which a facsimile can be sent to an individual person.',
                 'FULL_NAME': 'The complete name of a person, potentially including first name, middle name or '
                              'initial, and surname.',
                 'LAST_REPORTED_DATE': 'The most recent date the corresponding individual data was reported to the '
                                       'Source of Data.',
                 'PHONE_NUMBER': 'The primary telephone number for an individual person.',
                 'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                               'Internet.',
                 'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
                 'SOURCE_OF_DATA': 'The source of the associated individual data.',
                 'STD_FULL_NAME': "The person's full name after a set of standardization rules are applied for "
                                  'comparison purposes.  The rules include removing blanks, special characters and '
                                  'certain words (e.g., ",", "Mr.", "Ms.").',
                 'TITLE': 'The title held by a person in an organization.',
                 'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time the '
                                'corresponding information was updated in the database.',
                 'USER_ID': 'The user ID of the person who entered the data or the method by which the data was '
                            'entered into the system.'},
 'FRS_FACILITY_SITE': {'ADDR_TYPE': 'The type of address given in the LOCATION_ADDRESS column (i.e., standard urban, '
                                    'PO Box).',
                       'CITY_NAME': 'The name of the city, town, village or other locality, when identifiable, within '
                                    'whose boundaries (the majority of) the facility site is located. This is not '
                                    'always the same as the city used for USPS mail delivery.',
                       'COUNTRY_NAME': 'The name that represents a primary geopolitical unit of the world. Default:  '
                                       'USA',
                       'COUNTY_NAME': 'The name of the U.S. county or county equivalent in which the facility site is '
                                      'physically located.',
                       'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                      'corresponding information was first posted to the database.',
                       'DATA_QUALITY_CODE': 'A code assigned by the automated integration process to indicate whether '
                                            'the address data are missing, invalid, or non standard.',
                       'ENV_JUSTICE_CODE': 'The code that identifies the type of environmental justice concern '
                                           'affecting the facility or enforcement action.',
                       'EPA_REGION_CODE': 'The code that represents an EPA Region.',
                       'FEDERAL_AGENCY_CODE': 'The Federal Agency/Bureau code. The five character code consists of a '
                                              'letter followed by four numbers.  There are four possible letters that '
                                              "can occupy the first character position:  'C' for Civilian Federal "
                                              "Agency; 'D' for Department of Defense; 'E' for Department of Energy; "
                                              "'X' for Unknown. The second and third characters represent the agency "
                                              'code, while the fourth and fifth characters represent the bureau code.',
                       'FEDERAL_FACILITY_CODE': 'Code indicating whether or not the facility is the property of the '
                                                'Federal Government. \n'
                                                'Allowable Values: \n'
                                                'Y, for Yes, the facility is the property of the Federal Government. \n'
                                                'N, for No, the facility is not the property of the Federal '
                                                'Government.',
                       'FIPS_CODE': 'The code that represents the county or county equivalent and the state or state '
                                    'equivalent of the United States.',
                       'ICIS_IDENTIFIER': 'This column is not currently being used.',
                       'INTEREST_STATUS_CODE': 'The status of the facility in relation to regulatory interest.  \n'
                                               'Allowable Values: \n'
                                               " 'A' for Active or 'I' for Inactive",
                       'LAST_REPORTED_DATE': 'The most recent date the corresponding facility site data was reported '
                                             'to the Source of Data.',
                       'LEGISLATIVE_DIST_NUM': 'The number that represents a Legislative District within a state.',
                       'LOCATION_ADDRESS': 'The address that describes the physical (geographic) location of the front '
                                           'door or main entrance of a facility site, including urban-style street '
                                           'address or rural address.',
                       'LOCATION_DESCRIPTION': 'A brief explanation of where the facility site is located, including '
                                               'navigational directions and/or more descriptive information about the '
                                               'location of the facility site.',
                       'PARENT_REGISTRY_ID': 'The unique identification number, assigned by the EPA Facility Registry '
                                             'System, to the parent facility site (for example, the SDWIS water '
                                             'system).',
                       'POSTAL_CODE': 'The combination of the five digit Zone Improvement Plan (ZIP) code and the four '
                                      'digit extension code (if available) that represents the geographic segment that '
                                      'is a subunit of the ZIP Code, assigned by the U.S. Postal Service to a '
                                      'geographic location; or the postal zone specific to the country, other than the '
                                      'U.S., where the facility site is located.',
                       'PRIMARY_NAME': 'The public or commercial name of a facility site (i.e., the full name that '
                                       'commonly appears on invoices, signs, or other business documents, or as '
                                       'assigned by the state when the name is ambiguous).',
                       'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                                     'Internet.',
                       'REGISTRY_ID': 'The identification number assigned by the EPA Facility Registry System to '
                                      'uniquely identify a facility site.',
                       'REVIEW_FLAG': 'A flag that indicates the record requires a manual review due to changes from a '
                                      'data source.',
                       'REVIEW_REASON': 'The reason the record is flagged for manual review.',
                       'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
                       'SITE_TYPE_NAME': 'The descriptive name for the type of site the facility occupies. \n'
                                         'Allowable Values: \n'
                                         'Stationary               Contamination Addressed  \n'
                                         'Monitoring Station    Contaminated Site \n'
                                         'Brownfields Site       Potentially Contaminated Site \n'
                                         'Water System          Pipeline\n'
                                         'Portable',
                       'SMALL_BUS_IND': 'Code indicating whether or not a business is requesting relief under EPA\'s '
                                        'Small Business Policy, which applies to businesses having less than 100 '
                                        'employees.',
                       'STATE_CODE': 'The U.S. Postal Service abbreviation that represents the state or state '
                                     'equivalent for the U.S. and Canada.',
                       'STATE_NAME': 'The name of a principal administrative subdivision of the United States, Canada, '
                                     'or Mexico.',
                       'STD_BASE_NAME': 'The name of the street or road, not including the prefix, suffix, or pre- or '
                                        'post- directional codes.',
                       'STD_CITY_NAME': 'The standardized City Name returned by the standardization and parsing '
                                        'routines.',
                       'STD_COUNTRY': 'The standardized Country Name returned by the standardization and parsing '
                                      'routines.',
                       'STD_COUNTY_FIPS': 'The standardized State County FIPS Code returned by the standardization and '
                                          'parsing routines.',
                       'STD_COUNTY_NAME': 'The standardized County Name returned by the standardization and parsing '
                                          'routines.',
                       'STD_FULL_ADDRESS': 'The standardized complete address, including STD_LOC_ADDRESS, '
                                           'STD_CITY_NAME, STD_STATE_CODE, AND STD_POSTAL_CODE.',
                       'STD_HOUSE_NUMBER': 'The number assigned to a building or a land parcel along the street to '
                                           'identify location and to ensure accurate mail delivery.',
                       'STD_LOC_ADDRESS': 'The location address after a set of standardization rules are applied for '
                                          'comparison purposes.',
                       'STD_NAME': 'The primary name after a set of standardization rules are applied for comparison '
                                   'purposes.  The rules include removing special characters and certain words (e.g., '
                                   '"/", "Inc.") and replacing abbreviated words with standardized equivalents (e.g., '
                                   '"Assoc" becomes "Association").',
                       'STD_POSTAL_CODE': 'The standardized Postal Code returned by the standardization and parsing '
                                          'routines.',
                       'STD_PREFIX': 'The code that represents the qualifier that precedes the street name in a street '
                                     'address.',
                       'STD_STATE_CODE': 'The standardized State Code returned by the standardization and parsing '
                                         'routines.',
                       'STD_STREET_NAME': 'The name assigned to a street or road, not including other urban-style '
                                          'street address components.',
                       'STD_STYPE_AFTER': 'The code that represents a street vector, i.e. the direction the street has '
                                          'taken from some arbitrary starting point that follows the street suffix.',
                       'STD_STYPE_BEFORE': 'The code that represents a street vector, i.e. the direction the street '
                                           'has taken from some arbitrary starting point that precedes the street '
                                           'name.',
                       'STD_SUFFIX': 'The code that represents the qualifier that follows the street name in a street '
                                     'address.',
                       'SUPPLEMENTAL_LOCATION': 'The text that provides additional information about a place, '
                                                'including a building name with its secondary unit and number, an '
                                                'industrial park name, an installation name or descriptive text where '
                                                'no formal address is available.',
                       'TRIBAL_LAND_CODE': 'Code indicating whether or not the facility site is located on tribal '
                                           'land.',
                       'TRIBAL_LAND_NAME': 'The name of the Tribal Reservation, statistical area, or Public Domain '
                                           'Allotment. If the tribal entity has no land base, the name of the tribal '
                                           'entity is used as the Tribal Land Name. Examples: Colorado River Indian '
                                           'Reservation, Ponca Tribal Designated Statistical Area, Wampanoag Tribe of '
                                           'Gay Head (Aquinnah) of Massachusetts.',
                       'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time '
                                      'the corresponding information was updated in the database.',
                       'USER_ID': 'The user ID of the person who entered the data or the method by which the data was '
                                  'entered into the system.'},
 'FRS_INTEREST': {'ACTIVE_STATUS': 'The status of the environmental interest at the facility or site (e.g., Active, '
                                   'Inactive, Operating, Proposed for NPL, Deleted from Final NPL, Currently on Final '
                                   'NPL).',
                  'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                 'corresponding information was first posted to the database.',
                  'END_DATE': 'Date the agency ceased to be interested in the facility site for a particular '
                              'environmental interest type (YYYYMMDD).',
                  'END_DATE_QUALIFIER': 'The qualifier that specifies the meaning of the date being used as an '
                                        'approximation for the environmental interest end date. \n'
                                        'Allowable Values (examples):\n'
                                        'Date Last Submission Received         Date of Last Report  \n'
                                        'Date Permit Ended                         Date Operations Ended',
                  'FED_STATE_CODE': 'A flag which indicates whether the environmental interest data was provided by a '
                                    'federal, state, tribal, or private environmental information system.  \n'
                                    "Allowable Values: 'F' for Federal, 'S' for State, 'T' for Tribal, and 'P' for "
                                    'Private',
                  'INTEREST_TYPE': 'The environmental permit or regulatory program that applies to the facility site '
                                   '(e.g., TRI Reporter, NPDES Major, Air Stationary Source Major, Hazardous Waste '
                                   'TSD, Hazardous Waste LQG, Superfund NPL)',
                  'LAST_REPORTED_DATE': 'The most recent date the corresponding environmental interest data was '
                                        'reported to the Source of Data.',
                  'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information management system '
                                   'for an environmental program.',
                  'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an information '
                                'management system that represents a facility site, waste site, operable unit, or '
                                'other feature tracked by that Environmental Information System.',
                  'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                                'Internet.',
                  'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
                  'SOURCE_OF_DATA': 'The source of the associated environmental interest data.',
                  'START_DATE': 'Date the agency became interested in the facility site for a particular environmental '
                                'interest type (YYYYMMDD).',
                  'START_DATE_QUALIFIER': 'The qualifier that specifies the meaning of the date being used as an '
                                          'approximation for the environmental interest start date. \n'
                                          'Allowable Values (examples) : \n'
                                          'First Reporting Year                    Date of First Report \n'
                                          'Date Operations Commenced       Date Permit Issued  \n'
                                          'Date of Permit Application            Date Monitoring Started',
                  'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time the '
                                 'corresponding information was updated in the database.',
                  'USER_ID': 'The user ID of the person who entered the data or the method by which the data was '
                             'entered into the system.'},
 'FRS_INTEREST_REF': {'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                     'corresponding information was first posted to the database.',
                      'INTEREST_DESC': 'A description of the environmental permit or regulatory program.',
                      'INTEREST_TYPE': 'The environmental permit or regulatory program that applies to the facility '
                                       'site (e.g., TRI Reporter, NPDES Major, Air Stationary Source Major, Hazardous '
                                       'Waste TSD, Hazardous Waste LQG, Superfund NPL)',
                      'PROGRAM_CATEGORY': 'A higher level classification consisting of program categories that group '
                                          'similar environmental interest types together.',
                      'PROGRAM_CATEGORY_DESC': 'A description of the program category.',
                      'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                                    'Internet.',
                      'QUERY_FLAG': 'A flag which indicates whether or not the associated environmental interest is '
                                    'available as a selection criteria within the Environmental Interest Query.',
                      'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time '
                                     'the corresponding information was updated in the database.'},
 'FRS_MAILING_ADDRESS': {'CITY_NAME': 'The name of the city, town, or village where the mail is delivered.',
                         'COUNTRY_NAME': 'The name of the country where the addressee is located.  Default: United '
                                         'States',
                         'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                        'corresponding information was first posted to the database.',
                         'LAST_REPORTED_DATE': 'The most recent date the corresponding mailing address data was '
                                               'reported to the Source of Data.',
                         'MAILING_ADDRESS': 'The exact address where a mail piece is intended to be delivered, '
                                            'including urban-style street address, rural route, and PO Box.',
                         'MAIL_UIN': 'A system generated number that uniquely identifies a mailing address.',
                         'POSTAL_CODE': 'The combination of the five-digit Zone Improvement Plan (ZIP) code and the '
                                        'four-digit extension code (if available) that represents the geographic '
                                        'segment that is a subunit of the ZIP Code, assigned by the U.S. Postal '
                                        'Service to a geographic location to facilitate mail delivery; or the postal '
                                        'zone specific to the country, other than the U.S., where the mail is '
                                        'delivered.',
                         'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on '
                                       'the Internet.',
                         'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
                         'SOURCE_OF_DATA': 'The source of the associated mailing address data.',
                         'STATE_CODE': 'The U.S. Postal Service abbreviation that represents the state or state '
                                       'equivalent for the U.S. and Canada.',
                         'STATE_NAME': 'The name of the state where mail is delivered.',
                         'STD_CITY_NAME': 'The city name after a set of standardization rules are applied for '
                                          'comparison purposes.  The rules include removing special characters and '
                                          'buzz words (e.g., "/", "City of") and replacing abbreviated words with '
                                          'standardized equivalents (e.g., "FT" becomes "FORT").',
                         'STD_MAIL_ADDRESS': 'The mailing address after a set of standardization rules are applied for '
                                             'comparison purposes.  The rules include removing special characters '
                                             '(e.g., "/"), replacing abbreviated words with standardized equivalents '
                                             '(e.g., "Ave" becomes "Avenue"), and replacing state names with state '
                                             'abbreviations.',
                         'STD_SUPPLEMENTAL_ADDRESS': 'The supplemental address after a set of standardization rules '
                                                     'are applied for comparison purposes.  The rules include removing '
                                                     'special characters (e.g., "/"), replacing abbreviated words with '
                                                     'standardized equivalents (e.g., "Ave" becomes "Avenue"), and '
                                                     'replacing state names with state abbreviations.',
                         'SUPPLEMENTAL_ADDRESS': 'The text that provides additional information to facilitate the '
                                                 'delivery of a mail piece, including building name, secondary units, '
                                                 'and mail stop or local box numbers not serviced by the U.S. Postal '
                                                 'Service.',
                         'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and '
                                        'time the corresponding information was updated in the database.',
                         'USER_ID': 'The user ID of the person who entered the data or the method by which the data '
                                    'was entered into the system.'},
 'FRS_NAICS': {'CREATE_DATE': 'A system-generated value that represents the calendar date and time the corresponding '
                              'information was first posted to the database.',
               'LAST_REPORTED_DATE': 'The most recent date the corresponding NAICS data was reported to the Source of '
                                     'Data.',
               'NAICS_CODE': 'The code that represents a subdivision of an industry that accommodates user needs in '
                             'the United States (six-digits).',
               'NAICS_UIN': 'A system-generated number that uniquely identifies a NAICS record.',
               'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information management system for '
                                'an environmental program.',
               'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an information '
                             'management system that represents a facility site, waste site, operable unit, or other '
                             'feature tracked by that Environmental Information System.',
               'PRIMARY_INDICATOR': 'The name that indicates whether the associated NAICS Code represents the primary '
                                    "activity occurring at the facility site. Allowable Values are 'Primary', "
                                    "'Secondary', or 'Unknown'.",
               'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                             'Internet.',
               'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
               'SOURCE_OF_DATA': 'The source of the associated NAICS data.',
               'SUP_INTEREST_ID': 'A system-generated number that uniquely identifies a supplemental interest record.',
               'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time the '
                              'corresponding information was updated in the database.',
               'USER_ID': 'The user ID of the person who entered the data or the method by which the data was entered '
                          'into the system.'},
 'FRS_ORGANIZATION': {'ALTERNATE_PHONE': 'An alternate telephone number for an organization.',
                      'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                     'corresponding information was first posted to the database.',
                      'DIVISION_NAME': 'The name of a division or a department of a company.',
                      'DUNS_NUMBER': 'The Data Universal Numbering System (DUNS) number assigned by Dun and Bradstreet '
                                     'to identify unique business establishments.',
                      'EIN': 'The unique tax identification number issued by the Internal Revenue Service to the '
                             'employer.',
                      'EMAIL_ADDRESS': 'The text that describes an electronic mail address of an organization.',
                      'FAX_NUMBER': 'The telephone number to which a facsimile can be sent to an organization.',
                      'LAST_REPORTED_DATE': 'The most recent date the corresponding organization data was reported to '
                                            'the Source of Data.',
                      'ORG_NAME': 'The legal, formal name of an organization that is affiliated with the facility '
                                  'site.',
                      'ORG_TYPE': 'The type of organization. \n'
                                  'Allowable Values (examples): \n'
                                  'Federal, Private GOCO, County, District, Tribal, Municipal, State, Other',
                      'ORG_UIN': 'A system generated number that uniquely identifies an organization.',
                      'PHONE_NUMBER': 'The primary telephone number for an organization.',
                      'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                                    'Internet.',
                      'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
                      'SOURCE_OF_DATA': 'The source of the associated organization data.',
                      'STATE_BUSINESS_ID': 'The uniform business number assigned to an official business by a state.',
                      'STD_ORG_NAME': 'The organization name after a set of standardization rules are applied for '
                                      'comparison purposes.  The rules include removing special characters and certain '
                                      'words (e.g., "/", "Inc.") and replacing abbreviated words with standardized '
                                      'equivalents (e.g., "Assoc" becomes "Association").',
                      'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time '
                                     'the corresponding information was updated in the database.',
                      'USER_ID': 'The user ID of the person who entered the data or the method by which the data was '
                                 'entered into the system.'},
 'FRS_PROGRAM_FACILITY': {'ADDR_TYPE': 'The type of address given in the LOCATION_ADDRESS column (i.e., standard '
                                       'urban, PO Box).',
                          'CITY_NAME': 'The name of the city, town, village or other locality, when identifiable, '
                                       'within whose boundaries (the majority of ) the facility site is located.  This '
                                       'is not always the same as the city used for USPS mail delivery.',
                          'COUNTRY_NAME': 'The name that represents a primary geopolitical unit of the world.',
                          'COUNTY_NAME': 'The name of the U.S. county or county equivalent in which the facility site '
                                         'is physically located.',
                          'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                         'corresponding information was first posted to the database.',
                          'DATA_QUALITY_CODE': 'Code assigned by the automated resolution process to indicate whether '
                                               'the address data are missing, invalid, or non-standard.',
                          'ENV_JUSTICE_CODE': 'The code that identifies the type of environmental justice concern '
                                              'affecting the facility or enforcement action.',
                          'EPA_REGION_CODE': 'The code that represents an EPA region.',
                          'FEDERAL_AGENCY_CODE': 'The Federal Agency/Bureau code.  The five character code consists of '
                                                 'a letter followed by four numbers.  There are four possible letters '
                                                 "that can occupy the first character position:  'C'  for Civilian "
                                                 "Federal Agency; 'D' for Department of Defense; 'E' for Department of "
                                                 "Energy; 'X' for Unknown.  The second and third characters represent "
                                                 'the agency code, while the fourth and fifth characters represent the '
                                                 'bureau code.',
                          'FEDERAL_FACILITY_CODE': 'Code indicating whether or not the facility is the property of the '
                                                   'Federal Government. \n'
                                                   'Allowable Values: \n'
                                                   'Y, for Yes, the facility is the property of the Federal '
                                                   'Government. \n'
                                                   'N, for No, the facility is not the property of the Federal '
                                                   'Government.',
                          'FIPS_CODE': 'The code that represents the county or county equivalent and the state or '
                                       'state equivalent of the United States.',
                          'HUC_CODE_12': 'The 12-digit hydrologic unit code (HUC) that represents a geographic area '
                                         'representing part or all of a surface drainage basin, a combination of '
                                         'drainage basins, or a distinct hydrologic feature.',
                          'HUC_CODE_8': 'The 8-digit hydrologic unit code (HUC) that represents a geographic area '
                                        'representing part or all of a surface drainage basin, a combination of '
                                        'drainage basins, or a distinct hydrologic feature.',
                          'LAST_REPORTED_DATE': 'The most recent date the corresponding facility site data was '
                                                'reported to the Source of Data.',
                          'LEGISLATIVE_DIST_NUM': 'The number of the state legislative district  in which the facility '
                                                  'site is located.',
                          'LINK_MTHD': 'The method used to determine the association or "linkage" of this '
                                       'environmental interest to a particular facility site  (e.g., automated match, '
                                       'data steward).',
                          'LOCATION_ADDRESS': 'The address that describes the physical (geographic) location of the '
                                              'front door or main entrance of a facility site, including urban-style '
                                              'street address or rural address.',
                          'LOCATION_DESCRIPTION': 'A brief explanation of where the facility site is located, '
                                                  'including navigational directions and/or more descriptive '
                                                  'information about the location of the facility site.',
                          'PARENT_PGM_SYS_ID': 'The unique identification number assigned by an information management '
                                               'system to the parent facility or site (e.g., the SDWIS water system).',
                          'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information management '
                                           'system for an environmental program.',
                          'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an '
                                        'information management system that represents a facility site, waste site, '
                                        'operable unit, or other feature tracked by that Environmental Information '
                                        'System.',
                          'POSTAL_CODE': 'The combination of the 5-digit Zone Improvement Plan (ZIP) code and the '
                                         'four-digit extension code (if available) that represents the geographic '
                                         'segment that is a subunit of the ZIP Code, assigned by the U.S. Postal '
                                         'Service to a geographic location; or the postal zone specific to the '
                                         'country, other than the U.S., where the facility site is located.',
                          'PRIMARY_NAME': 'The public or commercial name of a facility site (i.e., the full name that '
                                          'commonly appears on invoices, signs, or other business documents, or as '
                                          'assigned by the state when the name is ambiguous).',
                          'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on '
                                        'the internet.',
                          'REFRESH_DATE': 'The date the data was last extracted from the data source.',
                          'REGISTRY_ID': 'The identification number assigned by the EPA Facility Registry System to '
                                         'uniquely identify a facility site.',
                          'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
                          'SITE_TYPE_NAME': 'The descriptive name for the type of site the facility occupies. \n'
                                            'Allowable Values: \n'
                                            'Stationary               Contamination Addressed  \n'
                                            'Monitoring Station    Contaminated Site \n'
                                            'Brownfields Site        Potentially Contaminated Site \n'
                                            'Water System          Pipeline\n'
                                            'Portable',
                          'SMALL_BUS_IND': 'Code indicating whether or not a business is requesting relief under EPA\'s '
                                           'Small Business Policy, which applies to businesses having less than 100 '
                                           'employees.',
                          'STATE_CODE': 'The U.S. Postal Service abbreviation that represents the state or state '
                                        'equivalent for the U.S. and Canada.',
                          'STATE_NAME': 'The name of a principal administrative subdivision of the United States, '
                                        'Canada, or Mexico.',
                          'STD_BASE_NAME': 'The name of the street or road, not including the prefix, suffix, or pre- '
                                           'or post- directional codes.',
                          'STD_CITY_NAME': 'The standardized City Name returned by the standardization and parsing '
                                           'routines.',
                          'STD_COUNTRY': 'The standardized Country Name returned by the standardization and parsing '
                                         'routines.',
                          'STD_COUNTY_FIPS': 'The standardized State County FIPS Code returned by the standardization '
                                             'and parsing routines.',
                          'STD_COUNTY_NAME': 'The standardized County Name returned by the standardization and parsing '
                                             'routines.',
                          'STD_FULL_ADDRESS': 'The standardized complete address, including STD_LOC_ADDRESS, '
                                              'STD_CITY_NAME, STD_STATE_CODE, AND STD_POSTAL_CODE.',
                          'STD_HOUSE_NUMBER': 'The number assigned to a building or a land parcel along the street to '
                                              'identify location and to ensure accurate mail delivery.',
                          'STD_LOC_ADDRESS': 'The location address after a set of standardization rules are applied '
                                             'for comparison purposes.',
                          'STD_NAME': 'The primary name after a set of standardization rules are applied for '
                                      'comparison purposes.  The rules include removing special characters and certain '
                                      'words (e.g., "/", "Inc.") and replacing abbreviated words with standardized '
                                      'equivalents (e.g., "Assoc" becomes "Association").',
                          'STD_POSTAL_CODE': 'The standardized Postal Code returned by the standardization and parsing '
                                             'routines.',
                          'STD_PREFIX': 'The code that represents the qualifier that precedes the street name in a '
                                        'street address.',
                          'STD_STATE_CODE': 'The standardized State Code returned by the standardization and parsing '
                                            'routines.',
                          'STD_STREET_NAME': 'The name assigned to a street or road, not including other urban-style '
                                             'street address components.',
                          'STD_STYPE_AFTER': 'The code that represents a street vector, i.e. the direction the street '
                                             'has taken from some arbitrary starting point that follows the street '
                                             'suffix.',
                          'STD_STYPE_BEFORE': 'The code that represents a street vector, i.e. the direction the street '
                                              'has taken from some arbitrary starting point that precedes the street '
                                              'name.',
                          'STD_SUFFIX': 'The code that represents the qualifier that follows the street name in a '
                                        'street address.',
                          'SUPPLEMENTAL_LOCATION': 'The text that provides additional information about a place, '
                                                   'including a building name with its secondary unit and number, an '
                                                   'industrial park name, an installation name,  or descriptive text '
                                                   'where no formal address is available.',
                          'TRIBAL_LAND_CODE': 'Code indicating whether or not the facility is the property of the '
                                              'Federal Government. \n'
                                              'Allowable Values: \n'
                                              'Y, for Yes, the facility is the property of the Federal Government. \n'
                                              'N, for No, the facility is not the property of the Federal Government.',
                          'TRIBAL_LAND_NAME': 'The name of the Tribal Reservation, statistical area, or Public Domain '
                                              'Allotment.  If the tribal entity has no land base, the name of the '
                                              'tribal entity is used as the Tribal Land Name.  Examples: Colorado '
                                              'River Indian Reservation, Ponca Tribal Designated Statistical Area, '
                                              'Wampanoag Tribe of Gay Head (Aquinnah) of Massachusetts.',
                          'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and '
                                         'time the corresponding information was updated in the database.',
                          'USER_COMMENT': 'Free form textual comments entered by the user/analyst to further describe '
                                          'the corresponding data.',
                          'USER_ID': 'The user ID of the person who entered the data or the method by which the data '
                                     'was entered into the system.'},
 'FRS_SIC': {'CREATE_DATE': 'A system-generated value that represents the calendar date and time the corresponding '
                            'information was first posted to the database.',
             'LAST_REPORTED_DATE': 'The most recent date the corresponding SIC data was reported to the Source of '
                                   'Data.',
             'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information management system for '
                              'an environmental program.',
             'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an information '
                           'management system that represents a facility site, waste site, operable unit, or other '
                           'feature tracked by that Environmental Information System.',
             'PRIMARY_INDICATOR': 'The name that indicates whether the associated SIC Code represents the primary '
                                  "activity occurring at the facility site. Allowable Values are 'Primary', "
                                  "'Secondary', or 'Unknown'.",
             'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the Internet.',
             'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement sensitive.',
             'SIC_CODE': 'The code that represents the economic activity of a company (four-digits).',
             'SIC_UIN': 'A system-generated number that uniquely identifies a SIC record.',
             'SOURCE_OF_DATA': 'The source of the associated SIC data.',
             'SUP_INTEREST_ID': 'A system-generated number that uniquely identifies a supplemental interest record.',
             'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time the '
                            'corresponding information was updated in the database.',
             'USER_ID': 'The user ID of the person who entered the data or the method by which the data was entered '
                        'into the system.'},
 'FRS_SUPPLEMENTAL_INTEREST': {'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                              'corresponding information was first posted to the database.',
                               'END_DATE': 'Date the agency ceased to be interested in the facility site for a '
                                           'particular environmental interest type (YYYYMMDD).',
                               'END_DATE_QUALIFIER': 'The qualifier that specifies the meaning of the date being used '
                                                     'as an approximation for the environmental interest end date. \n'
                                                     'Allowable Values (examples): \n'
                                                     'Date Last Submission Received       Date of Last Report  \n'
                                                     'Date Permit Ended                       Date Operations Ended',
                               'LAST_REPORTED_DATE': 'The most recent date the corresponding environmental interest '
                                                     'data was reported to the Source of Data.',
                               'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information '
                                                'management system for an environmental program.',
                               'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an '
                                             'information management system that represent a facility site, waste '
                                             'site, operable unit, or other feature tracked by that Environmental '
                                             'Information System.',
                               'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public '
                                             'on the Internet.',
                               'REPORTED_SUP_INTEREST_TYPE': 'The name of the environmental permit or regulatory '
                                                             'program, as reported by the supplemental information '
                                                             'system.',
                               'SENSITIVE_IND': 'Indicates whether or not the associated data is enforcement '
                                                'sensitive.',
                               'SOURCE_OF_DATA': 'The source of the associated supplemental environmental interest '
                                                 'data.',
                               'START_DATE': 'Date the agency became interested in the facility site for a particular '
                                             'environmental interest type (YYYYMMDD).',
                               'START_DATE_QUALIFIER': 'The qualifier that specifies the meaning of the date being '
                                                       'used as an approximation for the environmental interest start '
                                                       'date. \n'
                                                       'Allowable Values (examples): \n'
                                                       'First Reporting Year                    Date of First Report \n'
                                                       'Date Operations Commenced       Date Permit Issued  \n'
                                                       'Date of Permit Application            Date Monitoring Started',
                               'SUP_INTEREST_ID': 'A system generated number that uniquely identifies a supplemental '
                                                  'interest record.',
                               'SUP_INTEREST_TYPE': 'The supplemental environmental permit or regulatory program that '
                                                    'applies to the facility site or the environmental interest at the '
                                                    'facility site. For the purposes of FRS, supplemental program '
                                                    'interests include state programs, compliance and enforcement '
                                                    'programs, and general permits.',
                               'SUP_PGM_SYS_ACRNM': 'The abbreviated name that represents the name of a supplemental '
                                                    'information management system. For the purposes of FRS, '
                                                    'supplemental systems include state program systems, compliance '
                                                    'and enforcement systems, and program systems that include general '
                                                    'permits.',
                               'SUP_PGM_SYS_ID': 'The unique identification number assigned to a judicial or formal '
                                                 'administrative enforcement action, a compliance monitoring activity, '
                                                 'a general permit, or a state environmental program.',
                               'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date '
                                              'and time the corresponding information was updated in the database.',
                               'USER_ID': 'The user ID of the person who entered the data or the method by which the '
                                          'data was entered into the system.'},
 'FRS_SYSTEM_REF': {'CREATE_DATE': 'A system-generated value that represents the calendar date and time the '
                                   'corresponding information was first posted to the database.',
                    'FED_STATE_CODE': 'A flag which indicates whether the information management system is federal or '
                                      'state.',
                    'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information management '
                                     'system for an environmental program (e.g., RCRAINFO, ICIS, TRI, CERCLIS, ACRES, '
                                     'RMP, EIS)',
                    'PGM_SYS_DESC': 'A description of an information management system for an environmental program.',
                    'PGM_SYS_NAME': 'The full name of an information management system for an environmental program.',
                    'PUBLIC_IND': 'Indicates whether or not the associated data is accessible by the public on the '
                                  'Internet.',
                    'UPDATE_DATE': 'A system-generated value that represents the most recent calendar date and time '
                                   'the corresponding information was updated in the database.'},
 'FRS_TRIBAL_ENTITY_REF': {'FEDERAL_REGISTER': 'A flag indicating whether the TRIBAL ENTITY is federally recognized '
                                               'and therefore contained in the Federal Register.',
                           'ORGANIZATION_CODE': 'The unique identifier of the Tribal Entity, obtained from Department '
                                                'of Interior, Bureau of Indian Affairs, Division of Accounting '
                                                'Management, FY2000 Federal Financial System (FFS) Organization '
                                                'Codes.  This is a six-character code where the first character '
                                                '(alpha) represents the BIA Region, the next two numbers represent the '
                                                'BIA Agency or Field Office, and the final three numbers represent the '
                                                'reservation, trust land, or other feature.  There is usually a '
                                                'one-to-one relationship between the ORG-CODE and the R-CODE.  '
                                                'Acceptable values for the first alpha character include:  A   Great '
                                                'Plains  \n'
                                                'G   Eastern Oklahoma  \n'
                                                'M   Southwest \n'
                                                'B    Southern Plains  \n'
                                                'H   Western \n'
                                                'N   Navajo \n'
                                                'C   Rocky Mountain  \n'
                                                'J   Pacific  \n'
                                                'P   Northwest E Alaska  \n'
                                                'K   Central Office  \n'
                                                'S  Eastern \n'
                                                'F   Midwest  \n'
                                                'Example: Colorado River Indian Tribes FFS code is H51603.',
                           'TRIBAL_ENTITY_NAME': 'The name of the American Indian or Alaska Native entity associated '
                                                 'with the feature referenced in TRIBAL_LAND_NAME.  If the entity is '
                                                 'federally recognized, the name is obtained from the current list of '
                                                 '"Indian Entities Recognized and Eligible to Receive Services from '
                                                 'the United States Bureau of Indian Affairs" published in the Federal '
                                                 'Register (Vol. 77, No.155) August 10, 2012. See '
                                                 'http://www.access.gpo.gov/su_docs to obtain this document. If the '
                                                 'entity is not federally recognized, the name is obtained from other '
                                                 'sources. There is usually a one-to-one relationship between '
                                                 'TRIBAL_ENTITY_NAME and TRIBAL_LAND_NAME.  There are, however, a few '
                                                 'occurrences of two or more entities associated with one reservation '
                                                 'or other unit of land.  For example, both the Shoshone Tribe and the '
                                                 'Arapahoe Tribe reside on the Wind River Reservation.  There are a '
                                                 'number of occurrences of the reverse situation, where one entity is '
                                                 'associated with many features referenced in TRIBAL_LAND_NAME '
                                                 '(Example:  Seneca Nation of New York resides on three different '
                                                 'reservations:  Allegheny, Cattaraugas, and Oil Springs).  For '
                                                 'California Public Domain Allotments, TRIBAL_ENTITY_NAME is blank.',
                           'TRIBAL_LAND_R_CODE': 'A unique identifier for every unit of land within Indian Country.  '
                                                 'The value is a three-digit number preceded by an alpha character '
                                                 'denoting the category of the land.  \n'
                                                 'Alpha characters are coded as follows:  Q - California Public Domain '
                                                 'Allotments; W - State TDSA; R - Recognized by LRIS; X - Federal '
                                                 'TDSA; T - Not recognized by LRIS; Y - TJSA; V - State reservation; Z '
                                                 '- Alaska Native Village Statistical Areas. \n'
                                                 'The three-digit number is obtained as follows: For categories R, T, '
                                                 'and Z, the three-digit number is obtained by parsing the last three '
                                                 'digits of the Federal Financial System (FFS) organization code and '
                                                 'concatenating them with the appropriate letter.  For categories V, '
                                                 "W, X, and Y, FFS codes don't exist, so a unique sequential number "
                                                 'within each category was assigned. The number was assigned based on '
                                                 'an alphabetical list of the names. For category Q, the unique value '
                                                 'was determined by obtaining a frequency of both the NAME and '
                                                 'CNPSCODE items from the coverage supplied by the BIA Pacific Region '
                                                 'Office. The combinations were assigned a case item numeric value '
                                                 'that was then concatenated with the letter Q. The values in both the '
                                                 'NAME and CNPSCODE items were moved to the COMMENTS item in IND3. The '
                                                 'values in CNPSCODE were moved to the IND-NAME item in IND3.  '
                                                 'Examples:  Colorado River Indian Tribes FFS code of H51603 yields an '
                                                 'R-CODE of R603.  Ponca TDSA (no FFS code), R-CODE of X005.  From '
                                                 'coverage PDA3-83, NAME of SAC159 and CNPSCODE of 720B yielded an '
                                                 'R-CODE of Q097.  In cases where one entity is located on several '
                                                 'features, a second alpha character is added in place of the first '
                                                 'numeric. Example:  Seneca Nation of New York, FFS S51004, resides on '
                                                 'three different reservations:  Allegheny, Cattaraugas, and Oil '
                                                 'Springs.  In order to distinguish the tribe on each reservation, '
                                                 'R-CODE values are assigned as follows: Allegheny  TX04 Cattaraugas  '
                                                 'TY04 Oil Springs  TZ04'},
 'FRS_TRIBAL_LAND_REF': {'TRIBAL_LAND_NAME': 'The name of the Tribal Reservation, statistical area, or Public Domain '
                                             'Allotment.  If the tribal entity has no land base, the name of the '
                                             'tribal entity is used as the Tribal Land Name.  Examples: Colorado River '
                                             'Indian Reservation, Ponca Tribal Designated Statistical Area, Wampanoag '
                                             'Tribe of Gay Head (Aquinnah) of Massachusetts.',
                         'TRIBAL_LAND_R_CODE': 'A unique identifier for every unit of land within Indian Country.  The '
                                               'value is a three-digit number preceded by an alpha character denoting '
                                               'the category of the land.  \n'
                                               'Alpha characters are coded as follows:  Q - California Public Domain '
                                               'Allotments; W - State TDSA; R - Recognized by LRIS; X - Federal TDSA; '
                                               'T - Not recognized by LRIS; Y - TJSA; V - State reservation; Z - '
                                               'Alaska Native Village Statistical Areas. \n'
                                               'The three-digit number is obtained as follows: For categories R, T, '
                                               'and Z, the three-digit number is obtained by parsing the last three '
                                               'digits of the Federal Financial System (FFS) organization code and '
                                               'concatenating them with the appropriate letter.  For categories V, W, '
                                               "X, and Y, FFS codes don't exist, so a unique sequential number within "
                                               'each category was assigned. The number was assigned based on an '
                                               'alphabetical list of the names. For category Q, the unique value was '
                                               'determined by obtaining a frequency of both the NAME and CNPSCODE '
                                               'items from the coverage supplied by the BIA Pacific Region Office. The '
                                               'combinations were assigned a case item numeric value that was then '
                                               'concatenated with the letter Q. The values in both the NAME and '
                                               'CNPSCODE items were moved to the COMMENTS item in IND3. The values in '
                                               'CNPSCODE were moved to the IND-NAME item in IND3.  Examples:  Colorado '
                                               'River Indian Tribes FFS code of H51603 yields an R-CODE of R603.  '
                                               'Ponca TDSA (no FFS code), R-CODE of X005.  From coverage PDA3-83, NAME '
                                               'of SAC159 and CNPSCODE of 720B yielded an R-CODE of Q097.  In cases '
                                               'where one entity is located on several features, a second alpha '
                                               'character is added in place of the first numeric. Example:  Seneca '
                                               'Nation of New York, FFS S51004, resides on three different '
                                               'reservations:  Allegheny, Cattaraugas, and Oil Springs.  In order to '
                                               'distinguish the tribe on each reservation, R-CODE values are assigned '
                                               'as follows: Allegheny  TX04 Cattaraugas  TY04 Oil Springs  TZ04',
                         'USBC_TRIBAL_LAND_CODE': 'The code that represents an American Indian or Alaskan Native area '
                                                  'recognized by the United States Bureau of Census (USBC).'},
 'GEO_ASSIGN_ACC_LK': {'ASSIGN_ACC_VAL': 'Accuracy value assigned to the latitude/longitude coordinate based on the '
                                         'combination of collection method and scale.',
                       'COLLECT_MTH_CODE': 'The code that represents the method used to determine the latitude and '
                                           'longitude coordinates for a point on the earth.',
                       'SCALE_LOWERBOUND': 'The number that represents the proportional distance on the ground for one '
                                           'unit of measure on the map or photo, used as the lower value of a range.',
                       'SCALE_UPPERBOUND': 'The number that represents the proportional distance on the ground for one '
                                           'unit of measure on the map or photo, used as the upper value of a range.'},
 'GEO_COLLECT_MTH_LK': {'COLLECT_DESC': 'The text that describes the method used to determine the latitude and '
                                        'longitude coordinates for a point on the earth.',
                        'COLLECT_MTH_CODE': 'The code that represents the method used to determine the latitude and '
                                            'longitude coordinates for a point on the earth.'},
 'GEO_CONVEYOR': {'CONVEYOR': 'Identification of the party that transmitted the latitude and longitude coordinates.',
                  'PRIORITY': 'The ranking of the data provider that is used in the determination of the "best" '
                              "locational information for a facility. The highest rank (priority) is '1'. THIS RANKING "
                              'IS NO LONGER USED.'},
 'GEO_FACILITY_POINT': {'LATITUDE83': 'The measure of the angular distance on a meridian north or south of the equator '
                                      'standardized to NAD83 horizontal datum.',
                        'LONGITUDE83': 'The measure of the angular distance on a meridian east or west of the prime '
                                       'meridian standardized to NAD83 horizontal datum.',
                        'OBJECTID': 'A unique numeric identifier for each geometry in a layer.',
                        'REGISTRY_ID': 'The identification number assigned by the EPA Facility Registry System to '
                                       'uniquely identify a facility site.',
                        'SHAPE': 'Coordinates that define the geometry of the point feature.',
                        'TIMESTAMP': 'A system-generated value that represents the calendar date and time the '
                                     'corresponding information was posted to the database.'},
 'GEO_GEOMETRIC_TYPE_LK': {'GEOMETRIC_TYPE_CODE': 'The code that represents the geometric entity represented by one '
                                                  'point or a sequence of latitude and longitude points. \n'
                                                  'Allowable Values: \n'
                                                  'Value     Meaning\n'
                                                  '001        POINT\n'
                                                  '002        LINE\n'
                                                  '003        AREA\n'
                                                  '004        REGION\n'
                                                  '005        ROUTE',
                           'GEOMETRIC_TYPE_DESC': 'The name that describes the geometric entity represented by one '
                                                  'point or a sequence of latitude and longitude points. \n'
                                                  'Allowable Values: \n'
                                                  'Value     Meaning\n'
                                                  '001        POINT\n'
                                                  '002        LINE\n'
                                                  '003        AREA\n'
                                                  '004        REGION\n'
                                                  '005        ROUTE'},
 'GEO_HORIZ_DATUM_LK': {'HDATUM_CODE': 'The code that represents the reference datum used in determining latitude and '
                                       'longitude coordinates.\n'
                                       'Allowable Values:\n'
                                       'Value     Meaning\n'
                                       '001        NAD27\n'
                                       '002        NAD83\n'
                                       '003        WGS84',
                        'HDATUM_DESC': 'The name that describes the reference datum used in determining latitude and '
                                       'longitude coordinates. \n'
                                       'Allowable Values:\n'
                                       'Value     Meaning\n'
                                       '001        NAD27\n'
                                       '002        NAD83\n'
                                       '003        WGS84'},
 'GEO_PGM_FACILITY_COORDINATE': {'ACCURACY_SCORE': 'The accuracy score (in meters) derived as the accuracy value '
                                                   'either supplied by the location metadata or calculated based on '
                                                   'the collection method and then modified based on QA boundary '
                                                   'checks.',
                                 'ACCURACY_VALUE': 'The measure of the accuracy (in meters) of the latitude and '
                                                   'longitude coordinates.',
                                 'COLLECTION_DATE': 'The calendar data when data were collected.',
                                 'COLLECT_MTD_CODE': 'The code that represents the method used to determine the '
                                                     'latitude and longitude coordinates for a point on the earth.',
                                 'COMMENT_TEXT': 'The text that provides additional information about the geographic '
                                                 'coordinates.',
                                 'COMPLIANT_FLAG': 'Identifies whether a latitude/longitude coordinate set is method, '
                                                   'accuracy, and description (MAD) code compliant.',
                                 'CONVEYOR': 'Identification of the party that transmitted the associated latitude and '
                                             'longitude coordinates.',
                                 'GEOMETRIC_TYPE_CODE': 'The code that represents the geometric entity represented by '
                                                        'one point or a sequence of latitude and longitude points. \n'
                                                        'Allowable Values: \n'
                                                        'Value     Meaning\n'
                                                        '001        POINT\n'
                                                        '002        LINE\n'
                                                        '003        AREA\n'
                                                        '004        REGION\n'
                                                        '005        ROUTE',
                                 'HDATUM_CODE': 'The code that represents the reference datum used in determining '
                                                'latitude and longitude coordinates.\n'
                                                'Allowable Values:\n'
                                                'Value     Meaning\n'
                                                '001        NAD27\n'
                                                '002        NAD83\n'
                                                '003        WGS84',
                                 'LATITUDE': 'The measure of the angular distance on a meridian north or south of the '
                                             'equator, as reported by the data source.',
                                 'LATITUDE83': 'The measure of the angular distance on a meridian north or south of '
                                               'the equator standardized to NAD83 horizontal datum.',
                                 'LONGITUDE': 'The measure of the angular distance on a meridian east or west of the '
                                              'prime meridian, as reported by the data source.',
                                 'LONGITUDE83': 'The measure of the angular distance on a meridian east or west of the '
                                                'prime meridian standardized to NAD83 horizontal datum.',
                                 'OBJECTID': 'A unique numeric identifier for each geometry in a layer.',
                                 'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information '
                                                  'management system for an environmental program.',
                                 'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an '
                                               'information management system that represents a facility site, waste '
                                               'site, operable unit, or other feature tracked by that Environmental '
                                               'Information System.',
                                 'REF_POINT_CODE': 'The code that represents the place for which geographic '
                                                   'coordinates were established.',
                                 'SCALE': 'The number that represents the proportional distance on the ground for one '
                                          'unit of measure on the map or photo. Remarks: Mandatory for all horizontal '
                                          'data collection methods except for methods using Global Positioning System '
                                          '(GPS).',
                                 'SHAPE': 'Coordinates that define the geometry of the point feature.',
                                 'SOURCE': 'The source of the associated geographic coordinate data.',
                                 'SOURCE_CODE': 'The code that represents the party responsible for providing the '
                                                'latitude and longitude coordinates.',
                                 'SUB_ENTITY_DESC': 'The text that describes the sub-type code, which represents the '
                                                    'type of operable unit or sub-unit of a facility site.',
                                 'SUB_ID': 'The identification number for an operable unit or sub-unit of a facility '
                                           'site.',
                                 'SUB_TYPE_CODE': 'The code that represents the type of operable unit, or sub-unit of '
                                                  'a facility site (i.e., stack, sampling point, well head, point of '
                                                  'record).',
                                 'TIMESTAMP': 'A system-generated value that represents the calendar date and time the '
                                              'corresponding information was posted to the database.',
                                 'USER_ID': 'The user ID of the person who entered the data or the method by which the '
                                            "data was entered into the system (e.g., 'REFRESH').",
                                 'VACCURACY': 'The measure of the accuracy (in meters) of the vertical measure (i.e., '
                                              'the altitude) of a reference point.',
                                 'VDATUM_CODE': 'The code that represents the reference datum used to determine the '
                                                'vertical measure (i.e., the altitude). \n'
                                                'Allowable Values: \n'
                                                'Value     Meaning\n'
                                                '001        NAVD88 \n'
                                                '002        NGVD29\n'
                                                '003        MEAN SEA-LEVEL\n'
                                                '004        LOCAL TIDAL DATUM',
                                 'VERTICAL_MEASURE': 'The measure of elevation (i.e., the altitude), in meters, above '
                                                     'or below a reference datum.',
                                 'VMETHOD_CODE': 'The code that represents the method used to collect the vertical '
                                                 'measure (i.e., the altitude) of a reference point.'},
 'GEO_REF_POINT_LK': {'REF_POINT_CODE': 'The code that represents the place for which geographic coordinates were '
                                        'established.',
                      'REF_POINT_DESC': 'The name that identifies the place for which geographic coordinates were '
                                        'established.'},
 'GEO_SOURCE_LK': {'SOURCE_CODE': 'The code that represents the party responsible for providing the latitude and '
                                  'longitude coordinates.',
                   'SOURCE_DESC': 'The name of the party responsible for providing the latitude and longitude '
                                  'coordinates.'},
 'GEO_SUB_ID_REF': {'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information management '
                                     'system for an environmental program.',
                    'SUB_ID_SEQUENCE': 'A sequence number, by program system, for each sub-id entry.',
                    'TAB_COL_NAME': 'The table and column name from the source system that has the sub-unit '
                                    'identifier.'},
 'GEO_SUB_TYPE_LK': {'SUB_TYPE_CODE': 'The code that represents the type of operable unit, or sub-unit of a facility '
                                      'site (i.e., stack, sampling point, well head, point of record).',
                     'SUB_TYPE_DESC': 'The text that represents the type of operable unit, or sub-unit of a facility '
                                      'site (i.e., stack, sampling point, well head, point of record).'},
 'GEO_VERIFY_LK': {'VERIFY_CODE': 'The code that represents the process used to verify the latitude and longitude '
                                  'coordinates.',
                   'VERIFY_DESC': 'The text that describes the process used to verify the latitude and longitude '
                                  'coordinates.',
                   'VERIFY_WEIGHT': 'Weight assigned to the verification method.'},
 'GEO_VERT_DATUM_LK': {'VDATUM_CODE': 'The code that represents the reference datum used to determine the vertical '
                                      'measure (i.e., the altitude).\n'
                                      'Allowable Values: \n'
                                      'Value      Meaning\n'
                                      '001        NAVD88 \n'
                                      '002        NGVD29\n'
                                      '003        MEAN SEA-LEVEL\n'
                                      '004        LOCAL TIDAL DATUM',
                       'VDATUM_DESC': 'The name that represents the reference datum used to determine the vertical '
                                      'measure (i.e., the altitude). \n'
                                      'Allowable Values: \n'
                                      'Value      Meaning\n'
                                      '001        NAVD88 \n'
                                      '002        NGVD29\n'
                                      '003        MEAN SEA-LEVEL\n'
                                      '004        LOCAL TIDAL DATUM'},
 'GEO_VERT_METHOD_LK': {'VMETHOD_CODE': 'The code that represents the method used to collect the vertical measure '
                                        '(i.e., the altitude) of a reference point.',
                        'VMETHOD_DESC': 'The text that describes the method used to collect the vertical measure '
                                        '(i.e., the altitude) of a reference point.'},
 'MV_GEO_FACILITY_POINT': {'ACCURACY_SCORE': 'The accuracy score (in meters) derived as the accuracy value either '
                                             'supplied by the location metadata or calculated based on the collection '
                                             'method and then modified based on QA boundary checks.',
                           'ACCURACY_VALUE': 'The measure of the accuracy (in meters) of the latitude and longitude '
                                             'coordinates.',
                           'CITY_NAME': 'The name of the city, town, village or other locality, when identifiable, '
                                        'within whose boundaries (the majority of) the facility site is located. This '
                                        'is not always the same as the city used for USPS mail delivery.',
                           'COLLECT_MTH_DESC': 'The text that describes the method used to determine the latitude and '
                                               'longitude coordinates for a point on the earth.',
                           'CONVEYOR': 'Identification of the party that transmitted the latitude and longitude '
                                       'coordinates.',
                           'COUNTRY_NAME': 'The name that represents a primary geopolitical unit of the world.',
                           'COUNTY_NAME': 'The name of the U.S. county or county equivalent in which the facility site '
                                          'is physically located.',
                           'DERIVED_CB_2010': 'The spatially derived 2010 Census Block Code, which represents the '
                                              'smallest entity for which the Census Bureau collects and tabulates '
                                              'decennial census information; bounded on all sides by visible and '
                                              'nonvisible features shown on Census Bureau maps.',
                           'DERIVED_CD_112': 'The number that represents the 112th Congressional District for a state '
                                             'within the United States.',
                           'DERIVED_CITY': 'The spatially derived city name.',
                           'DERIVED_COUNTY': 'The spatially derived county name.',
                           'DERIVED_FIPS': 'The spatially derived FIPS code.',
                           'DERIVED_HUC': 'The spatially derived 8-digit Hydrologic Unit Code (HUC) that represents a '
                                          'geographic area representing part or all of a surface drainage basin, a '
                                          'combination of drainage basins, or a distinct hydrologic feature.',
                           'DERIVED_STATE': 'The spatially derived State Code.',
                           'DERIVED_WBD': 'The spatially derived 12-digit Hydrologic Unit Code (HUC) from the '
                                          'Watershed Boundary Dataset (WBD) that represents a geographic area '
                                          'representing part or all of a surface drainage basin, a combination of '
                                          'drainage basins, or a distinct hydrologic feature.',
                           'DERIVED_ZIP': 'The spatially derived ZIP Code.',
                           'FIPS_ CODE': 'The code that represents the county or county equivalent and the state or '
                                         'state equivalent of the United States.',
                           'HDATUM_DESC': 'The name that describes the reference datum used in determining latitude '
                                          'and longitude coordinates.\n'
                                          'Allowable Values: \n'
                                          'NAD27 \n'
                                          'NAD83\n'
                                          'WGS84',
                           'LATITUDE83': 'The measure of the angular distance on a meridian north or south of the '
                                         'equator standardized to NAD83 horizontal datum.',
                           'LOCATION_ ADDRESS': 'The address that describes the physical (geographic) location of the '
                                                'front door or main entrance of a facility site, including urban style '
                                                'street address or rural address.',
                           'LONGITUDE83': 'The measure of the angular distance on a meridian east or west of the prime '
                                          'meridian standardized to NAD83 horizontal datum.',
                           'OBJECTID': 'A unique numeric identifier for each geometry in a layer.',
                           'OZONE_8HR_1997_ AREA_NAME': 'The 8-hour Ozone (1997) non-attainment area name, spatially '
                                                        'derived from the Air Green Book.',
                           'OZONE_8HR_2008_ AREA_NAME': 'The 8-hour Ozone (2008) non-attainment area name, spatially '
                                                        'derived from the Air Green Book.',
                           'PB_2008_AREA_NAME': 'The Lead 2008 non-attainment area name, spatially derived from the '
                                                'Air Green Book.',
                           'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information '
                                            'management system for an environmental program. This represents the '
                                            'source program for the associated representative point.',
                           'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an '
                                         'information management system that represents a facility site, waste site, '
                                         'operable unit, or other feature tracked by that Environmental Information '
                                         'System. This represents the source program identifier for the associated '
                                         'representative point.',
                           'PM25_1997_AREA_ NAME': 'The Particulate Matter 2.5 (1997) non-attainment area name, '
                                                   'spatially derived from the Air Green Book.',
                           'PM25_2006_AREA_ NAME': 'The Particulate Matter 2.5 (2006) non-attainment area name, '
                                                   'spatially derived from the Air Green Book.',
                           'POSTAL_CODE': 'The combination of the five-digit Zone Improvement Plan (ZIP) code and the '
                                          'four-digit extension code (if available) that represents the geographic '
                                          'segment that is a subunit of the ZIP Code, assigned by the U.S. Postal '
                                          'Service to a geographic location; or the postal zone specific to the '
                                          'country, other than the U.S., where the facility site is located.',
                           'PRIMARY_NAME': 'The public or commercial name of a facility site (that is., the full name '
                                           'that commonly appears on invoices, signs, or other business documents, or '
                                           'as assigned by the state when the name is ambiguous).',
                           'REF_POINT_DESC': 'The name that identifies the place for which geographic coordinates were '
                                             'established.',
                           'REGISTRY_ID': 'The identification number assigned by the EPA Facility Registry System to '
                                          'uniquely identify a facility site.',
                           'SCALE': 'The number that represents the proportional distance on the ground for one unit '
                                    'of measure on the map or photo. Remarks: Mandatory for all horizontal data '
                                    'collection methods except for methods using Global Positioning System (GPS).',
                           'SHAPE': 'Coordinates that define the geometry of the point feature.',
                           'SOURCE_DESC': 'The name of the party responsible for providing the latitude and longitude '
                                          'coordinates.',
                           'STATE_CODE': 'The U.S. Postal Service abbreviation that represents the state or state '
                                         'equivalent for the U.S. and Canada.',
                           'VERTICAL_MEASURE': 'The measure of elevation (i.e., the altitude), in meters, above or '
                                               'below a reference datum.'},
 'V_GEO_PGM_COORDINATE_ALL': {'ACCURACY_SCORE': 'The accuracy score (in meters) derived as the accuracy value either '
                                                'supplied by the location metadata or calculated based on the '
                                                'collection method and then modified based on QA boundary checks.',
                              'ACCURACY_VALUE': 'The measure of the accuracy (in meters) of the latitude and longitude '
                                                'coordinates.',
                              'CITY_NAME': 'The name of the city, town, village or other locality, when identifiable, '
                                           'within whose boundaries (the majority of) the facility site is located. '
                                           'This is not always the same as the city used for USPS mail delivery.',
                              'COLLECT_MTH_DESC': 'The text that describes the method used to determine the latitude '
                                                  'and longitude coordinates for a point on the earth.',
                              'CONVEYOR': 'Identification of the party that transmitted the latitude and longitude '
                                          'coordinates.',
                              'COUNTRY_NAME': 'The name that represents a primary geopolitical unit of the world.',
                              'COUNTY_NAME': 'The name of the U.S. county or county equivalent in which the facility '
                                             'site is physically located.',
                              'DERIVED_CB_2010': 'The spatially derived 2010 Census Block Code, which represents the '
                                                 'smallest entity for which the Census Bureau collects and tabulates '
                                                 'decennial census information; bounded on all sides by visible and '
                                                 'nonvisible features shown on Census Bureau maps.',
                              'DERIVED_CD_112': 'The number that represents the 112th Congressional District for a '
                                                'state within the United States.',
                              'DERIVED_CITY': 'The spatially derived city name.',
                              'DERIVED_COUNTY': 'The spatially derived county name.',
                              'DERIVED_FIPS': 'The spatially derived FIPS code.',
                              'DERIVED_HUC': 'The spatially derived 8-digit Hydrologic Unit Code (HUC) that represents '
                                             'a geographic area representing part or all of a surface drainage basin, '
                                             'a combination of drainage basins, or a distinct hydrologic feature.',
                              'DERIVED_STATE': 'The spatially derived State Code.',
                              'DERIVED_WBD': 'The spatially derived 12-digit Hydrologic Unit Code (HUC) from the '
                                             'Watershed Boundary Dataset (WBD) that represents a geographic area '
                                             'representing part or all of a surface drainage basin, a combination of '
                                             'drainage basins, or a distinct hydrologic feature.',
                              'DERIVED_ZIP': 'The spatially derived ZIP Code.',
                              'FIPS_ CODE': 'The code that represents the county or county equivalent and the state or '
                                            'state equivalent of the United States.',
                              'HDATUM_DESC': 'The name that describes the reference datum used in determining latitude '
                                             'and longitude coordinates.\n'
                                             'Allowable Values: \n'
                                             'NAD27 \n'
                                             'NAD83\n'
                                             'WGS84',
                              'LATITUDE83': 'The measure of the angular distance on a meridian north or south of the '
                                            'equator standardized to NAD83 horizontal datum.',
                              'LOCATION_ ADDRESS': 'The address that describes the physical (geographic) location of '
                                                   'the front door or main entrance of a facility site, including '
                                                   'urban style street address or rural address.',
                              'LONGITUDE83': 'The measure of the angular distance on a meridian east or west of the '
                                             'prime meridian standardized to NAD83 horizontal datum.',
                              'OBJECTID': 'A unique numeric identifier for each geometry in a layer.',
                              'OZONE_8HR_1997_ AREA_NAME': 'The 8-hour Ozone (1997) non-attainment area name, '
                                                           'spatially derived from the Air Green Book.',
                              'OZONE_8HR_2008_ AREA_NAME': 'The 8-hour Ozone (2008) non-attainment area name, '
                                                           'spatially derived from the Air Green Book.',
                              'PB_2008_AREA_NAME': 'The Lead 2008 non-attainment area name, spatially derived from the '
                                                   'Air Green Book.',
                              'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information '
                                               'management system for an environmental program.',
                              'PGM_SYS_ID': 'The identification number, such as the permit number, assigned by an '
                                            'information management system that represents a facility site, waste '
                                            'site, operable unit, or other feature tracked by that Environmental '
                                            'Information System.',
                              'PM25_1997_AREA_ NAME': 'The Particulate Matter 2.5 (1997) non-attainment area name, '
                                                      'spatially derived from the Air Green Book.',
                              'PM25_2006_AREA_ NAME': 'The Particulate Matter 2.5 (2006) non-attainment area name, '
                                                      'spatially derived from the Air Green Book.',
                              'POSTAL_CODE': 'The combination of the five-digit Zone Improvement Plan (ZIP) code and '
                                             'the four-digit extension code (if available) that represents the '
                                             'geographic segment that is a subunit of the ZIP Code, assigned by the '
                                             'U.S. Postal Service to a geographic location; or the postal zone '
                                             'specific to the country, other than the U.S., where the facility site is '
                                             'located.',
                              'PRIMARY_NAME': 'The public or commercial name of a facility site (that is., the full '
                                              'name that commonly appears on invoices, signs, or other business '
                                              'documents, or as assigned by the state when the name is ambiguous).',
                              'REF_POINT_DESC': 'The name that identifies the place for which geographic coordinates '
                                                'were established.',
                              'REGISTRY_ID': 'The identification number assigned by the EPA Facility Registry System '
                                             'to uniquely identify a facility site.',
                              'REP_LATITUDE83': 'The latitude coordinate of the facility representative point for this '
                                                'program record.',
                              'REP_LONGITUDE83': 'The longitude coordinate of the facility representative point for '
                                                 'this program record.',
                              'REP_OBJECTID': 'The unique numeric identifier for the geometry of the facility '
                                              'representative point for this program record.',
                              'REP_TIMESTAMP': 'A system-generated value that represents the calendar date and time '
                                               'the facility representative point for this program record was posted '
                                               'to the database.',
                              'SCALE': 'The number that represents the proportional distance on the ground for one '
                                       'unit of measure on the map or photo. Remarks: Mandatory for all horizontal '
                                       'data collection methods except for methods using Global Positioning System '
                                       '(GPS).',
                              'SHAPE': 'Coordinates that define the geometry of the point feature.',
                              'SOURCE_DESC': 'The name of the party responsible for providing the latitude and '
                                             'longitude coordinates.',
                              'STATE_CODE': 'The U.S. Postal Service abbreviation that represents the state or state '
                                            'equivalent for the U.S. and Canada.',
                              'SUB_ID': 'The identification number for an operable unit or sub-unit of a facility '
                                        'site.',
                              'TIMESTAMP': 'A system-generated value that represents the calendar date and time the '
                                           'corresponding information was posted to the database.',
                              'VERTICAL_MEASURE': 'The measure of elevation (i.e., the altitude), in meters, above or '
                                                  'below a reference datum.'}}
