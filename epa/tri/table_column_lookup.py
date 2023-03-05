table_column_lookup = \
{'TRI_ADDITIONAL_INFO': {'ADDITIONAL_TEXT': 'Text describing additional optional information on source reduction, '
                                            'recycling, or pollution control activities implemented in the reporting '
                                            'year or prior years for the reported EPCRA section 313 chemical. In part '
                                            'II, section 8.11 of the form R, facilities indicate if they are including '
                                            'optional additional information about their source reduction, recycling, '
                                            'or pollution control activities. The text that appears in the '
                                            'ADDITIONAL_INFO column of this table represents that additional '
                                            'information that the facility is including.',
                         'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each submission.  '
                                         'The format is TTYYNNNNNNNNN, where TT = document type, YY = reporting year, '
                                         'and NNNNNNNNN = assigned number with a check digit.',
                         'TYPE': ''},
 'TRI_CHEM_ACTIVITY': {'ANCILLARY': 'Indicates the toxic chemical is used at the facility for purposes other than as a '
                                    'manufacturing aid or chemical processing aid, such as cleaners, degreasers, '
                                    'lubricants, fuels, toxic chemicals used for treating wastes, and toxic chemicals '
                                    "used to treat water at the facility.  Values: 1 = 'Yes', 0 = 'No'.",
                       'ARTICLE_COMPONENT': 'Indicates the toxic chemical becomes an integral part of an article '
                                            'distributed into commerce, such as copper in wire or resins in a plastic '
                                            'pen, or the pigment components of paint applied to a chair that is sold.  '
                                            "Values: 1 = 'Yes', 0 = 'No'.",
                       'BYPRODUCT': 'Indicates the toxic chemical is produced coincidentally during the manufacture, '
                                    'process, or otherwise use of another chemical substance or mixture and, following '
                                    'its production, is separated from that other chemical substance or mixture.  This '
                                    'includes toxic chemicals that may be created as the result of waste management.  '
                                    "Values: 1 = 'Yes', 0 = 'No'.",
                       'CHEM_PROCESSING_AID': 'Indicates the toxic chemical is used to aid in the manufacture or '
                                              'synthesis of another chemical substance such that it comes into contact '
                                              'with the product during manufacture, but is not intended to remain with '
                                              'or become part of the final product or mixture.  Some examples of '
                                              'chemical processing aids are process solvents, catalysts, solution '
                                              "buffers, inhibitors, and reaction terminators.  Values: 1 = 'Yes', 0 = "
                                              "'No'.",
                       'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each submission.  '
                                       'The format is TTYYNNNNNNNNN, where TT = document type, YY = reporting year, '
                                       'and NNNNNNNNN = assigned number with a check digit.',
                       'FORMULATION_COMPONENT': 'Indicates the toxic chemical is used as an ingredient in a product '
                                                'mixture to enhance performance of the product during its use, such as '
                                                'dyes in ink, solvents in paint, additions, reaction diluents, '
                                                'initiators, inhibitors, emulsifiers, surfactants, lubricants, flame '
                                                "retardants, and rheological modifiers.  Values: 1 = 'Yes', 0 = 'No'.",
                       'IMPORTED': 'Indicates the toxic chemical was imported into the Customs Territory of the United '
                                   'States by the facility.  This includes the facility directly importing the toxic '
                                   'chemical or specifically requesting a broker or other party to obtain the toxic '
                                   'chemical from a foreign source.  The Customs Territory of the United States '
                                   'includes the 50 States, Guam, Puerto Rico, American Samoa, and the U.S. Virgin '
                                   "Islands.  Values: 1 = 'Yes', 0 = 'No'.",
                       'MANUFACTURE_AID': 'Indicates the toxic chemical is used to aid in the manufacturing process '
                                          'but does not come into contact with the product during manufacture.  Some '
                                          'examples include valve lubricants, refrigerants, metalworking fluids, '
                                          "coolants, and hydraulic fluids.  Values: 1 = 'Yes', 0 = 'No'.",
                       'MANUFACTURE_IMPURITY': 'Indicator that shows whether the facility produces the reported '
                                               'chemical as a result of the manufacture, processing, or otherwise use '
                                               'of another chemical, but does not separate the chemical and it remains '
                                               'primarily in the mixture or product with that other chemical.  Values: '
                                               "1 = 'Yes', 0 = 'No'.",
                       'PROCESSED_RECYCLING': 'Indicates the facility reported the toxic chemical as being recycled as '
                                              'a process activity or use in section 3.2 of the form R.   This data '
                                              'element is reported in Part II, section 3 of the form R in the section '
                                              '"Activities and Uses of the Toxic Chemical at the Facility".  '
                                              'Specifically, it\'s reported in Part II, Subsection 3.2, "Process the '
                                              'Toxic Chemical".  If the "Recycled" check box is checked in this '
                                              'section, it indicates that facility recycled this chemical as part of '
                                              'its processing.  The values for PROCESSED_RECYCLING are:',
                       'PROCESS_IMPURITY': 'Indicator that shows whether the facility processed the reported chemical '
                                           'but did not separate it and it remains as an impurity in the primary the '
                                           "mixture or trade name product.  Values: 1 = 'Yes', 0 = 'No'.",
                       'PRODUCE': 'Indicates the toxic chemical was created by the facility.  A toxic chemical is '
                                  'considered manufactured even if the toxic chemical is created unintentionally or '
                                  "exists only for a short period of time.  Values: 1 = 'Yes', 0 = 'No'.",
                       'REACTANT': 'Indicates the toxic chemical is used in chemical reactions to create another '
                                   'chemical substance or product that is then sold or otherwise distributed to other '
                                   'facilities.  Some examples of reactants include feedstocks, raw materials, '
                                   "intermediates, and initiators.  Values: 1 = 'Yes', 0 = 'No'.",
                       'REPACKAGING': 'Indicates the toxic chemical has been received by the facility and subsequently '
                                      'prepared for distribution into commerce in a different form, state, or quantity '
                                      'than it was received, such as petroleum being transferred from a storage tank '
                                      "to tanker trucks.  Values: 1 = 'Yes', 0 = 'No'.",
                       'SALE_DISTRIBUTION': 'Indicates the toxic chemical was produced or imported by the facility '
                                            'specifically to be sold or distributed to other outside facilities.  '
                                            "Values: 1 = 'Yes', 0 = 'No'.",
                       'USED_PROCESSED': 'Indicates the toxic chemical was produced or imported by the facility and '
                                         'then further processed or otherwise used at the same facility.  If this box '
                                         'is checked, at least one box in section 3.2 or section 3.3 will be checked.  '
                                         "Values: 1 = 'Yes', 0 = 'No'."},
 'TRI_CHEM_INFO': {'ACTIVE_DATE': 'First year that this chemical must be reported to TRI.',
                   'CAAC_IND': 'Indicates whether the chemical is reportable under the Clean Air Act.  Values: 1 = '
                               "'Yes', 0 = 'No'.",
                   'CARC_IND': 'Indicates whether the chemical is reportable as a carcinogen under the CARC.  Values: '
                               "1 = 'Yes', 0 = 'No'.",
                   'CAS_REGISTRY_NUMBER': 'Unique numerical identifier assigned by Chemical Abstracts Service to every '
                                          'chemical substance described in the open scientific literature, including '
                                          'organic and inorganic compounds, minerals, isotopes, alloys and '
                                          'nonstructurable materials.',
                   'CHEM_NAME': 'The official name of the toxic chemical, toxic chemical mixture,  (e.g., xylene mixed '
                                'isomers), or chemical category as it appears on the EPCRA Section 313 list.',
                   'CLASSIFICATION': 'Indicates the classification of the chemical.  Chemicals can be classified as '
                                     'either a Dioxin or Dioxin-like compounds, a PBT (Persistent, Bioaccumulative and '
                                     'Toxic) chemical or a general EPCRA Section 313 chemical.  Values:  0=TRI, 1=PBT, '
                                     '2=Dioxin',
                   'DEFAULT_PERCENTAGE_TO_81C': 'For this chemical, the assigned percent of a POTW transfer that would '
                                                'considered part of 8.1.C (Total off-site disposal to Class I '
                                                'Underground Inj',
                   'DEFAULT_PERCENTAGE_TO_81D': 'For this chemical, the assigned percent of a POTW transfer that would '
                                                'considered part of 8.1.D (Total other off-site disposal or other '
                                                'releases).  This percentage will be used in RY 2014 and forward when '
                                                'calculating potw releases, off-site releases and  total releases.',
                   'DEFAULT_PERCENTAGE_TO_87': 'For this chemical, the assigned percent of a POTW transfer that would '
                                               'considered part of 8.7 (Quantity treated off-site).  This percentage '
                                               'will be used in RY 2014 and forward when calculating total amount '
                                               'treated off-site.',
                   'FEDS_IND': 'Indicates whether the chemical is a non-Section 313 chemical submitted by a federal '
                               "facility under Executive Order 12856.  Values: 1 = 'Yes', 0 = 'No'.",
                   'INACTIVE_DATE': 'Final year that this chemical must be reported to TRI.',
                   'METAL_IND': '',
                   'NO_DECIMALS': 'Indicates the maximum number of decimals that can be used to quantify a chemical.   '
                                  'This measurement applies to release, transfer and source reduction quantities.  PBT '
                                  '(Persistent, Bioaccumulative and Toxic) chemicals, including Dioxins and '
                                  'Dioxin-like Compounds, can be quantified using numbers to the right of the decimal '
                                  'point.   The measurement expresses the maximum number of positions to the right of '
                                  'the decimal point that a PBT chemical can be expressed in.   All other Non-PBT '
                                  'chemicals arereported as whole numbers.',
                   'PBT_END_YEAR': 'Indicates the year that a PBT (Persistent, Bioaccumulative and Toxic) chemical was '
                                   'dropped as an EPCRA Section 313 PBT Chemical, Toxics Release Inventory.',
                   'PBT_IND': "A value of 'Y' indicates the chemical is a PBT chemical.  A value of 'N' indicates the "
                              'chemical is not a PBT chemical.',
                   'PBT_START_YEAR': 'Indicates the year that a PBT (Persistent, Bioaccumulative and Toxic) chemical '
                                     'was designated as an EPCRA Section 313 PBT Chemical, Toxics Release Inventory.',
                   'PFAS_IND': "A value of 'Y' indicates the chemical is a PFAS chemical.  A value of 'N' indicates "
                               'the chemical is not a PFAS chemical.',
                   'R3350_IND': 'Indicates whether the chemical is reportable under Regulation 3350.  Values: 1 = '
                                "'Yes', 0 = 'No'.",
                   'SRS_ID': 'This is the unique identifier assigned to a substance for internal tracking within EPA '
                             'systems.',
                   'TRI_CHEM_ID': 'The number assigned to chemicals regulated under Section 313 of the Emergency '
                                  'Planning and Community Right-to-Know Act (EPCRA). For most toxic chemicals or '
                                  'mixture of chemicals (e.g., xylene mixed isomers), the TRI_CHEM_ID is the Chemical '
                                  'Abstract Service Registry (CAS) number.  A given listed toxic chemical or mixture '
                                  'may be known by many names but it will have only one CAS number.  For example, '
                                  'methyl ethyl ketone and 2-butanone are synonyms for the same toxic chemical and '
                                  'thus have only one CAS number (78-93-3).  For categories of chemicals for which CAS '
                                  'Registry numbers have not been assigned, a four-character category code, asssigned '
                                  'by TRI, is included in TRI_CHEM_ID.   Form R section 1.1 will be empty if a trade '
                                  'secret was claimed for the toxic chemical and information is provided in Section '
                                  '1.3 or 2.1.',
                   'UNIT_OF_MEASURE': 'Indicates the unit of measure used to quantify the chemical.    Values:  '
                                      '{Pounds, Grams}'},
 'TRI_CODE_DESC': {'CODE': 'The permissible values for a column.',
                   'DESCRIPT': 'The text description of a permissible value contained in CODE.',
                   'TABLE_ID': 'A designation for a related group of permissible values.  The name that identifies '
                               'this group is located in TRI_TABLE_ID_NAME.'},
 'TRI_COUNTY': {'COUNTY_NAME': 'The standardized name of the county where the facility is located.',
                'ZIP_CODE': 'The Zone Improvement Plan (ZIP) code assigned by the U.S. Postal Service as part of the '
                            'address of a facility.'},
 'TRI_ENERGY_RECOVERY': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each submission.  '
                                         'The format is TTYYNNNNNNNNN, where TT = document type, YY = reporting year, '
                                         'and NNNNNNNNN = assigned number with a check digit.',
                         'ONSITE_ENERGY_PROC_CODE': 'Code for the specific energy recovery method applied to the toxic '
                                                    'chemical.  Unlike section 7A which includes all treatment methods '
                                                    'applied to the waste stream, the energy recovery must be directed '
                                                    'at the specific toxic chemical being reported.  This means that '
                                                    'the toxic chemical must have significant heating value.   Section '
                                                    '7B should not be used for chemicals that do not have significant '
                                                    'heating values such as metals.  Values:  U01 = Industrial Kiln, '
                                                    'U02 = Industrial Furnace, U03 = IndustrialBoiler, U09 = Other '
                                                    'Energy Recovery Methods, NA = not applicable, no on-site energy '
                                                    'recovery applied to the toxic chemical.'},
 'TRI_FACILITY': {'ASGN_AGENCY': 'An abbreviation for the name of the agency supported by a federal or Government '
                                 'Owned/Contractor Operated (GOCO) reporting site.',
                  'ASGN_FEDERAL_IND': 'An identifier that indicates the ownership status of a facility.  A Federal '
                                      'facility is a facility owned or operated by the Federal government.  This '
                                      'includes facilities that are operated by contractors to the Federal government '
                                      '(i.e., a facility where the land is owned by the Federal government but a '
                                      "private company is under contract to run the facility's operations).  The types "
                                      'of Federal facilities that report to TRI are broader than the types of private '
                                      'sector facilities that report to TRI (e.g., DOD military bases).  Values:  C = '
                                      "'Commercial', F = 'Federal facility', and G = 'Government owned/contractor "
                                      "operated' (GOCO).",
                  'ASGN_PARTIAL_IND': 'Indicates that the facility reports by establishment or groups of '
                                      'establishments as assigned by TRI from Form R submisions.  Partial facilities '
                                      'may have more than one submission for the same chemical in one reporting year.  '
                                      "Values:  0 = 'Entire facility', 1 = 'Partial facility'.",
                  'ASGN_PUBLIC_CONTACT': 'The name of the individual who may be contacted by the general public with '
                                         'questions regarding the company and the information reported to TRI as '
                                         'assigned by TRI from Form R submissions..  This person may or may not be '
                                         'familiar with the information provided in the form but has been designated '
                                         'by the facility or establishment to handle public inquiries.',
                  'ASGN_PUBLIC_PHONE': 'The phone number to reach the person identified in the Public Contact Name box '
                                       '(PUBLIC_CONTACT_PERSON), as assigned by TRI from Form R submissions.',
                  'ASGN_PUBLIC_PHONE_EXT': 'The telephone extension of the Public Contact Person as reported on the '
                                           'form R',
                  'BIA_CODE': 'The Bureau of Indian Affairs (BIA) Tribal Code that indicates the tribal land that the '
                              'facility is located on.  A facility reports this three digit code to the Toxics Release '
                              'Inventory (TRI) program on the form R or form A.  There are over 300 BIA Tribal Codes.  '
                              'For a list of BIA Tribal Codes and associated Tribe Names',
                  'CITY_NAME': 'The city where the facility or establishment is physically located.',
                  'COUNTY_NAME': 'The standardized name of the county where the facility is located.',
                  'EPA_REGISTRY_ID': 'Indicates the Facility Registry Service (FRS) id for a TRI Facility, POTW '
                                     'Facility or Off-site Transfer Location facility.  The Facility Registry Service '
                                     '(FRS) is a centrally managed database at EPA that identifies facilities, sites '
                                     'or places subject to environmental regulations or of environmental interest.  '
                                     'Using the FRS Id (EPA_REGISTRY_ID), data users can link data from different EPA '
                                     'programs together.    See the Facility Registry Service at',
                  'FACILITY_NAME': 'The name of the facility or establishment for which the form was submitted. For '
                                   'purposes of TRI a "facility" is generally considered to be all buildings and '
                                   'equipment owned or operated by a company on a single piece of property. The '
                                   'facility may be only one building in an industrial park or it may be a large '
                                   'complex covering many acres. At some larger facilities there may be several '
                                   'different businesses that are all run by the same company. These different '
                                   'businesses are referred to as "establishments." Generally, a company will submit '
                                   'one Form R for the entire facility. A facility may choose, however, to submit a '
                                   'Form R for each establishment separately. The name in this section will either be '
                                   'the name used for the entire facility or the name of the specific establishment, '
                                   'depending on how the facility chooses to report.',
                  'FAC_CLOSED_IND': "A flag that indicates whether a facility is open (value =' 0'), closed (value = "
                                    "'1'), or inactive for TRI (value = '2').",
                  'FAC_LATITUDE': 'The series of numbers that identifies the exact physical location of the facility '
                                  "as a measure of the angular distance north form the earth's equator to the center "
                                  'of the facility.  The  value is stored as degrees, minutes and seconds (0DDMMSS), '
                                  'and the first position is zero-filled.  The value is positive for locations north '
                                  'of the equator.',
                  'FAC_LONGITUDE': 'The series of numbers which identifies the exact physical location of the facility '
                                   "as a measure of the arc or portion of the earth's equator between the meridian of "
                                   'the center of the facility and the prime meridian.  The right-justified value is '
                                   'stored as degrees, minutes and seconds (0DDDMMSS). Tenths of seconds are not '
                                   'stored.  The value is negative for locations in the Western hemisphere.',
                  'FRS_ID': 'Indicates the Facility Registry Service (FRS) id for a TRI Facility, POTW Facility or '
                            'Off-site Transfer Location facility.  The Facility Registry Service (FRS) is a centrally '
                            'managed database at EPA that identifies facilities, sites or places subject to '
                            'environmental regulations or of environmental interest.  Using the FRS Id '
                            '(EPA_REGISTRY_ID), data users can link data from different EPA programs together.    See '
                            'the Facility Registry Service at',
                  'MAIL_CITY': 'The city the facility or establishment uses to receive mail.  This may or may not be '
                               'the same as the information reported in the City box.',
                  'MAIL_COUNTRY': 'The country  the facility or establishment uses to receive mail.',
                  'MAIL_NAME': 'The name which the facility or establishment uses for receiving mail if the address '
                               'used for mail is different than in the Street box.  This may or may not be the same as '
                               'the name listed in the Facility or Establishment Name box.',
                  'MAIL_PROVINCE': 'The province the facility or establishment uses to receive mail.   A facility may '
                                   'receive mail at an address outside of the United States.   The province field '
                                   'gives a facility the flexibility needed to enter a correct mailing address outside '
                                   'the United States.',
                  'MAIL_STATE_ABBR': 'The state abbreviation the facility or establishment uses to receive mail.  This '
                                     'may or may not be the same as the information reported in the State box.',
                  'MAIL_STREET_ADDRESS': 'The address the facility or establishment uses for receiving mail.  Form R '
                                         'instructs the submitter to enter the address used for mail only if different '
                                         'than in the Street box.    The TRIS database stores the address from the '
                                         'Street box (STREET_ADDRESS) in MAILING_STREET_ADDRESS even when the facility '
                                         'Mailing address is not different.',
                  'MAIL_ZIP_CODE': 'The zip code the facility or establishment uses to receive mail.  This may or may '
                                   'not be the same as the information reported in the Zip Code box.',
                  'PARENT_CO_DB_NUM': 'The number which has been assigned to the parent company by Dun & Bradstreet.  '
                                      'Dun & Bradstreet is a private financial tracking and accounting firm.  Not all '
                                      "parent companies will have a Dun & Bradstreet number.  'NA' indicates that the "
                                      "facility or establishment's parent company does not have a Dun & Bradstreet "
                                      'number.',
                  'PARENT_CO_NAME': 'Name of the corporation or other business company that is the ultimate parent '
                                    'company, located in the United States, of the facility or establishment '
                                    'submitting the data.  The parent company is the company that directly owns at '
                                    'least 50 percent of the voting stock of the reporting company.  This does not '
                                    "include foreign parent companies.  'NA' indicates that the facility does not have "
                                    'a parent company.',
                  'PREF_ACCURACY': "The EPA's preferred geographic coordinate accuracy estimation for thereporting "
                                   'facility.  Describes the accuracy value as a range (+/) inmeters of the latitude '
                                   'and longitude.',
                  'PREF_COLLECT_METH': "The EPA's preferred geographic coordinate collection method code forthe "
                                       'reporting facility.  Method used to determine the latitude andlongitude.',
                  'PREF_DESC_CATEGORY': "The EPA's preferred geographic coordinate description category.Describes the "
                                        'category of feature referenced by the latitude andlongitude.',
                  'PREF_HORIZONTAL_DATUM': "The EPA's preferred geographic coordinate horizontal datum.  "
                                           'Referencedatum of the latitude and longitude.',
                  'PREF_LATITUDE': "The EPA's preferred geographic latitude estimation of the reportingfacility.  "
                                   'Value for latitude is in decimal degrees. This is a signedfield.',
                  'PREF_LONGITUDE': "The EPA's preferred geographic longitude estimation of the reportingfacility.  "
                                    'Value for longitude is in decimal degrees. This is a signedfield.',
                  'PREF_QA_CODE': 'Contains the results of four quality assurance tests (Test 1 throughTest 4 below) '
                                  'used to determine facility location. "ZIP Code BoundingBox" is a rectangle '
                                  'generated from the ZIP Code boundaries, which isdefined by the extreme north-south '
                                  'latitude and east-west longitudes,plus 1 kilometer (km) in each direction.  The '
                                  'quality assurance tests are:',
                  'PREF_SOURCE_SCALE': "The EPA's preferred geographic coordinate source map scale code.  This is the "
                                       'scaleof the source used to determine the latitude and longitude.',
                  'REGION': 'The EPA region in which the facility is located.',
                  'STANDARDIZED_PARENT_COMPANY': 'A data field developed by EPA that is intended to best reflect the '
                                                 'current ultimate US parent company for the facility.  EPA developed '
                                                 'this field to facilitate the aggregation of TRI facility-level '
                                                 'information to the associated parent company by ensuring that each '
                                                 'company is referenced consistently by the same name.  Filers often '
                                                 'submit names with small variations (e.g., Exopack vs. Exopack '
                                                 'Holdings Corp) that make aggregation at the corporate level '
                                                 'challenging when using parent names as reported.  The standardized '
                                                 'parent company field was developed by standardizing the '
                                                 'self-submitted parent company names through a process described on '
                                                 'the TRI website (e.g., eliminating periods, standardizing common '
                                                 'acronyms such as Inc and Corp, etc.). The process also includes the '
                                                 'replacement of subsidiary names with the name of the ultimate US '
                                                 'parent in cases where EPA identified a subsidiary in the submitted '
                                                 'parent company field.',
                  'STATE_ABBR': 'The state abbreviation where the tribe is located.',
                  'STATE_COUNTY_FIPS_CODE': 'Combination of the two-letter state abbreviation and the county code.',
                  'STREET_ADDRESS': 'The street address for the physical location of the facility or establishment.',
                  'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI program.  '
                                     'Usually, only one number is assigned to each facility and the number is for the '
                                     'entire facility.  One company may have multiple TRI Facility Identification (ID) '
                                     'numbers if they have multiple facilities.  One facility with many establishments '
                                     'will usually have only one TRI Facility ID number.  They will then use this '
                                     'number for all of their Form Rs even if they are submitting a Form R for '
                                     'different establishments with different names.  In a few instances different '
                                     'establishments of the same facility will have different TRI Facility ID '
                                     'numbers.  The format is ZZZZZNNNNNSSSSS, where ZZZZZ = ZIP code, NNNNN = the '
                                     'first 5 consonants of the name, and SSSSS = the first 5 non-blank non-special '
                                     'characters in the street address.',
                  'ZIP_CODE': 'The Zone Improvement Plan (ZIP) code assigned by the U.S. Postal Service as part of the '
                              'address of a facility.'},
 'TRI_FACILITY_DB': {'ASGN_DB_IND': 'Indicates that the associated DB_NUM represents the principal Dun & Bradstreet '
                                    'number assigned  to the facility by TRI from Form R or Form A submissions.  '
                                    "Values: 1 = 'Yes', 0 = 'No'.",
                     'DB_NUM': 'The number or numbers which have been assigned to the facility by Dun & Bradstreet.  '
                               'Dun & Bradstreet is a private financial tracking and accounting firm.  Not all '
                               'facilities will have Dun & Bradstreet numbers.',
                     'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI program.  '
                                        'Usually, only one number is assigned to each facility and the number is for '
                                        'the entire facility.  One company may have multiple TRI Facility '
                                        'Identification (ID) numbers if they have multiple facilities.  One facility '
                                        'with many establishments will usually have only one TRI Facility ID number.  '
                                        'They will then use this number for all of their Form Rs even if they are '
                                        'submitting a Form R for different establishments with different names.  In a '
                                        'few instances different establishments of the same facility will have '
                                        'different TRI Facility ID numbers.  The format is ZZZZZNNNNNSSSSS, where '
                                        'ZZZZZ = ZIP code, NNNNN = the first 5 consonants of the name, and SSSSS = the '
                                        'first 5 non-blank non-special characters in the street address.'},
 'TRI_FACILITY_DB_HISTORY': {'ASGN_DB_IND': 'Indicates that the associated DB_NUM represents the principal Dun & '
                                            'Bradstreet number assigned  to the facility by TRI from Form R or Form A '
                                            "submissions.  Values: 1 = 'Yes', 0 = 'No'.",
                             'DB_NUM': 'The number or numbers which have been assigned to the facility by Dun & '
                                       'Bradstreet.  Dun & Bradstreet is a private financial tracking and accounting '
                                       'firm.  Not all facilities will have Dun & Bradstreet numbers.',
                             'REPORTING_YEAR': 'The year for which the form was submitted.  This is not the year in '
                                               'which the form was filed but rather it is the calendar year (January 1 '
                                               '- December 31) during which the toxic chemical was manufactured, '
                                               'processed and/or otherwise used and released or otherwise managed as a '
                                               'waste.',
                             'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                                'program.  Usually, only one number is assigned to each facility and '
                                                'the number is for the entire facility.  One company may have multiple '
                                                'TRI Facility Identification (ID) numbers if they have multiple '
                                                'facilities.  One facility with many establishments will usually have '
                                                'only one TRI Facility ID number.  They will then use this number for '
                                                'all of their Form Rs even if they are submitting a Form R for '
                                                'different establishments with different names.  In a few instances '
                                                'different establishments of the same facility will have different TRI '
                                                'Facility ID numbers.  The format is ZZZZZNNNNNSSSSS, where ZZZZZ = '
                                                'ZIP code, NNNNN = the first 5 consonants of the name, and SSSSS = the '
                                                'first 5 non-blank non-special characters in the street address.'},
 'TRI_FACILITY_HISTORY': {'ASGN_AGENCY': 'An abbreviation for the name of the agency supported by a federal or '
                                         'Government Owned/Contractor Operated (GOCO) reporting site.',
                          'ASGN_FEDERAL_IND': 'An identifier that indicates the ownership status of a facility.  A '
                                              'Federal facility is a facility owned or operated by the Federal '
                                              'government.  This includes facilities that are operated by contractors '
                                              'to the Federal government (i.e., a facility where the land is owned by '
                                              'the Federal government but a private company is under contract to run '
                                              "the facility's operations).  The types of Federal facilities that "
                                              'report to TRI are broader than the types of private sector facilities '
                                              'that report to TRI (e.g., DOD military bases).  Values:  C = '
                                              "'Commercial', F = 'Federal facility', and G = 'Government "
                                              "owned/contractor operated' (GOCO).",
                          'ASGN_PARTIAL_IND': 'Indicates that the facility reports by establishment or groups of '
                                              'establishments as assigned by TRI from Form R submisions.  Partial '
                                              'facilities may have more than one submission for the same chemical in '
                                              "one reporting year.  Values:  0 = 'Entire facility', 1 = 'Partial "
                                              "facility'.",
                          'ASGN_PUBLIC_CONTACT': 'The name of the individual who may be contacted by the general '
                                                 'public with questions regarding the company and the information '
                                                 'reported to TRI as assigned by TRI from Form R submissions..  This '
                                                 'person may or may not be familiar with the information provided in '
                                                 'the form but has been designated by the facility or establishment to '
                                                 'handle public inquiries.',
                          'ASGN_PUBLIC_PHONE': 'The phone number to reach the person identified in the Public Contact '
                                               'Name box (PUBLIC_CONTACT_PERSON), as assigned by TRI from Form R '
                                               'submissions.',
                          'ASGN_PUBLIC_PHONE_EXT': 'The telephone extension of the Public Contact Person as reported '
                                                   'on the form R',
                          'BIA_CODE': 'The Bureau of Indian Affairs (BIA) Tribal Code that indicates the tribal land '
                                      'that the facility is located on.  A facility reports this three digit code to '
                                      'the Toxics Release Inventory (TRI) program on the form R or form A.  There are '
                                      'over 300 BIA Tribal Codes.  For a list of BIA Tribal Codes and associated Tribe '
                                      'Names',
                          'CITY_NAME': 'The city where the facility or establishment is physically located.',
                          'COUNTY_NAME': 'The standardized name of the county where the facility is located.',
                          'FACILITY_NAME': 'The name of the facility or establishment for which the form was '
                                           'submitted. For purposes of TRI a "facility" is generally considered to be '
                                           'all buildings and equipment owned or operated by a company on a single '
                                           'piece of property. The facility may be only one building in an industrial '
                                           'park or it may be a large complex covering many acres. At some larger '
                                           'facilities there may be several different businesses that are all run by '
                                           'the same company. These different businesses are referred to as '
                                           '"establishments." Generally, a company will submit one Form R for the '
                                           'entire facility. A facility may choose, however, to submit a Form R for '
                                           'each establishment separately. The name in this section will either be the '
                                           'name used for the entire facility or the name of the specific '
                                           'establishment, depending on how the facility chooses to report.',
                          'FAC_LATITUDE': 'The series of numbers that identifies the exact physical location of the '
                                          "facility as a measure of the angular distance north form the earth's "
                                          'equator to the center of the facility.  The  value is stored as degrees, '
                                          'minutes and seconds (0DDMMSS), and the first position is zero-filled.  The '
                                          'value is positive for locations north of the equator.',
                          'FAC_LONGITUDE': 'The series of numbers which identifies the exact physical location of the '
                                           "facility as a measure of the arc or portion of the earth's equator between "
                                           'the meridian of the center of the facility and the prime meridian.  The '
                                           'right-justified value is stored as degrees, minutes and seconds '
                                           '(0DDDMMSS). Tenths of seconds are not stored.  The value is negative for '
                                           'locations in the Western hemisphere.',
                          'MAIL_CITY': 'The city the facility or establishment uses to receive mail.  This may or may '
                                       'not be the same as the information reported in the City box.',
                          'MAIL_COUNTRY': 'The country  the facility or establishment uses to receive mail.',
                          'MAIL_NAME': 'The name which the facility or establishment uses for receiving mail if the '
                                       'address used for mail is different than in the Street box.  This may or may '
                                       'not be the same as the name listed in the Facility or Establishment Name box.',
                          'MAIL_PROVINCE': 'The province the facility or establishment uses to receive mail.   A '
                                           'facility may receive mail at an address outside of the United States.   '
                                           'The province field gives a facility the flexibility needed to enter a '
                                           'correct mailing address outside the United States.',
                          'MAIL_STATE_ABBR': 'The state abbreviation the facility or establishment uses to receive '
                                             'mail.  This may or may not be the same as the information reported in '
                                             'the State box.',
                          'MAIL_STREET_ADDRESS': 'The address the facility or establishment uses for receiving mail.  '
                                                 'Form R instructs the submitter to enter the address used for mail '
                                                 'only if different than in the Street box.    The TRIS database '
                                                 'stores the address from the Street box (STREET_ADDRESS) in '
                                                 'MAILING_STREET_ADDRESS even when the facility Mailing address is not '
                                                 'different.',
                          'MAIL_ZIP_CODE': 'The zip code the facility or establishment uses to receive mail.  This may '
                                           'or may not be the same as the information reported in the Zip Code box.',
                          'PARENT_CO_DB_NUM': 'The number which has been assigned to the parent company by Dun & '
                                              'Bradstreet.  Dun & Bradstreet is a private financial tracking and '
                                              'accounting firm.  Not all parent companies will have a Dun & Bradstreet '
                                              "number.  'NA' indicates that the facility or establishment's parent "
                                              'company does not have a Dun & Bradstreet number.',
                          'PARENT_CO_NAME': 'Name of the corporation or other business company that is the ultimate '
                                            'parent company, located in the United States, of the facility or '
                                            'establishment submitting the data.  The parent company is the company '
                                            'that directly owns at least 50 percent of the voting stock of the '
                                            "reporting company.  This does not include foreign parent companies.  'NA' "
                                            'indicates that the facility does not have a parent company.',
                          'PREF_ACCURACY': "The EPA's preferred geographic coordinate accuracy estimation for "
                                           'thereporting facility.  Describes the accuracy value as a range (+/) '
                                           'inmeters of the latitude and longitude.',
                          'PREF_COLLECT_METH': "The EPA's preferred geographic coordinate collection method code "
                                               'forthe reporting facility.  Method used to determine the latitude '
                                               'andlongitude.',
                          'PREF_DESC_CATEGORY': "The EPA's preferred geographic coordinate description "
                                                'category.Describes the category of feature referenced by the latitude '
                                                'andlongitude.',
                          'PREF_HORIZONTAL_DATUM': "The EPA's preferred geographic coordinate horizontal datum.  "
                                                   'Referencedatum of the latitude and longitude.',
                          'PREF_LATITUDE': "The EPA's preferred geographic latitude estimation of the "
                                           'reportingfacility.  Value for latitude is in decimal degrees. This is a '
                                           'signedfield.',
                          'PREF_LONGITUDE': "The EPA's preferred geographic longitude estimation of the "
                                            'reportingfacility.  Value for longitude is in decimal degrees. This is a '
                                            'signedfield.',
                          'PREF_QA_CODE': 'Contains the results of four quality assurance tests (Test 1 throughTest 4 '
                                          'below) used to determine facility location. "ZIP Code BoundingBox" is a '
                                          'rectangle generated from the ZIP Code boundaries, which isdefined by the '
                                          'extreme north-south latitude and east-west longitudes,plus 1 kilometer (km) '
                                          'in each direction.  The quality assurance tests are:',
                          'PREF_SOURCE_SCALE': "The EPA's preferred geographic coordinate source map scale code.  This "
                                               'is the scaleof the source used to determine the latitude and '
                                               'longitude.',
                          'REGION': 'The EPA region in which the facility is located.',
                          'REPORTING_YEAR': 'The year for which the form was submitted.  This is not the year in which '
                                            'the form was filed but rather it is the calendar year (January 1 - '
                                            'December 31) during which the toxic chemical was manufactured, processed '
                                            'and/or otherwise used and released or otherwise managed as a waste.',
                          'STANDARDIZED_PARENT_COMPANY': 'A data field developed by EPA that is intended to best '
                                                         'reflect the current ultimate US parent company for the '
                                                         'facility.  EPA developed this field to facilitate the '
                                                         'aggregation of TRI facility-level information to the '
                                                         'associated parent company by ensuring that each company is '
                                                         'referenced consistently by the same name.  Filers often '
                                                         'submit names with small variations (e.g., Exopack vs. '
                                                         'Exopack Holdings Corp) that make aggregation at the '
                                                         'corporate level challenging when using parent names as '
                                                         'reported.  The standardized parent company field was '
                                                         'developed by standardizing the self-submitted parent company '
                                                         'names through a process described on the TRI website (e.g., '
                                                         'eliminating periods, standardizing common acronyms such as '
                                                         'Inc and Corp, etc.). The process also includes the '
                                                         'replacement of subsidiary names with the name of the '
                                                         'ultimate US parent in cases where EPA identified a '
                                                         'subsidiary in the submitted parent company field.',
                          'STATE_ABBR': 'The state abbreviation where the tribe is located.',
                          'STATE_COUNTY_FIPS_CODE': 'Combination of the two-letter state abbreviation and the county '
                                                    'code.',
                          'STREET_ADDRESS': 'The street address for the physical location of the facility or '
                                            'establishment.',
                          'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                             'program.  Usually, only one number is assigned to each facility and the '
                                             'number is for the entire facility.  One company may have multiple TRI '
                                             'Facility Identification (ID) numbers if they have multiple facilities.  '
                                             'One facility with many establishments will usually have only one TRI '
                                             'Facility ID number.  They will then use this number for all of their '
                                             'Form Rs even if they are submitting a Form R for different '
                                             'establishments with different names.  In a few instances different '
                                             'establishments of the same facility will have different TRI Facility ID '
                                             'numbers.  The format is ZZZZZNNNNNSSSSS, where ZZZZZ = ZIP code, NNNNN = '
                                             'the first 5 consonants of the name, and SSSSS = the first 5 non-blank '
                                             'non-special characters in the street address.',
                          'ZIP_CODE': 'The Zone Improvement Plan (ZIP) code assigned by the U.S. Postal Service as '
                                      'part of the address of a facility.'},
 'TRI_FACILITY_NPDES': {'ASGN_NPDES_IND': 'Indicates that the associated NPDES_NUM represents the principal NPDES '
                                          'permit number as assigned to the facility by TRI from Form R or Form A '
                                          "submissions.  Values: 1 = 'Yes', 0 = 'No'.",
                        'NPDES_NUM': 'The permit number of a specific discharge to a water body under the National '
                                     'Pollutant Discharge Elimination System (NPDES) of the Clean Water Act (CWA).  '
                                     'Not all facilities will have a NPDES permit number.  A facility may have '
                                     'multiple NPDES permit numbers.  The NPDES permit number may not pertain to the '
                                     'toxic chemical reported to TRI.',
                        'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                           'program.  Usually, only one number is assigned to each facility and the '
                                           'number is for the entire facility.  One company may have multiple TRI '
                                           'Facility Identification (ID) numbers if they have multiple facilities.  '
                                           'One facility with many establishments will usually have only one TRI '
                                           'Facility ID number.  They will then use this number for all of their Form '
                                           'Rs even if they are submitting a Form R for different establishments with '
                                           'different names.  In a few instances different establishments of the same '
                                           'facility will have different TRI Facility ID numbers.  The format is '
                                           'ZZZZZNNNNNSSSSS, where ZZZZZ = ZIP code, NNNNN = the first 5 consonants of '
                                           'the name, and SSSSS = the first 5 non-blank non-special characters in the '
                                           'street address.'},
 'TRI_FACILITY_NPDES_HISTORY': {'ASGN_NPDES_IND': 'Indicates that the associated NPDES_NUM represents the principal '
                                                  'NPDES permit number as assigned to the facility by TRI from Form R '
                                                  "or Form A submissions.  Values: 1 = 'Yes', 0 = 'No'.",
                                'NPDES_NUM': 'The permit number of a specific discharge to a water body under the '
                                             'National Pollutant Discharge Elimination System (NPDES) of the Clean '
                                             'Water Act (CWA).  Not all facilities will have a NPDES permit number.  A '
                                             'facility may have multiple NPDES permit numbers.  The NPDES permit '
                                             'number may not pertain to the toxic chemical reported to TRI.',
                                'REPORTING_YEAR': 'The year for which the form was submitted.  This is not the year in '
                                                  'which the form was filed but rather it is the calendar year '
                                                  '(January 1 - December 31) during which the toxic chemical was '
                                                  'manufactured, processed and/or otherwise used and released or '
                                                  'otherwise managed as a waste.',
                                'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the '
                                                   'TRI program.  Usually, only one number is assigned to each '
                                                   'facility and the number is for the entire facility.  One company '
                                                   'may have multiple TRI Facility Identification (ID) numbers if they '
                                                   'have multiple facilities.  One facility with many establishments '
                                                   'will usually have only one TRI Facility ID number.  They will then '
                                                   'use this number for all of their Form Rs even if they are '
                                                   'submitting a Form R for different establishments with different '
                                                   'names.  In a few instances different establishments of the same '
                                                   'facility will have different TRI Facility ID numbers.  The format '
                                                   'is ZZZZZNNNNNSSSSS, where ZZZZZ = ZIP code, NNNNN = the first 5 '
                                                   'consonants of the name, and SSSSS = the first 5 non-blank '
                                                   'non-special characters in the street address.'},
 'TRI_FACILITY_RCRA': {'ASGN_RCRA_IND': 'Indicates that the associated RCRA_NUM represents the principal RCRA '
                                        'Identification Number as assigned to the facility by TRI from Form R or Form '
                                        "A submissions.  Values: 1 = 'Yes', 0 = 'No'.",
                       'RCRA_NUM': 'The number assigned to the facility by EPA for purposes of the Resource '
                                   'Conservation and Recovery Act (RCRA).  Not all facilities will have a RCRA '
                                   'Identification Number.  A facility will only have a RCRA Identification Number if '
                                   'it manages RCRA regulated hazardous waste.  Some facilities may have more than one '
                                   'RCRA Identification Number.',
                       'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                          'program.  Usually, only one number is assigned to each facility and the '
                                          'number is for the entire facility.  One company may have multiple TRI '
                                          'Facility Identification (ID) numbers if they have multiple facilities.  One '
                                          'facility with many establishments will usually have only one TRI Facility '
                                          'ID number.  They will then use this number for all of their Form Rs even if '
                                          'they are submitting a Form R for different establishments with different '
                                          'names.  In a few instances different establishments of the same facility '
                                          'will have different TRI Facility ID numbers.  The format is '
                                          'ZZZZZNNNNNSSSSS, where ZZZZZ = ZIP code, NNNNN = the first 5 consonants of '
                                          'the name, and SSSSS = the first 5 non-blank non-special characters in the '
                                          'street address.'},
 'TRI_FACILITY_RCRA_HISTORY': {'ASGN_RCRA_IND': 'Indicates that the associated RCRA_NUM represents the principal RCRA '
                                                'Identification Number as assigned to the facility by TRI from Form R '
                                                "or Form A submissions.  Values: 1 = 'Yes', 0 = 'No'.",
                               'RCRA_NUM': 'The number assigned to the facility by EPA for purposes of the Resource '
                                           'Conservation and Recovery Act (RCRA).  Not all facilities will have a RCRA '
                                           'Identification Number.  A facility will only have a RCRA Identification '
                                           'Number if it manages RCRA regulated hazardous waste.  Some facilities may '
                                           'have more than one RCRA Identification Number.',
                               'REPORTING_YEAR': 'The year for which the form was submitted.  This is not the year in '
                                                 'which the form was filed but rather it is the calendar year (January '
                                                 '1 - December 31) during which the toxic chemical was manufactured, '
                                                 'processed and/or otherwise used and released or otherwise managed as '
                                                 'a waste.',
                               'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                                  'program.  Usually, only one number is assigned to each facility and '
                                                  'the number is for the entire facility.  One company may have '
                                                  'multiple TRI Facility Identification (ID) numbers if they have '
                                                  'multiple facilities.  One facility with many establishments will '
                                                  'usually have only one TRI Facility ID number.  They will then use '
                                                  'this number for all of their Form Rs even if they are submitting a '
                                                  'Form R for different establishments with different names.  In a few '
                                                  'instances different establishments of the same facility will have '
                                                  'different TRI Facility ID numbers.  The format is ZZZZZNNNNNSSSSS, '
                                                  'where ZZZZZ = ZIP code, NNNNN = the first 5 consonants of the name, '
                                                  'and SSSSS = the first 5 non-blank non-special characters in the '
                                                  'street address.'},
 'TRI_FACILITY_SIC': {'PRIMARY_IND': "Indicates whether the associated SIC_CODE/NAICS_CODE represents the facility's "
                                     'primary business activity as entered by the submitter. EPA instructs facilities '
                                     'to enter their primary SIC/NAICS  on the Form R or Form A in part I, section '
                                     "4.5, box a. Values: 1 = 'Yes', 0 = 'No'.",
                      'SIC_CODE': 'The Standard Industrial Classification (SIC) code or codes which best describes the '
                                  'activities conducted at the facility.  SIC codes are 4 digit numbers used by the '
                                  'Bureau of Census as part of a system to categorize and track the types of business '
                                  'activities conducted in the United States.  The first two digits of the code '
                                  'represent the major industry group (e.g., SIC code 25XX indicates Furniture and '
                                  'Fixtures) and the second two digits represent the specific subset of that group '
                                  '(e.g., 2511 indicates wood household furniture).  EPA instructs facilities to enter '
                                  'their primary SIC code first.  Many facilities do not report their primary SIC code '
                                  'first.',
                      'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                         'program.  Usually, only one number is assigned to each facility and the '
                                         'number is for the entire facility.  One company may have multiple TRI '
                                         'Facility Identification (ID) numbers if they have multiple facilities.  One '
                                         'facility with many establishments will usually have only one TRI Facility ID '
                                         'number.  They will then use this number for all of their Form Rs even if '
                                         'they are submitting a Form R for different establishments with different '
                                         'names.  In a few instances different establishments of the same facility '
                                         'will have different TRI Facility ID numbers.  The format is ZZZZZNNNNNSSSSS, '
                                         'where ZZZZZ = ZIP code, NNNNN = the first 5 consonants of the name, and '
                                         'SSSSS = the first 5 non-blank non-special characters in the street address.'},
 'TRI_FACILITY_SIC_HISTORY': {'PRIMARY_IND': 'Indicates whether the associated SIC_CODE/NAICS_CODE represents the '
                                             "facility's primary business activity as entered by the submitter. EPA "
                                             'instructs facilities to enter their primary SIC/NAICS  on the Form R or '
                                             "Form A in part I, section 4.5, box a. Values: 1 = 'Yes', 0 = 'No'.",
                              'REPORTING_YEAR': 'The year for which the form was submitted.  This is not the year in '
                                                'which the form was filed but rather it is the calendar year (January '
                                                '1 - December 31) during which the toxic chemical was manufactured, '
                                                'processed and/or otherwise used and released or otherwise managed as '
                                                'a waste.',
                              'SIC_CODE': 'The Standard Industrial Classification (SIC) code or codes which best '
                                          'describes the activities conducted at the facility.  SIC codes are 4 digit '
                                          'numbers used by the Bureau of Census as part of a system to categorize and '
                                          'track the types of business activities conducted in the United States.  The '
                                          'first two digits of the code represent the major industry group (e.g., SIC '
                                          'code 25XX indicates Furniture and Fixtures) and the second two digits '
                                          'represent the specific subset of that group (e.g., 2511 indicates wood '
                                          'household furniture).  EPA instructs facilities to enter their primary SIC '
                                          'code first.  Many facilities do not report their primary SIC code first.',
                              'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                                 'program.  Usually, only one number is assigned to each facility and '
                                                 'the number is for the entire facility.  One company may have '
                                                 'multiple TRI Facility Identification (ID) numbers if they have '
                                                 'multiple facilities.  One facility with many establishments will '
                                                 'usually have only one TRI Facility ID number.  They will then use '
                                                 'this number for all of their Form Rs even if they are submitting a '
                                                 'Form R for different establishments with different names.  In a few '
                                                 'instances different establishments of the same facility will have '
                                                 'different TRI Facility ID numbers.  The format is ZZZZZNNNNNSSSSS, '
                                                 'where ZZZZZ = ZIP code, NNNNN = the first 5 consonants of the name, '
                                                 'and SSSSS = the first 5 non-blank non-special characters in the '
                                                 'street address.'},
 'TRI_FACILITY_UIC': {'ASGN_UIC_IND': 'Indicates that the associated UIC_NUM represents the principal underground '
                                      'injection code identification number (UIC ID) as assigned to the facility by '
                                      "TRI from Form R or Form A submissions.  Values: 1 = 'Yes', 0 = 'No'.",
                      'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                         'program.  Usually, only one number is assigned to each facility and the '
                                         'number is for the entire facility.  One company may have multiple TRI '
                                         'Facility Identification (ID) numbers if they have multiple facilities.  One '
                                         'facility with many establishments will usually have only one TRI Facility ID '
                                         'number.  They will then use this number for all of their Form Rs even if '
                                         'they are submitting a Form R for different establishments with different '
                                         'names.  In a few instances different establishments of the same facility '
                                         'will have different TRI Facility ID numbers.  The format is ZZZZZNNNNNSSSSS, '
                                         'where ZZZZZ = ZIP code, NNNNN = the first 5 consonants of the name, and '
                                         'SSSSS = the first 5 non-blank non-special characters in the street address.',
                      'UIC_NUM': 'The unique number assigned to a specific underground injection well under the Safe '
                                 'Drinking Water Act (SDWA).  A facility with multiple injection wells will have '
                                 'multiple underground injection code identification number (UIC ID) Numbers.  If the '
                                 'facility does not have an underground injection well regulated by the SDWA, it will '
                                 'not have a UIC ID number.'},
 'TRI_FACILITY_UIC_HISTORY': {'ASGN_UIC_IND': 'Indicates that the associated UIC_NUM represents the principal '
                                              'underground injection code identification number (UIC ID) as assigned '
                                              'to the facility by TRI from Form R or Form A submissions.  Values: 1 = '
                                              "'Yes', 0 = 'No'.",
                              'REPORTING_YEAR': 'The year for which the form was submitted.  This is not the year in '
                                                'which the form was filed but rather it is the calendar year (January '
                                                '1 - December 31) during which the toxic chemical was manufactured, '
                                                'processed and/or otherwise used and released or otherwise managed as '
                                                'a waste.',
                              'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                                 'program.  Usually, only one number is assigned to each facility and '
                                                 'the number is for the entire facility.  One company may have '
                                                 'multiple TRI Facility Identification (ID) numbers if they have '
                                                 'multiple facilities.  One facility with many establishments will '
                                                 'usually have only one TRI Facility ID number.  They will then use '
                                                 'this number for all of their Form Rs even if they are submitting a '
                                                 'Form R for different establishments with different names.  In a few '
                                                 'instances different establishments of the same facility will have '
                                                 'different TRI Facility ID numbers.  The format is ZZZZZNNNNNSSSSS, '
                                                 'where ZZZZZ = ZIP code, NNNNN = the first 5 consonants of the name, '
                                                 'and SSSSS = the first 5 non-blank non-special characters in the '
                                                 'street address.',
                              'UIC_NUM': 'The unique number assigned to a specific underground injection well under '
                                         'the Safe Drinking Water Act (SDWA).  A facility with multiple injection '
                                         'wells will have multiple underground injection code identification number '
                                         '(UIC ID) Numbers.  If the facility does not have an underground injection '
                                         'well regulated by the SDWA, it will not have a UIC ID number.'},
 'TRI_FORM_R_SCHEDULE_ONE': {'CALCULATED_TEQ': 'Calculated total Toxic Equivalents or TEQ on Form R Schedule 1.',
                             'DIOXIN_CONGENER1': 'Gram data for compound 1- 2,3,7,8-Tetrachlorodibenzo-p-dioxin, in an '
                                                 'Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER10': 'Gram data for compound 10- 2,3,4,7,8-Pentachlorodibenzofuran, in an '
                                                  'Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER11': 'Gram data for compound 11- 1,2,3,4,7,8-Hexachlorodibenzofuran, in '
                                                  'an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER12': 'Gram data for compound 12- 1,2,3,6,7,8-Hexachlorodibenzofuran, in '
                                                  'an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER13': 'Gram data for compound 13- 1,2,3,7,8,9-Hexachlorodibenzofuran, in '
                                                  'an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER14': 'Gram data for compound 14- 2,3,4,6,7,8-Hexachlorodibenzofuran, in '
                                                  'an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER15': 'Gram data for compound 15- 1,2,3,4,6,7,8-Heptachlorodibenzofuran, '
                                                  'in an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER16': 'Gram data for compound 16- 1,2,3,4,7,8,9-Heptachlorodibenzofuran, '
                                                  'in an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER17': 'Gram data for compound 17- 1,2,3,4,6,7,8,9-Octachlorodibenzofuran, '
                                                  'in an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER2': 'Gram data for compound 2- 1,2,3,7,8-Pentachlorodibenzo-p-dioxin, in '
                                                 'an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER3': 'Gram data for compound 3- 1,2,3,4,7,8-Hexachlorodibenzo-p-dioxin, in '
                                                 'an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER4': 'Gram data for compound 4- 1,2,3,6,7,8-Hexachlorodibenzo-p-dioxin, in '
                                                 'an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER5': 'Gram data for compound 5- 1,2,3,7,8,9-Hexachlorodibenzo-p-dioxin, in '
                                                 'an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER6': 'Gram data for compound 6- 1,2,3,4,6,7,8-Heptachlorodibenzo-p-dioxin, '
                                                 'in an Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER7': 'Gram data for compound 7- '
                                                 '1,2,3,4,6,7,8,9-Octachlorodibenzo-p-dioxin, in an Environmental '
                                                 'Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER8': 'Gram data for compound 8- 2,3,7,8-Tetrachlorodibenzofuran, in an '
                                                 'Environmental Medium category reported on Form R Schedule 1.',
                             'DIOXIN_CONGENER9': 'Gram data for compound 9- 1,2,3,7,8-Pentachlorodibenzofuran, in an '
                                                 'Environmental Medium category reported on Form R Schedule 1.',
                             'SEQUENCE_NUM': 'Sequential value for repeating items gram data for each of the 17 '
                                             'compounds reported on Form R Schedule 1.'},
 'TRI_OFF_SITE_TRANSFER_LOCATION': {'CITY_NAME': 'The city where the facility or establishment is physically located.',
                                    'CONTROLLED_LOC': 'Indicator that shows whether the off-site location to which '
                                                      'toxic chemicals are transferred in wastes is owned or '
                                                      'controlled by the facility or the parent company.  Values: 1 = '
                                                      "'Yes', 0 = 'No', 2 = blank or not entered.",
                                    'COUNTRY_CODE': 'The country code where the entity receiving the toxic chemical is '
                                                    'located.',
                                    'COUNTY_NAME': 'The standardized name of the county where the facility is located.',
                                    'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each '
                                                    'submission.  The format is TTYYNNNNNNNNN, where TT = document '
                                                    'type, YY = reporting year, and NNNNNNNNN = assigned number with a '
                                                    'check digit.',
                                    'EPA_REGISTRY_ID': 'Indicates the Facility Registry Service (FRS) id for a TRI '
                                                       'Facility, POTW Facility or Off-site Transfer Location '
                                                       'facility.  The Facility Registry Service (FRS) is a centrally '
                                                       'managed database at EPA that identifies facilities, sites or '
                                                       'places subject to environmental regulations or of '
                                                       'environmental interest.  Using the FRS Id (EPA_REGISTRY_ID), '
                                                       'data users can link data from different EPA programs '
                                                       'together.    See the Facility Registry Service at',
                                    'OFF_SITE_NAME': 'The name of the entity receiving the toxic chemical.',
                                    'OFF_SITE_STREET_ADDRESS': 'The street address for the physical location of the '
                                                               'entity receiving the toxic chemical.',
                                    'PROVINCE': 'The province of the location to which the toxic chemical in wastes is '
                                                'transferred.  A facility may transfer toxic chemicals in waste to '
                                                'off-site locations that are outside of the United States. The '
                                                'province field gives a facility the flexibility needed to enter a '
                                                'correct off-site location address that is outside the United States.',
                                    'RCRA_NUM': 'The number assigned to the facility by EPA for purposes of the '
                                                'Resource Conservation and Recovery Act (RCRA).  Not all facilities '
                                                'will have a RCRA Identification Number.  A facility will only have a '
                                                'RCRA Identification Number if it manages RCRA regulated hazardous '
                                                'waste.  Some facilities may have more than one RCRA Identification '
                                                'Number.',
                                    'STATE_ABBR': 'The state abbreviation where the tribe is located.',
                                    'TRANSFER_LOC_NUM': 'The sequence in which an off-site transfer is reported on a '
                                                        'Form R submission.',
                                    'ZIP_CODE': 'The Zone Improvement Plan (ZIP) code assigned by the U.S. Postal '
                                                'Service as part of the address of a facility.'},
 'TRI_ONSITE_WASTESTREAM': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each '
                                            'submission.  The format is TTYYNNNNNNNNN, where TT = document type, YY = '
                                            'reporting year, and NNNNNNNNN = assigned number with a check digit.',
                            'EFFICIENCY_RANGE_CODE': 'The range code representing the percentage of the toxic      '
                                                     'chemical removed from the waste stream through destruction, '
                                                     'biological degradation,      chemical conversion, or physical '
                                                     'removal. This range code represents the      overall percentage '
                                                     'of the toxic chemical destroyed or removed (based on      amount '
                                                     'or mass) throughout all waste management methods, not merely '
                                                     'changes      in volume or concentration and not merely the '
                                                     'efficiency of one method in      a sequence of activities. This '
                                                     'also does not represent the waste treatment      efficiency for '
                                                     'the entire waste stream but only the removal or destruction      '
                                                     'of this specific toxic chemical in that waste stream. This does '
                                                     'not include      energy recovery or recycling activities. Energy '
                                                     'recovery and recycling activities      are reported in sections '
                                                     '7B and 7C, respectively.',
                            'INFLUENT_CONC_RANGE': 'Indicates the range of concentration of the toxic chemical in the '
                                                   'waste stream as it typically enters the waste treatment step or '
                                                   'sequence.  The concentration is based on the amount or mass of the '
                                                   'toxic chemical in the waste stream as compared to the total amount '
                                                   'or mass of the waste stream and is determined prior to the '
                                                   'application of any waste management methods.  Facilities report '
                                                   'using one of the following five codes:',
                            'OPERATING_DATA_IND': 'Indicates if the waste treatment efficiency estimate '
                                                  '(TREATMENT_EFFCIENCY_EST) is based on actual operating data, such '
                                                  'as monitoring influent and effluent toxic chemical levels in the '
                                                  'waste stream;  or, indicates if TREATMENT_EFFCIENCY_EST is not '
                                                  'based on actual operating or monitoring data, but rather some other '
                                                  'technique, such as published data for similar processes or the '
                                                  "equipment supplier's literature.   Values: 1 = 'Yes', 0 = 'No'', 2 "
                                                  '= blank or not entered.',
                            'SEQUENTIAL_TREAT_87_90': 'Indicator that shows whether treatment steps were used in '
                                                      'sequence, for Reporting Years 1987 through 1990, to estimate '
                                                      'treatment efficiency of the overall treatment process.',
                            'TREATMENT_EFFICIENCY_EST': 'The percentage of the toxic chemical removed from the waste '
                                                        'stream through destruction, biological degradation, chemical '
                                                        'conversion, or physical removal.  This estimate represents '
                                                        'the overall percentage of the toxic chemical destroyed or '
                                                        'removed (based on amount or mass) throughout all waste '
                                                        'management methods, not merely changes in volume or '
                                                        'concentration and not merely the efficiency of one method in '
                                                        'a sequence of activities.  This also does not represent the '
                                                        'waste treatment efficiency for the entire waste stream but '
                                                        'only the removal or destruction of this specific toxic '
                                                        'chemical in that waste stream.  This does not include energy '
                                                        'recovery or recycling activities. Energy recovery and '
                                                        'recycling activities are reported in sections 7B and 7C, '
                                                        'respectively.  The value is calculated as follows:  ((I - '
                                                        'E)/1) * 100, where I equals the amount of toxic chemical in '
                                                        'the influent waste stream, and E equals the amount of the '
                                                        'toxic chemical in the effluent waste stream.',
                            'TREATMENT_EFFICIENCY_EST_NA': "Indicates whether 'NA' (Not Applicable) was entered on "
                                                           'Form R for the waste treatment efficiency estimate.  '
                                                           "Values: 1 = 'Yes', 0 = 'No'.",
                            'WASTESTREAM_CODE': 'Indicates the general waste stream type containing the toxic '
                                                'chemical.  The four codes used to indicate the general waste stream '
                                                'types are:  A = Gaseous (gases, vapors, airborne particles), W = '
                                                'Wastewater (aqueous waste),  L = Liquid (non-aqueous, liquid waste), '
                                                'and S = Solid (including sludges and slurries).',
                            'WASTESTREAM_SEQ_NUM': 'Sequence in which an on-site waste treatment process is reported '
                                                   'on a Form R submission.'},
 'TRI_ONSITE_WASTE_TREATMENT_MET': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each '
                                                    'submission.  The format is TTYYNNNNNNNNN, where TT = document '
                                                    'type, YY = reporting year, and NNNNNNNNN = assigned number with a '
                                                    'check digit.',
                                    'TREATMENT_METHOD_CODE': 'The on-site waste treatment activity that is applied to '
                                                             'the waste stream containing the toxic chemical.  This '
                                                             'includes all waste treatment methods through which the '
                                                             'toxic chemical passes as part of that waste stream, '
                                                             'regardless of whether or not the method has, or is '
                                                             'intended to have, any effect on the toxic chemical.  If '
                                                             'the waste stream moves through a series of waste '
                                                             'treatment activities, each method will be listed '
                                                             'sequentially.',
                                    'TREATMENT_SEQUENCE': 'Sequence in which a TREATMENT_METHOD_CODE is entered on a '
                                                          'Form R submission, and indicates the on-site order of '
                                                          'treatment.',
                                    'WASTESTREAM_SEQ_NUM': 'Sequence in which an on-site waste treatment process is '
                                                           'reported on a Form R submission.'},
 'TRI_POTW_LOCATION': {'CITY_NAME': 'The city where the facility or establishment is physically located.',
                       'COUNTY_NAME': 'The standardized name of the county where the facility is located.',
                       'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each submission.  '
                                       'The format is TTYYNNNNNNNNN, where TT = document type, YY = reporting year, '
                                       'and NNNNNNNNN = assigned number with a check digit.',
                       'EPA_REGISTRY_ID': 'Indicates the Facility Registry Service (FRS) id for a TRI Facility, POTW '
                                          'Facility or Off-site Transfer Location facility.  The Facility Registry '
                                          'Service (FRS) is a centrally managed database at EPA that identifies '
                                          'facilities, sites or places subject to environmental regulations or of '
                                          'environmental interest.  Using the FRS Id (EPA_REGISTRY_ID), data users can '
                                          'link data from different EPA programs together.    See the Facility '
                                          'Registry Service at',
                       'POTW_LOC_NUM': 'The sequence in which an POTW transfer is reported on a Form R submission.',
                       'POTW_NAME': 'The name of the publicly owned treatment works (POTW) receiving the toxic '
                                    'chemical.',
                       'POTW_STREET_ADDRESS': 'The street address for the physical location of the publicly owned '
                                              'treatment works (POTW) receiving the toxic chemical.',
                       'STATE_ABBR': 'The state abbreviation where the tribe is located.',
                       'ZIP_CODE': 'The Zone Improvement Plan (ZIP) code assigned by the U.S. Postal Service as part '
                                   'of the address of a facility.'},
 'TRI_RECYCLING_PROCESS': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each '
                                           'submission.  The format is TTYYNNNNNNNNN, where TT = document type, YY = '
                                           'reporting year, and NNNNNNNNN = assigned number with a check digit.',
                           'ONSITE_RECYCLING_PROC_CODE': 'Indicates the specific on-site recycling method or methods '
                                                         'applied to the toxic chemical.  Similar to section 7B and '
                                                         'unlike section 7A, on-site recycling under section 7C refers '
                                                         'only to recycling activities directed at the specific toxic '
                                                         'chemical being reported, not all recycling methods applied '
                                                         'to the waste stream.  Section 7C is not completed unless the '
                                                         'specific toxic chemical being reported is recovered from the '
                                                         'waste stream for reuse.'},
 'TRI_RELEASE_QTY': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each submission.  The '
                                     'format is TTYYNNNNNNNNN, where TT = document type, YY = reporting year, and '
                                     'NNNNNNNNN = assigned number with a check digit.',
                     'ENVIRONMENTAL_MEDIUM': 'Code indicating the environmental medium to which the toxic chemical is '
                                             'released from the facility.',
                     'RELEASE_BASIS_EST_CODE': 'The code representing the technique used to develop theestimate of '
                                               "releases reported in the 'Total Release' box (TOTAL_RELEASE). The "
                                               'values are as follows:',
                     'RELEASE_NA': "Indicates whether 'NA' (Not Applicable) was entered on Form R for the release "
                                   "estimate.  Values: 1 = 'Yes', 0 = 'No'.  Descriptions by Form R Section number for "
                                   'each environmental medium follow.',
                     'RELEASE_RANGE_CODE': 'The code that corresponds to the amount of toxic chemical released '
                                           'annually by the reporting facility, reported as a range for releases less '
                                           'than 1,000 pounds.  When a facility uses a range code, the amount reported '
                                           'to TRI is the midpoint of the range.  On Form R, letter codes are used to '
                                           'represent ranges:  A = 1-10 pounds, B = 11-499 pounds, and C = 500-999 '
                                           'pounds.  The letters are converted to numbers for storage in the TRIS  '
                                           "database where  '1' represents range 'A', '3' represents range 'B',and '4' "
                                           "represents range 'C'.  The historical value '2' = 1-499 pounds.",
                     'TOTAL_RELEASE': 'The total amount (in pounds) of the toxic chemical released to air, water, '
                                      'land, and underground injection wells during the calendar year (January 1 - '
                                      'December 31).  Release amounts may be reported as specific numbers or as ranges '
                                      '(RELEASE_RANGE_CODE).  Descriptions by Form R Section number for each '
                                      'environmental medium follow.',
                     'WATER_SEQUENCE_NUM': 'Sequence in which a release to water is reported on a Form R submission.'},
 'TRI_REPORTING_FORM': {'ACTIVE_STATUS': "Indicates the status of the submitted Form R.  Value: 1 = 'Active "
                                         "submission'.",
                        'ADDITIONAL_DATA_IND': 'For reporting years beginning in 1991, the indicator that shows '
                                               'whether additional optional information on source reduction, pollution '
                                               'control, or recycling activities implemented during the reporting year '
                                               'or prior years has been attached to the submission.  For reporting '
                                               'years 1987 through 1990, the indicator shows whether waste '
                                               'minimization data was reported on Form R and has since been archived.  '
                                               "Values: 1 = 'Yes', 0 = 'No'', 2 = blank or not entered.",
                        'CAS_CHEM_NAME': 'The official name of the toxic chemical, toxic chemical mixture,  (e.g., '
                                         'xylene mixed isomers), or chemical category as it appears on the EPCRA '
                                         'Section 313 list. ) or 2.1 .  This space will be empty if a trade secret was '
                                         'claimed for the toxic chemical and information is provided in Section 1.3 '
                                         '(MIXTURE_NAME) or 2.1 (GENERIC_CHEM_NAME).',
                        'CERTIF_DATE_SIGNED': 'The date that the senior management official signed the certification '
                                              'statement.',
                        'CERTIF_NAME': 'The name of the owner, operator, or senior management official who is '
                                       'certifying that the information provided is true and complete and that the '
                                       'values reported are accurate based on reasonable estimates.  This individual '
                                       'has management responsibility for the person or persons completing the report.',
                        'CERTIF_OFFICIAL_TITLE': 'The title of the owner, operator, or senior management official who '
                                                 'is certifying that the information provided is true and complete and '
                                                 'that the values reported are accurate based on reasonable '
                                                 'estimates.  This individual has management responsibility for the '
                                                 'person or persons completing the report.',
                        'CERTIF_SIGNATURE': 'Indicator for the signature of the individual who is certifying that the '
                                            'information being provided in the form is true and complete and that the '
                                            'values reported are accurate based on reasonable estimates.',
                        'DIOXIN_DISTRIBUTION_1': 'Indicates the distribution (percentage) of '
                                                 '1,2,3,4,6,7,8-Heptachlorodibenzofuran (CAS Number: 67562-39-4) in '
                                                 'the reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_10': 'Indicates the distribution (percentage) of '
                                                  '1,2,3,4,6,7,8-Hexachlorodibenzo-p-dioxin (CAS Number: 35822-46-9) '
                                                  'in the reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_11': 'Indicates the distribution (percentage) of '
                                                  '1,2,3,4,6,7,8,9-Octachlorodibenzofuran (CAS Number: 39001-02-0) in '
                                                  'the reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_12': 'Indicates the distribution (percentage) of '
                                                  '1,2,3,4,6,7,8,9-Octachlorodibenzo-p-dioxin (CAS Number: 03268-87-9) '
                                                  'in the reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_13': 'Indicates the distribution (percentage) of '
                                                  '1,2,3,7,8-Pentachlorodibenzofuran (CAS Number: 57117-41-6) in the '
                                                  'reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_14': 'Indicates the distribution (percentage) of '
                                                  '2,3,4,7,8-Pentachlorodibenzofuran (CAS Number: 57117-31-4) in the '
                                                  'reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_15': 'Indicates the distribution (percentage) of '
                                                  '1,2,3,7,8-Pentachlorodibenzo-p-dioxin (CAS Number: 40321-76-4) in '
                                                  'the reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_16': 'Indicates the distribution (percentage) of '
                                                  '2,3,7,8-Tetrachlorodibenzofuran (CAS Number: 51207-31-9) in the '
                                                  'reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_17': 'Indicates the distribution (percentage) of '
                                                  '2,3,7,8-Tetrachlorodibenzo-p-dioxin (CAS Number: 01746-01-6) in the '
                                                  'reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_2': 'Indicates the distribution (percentage) of '
                                                 '1,2,3,4,7,8,9-Heptachlorodibenzofuran (CAS Number: 55673-89-7) in '
                                                 'the reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_3': 'Indicates the distribution (percentage) of '
                                                 '1,2,3,4,7,8-Hexachlorodibenzofuran (CAS Number: 70648-26-9) in the '
                                                 'reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_4': 'Indicates the distribution (percentage) of '
                                                 '1,2,3,6,7,8-Hextachlorodibenzofuran (CAS Number: 57117-44-9) in the '
                                                 'reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_5': 'Indicates the distribution (percentage) of '
                                                 '1,2,3,7,8,9-Hexachlorodibenzofuran (CAS Number: 72918-21-9) in the '
                                                 'reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_6': 'Indicates the distribution (percentage) of '
                                                 '2,3,4,6,7,8-Hexachlorodibenzofuran (CAS Number: 60851-34-5) in the '
                                                 'reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_7': 'Indicates the distribution (percentage) of '
                                                 '1,2,3,4,7,8-Hexachlorodibenzo-p-dioxin (CAS Number: 39227-28-6) in '
                                                 'the reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_8': 'Indicates the distribution (percentage) of '
                                                 '1,2,3,6,7,8-Hexachlorodibenzo-p-dioxin (CAS Number: 57653-85-7) in '
                                                 'the reported dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_9': 'Indicates the distribution (percentage) of '
                                                 '1,2,3,7,8,9-Hexachlorodibenzo-p-dioxin (CAS Number: 19408-74-3) in '
                                                 'the reported  dioxin or dioxin-like compounds.',
                        'DIOXIN_DISTRIBUTION_NA': "Indicates whether 'NA' (Not Applicable) was entered on the Form R "
                                                  'for the Distribution of Each Member of the Dioxin and Dioxin-like '
                                                  'Compounds Category.   The Form R asks facilities to report a '
                                                  'distribution of chemicals included in the Dioxin and Dioxin-like '
                                                  'compounds category.  There are 17 individual chemicals listed in '
                                                  "the Dioxin and Dioxin-like compounds category.  A value of '1' for "
                                                  'this variable indicates that the facility did not have the '
                                                  'speciation (distribution) information available.',
                        'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each submission.  '
                                        'The format is TTYYNNNNNNNNN, where TT = document type, YY = reporting year, '
                                        'and NNNNNNNNN = assigned number with a check digit.',
                        'ELEMENTAL_METAL_INCLUDED': 'Is a flag that indicates when release and management data for a '
                                                    'metal compound (i.e. Lead compounds) have been reported in '
                                                    'combination with the data for the corresponding elemental metal '
                                                    '(i.e. Lead).  An option was added in reporting year (RY) 2018 to '
                                                    'the TRI Form R that allows facilities to submit a combined report '
                                                    'for a metal compound and the corresponding elemental metal '
                                                    'provided they are both (individually) above reporting '
                                                    'thresholds.  For example, a facility could report their releases '
                                                    'and other waste manage for both Copper compounds and Copper on '
                                                    'one form R given both were individually above the reporting '
                                                    'thresholds. This data element, Elemental_Metal_Included, '
                                                    "indicates when that has happened.  A value of 'Y' indicates the "
                                                    'Form R report contains combined data for a metal compound (i.e. '
                                                    'Mercury Compounds) and the corresponding elemental metal (i.e. '
                                                    'Mercury).',
                        'ENTIRE_FAC': 'Indicates that only one Form R was filed for this chemical for the entire '
                                      "facility.  Values:  1 = Form R 'Entire' box check, 0 = box not checked.",
                        'FEDERAL_FAC_IND': "Indicates whether the 'Federal' box was checked on the submission.  A "
                                           'Federal facility is a facility owned or operated by the Federal '
                                           'government.  This includes facilities that are operated by contractors to '
                                           'the Federal government (i.e., a facility where the land is owned by the '
                                           'Federal government but a private company is under contract to run the '
                                           "facility's operations).  The types of Federal facilities that report to "
                                           'TRI are broader than the types of private sector facilities that report to '
                                           'TRI (e.g., DOD military bases).  Values:  1 =  box checked, 0 = box not '
                                           'checked.',
                        'FORM_TYPE_IND': 'Indicates the type of form received.  Values:  L = Form R, S = Form A.',
                        'GENERIC_CHEM_NAME': 'The generic, structurally descriptive term used in place of the toxic '
                                             'chemical name when a trade secret was claimed for the toxic chemical.  '
                                             'The name must appear on both sanitized and unsanitized Form Rs and be '
                                             'the same as that used on the substantiation form.  Section 1.3 will be '
                                             "'NA' or blank if information is provided in Sections 1.1 (TRI_CHEM_ID) "
                                             'and 1.2 (CAS_CHEM_NAME), or 2.1 (MIXTURE_NAME).  Note: Only Sanitized '
                                             'Trade Secret submissions are stored in the TRIS database.',
                        'GOCO_FLAG': "Indicates whether the 'GOCO' box was checked on the submission.   A GOCO "
                                     'facility is a Government-Owned, Contractor-Operated facility.   Values: 1= box '
                                     'checked, 0= box not checked.',
                        'MAX_AMOUNT_OF_CHEM': 'The two digit code indicating a range for the maximum amount of the '
                                              'chemical present at the facility at any one time during the calendar '
                                              'year (January 1 - December 31) for which the report was submitted.',
                        'MEDIA_TYPE': 'Indicates which media type the form was submitted on.',
                        'MIXTURE_NAME': 'The generic term used in place of the toxic chemical name when a trade secret '
                                        'was claimed for the toxic chemical by the supplier of the toxic chemical.  '
                                        'This is generally used when the supplier of a chemical formulation wishes to '
                                        'keep the identity of a particular ingredient in the formulation a secret.  It '
                                        'is only used when the supplier, not the reporting facility, is claiming the '
                                        'trade secret.  If the reporting facility is claiming a trade secret for the '
                                        'toxic chemical, the generic name is provided in Section 1.3 '
                                        '(GENERIC_CHEM_NAME) and this section (MIXTURE_NAME) is left blank.  This '
                                        'space will also be left blank if a trade secret is not being claimed for the '
                                        'toxic chemical.',
                        'ONE_TIME_RELEASE_QTY': 'The total amount (in pounds) of the toxic chemical released directly '
                                                'to the environment or sent offsite for recycling, energy recovery, '
                                                'treatment, or disposal during the reporting year due to remedial '
                                                'actions, catastrophic events such as earthquakes or floods, and '
                                                'one-time events not associated with normal or routine production '
                                                'processes.  These amounts are not included in the amounts reported in '
                                                'sections 8.1-8.7 (TRI_SOURCE_REDUCTION_QTY).',
                        'ONE_TIME_RELEASE_QTY_NA': "Indicator that shows whether 'NA' was entered in Section 8.8, "
                                                   'Quantity Released to the Environment as Result of Remedial '
                                                   'Actions, Catastrophic Events, or One-Time Events Not Associated '
                                                   'with Production Process (ONE_TIME_RELEASE_QTY).   Values: 1 = '
                                                   "'Yes', 0 = 'No'.",
                        'ORIG_POSTMARK': 'The original postmark date for a submission for this chemical from this '
                                         'facility and this reporting year.',
                        'ORIG_RECEIVED': 'The original received date for a submission for this chemical from this '
                                         'facility and this reporting year.',
                        'PARTIAL_FAC': 'Indicates that the facility has chosen to report by establishment or groups of '
                                       'establishments.  Therefore, there may be other reports filed for this chemical '
                                       "by other establishments of the facility.Values:  1 = Form R 'Partial' box "
                                       'checked, 0 = box not checked.',
                        'POSTMARK_DATE': 'The most recent postmark date for a submission for this chemical from this '
                                         'facility and this reporting year .  The date may represent a revised '
                                         'submission or be the same as the ORIG_POSTMARK.',
                        'PRODUCTION_RATIO': 'Indicates the level of increase or decrease from the previous year, of '
                                            'the production process or other activity in which the toxic chemical is '
                                            'used.  This number is usually  around 1.0.  For example, a production '
                                            'ratio or activity index of 1.5 would indicate that production associated '
                                            'with the use of the toxic chemical has increased by about 50 percent.  '
                                            'Conversely, a production ratio or activity index of 0.3 would indicate '
                                            'that production associated with the use of the toxic chemical has '
                                            'decreased by about 70 percent.',
                        'PRODUCTION_RATIO_NA': "Indicator that shows whether 'NA' was entered in Section 8.9, "
                                               'Production Ratio or Activity Index (PRODUCTION_RATIO).  Values: 1 = '
                                               "'Yes', 0 = 'No'.",
                        'PROD_RATIO_OR_ACTIVITY': 'The production or activity ratio is a flag that indicates whether '
                                                  'a  facility reported a production or activity ratio as a measure of '
                                                  'their year  to year output.   The two possible values for this data '
                                                  'element are "PRODUCTION"  or "ACTIVITY".  The Produciton or '
                                                  'Activity Ratio value is set when a   faciity chooses either the '
                                                  '""Production"" or ""Activity"" check box in Part II,   Section 8.9 '
                                                  'of the TRI Form R.',
                        'PUBLIC_CONTACT_EMAIL': '',
                        'PUBLIC_CONTACT_PERSON': 'The name of the individual who may be contacted by the general '
                                                 'public with questions regarding the information reported to TRI on '
                                                 'this chemical.  This person may or may not be familiar with the '
                                                 'information provided in the form but has been designated by the '
                                                 'facility or establishment to handle public inquiries.',
                        'PUBLIC_CONTACT_PHONE': 'The phone number to reach the person identified in the Public Contact '
                                                'Name box (PUBLIC_CONTACT_PERSON).',
                        'PUBLIC_PHONE_EXT': 'The telephone extension of the Public Contact Person as reported on the '
                                            'form R.',
                        'RECEIVED_DATE': 'The date the submission was received at the EPCRA Reporting Center.',
                        'REPORTING_YEAR': 'The year for which the form was submitted.  This is not the year in which '
                                          'the form was filed but rather it is the calendar year (January 1 - December '
                                          '31) during which the toxic chemical was manufactured, processed and/or '
                                          'otherwise used and released or otherwise managed as a waste.',
                        'REVISION_NA': "Indicator that shows whether the submission 'Revision' box on form R was "
                                       'checked by the submitter.   Values:  1 =  box checked, 0 = box not checked.',
                        'SANITIZED_IND': "Indicator that shows whether the submission 'Sanitized Trade Secret'  box "
                                         'was checked by the submitter.  Note: Only Sanitized Trade Secret submissions '
                                         'are stored in the TRIS database.   Values:  1 =  box checked, 0 = box not '
                                         'checked.',
                        'TRADE_SECRET_IND': 'Indicator that shows whether the identity of the toxic chemical has been '
                                            'claimed a trade secret.  If the facility has indicated that the chemical '
                                            'name is a trade secret, the chemical name will not be released to the '
                                            "public.   Values:  1 =  'Trade Secret' box checked, 0 =  'Trade Secret' "
                                            'box not checked.',
                        'TRI_CHEM_ID': 'The number assigned to chemicals regulated under Section 313 of the Emergency '
                                       'Planning and Community Right-to-Know Act (EPCRA). For most toxic chemicals or '
                                       'mixture of chemicals (e.g., xylene mixed isomers), the TRI_CHEM_ID is the '
                                       'Chemical Abstract Service Registry (CAS) number.  A given listed toxic '
                                       'chemical or mixture may be known by many names but it will have only one CAS '
                                       'number.  For example, methyl ethyl ketone and 2-butanone are synonyms for the '
                                       'same toxic chemical and thus have only one CAS number (78-93-3).  For '
                                       'categories of chemicals for which CAS Registry numbers have not been assigned, '
                                       'a four-character category code, asssigned by TRI, is included in '
                                       'TRI_CHEM_ID.   Form R section 1.1 will be empty if a trade secret was claimed '
                                       'for the toxic chemical and information is provided in Section 1.3 or 2.1.',
                        'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                           'program.  Usually, only one number is assigned to each facility and the '
                                           'number is for the entire facility.  One company may have multiple TRI '
                                           'Facility Identification (ID) numbers if they have multiple facilities.  '
                                           'One facility with many establishments will usually have only one TRI '
                                           'Facility ID number.  They will then use this number for all of their Form '
                                           'Rs even if they are submitting a Form R for different establishments with '
                                           'different names.  In a few instances different establishments of the same '
                                           'facility will have different TRI Facility ID numbers.  The format is '
                                           'ZZZZZNNNNNSSSSS, where ZZZZZ = ZIP code, NNNNN = the first 5 consonants of '
                                           'the name, and SSSSS = the first 5 non-blank non-special characters in the '
                                           'street address.',
                        'WASTE_ROCK_MANAGED_PILE': 'Indicates if the on-site land disposal in reported in section 5.5 '
                                                   'is being managed in "waste rock piles".   Waste rock refers to '
                                                   'rock that contains insufficient metal concentration to '
                                                   'economically process at any given time and is thus typically '
                                                   'removed from a mine to allow access to the ore-grade rock. A '
                                                   'facility may indicate that quantities reported in section 5.5 were '
                                                   'managed in waste rock piles and may provide the quantity of the '
                                                   'chemical managed in such piles.  This data element was added in '
                                                   'reporting year 2018.'},
 'TRI_SOURCE_REDUCT_METHOD': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each '
                                              'submission.  The format is TTYYNNNNNNNNN, where TT = document type, YY '
                                              '= reporting year, and NNNNNNNNN = assigned number with a check digit.',
                              'EST_ANNUAL_REDUCT': 'The Estimated Annual Reduction is an optional percentage range '
                                                   'code indicating the estimated annual reduction in chemical waste '
                                                   'generation associated with any source reduction activity(s) a '
                                                   'facility reported in Section 8.10 of the Form R.  The reporting of '
                                                   'this data element began in reporting year 2014 when it was added '
                                                   'to the Form R.',
                              'REDUCTION_SEQUENCE_NUM': 'Sequence in which a source reduction method is reported on a '
                                                        'submission.',
                              'SOURCE_REDUCT_ACTIVITY': 'Indicates the type of source reduction activity implemented '
                                                        'at the facility during the reporting year.  This does not '
                                                        'include all source reduction activities ongoing at the '
                                                        'facility but only those activities related to the reported '
                                                        'toxic chemical.  An example of a source reduction activity '
                                                        'would include a spill and leak prevention program such as the '
                                                        'installation of a vapor recovery system.',
                              'SOURCE_REDUCT_METHOD_1': 'Indicates the method or methods used at the facility to '
                                                        'identify the possibility for a source reduction activity '
                                                        'implementation at the facility.  This does not include all '
                                                        'source reduction activities ongoing at the facility but only '
                                                        'those activities related to the reported toxic chemical.  An '
                                                        'example of a method used to identify source reduction '
                                                        'opportunities would be an internal pollution prevention '
                                                        'audit.',
                              'SOURCE_REDUCT_METHOD_2': 'Indicates the method or methods used at the facility to '
                                                        'identify the possibility for a source reduction activity '
                                                        'implementation at the facility.  This does not include all '
                                                        'source reduction activities ongoing at the facility but only '
                                                        'those activities related to the reported toxic chemical.  An '
                                                        'example of a method used to identify source reduction '
                                                        'opportunities would be an internal pollution prevention '
                                                        'audit.',
                              'SOURCE_REDUCT_METHOD_3': 'Indicates the method or methods used at the facility to '
                                                        'identify the possibility for a source reduction activity '
                                                        'implementation at the facility.  This does not include all '
                                                        'source reduction activities ongoing at the facility but only '
                                                        'those activities related to the reported toxic chemical.  An '
                                                        'example of a method used to identify source reduction '
                                                        'opportunities would be an internal pollution prevention '
                                                        'audit.'},
 'TRI_SOURCE_REDUCT_QTY': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each '
                                           'submission.  The format is TTYYNNNNNNNNN, where TT = document type, YY = '
                                           'reporting year, and NNNNNNNNN = assigned number with a check digit.',
                           'ENERGY_OFFSITE_CURR_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                        'entered for the energy recovery offsite current year '
                                                        "quantity.   Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'ENERGY_OFFSITE_CURR_YR_QTY': 'The total amount (in pounds) of the toxic chemical in waste '
                                                         'sent offsite to be burned for energy recovery during the '
                                                         'calendar year (January 1 - December 31)  for which the '
                                                         'report was submitted.  This includes all amounts of the '
                                                         'toxic chemical that were intended to be recovered for energy '
                                                         'and were sent offsite for that purpose.  This figure '
                                                         'includes all transfers offsite reported in section 6.2 which '
                                                         'are classified with an energy recovery code.  This does not '
                                                         'include quantities of the toxic chemical that are combusted '
                                                         'for energy recovery offsite as the result of a catastrophic '
                                                         'event, remedial action or other, one-time event not '
                                                         'associated with production.',
                           'ENERGY_OFFSITE_FOLL_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                        'entered for the energy recovery offsite following year '
                                                        "quantity.   Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'ENERGY_OFFSITE_FOLL_YR_QTY': 'The total amount (in pounds) of the toxic chemical in waste '
                                                         'expected to be sent offsite to be burned for energy recovery '
                                                         'during the calendar year (January 1 - December 31) following '
                                                         'the year for which the report was submitted. This does not '
                                                         'include quantities of the toxic chemical that will be '
                                                         'combusted for energy recovery offsite as the result of a '
                                                         'catastrophic event, remedial action or other, one-time event '
                                                         'not associated with production.',
                           'ENERGY_OFFSITE_PREV_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                        'entered for the energy recovery offsite previous year '
                                                        "quantity.   Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'ENERGY_OFFSITE_PREV_YR_QTY': 'The total amount (in pounds) of the toxic chemical in waste '
                                                         'sent offsite to be burned for energy recovery during the '
                                                         'calendar year (January 1 - December 31) prior to the year '
                                                         'for which the report was submitted.  This includes all '
                                                         'amounts of the toxic chemical that were intended to be '
                                                         'recovered for energy and were sent offsite for that '
                                                         'purpose.  This figure includes all transfers offsite '
                                                         'reported in section 6.2 which are classified with an energy '
                                                         'recovery code.  This does not include quantities of the '
                                                         'toxic chemical that are combusted for energy recovery '
                                                         'offsite as the result of a catastrophic event, remedial '
                                                         'action or other, one-time event not associated with '
                                                         'production.',
                           'ENERGY_OFFSITE_SECD_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                        'entered for the energy recovery offsite second following  '
                                                        "year quantity.   Values:  1 = 'NA', 0 = '0' (zero) or not "
                                                        "'NA'.",
                           'ENERGY_OFFSITE_SECD_YR_QTY': 'The total amount (in pounds) of the toxic chemical in waste '
                                                         'expected to be sent offsite to be burned for energy recovery '
                                                         'during the calendar year (January 1 - December 31) two years '
                                                         'following the year for which the report was submitted.  This '
                                                         'does not include quantities of the toxic chemical that will '
                                                         'be combusted for energy recovery offsite as the result of a '
                                                         'catastrophic event, remedial action or other, one-time event '
                                                         'not associated with production.',
                           'ENERGY_ONSITE_CURR_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                       'for the energy recovery onsite current year quantity.  '
                                                       "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'ENERGY_ONSITE_CURR_YR_QTY': 'The total amount (in pounds) of the toxic chemical in waste '
                                                        'burned for energy recovery onsite during the calendar year '
                                                        '(January 1 - December 31) for which the report was '
                                                        'submitted.  This includes only the amount of the toxic '
                                                        'chemical actually combusted in the unit, not the total amount '
                                                        'of the toxic chemical in the wastestream sent for energy '
                                                        'recovery.  This also does not include quantities of the toxic '
                                                        'chemical that are combusted for energy recovery onsite as the '
                                                        'result of a catastrophic event,remedial action or other, '
                                                        'one-time event not associated with production.',
                           'ENERGY_ONSITE_FOLL_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                       'for the energy recovery onsite following year quantity.   '
                                                       "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'ENERGY_ONSITE_FOLL_YR_QTY': 'The total amount (in pounds) of the toxic chemical in waste '
                                                        'expected to be burned for energy recovery onsite during the '
                                                        'calendar year (January 1 - December 31) following the year '
                                                        'for which the report was submitted.   This should not include '
                                                        'quantities of the toxic chemical that will be combusted for '
                                                        'energy recovery onsite as the result of a catastrophic event, '
                                                        'remedial action or other, one-time event not associated with '
                                                        'production.',
                           'ENERGY_ONSITE_PREV_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                       'for the energy recovery onsite previous year quantity.   '
                                                       "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'ENERGY_ONSITE_PREV_YR_QTY': 'The total amount (in pounds) of the toxic chemical in waste '
                                                        'burned for energy recovery onsite during the calendar year '
                                                        '(January 1 - December 31) prior to the year for which the '
                                                        'report was submitted.  This includes only the amount of the '
                                                        'toxic chemical actually combusted in the unit, not the total '
                                                        'amount of the toxic chemical in the wastestream sent for '
                                                        'energy recovery.  This also does not include quantities of '
                                                        'the toxic chemical that are combusted for energy recovery '
                                                        'onsite as the result of a catastrophic event, remedial action '
                                                        'or other, one-time event not associated with production.',
                           'ENERGY_ONSITE_SECD_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                       'for the energy recovery onsite second following  year '
                                                       "quantity.   Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'ENERGY_ONSITE_SECD_YR_QTY': 'The total amount (in pounds) of the toxic chemical in waste '
                                                        'expected to be burned for energy recovery onsite during the '
                                                        'calendar year (January 1 - December 31) two years following '
                                                        'the year for which the report was submitted.  This should not '
                                                        'include quantities of the toxic chemical that will be '
                                                        'combusted for energy recovery onsite as the result of a '
                                                        'catastrophic event, remedial action or other, one-time event '
                                                        'not associated with production.',
                           'RECYC_OFFSITE_CURR_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                       'for the recycled off-site current year quantity.   Values:  1 '
                                                       "= 'NA', 0 = '0' (zero) or not 'NA'.",
                           'RECYC_OFFSITE_CURR_YR_QTY': 'The total amount (in pounds) of the toxic chemical sent '
                                                        'offsite for recycling during the calendar year (January 1 - '
                                                        'December 31) for which the report was submitted.  This '
                                                        'includes all amounts of the toxic chemical intended to be '
                                                        'recycled, not just the amount of the toxic chemical actually '
                                                        'recovered.  This figure includes all transfers offsite '
                                                        'reported in section 6.2 which are classified with an '
                                                        'recycling code.  This amount does not include quantities of '
                                                        'the toxic chemical that were transferred offsite for '
                                                        'recycling as the result of a catastrophic event, remedial '
                                                        'action or other, one-time event not associated with '
                                                        'production.',
                           'RECYC_OFFSITE_FOLL_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                       'for the recycled off-site following year quantity.   Values:  '
                                                       "1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'RECYC_OFFSITE_FOLL_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected '
                                                        'to be sent offsite for recycling during the calendar year '
                                                        '(January 1 - December 31) following the year for which the '
                                                        'report was submitted.  This amount does not include '
                                                        'quantities of the toxic chemical that will be transferred '
                                                        'offsite for recycling as the result of a catastrophic event, '
                                                        'remedial action or other, one-time event not associated with '
                                                        'production.',
                           'RECYC_OFFSITE_PREV_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                       'for the recycled off-site previous year quantity.   Values:  1 '
                                                       "= 'NA', 0 = '0' (zero) or not 'NA'.",
                           'RECYC_OFFSITE_PREV_YR_QTY': 'The total amount (in pounds) of the toxic chemical sent '
                                                        'offsite for recycling during the calendar year (January 1 - '
                                                        'December 31) prior to the year for which the report was '
                                                        'submitted.  This includes all amounts of the toxic chemical '
                                                        'intended to be recycled and sent offsite for that purpose, '
                                                        'not just the amount of the toxic chemical actually '
                                                        'recovered.  This figure includes all transfers offsite '
                                                        'reported in section 6.2 which are classified with a recycling '
                                                        'code.    This amount does not include quantities of the toxic '
                                                        'chemical that were transferred offsite for recycling as the '
                                                        'result of a catastrophic event, remedial action or other, '
                                                        'one-time event not associated with production',
                           'RECYC_OFFSITE_SECD_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                       'for the recycled off-site second following year quantity.   '
                                                       "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'RECYC_OFFSITE_SECD_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected '
                                                        'to be sent offsite for recycling during the calendar year '
                                                        '(January 1 - December 31) two years following the year for '
                                                        'which the report was submitted.  This amount does not include '
                                                        'quantities of the toxic chemical that will be transferred '
                                                        'offsite for recycling as the result of a catastrophic event, '
                                                        'remedial action or other, one-time event not associated with '
                                                        'production.',
                           'RECYC_ONSITE_CURR_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                      'for the recycled on-site current year quantity.  Values:  1 = '
                                                      "'NA', 0 = '0' (zero) or not 'NA'.",
                           'RECYC_ONSITE_CURR_YR_QTY': 'The total amount (in pounds) of the toxic chemical recycled '
                                                       'onsite during the calendar year (January 1 - December 31) for '
                                                       'which the report was submitted.  This includes only the amount '
                                                       'of the toxic chemical actually recovered, not the total amount '
                                                       'of the toxic chemical in the wastestream sent for recycling '
                                                       'activities.  This amount does not include quantities of the '
                                                       'toxic chemical that were recycled onsite as the result of a '
                                                       'catastrophic event, remedial action or other, one-time event '
                                                       'not associated with production.',
                           'RECYC_ONSITE_FOLL_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                      'for the recycled on-site following year quantity.   Values:  1 '
                                                      "= 'NA', 0 = '0' (zero) or not 'NA'.",
                           'RECYC_ONSITE_FOLL_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected to '
                                                       'be recycled onsite during the calendar year (January 1 - '
                                                       'December 31) following the year for which the report was '
                                                       'submitted.   This amount does not include quantities of the '
                                                       'toxic chemical that will be recycled onsite as the result of a '
                                                       'catastrophic event, remedial action or other, one-time event '
                                                       'not associated with production.',
                           'RECYC_ONSITE_PREV_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                      'for the recycled on-site previous year quantity.  Values:  1 = '
                                                      "'NA', 0 = '0' (zero) or not 'NA'.",
                           'RECYC_ONSITE_PREV_YR_QTY': 'The total amount (in pounds) of the toxic chemical recycled '
                                                       'onsite during the calendar year (January 1 - December 31) '
                                                       'prior to the year for which the report was submitted.  This '
                                                       'includes only the amount of the toxic chemical actually '
                                                       'recovered for reuse, not the total amount of the toxic '
                                                       'chemical in the wastestream entering recycling units onsite.  '
                                                       'This amount does not include quantities of the toxic chemical '
                                                       'that were recycled onsite as the result of a catastrophic '
                                                       'event, remedial action or other, one-time event not associated '
                                                       'with production.',
                           'RECYC_ONSITE_SECD_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered "
                                                      'for the recycled on-site second following year quantity.   '
                                                      "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'RECYC_ONSITE_SECD_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected to '
                                                       'be recycled onsite during the calendar year (January 1 - '
                                                       'December 31) two years following the year for which the report '
                                                       'was submitted.   This amount does not include quantities of '
                                                       'the toxic chemical that will be recycled onsite as the result '
                                                       'of a catastrophic event, remedial action or other, one-time '
                                                       'event not associated with production.',
                           'REL_81A_CURR_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.A, "
                                                 'on-site releases to Class I Underground Injection Wells, RCRA '
                                                 "Subtitle C landfills, and other landfills. Values: 1 = 'NA'; 0 = '0' "
                                                 "(zero) or not 'NA'.",
                           'REL_81A_CURR_YR_QTY': 'The total amount of the toxic chemical released on-site due to '
                                                  'production related events by the facility to Class I Underground '
                                                  'Injection Wells, RCRA Subtitle C landfills, and other landfills '
                                                  'during the calendar year (January 1 - December 31). This total does '
                                                  'not include on-site releases or disposal due to catastrophic '
                                                  'events.',
                           'REL_81A_FOLL_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.A, "
                                                 'following year on-site releases to Class I Underground Injection '
                                                 'Wells, RCRA Subtitle C landfills, and other landfills. Values: 1 = '
                                                 "'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81A_FOLL_YR_QTY': 'The total amount of the toxic chemical expected to be released '
                                                  'on-site by the facility to Class I Underground Injection Wells, '
                                                  'RCRA Subtitle C landfills, and other landfills during the following '
                                                  'calendar year (January 1 - December 31). This total does not '
                                                  'include on-site releases or disposal due to catastrophic events.',
                           'REL_81A_PREV_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.A, "
                                                 'prior year on-site releases to Class I Underground Injection Wells, '
                                                 "RCRA Subtitle C landfills, and other landfills. Values: 1 = 'NA'; 0 "
                                                 "= '0' (zero) or not 'NA'.",
                           'REL_81A_PREV_YR_QTY': 'The total amount of the toxic chemical released on-site due to '
                                                  'production related events by the facility to Class I Underground '
                                                  'Injection Wells, RCRA Subtitle C landfills, and other landfills '
                                                  'during the prior calendar year (January 1 - December 31). This '
                                                  'total does not include on-site releases or disposal due to '
                                                  'catastrophic events.',
                           'REL_81A_SECD_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.A, "
                                                 'second following year on-site releases to Class I Underground '
                                                 'Injection Wells, RCRA Subtitle C landfills, and other landfills. '
                                                 "Values: 1 = 'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81A_SECD_YR_QTY': 'The total amount of the toxic chemical expected to be released '
                                                  'on-site by the facility to Class I Underground Injection Wells, '
                                                  'RCRA Subtitle C landfills, and other landfills during the second '
                                                  'following calendar year (January 1 - December 31). This total does '
                                                  'not include on-site releases or disposal due to catastrophic '
                                                  'events.',
                           'REL_81B_CURR_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.B, "
                                                 'on-site releases to mediums other than Class I Underground Injection '
                                                 'Wells, RCRA Subtitle C landfills, and other landfills. Values: 1 = '
                                                 "'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81B_CURR_YR_QTY': 'The total amount of the toxic chemical released on-site due to '
                                                  'production related events by the facility to mediums other than '
                                                  'Class I Underground Injection Wells, RCRA Subtitle C landfills, and '
                                                  'other landfills during the calendar year (January 1 - December 31). '
                                                  'These mediums include fugitive and stack air emissions, discharges '
                                                  'to water bodies, underground injection to class II-V wells, land '
                                                  'treatment/application farming, RCRA subtitle C surface '
                                                  'impoundments, Other surface Impoundments and Other disposals. This '
                                                  'total does not include on-site releases or disposal due to '
                                                  'catastrophic events.',
                           'REL_81B_FOLL_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.B, "
                                                 'following year on-site releases to mediums other than Class I '
                                                 'Underground Injection Wells, RCRA Subtitle C landfills, and other '
                                                 "landfills. Values: 1 = 'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81B_FOLL_YR_QTY': 'The total amount of the toxic chemical expected to be released '
                                                  'on-site due to production related events by the facility to mediums '
                                                  'other than Class I Underground Injection Wells, RCRA Subtitle C '
                                                  'landfills, and other landfills during the following calendar year '
                                                  '(January 1 - December 31). These mediums include fugitive and stack '
                                                  'air emissions, discharges to water bodies, underground injection to '
                                                  'class II-V wells, land treatment/application farming, RCRA subtitle '
                                                  'C surface impoundments, Other surface Impoundments and Other '
                                                  'disposals. This total does not include on-site releases or disposal '
                                                  'due to catastrophic events.',
                           'REL_81B_PREV_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.B, "
                                                 'prior year on-site releases to mediums other than Class I '
                                                 'Underground Injection Wells, RCRA Subtitle C landfills, and other '
                                                 "landfills. Values: 1 = 'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81B_PREV_YR_QTY': 'The total amount of the toxic chemical released on-site due to '
                                                  'production related events by the facility to mediums other than '
                                                  'Class I Underground Injection Wells, RCRA Subtitle C landfills, and '
                                                  'other landfills during the prior calendar year (January 1 - '
                                                  'December 31). These mediums include fugitive and stack air '
                                                  'emissions, discharges to water bodies, underground injection to '
                                                  'class II-V wells, land treatment/application farming, RCRA subtitle '
                                                  'C surface impoundments, Other surface Impoundments and Other '
                                                  'disposals. This total does not include on-site releases or disposal '
                                                  'due to catastrophic events.',
                           'REL_81B_SECD_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.B, "
                                                 'second following year on-site releases to mediums other than Class I '
                                                 'Underground Injection Wells, RCRA Subtitle C landfills, and other '
                                                 "landfills. Values: 1 = 'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81B_SECD_YR_QTY': 'The total amount of the toxic chemical expected to be released '
                                                  'on-site due to production related events by the facility to mediums '
                                                  'other than Class I Underground Injection Wells, RCRA Subtitle C '
                                                  'landfills, and other landfills during the second following calendar '
                                                  'year (January 1 - December 31). These mediums include fugitive and '
                                                  'stack air emissions, discharges to water bodies, underground '
                                                  'injection to class II-V wells, land treatment/application farming, '
                                                  'RCRA subtitle C surface impoundments, Other surface Impoundments '
                                                  'and Other disposals. This total does not include on-site releases '
                                                  'or disposal due to catastrophic events.',
                           'REL_81C_CURR_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.C, "
                                                 'off-site releases to Class I Underground Injection Wells, RCRA '
                                                 "Subtitle C landfills, and other landfills. Values: 1 = 'NA'; 0 = '0' "
                                                 "(zero) or not 'NA'.",
                           'REL_81C_CURR_YR_QTY': 'The total amount of the toxic chemical released off-site due to '
                                                  'production related events by the facility to Class I Underground '
                                                  'Injection Wells, RCRA Subtitle C landfills, and other landfills '
                                                  'during the calendar year (January 1 - December 31). This total does '
                                                  'not include off-site releases or disposal due to catastrophic '
                                                  'events.',
                           'REL_81C_FOLL_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.C, "
                                                 'following year off-site releases to Class I Underground Injection '
                                                 'Wells, RCRA Subtitle C landfills, and other landfills. Values: 1 = '
                                                 "'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81C_FOLL_YR_QTY': 'The total amount of the toxic chemical expected to be released '
                                                  'off-site by the facility to Class I Underground Injection Wells, '
                                                  'RCRA Subtitle C landfills, and other landfills during the following '
                                                  'calendar year (January 1 - December 31). This total does not '
                                                  'include off-site releases or disposal due to catastrophic events.',
                           'REL_81C_PREV_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.C, "
                                                 'prior year off-site releases to Class I Underground Injection Wells, '
                                                 "RCRA Subtitle C landfills, and other landfills. Values: 1 = 'NA'; 0 "
                                                 "= '0' (zero) or not 'NA'.",
                           'REL_81C_PREV_YR_QTY': 'The total amount of the toxic chemical released off-site due to '
                                                  'production related events by the facility to Class I Underground '
                                                  'Injection Wells, RCRA Subtitle C landfills, and other landfills '
                                                  'during the prior calendar year (January 1 - December 31). This '
                                                  'total does not include off-site releases or disposal due to '
                                                  'catastrophic events.',
                           'REL_81C_SECD_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.C, "
                                                 'second following year off-site releases to Class I Underground '
                                                 'Injection Wells, RCRA Subtitle C landfills, and other landfills. '
                                                 "Values: 1 = 'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81C_SECD_YR_QTY': 'The total amount of the toxic chemical expected to be released '
                                                  'off-site by the facility to Class I Underground Injection Wells, '
                                                  'RCRA Subtitle C landfills, and other landfills during the second '
                                                  'following calendar year (January 1 - December 31). This total does '
                                                  'not include off-site releases or disposal due to catastrophic '
                                                  'events.',
                           'REL_81D_CURR_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.D, "
                                                 'off-site releases to mediums other than Class I Underground '
                                                 'Injection Wells, RCRA Subtitle C landfills, and other landfills. '
                                                 "Values: 1 = 'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81D_CURR_YR_QTY': 'The total amount of the toxic chemical released off-site due to '
                                                  'production related events by the facility to mediums other than '
                                                  'Class I Underground Injection Wells, RCRA Subtitle C landfills, and '
                                                  'other landfills during the calendar year (January 1 - December 31). '
                                                  'These off-site mediums include Storage Only, '
                                                  'Solidification/Stabilization (for metals only), Wastewater '
                                                  'Treatment (Excluding POTWs) (for metals only), Subtitle C Surface '
                                                  'Impoundment, Other Surface Impoundment, Land Treatment, Other Land '
                                                  'Disposal, Underground Injection to Class II-V Wells, Other off-site '
                                                  'Management, Transfers to Waste brokers for Disposal and Unknown. '
                                                  'This total does not include off-site releases or disposal due to '
                                                  'catastrophic events.',
                           'REL_81D_FOLL_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.D, "
                                                 'following year off-site releases to mediums other than Class I '
                                                 'Underground Injection Wells, RCRA Subtitle C landfills, and other '
                                                 "landfills. Values: 1 = 'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81D_FOLL_YR_QTY': 'The total amount of the toxic chemical expected to be released '
                                                  'off-site due to production related events by the facility to '
                                                  'mediums other than Class I Underground Injection Wells, RCRA '
                                                  'Subtitle C landfills, and other landfills during the following '
                                                  'calendar year (January 1 - December 31). These off-site mediums '
                                                  'include Storage Only, Solidification/Stabilization (for metals '
                                                  'only), Wastewater Treatment (Excluding POTWs) (for metals only), '
                                                  'Subtitle C Surface Impoundment, Other Surface Impoundment, Land '
                                                  'Treatment, Other Land Disposal, Underground Injection to Class II-V '
                                                  'Wells, Other off-site Management, Transfers to Waste brokers for '
                                                  'Disposal and Unknown. This total does not include off-site releases '
                                                  'or disposal due to catastrophic events.',
                           'REL_81D_PREV_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.D, "
                                                 'prior year off-site releases to mediums other than Class I '
                                                 'Underground Injection Wells, RCRA Subtitle C landfills, and other '
                                                 "landfills. Values: 1 = 'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81D_PREV_YR_QTY': 'The total amount of the toxic chemical released off-site due to '
                                                  'production related events by the facility to mediums other than '
                                                  'Class I Underground Injection Wells, RCRA Subtitle C landfills, and '
                                                  'other landfills during the prior calendar year (January 1 - '
                                                  'December 31). These off-site mediums include Storage Only, '
                                                  'Solidification/Stabilization (for metals only), Wastewater '
                                                  'Treatment (Excluding POTWs) (for metals only), Subtitle C Surface '
                                                  'Impoundment, Other Surface Impoundment, Land Treatment, Other Land '
                                                  'Disposal, Underground Injection to Class II-V Wells, Other off-site '
                                                  'Management, Transfers to Waste brokers for Disposal and Unknown. '
                                                  'This total does not include off-site releases or disposal due to '
                                                  'catastrophic events.',
                           'REL_81D_SECD_YR_NA': "Indicates if 'NA' ('not applicable') was entered for Section 8.1.D, "
                                                 'second following year off-site releases to mediums other than Class '
                                                 'I Underground Injection Wells, RCRA Subtitle C landfills, and other '
                                                 "landfills. Values: 1 = 'NA'; 0 = '0' (zero) or not 'NA'.",
                           'REL_81D_SECD_YR_QTY': 'The total amount of the toxic chemical expected to be released '
                                                  'off-site due to production related events by the facility to '
                                                  'mediums other than Class I Underground Injection Wells, RCRA '
                                                  'Subtitle C landfills, and other landfills during the second '
                                                  'following calendar year (January 1 - December 31). These off-site '
                                                  'mediums include Storage Only, Solidification/Stabilization (for '
                                                  'metals only), Wastewater Treatment (Excluding POTWs) (for metals '
                                                  'only), Subtitle C Surface Impoundment, Other Surface Impoundment, '
                                                  'Land Treatment, Other Land Disposal, Underground Injection to Class '
                                                  'II-V Wells, Other off-site Management, Transfers to Waste brokers '
                                                  'for Disposal and Unknown. This total does not include off-site '
                                                  'releases or disposal due to catastrophic events.',
                           'REL_CURR_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered for the "
                                             "released current year quantity.   Values:  1 = 'NA', 0 = '0' (zero) or "
                                             "not 'NA'.",
                           'REL_CURR_YR_QTY': 'The total amount (in pounds) of the toxic chemical released due to '
                                              'production related events by the facility to all environmental media '
                                              'both on and off site during the calendar year (January 1 - December 31) '
                                              'for which the report was submitted.   This includes both fugitive and '
                                              'stack air emissions, discharges to water bodies, underground injection, '
                                              'and land disposal on site (all releases reported in section 5).  It '
                                              'also includes transfers of the toxic chemical offsite for disposal '
                                              '(transfers reported in section 6.2 which are classified with a disposal '
                                              'waste management code) and amounts of metals transferred to POTWs, '
                                              'because metals cannot be treated (destroyed) and will ultimately be '
                                              'disposed (metals reported in 6.1).',
                           'REL_FOLL_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered for the "
                                             "released following year quantity.    Values:  1 = 'NA', 0 = '0' (zero) "
                                             "or not 'NA'.",
                           'REL_FOLL_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected to be '
                                              'released by the facility to all environmental media both on and off '
                                              'site during the calendar year (January 1 - December 31) following the '
                                              'year for which the report was submitted.   This includes air emissions, '
                                              'discharges to water bodies, underground injection, and land disposal on '
                                              'site (all releases reported in section 5).  It also includes transfers '
                                              'of the toxic chemical offsite for disposal (transfers reported in '
                                              'section 6.2 which are classified with a disposal waste management code) '
                                              'and amounts of metals transferred to POTWs (metals reported in 6.1).',
                           'REL_PREV_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered for the "
                                             "released previous year quantity.   Values:  1 = 'NA', 0 = '0' (zero) or "
                                             "not 'NA'.",
                           'REL_PREV_YR_QTY': 'The total amount (in pounds) of the toxic chemical released due to '
                                              'production related events by the facility to all environmental media '
                                              'both on and off site during the calendar year (January 1 - December 31) '
                                              'prior to the year for which the report was submitted.   This includes '
                                              'air emissions, discharges to water bodies, underground injection, and '
                                              'land disposal on site (all releases reported in section 5).  It also '
                                              'includes transfers of the toxic chemical offsite for disposal '
                                              '(transfers reported in section 6.2 which are classified with a disposal '
                                              'waste management code) and amounts of metals transferred to POTWs '
                                              '(metals reported in 6.1).',
                           'REL_SECD_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was entered for the "
                                             "released second following year quantity.   Values:  1 = 'NA', 0 = '0' "
                                             "(zero) or not 'NA'.",
                           'REL_SECD_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected to be '
                                              'released by the facility to all environmental media both on and off '
                                              'site during the calendar year (January 1 - December 31) two years '
                                              'following the year for which the report was submitted.   This includes '
                                              'air emissions, discharges to water bodies, underground injection, and '
                                              'land disposal on site (all releases reported in section 5).  It also '
                                              'includes transfers of the toxic chemical offsite for disposal '
                                              '(transfers reported in section 6.2 which are classified with a disposal '
                                              'waste management code) and amounts of metals transferred to POTWs '
                                              '(metals reported in 6.1).',
                           'TREATED_OFFSITE_CURR_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                         'entered for the treated offsite current year quantity.   '
                                                         "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'TREATED_OFFSITE_CURR_YR_QTY': 'The total amount (in pounds) of the toxic chemical sent for '
                                                          'treatment offsite during the calendar year (January 1 - '
                                                          'December 31) for which the report was submitted.  This '
                                                          'includes the total amount of the toxic chemical intended to '
                                                          'be treated (destroyed) and sent offsite for that purpose, '
                                                          'not the amount of the toxic chemical actually treated '
                                                          '(destroyed) by offsite processes. This figure includes all '
                                                          'transfers offsite reported in section 6.2 which are '
                                                          'classified with treatment waste management codes and most '
                                                          'transfers to POTWs reported in section 6.1, except for '
                                                          'metals.  This does not include transfers of metals to '
                                                          'publicly owned treatment works (POTWs) because metals '
                                                          'cannot be treated (destroyed) and will ultimately be '
                                                          'disposed.  Transfers of metals to POTWs are included in '
                                                          'section 8.1.  This amount also does not include quantities '
                                                          'of the toxic chemical that were transferred off-site for '
                                                          'treatment as the result of a catastrophic event, remedial '
                                                          'action or other, one-time event not associated with '
                                                          'production.',
                           'TREATED_OFFSITE_FOLL_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                         'entered for the treated offsite following year quantity.   '
                                                         "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'TREATED_OFFSITE_FOLL_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected '
                                                          'to be sent for treatment offsite during the calendar year '
                                                          '(January 1 - December 31) following the year for which the '
                                                          'report was submitted.  This does not include expected '
                                                          'transfers of metals to publicly owned treatment works '
                                                          '(POTWs) because metals cannot be treated (destroyed) and '
                                                          'will ultimately be disposed.  Expected transfers of metals '
                                                          'to POTWs are included in section 8.1.  This amount also '
                                                          'does not include quantities of the toxic chemical that will '
                                                          'be transferred off-site for treatment as the result of a '
                                                          'catastrophic event, remedial action or other, one-time '
                                                          'event not associated with production.',
                           'TREATED_OFFSITE_PREV_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                         'entered for the treated offsite previous year quantity.   '
                                                         "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'TREATED_OFFSITE_PREV_YR_QTY': 'The total amount (in pounds) of the toxic chemical sent for '
                                                          'treatment offsite during the calendar year (January 1 - '
                                                          'December 31) prior to the year for which the report was '
                                                          'submitted.  This includes the total amount of the toxic '
                                                          'chemical intended to be treated (destroyed) and sent '
                                                          'offsite for that purpose, not the amount of the toxic '
                                                          'chemical actually treated (destroyed) by offsite '
                                                          'processes.  This figure includes all transfers offsite '
                                                          'reported in section 6.2 which are classified with treatment '
                                                          'waste management codes and most transfers to POTWs reported '
                                                          'in section 6.1, except for metals.  This does not include '
                                                          'transfers of metals to publicly owned treatment works '
                                                          '(POTWs) because metals cannot be treated (destroyed) and '
                                                          'will ultimately be disposed.  Transfers of metals to POTWs '
                                                          'are included in section 8.1.  This amount also does not '
                                                          'include quantities of the toxic chemical that were '
                                                          'transferred off-site for treatment as the result of a '
                                                          'catastrophic event, remedial action or other, one-time '
                                                          'event not associated with production.',
                           'TREATED_OFFSITE_SECD_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                         'entered for the treated offsite second following year '
                                                         "quantity.   Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'TREATED_OFFSITE_SECD_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected '
                                                          'to be sent for treatment offsite during the calendar year '
                                                          '(January 1 - December 31) two years following the year for '
                                                          'which the report was submitted.  This does not include '
                                                          'expected transfers of metals to publicly owned treatment '
                                                          'works (POTWs) because metals cannot be treated (destroyed) '
                                                          'and will ultimately be disposed.  Expected transfers of '
                                                          'metals to POTWs are included in section 8.1.  This amount '
                                                          'also does not include quantities of the toxic chemical that '
                                                          'will be transferred off-site for treatment as the result of '
                                                          'a catastrophic event, remedial action or other, one-time '
                                                          'event not associated with production.',
                           'TREATED_ONSITE_CURR_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                        'entered for the treated onsite current year quantity.   '
                                                        "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'TREATED_ONSITE_CURR_YR_QTY': 'The total amount (in pounds) of the toxic chemical treated '
                                                         'onsite during the calendar year (January 1 - December 31) '
                                                         'for which the report was submitted.  This includes only the '
                                                         'amount of the toxic chemical actually treated (destroyed) by '
                                                         'processes at the facility, not the total amount of the toxic '
                                                         'chemical present in wastestreams sent to those processes.  '
                                                         'This amount does not include quantities of the toxic '
                                                         'chemical that were treated for destruction onsite as the '
                                                         'result of a catastrophic event,remedial action or other, '
                                                         'one-time event not associated with production.',
                           'TREATED_ONSITE_FOLL_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                        'entered for the treated onsite following year quantity.   '
                                                        "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'TREATED_ONSITE_FOLL_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected '
                                                         'to be treated onsite during the calendar year (January 1 - '
                                                         'December 31) following the year for which the report was '
                                                         'submitted.  This amount does not include quantities of the '
                                                         'toxic chemical that will be treated for destruction onsite '
                                                         'as the result of a catastrophic event, remedial action or '
                                                         'other, one-time event not associated with production.',
                           'TREATED_ONSITE_PREV_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                        'entered for the treated onsite previous year quantity.   '
                                                        "Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'TREATED_ONSITE_PREV_YR_QTY': 'The total amount (in pounds) of the toxic chemical treated '
                                                         'onsite during the calendar year (January 1 - December 31) '
                                                         'prior to the year for which the report was submitted.  This '
                                                         'includes only the amount of the toxic chemical actually '
                                                         'treated (destroyed) by processes at the facility, not the '
                                                         'total amount of the toxic chemical present in wastestreams '
                                                         'sent to those processes.  This amount does not include '
                                                         'quantities of the toxic chemical that were treated for '
                                                         'destruction onsite as the result of a catastrophic event, '
                                                         'remedial action or other, one-time event not associated with '
                                                         'production.',
                           'TREATED_ONSITE_SECD_YR_NA': "Indicates if '0' (zero) or 'NA' ('not applicable') was "
                                                        'entered for the treated onsite second following year '
                                                        "quantity.   Values:  1 = 'NA', 0 = '0' (zero) or not 'NA'.",
                           'TREATED_ONSITE_SECD_YR_QTY': 'The total amount (in pounds) of the toxic chemical expected '
                                                         'to be treated onsite during the calendar year (January 1 - '
                                                         'December 31) two years following the year for which the '
                                                         'report was submitted.  This amount does not include '
                                                         'quantities of the toxic chemical that will be treated for '
                                                         'destruction onsite as the result of a catastrophic event, '
                                                         'remedial action or other, one-time event not associated with '
                                                         'production.'},
 'TRI_SUBMISSION_NAICS': {'ADJUSTED': 'This column indicates that a NAICS code assigned to a TRI Form/Submission was '
                                      'adjusted to fit within the boundaries of the valid NAICS list for the current '
                                      "reporting year.  A value of '1' indicates the assigned code was adjusted.  A "
                                      "value of '0' (zero) means no adjustment was made.",
                          'COVERED_NAICS': 'COVERED_NAICS indicates whether the reported or assigned primary NAICS '
                                           'code of a TRI submission (form R or form A) is that of a facility that is '
                                           'required to report to TRI.  This means that the primary NAICS code '
                                           'reported by the facility is in the list of EPCRA section 313/TRI covered '
                                           'NAICS codes.  And, as such, the facility has met one of the three criteria '
                                           'for being required to report to the TRI program.  The three criteria are '
                                           'as follows:',
                          'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each '
                                          'submission.  The format is TTYYNNNNNNNNN, where TT = document type, YY = '
                                          'reporting year, and NNNNNNNNN = assigned number with a check digit.',
                          'INDUSTRY_CODE': 'The Industry code identifies what industry or sector (Coal Mining, Metal '
                                           'Mining, Electrical Utilities, etc.) a TRI submission (form R or form A) '
                                           'belongs to.  Industry sector codes are used to categorize and analyze TRI '
                                           'data.  One of their primary uses of the INDUSTRY_CODE is to facilitate the '
                                           'display of industrial trends.  Here is the complete list of TRI Industry '
                                           'Codes and their corresponding names.  Note that this list of values '
                                           "appears in the TRI_CODE_DESC table where TABLE_ID = '26'.",
                          'METHOD': 'Identifies the method used to assign a NAICS code to a TRI submission.  In '
                                    'reporting years 1987 through 2005, the TRI program collected Standard Industrial '
                                    'Classification (SIC) codes on submissions to identify the primary business lines '
                                    'of reporting facilities.  In reporting year 2006, the TRI switched to the North '
                                    'American Industrial Classification System (NAICS) codes.  To facilitate the '
                                    'comparison of TRI data across these two time periods, NAICS codes were assigned '
                                    'to submissions in reporting years 1987-2005.',
                          'NAICS_CODE': 'The North American Industry Classification System (NAICS) Codes(s) that best '
                                        'describe the business activities conducted at a facility or establishment. '
                                        'NAICS codes are 6 digit numbers used by the Bureau of Census as part of a '
                                        'system to categorizeand track the types of business activities conducted in '
                                        'the United States.',
                          'NAICS_SEQUENCE_NUM': "The sequence of the facility's North American Industry Classification "
                                                'System (NAICS) code as entered in section 4.5 of part I of the Form R '
                                                'or Form A.',
                          'PRIMARY_IND': 'Indicates whether the associated SIC_CODE/NAICS_CODE represents the '
                                         "facility's primary business activity as entered by the submitter. EPA "
                                         'instructs facilities to enter their primary SIC/NAICS  on the Form R or Form '
                                         "A in part I, section 4.5, box a. Values: 1 = 'Yes', 0 = 'No'.",
                          'SOURCE': 'Indicates whether the NAICS code on a TRI submission was reported or assigned.  '
                                    'In reporting years 1987 through 2005, the TRI program collected Standard '
                                    'Industrial Classification (SIC) codes on submissions to identify the primary '
                                    'business lines of reporting facilities.  In reporting year 2006, TRI switched to '
                                    'the North American Industrial Classification System (NAICS) codes.   To '
                                    'facilitate the comparison of TRI data across these two TIME periods, NAICS codes '
                                    'were assigned to submissions in reporting years 1987-2005.  All forms from 1987 '
                                    'through 2005 should have assigned primary NAICS codes.   All forms after '
                                    'reporting year 2005 should have reported NAICS codes.  The list of values for '
                                    'this data element are:',
                          'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                             'program.  Usually, only one number is assigned to each facility and the '
                                             'number is for the entire facility.  One company may have multiple TRI '
                                             'Facility Identification (ID) numbers if they have multiple facilities.  '
                                             'One facility with many establishments will usually have only one TRI '
                                             'Facility ID number.  They will then use this number for all of their '
                                             'Form Rs even if they are submitting a Form R for different '
                                             'establishments with different names.  In a few instances different '
                                             'establishments of the same facility will have different TRI Facility ID '
                                             'numbers.  The format is ZZZZZNNNNNSSSSS, where ZZZZZ = ZIP code, NNNNN = '
                                             'the first 5 consonants of the name, and SSSSS = the first 5 non-blank '
                                             'non-special characters in the street address.'},
 'TRI_SUBMISSION_SIC': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each submission.  '
                                        'The format is TTYYNNNNNNNNN, where TT = document type, YY = reporting year, '
                                        'and NNNNNNNNN = assigned number with a check digit.',
                        'PRIMARY_IND': "Indicates whether the associated SIC_CODE/NAICS_CODE represents the facility's "
                                       'primary business activity as entered by the submitter. EPA instructs '
                                       'facilities to enter their primary SIC/NAICS  on the Form R or Form A in part '
                                       "I, section 4.5, box a. Values: 1 = 'Yes', 0 = 'No'.",
                        'SIC_CODE': 'The Standard Industrial Classification (SIC) code or codes which best describes '
                                    'the activities conducted at the facility.  SIC codes are 4 digit numbers used by '
                                    'the Bureau of Census as part of a system to categorize and track the types of '
                                    'business activities conducted in the United States.  The first two digits of the '
                                    'code represent the major industry group (e.g., SIC code 25XX indicates Furniture '
                                    'and Fixtures) and the second two digits represent the specific subset of that '
                                    'group (e.g., 2511 indicates wood household furniture).  EPA instructs facilities '
                                    'to enter their primary SIC code first.  Many facilities do not report their '
                                    'primary SIC code first.',
                        'SIC_SEQUENCE_NUM': "The sequence of the facility's Standard Industrial Classification (SIC) "
                                            'code as entered on Form R or Form A.',
                        'TRI_FACILITY_ID': 'The unique number assigned to each facility for purposes of the TRI '
                                           'program.  Usually, only one number is assigned to each facility and the '
                                           'number is for the entire facility.  One company may have multiple TRI '
                                           'Facility Identification (ID) numbers if they have multiple facilities.  '
                                           'One facility with many establishments will usually have only one TRI '
                                           'Facility ID number.  They will then use this number for all of their Form '
                                           'Rs even if they are submitting a Form R for different establishments with '
                                           'different names.  In a few instances different establishments of the same '
                                           'facility will have different TRI Facility ID numbers.  The format is '
                                           'ZZZZZNNNNNSSSSS, where ZZZZZ = ZIP code, NNNNN = the first 5 consonants of '
                                           'the name, and SSSSS = the first 5 non-blank non-special characters in the '
                                           'street address.'},
 'TRI_TABLE_ID_NAME': {'TABLE_ID': 'A designation for a related group of permissible values.  The name that identifies '
                                   'this group is located in TRI_TABLE_ID_NAME.',
                       'TABLE_NAME': 'The table description for the TRI_CODE_DESC.TABLE_ID .'},
 'TRI_TRANSFER_QTY': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each submission.  '
                                      'The format is TTYYNNNNNNNNN, where TT = document type, YY = reporting year, and '
                                      'NNNNNNNNN = assigned number with a check digit.',
                      'OFF_SITE_AMOUNT_SEQUENCE': 'Sequence in which an off-site transfer amount is reported on a '
                                                  'submission.',
                      'POTW_AMOUNT_SEQ': 'The POTW_AMOUNT_SEQ represents the sequence or order that POTW waste type '
                                         'management codes are entered in Part II, Section 6.1of the Form R under the '
                                         'section "Discharges to Publicly Owned Treatment Works (POTWs)".  Starting in '
                                         'Reporting Year 2018, facilities will report transfer quantities to POTWs for '
                                         'individual waste management activities.  The POTW_AMOUNT_SEQ represents the '
                                         'order that those waste management activities are reported in.  The '
                                         'POTW_WASTE_TYPE_CODE represents the waste management activity.  '
                                         'POTW_AMOUNT_SEQ represents the order the POTW_WASTE_TYPE_CODE was reported.  '
                                         'See POTW_WASTE_TYPE_CODE for more information.',
                      'POTW_PERCENTAGE_PROVIDED': 'This flag indicates whether the facility has provided percentages '
                                                  'of how a POTW transfer should be divided up between Section 8.1c - '
                                                  'Total off-site disposal to Class I Underground Injection Wells, '
                                                  'RCRA Subtitle C landfills, and other landfills; 8.1d - Total other '
                                                  'off-site disposal or other releases and 8.7 - Quantity treated '
                                                  'off-site.   These provide percentages override the default '
                                                  'percentages provide in the TRI reporting application, TRI-MEweb.   '
                                                  'There values for this data element are  0 = NO, 1=YES.  This data '
                                                  'element was introduced in reporting year 2014.',
                      'POTW_PERCENTAGE_TO_81C': 'The POTW Percentage to 81C is an optional percentage that a facility '
                                                'can provide to better indicate the amount of a transfer to a Publicly '
                                                'Owned Treatment Works (POTW) that is released at the POTW (off-site '
                                                'relative to the reporting facility) to Class I Underground Injection '
                                                'Wells, RCRA Subtitle C landfills, and/or other landfills.',
                      'POTW_PERCENTAGE_TO_81D': 'The POTW Percentage to 81D is an optional percentage that a facility '
                                                'can provide to better indicate the amount of a transfer to a Publicly '
                                                'Owned Treatment Works (POTW) that is released at the POTW (off-site '
                                                'relative to the reporting facility) to other media besides Class I '
                                                'Underground Injection Wells, RCRA Subtitle C landfills, and/or other '
                                                'landfills.',
                      'POTW_PERCENTAGE_TO_87': 'The POTW Percentage to 87 is an optional percentage that a facility '
                                               'can provide to better indicate the amount of a transfer to a Publicly '
                                               'Owned Treatment Works (POTW) that is treated at the POTW.',
                      'POTW_WASTE_TYPE_CODE': 'A code that represents the type of waste management chemical transfers '
                                              'are undergoing at Publicly Owned Treatment Works (POTWs).  Starting in '
                                              'Reporting Year 2018, facilities will report transfer quantities to '
                                              'POTWs for individual waste management activities.  The POTW waste type '
                                              'code (POTW_WASTE_TYPE_CODE) is reported in Part II, Section 6.1 of the '
                                              'Form R under the section "Discharges to Publicly Owned Treatment Works '
                                              '(POTWs)".  With this change in Reporting Year 2018, reporting of '
                                              'transfers to POTWs now more closely align with how transfers to other '
                                              'off-site locations (in part II, section 6.2 of the Form R) are '
                                              'reported. Because not all facilities may have POTW waste management '
                                              'information, EPA is providing two codes, P36 and P37, that a facility '
                                              'should use when the ultimate disposition of the chemical is unknown.  '
                                              'The POTW_WASTE_TYPE_CODE can have the following values:',
                      'TOTAL_TRANSFER': 'The total estimate of a chemical transferred off-site.  Transfer amounts are '
                                        'reported in grams for Dioxin and Dioxin like compounds and in pounds for all '
                                        'other chemicals.  If any transfer that is part of this total was reported as '
                                        'a range estimate, the mid-point of the range was used as the transfer '
                                        'amount.   This total consists of the sum of the following:',
                      'TRANSFER_BASIS_EST_CODE': 'The code representing the technique used to develop the estimate of '
                                                 "the release amount reported in the 'Total Transfers' box "
                                                 '(TOTAL_TRANSFER). The values are as follows:',
                      'TRANSFER_EST_NA': "Indicates that 'NA' (Not Applicable) was entered on Form R when a facility "
                                         'does not discharge wastewater containing the toxic chemical to Publicly '
                                         'Owned Treatment Works (Section 6.1.B_) or in wastes to other off-site '
                                         "facilities (section 6.2_).  Values: 1 = 'Yes', 0 = 'No'.",
                      'TRANSFER_LOC_NUM': 'The sequence in which an off-site transfer is reported on a Form R '
                                          'submission.',
                      'TRANSFER_RANGE_CODE': 'Code that corresponds to the amount of toxic chemical released annually '
                                             'by the reporting facility, reported as a range for releases less than '
                                             '1,000 pounds.  When a facility uses a range code, the amount reported to '
                                             'TRI is the midpoint of the range.  On Form R, letter codes are used to '
                                             'represent ranges:  A = 1-10 pounds, B = 11-499 pounds, and C = 500-999 '
                                             'pounds.  The letters are converted to numbers for storage in the TRIS  '
                                             "database where  '1' represents range 'A', '3' represents range 'B', "
                                             "and'4' represents range 'C'.  The historical value '2' = 1-499 pounds.",
                      'TYPE_OF_WASTE_MANAGEMENT': 'The type of waste treatment, disposal, recycling, or energy '
                                                  'recovery methods the off-site location uses to manage the toxic '
                                                  'chemical.  A two-digit code is used to indicate the type of waste '
                                                  'management activity employed.  This refers to the ultimate '
                                                  'disposition of the toxic chemical, not the intermediate activities '
                                                  "used for the waste stream.  (In Envirofacts, the code 'P91' "
                                                  'indicates a transfer to a POTW.  All other codes refer to off-site '
                                                  'transfers.)'},
 'TRI_TRIBE_DESC': {'BIA_CODE': 'The Bureau of Indian Affairs (BIA) Tribal Code that indicates the tribal land that '
                                'the facility is located on.  A facility reports this three digit code to the Toxics '
                                'Release Inventory (TRI) program on the form R or form A.  There are over 300 BIA '
                                'Tribal Codes.  For a list of BIA Tribal Codes and associated Tribe Names',
                    'EPA_TRIBE_ID': 'The unique EPA Tribe Identifier.',
                    'REGION': 'The EPA region in which the facility is located.',
                    'STATE_ABBR': 'The state abbreviation where the tribe is located.',
                    'TRIBE': 'The name of the Tribe associated with the Bureau of Indian Affairs (BIA) Tribal Code '
                             'that was reported by the facility.  There are over 300 BIA Tribal Codes.  For a list of '
                             'BIA Tribal Codes and associated Tribe Names'},
 'TRI_TRIPS_COMMENT': {},
 'TRI_WATER_STREAM': {'DOC_CTRL_NUM': 'DOC_CTRL_NUM is a unique identification number assigned to each submission.  '
                                      'The format is TTYYNNNNNNNNN, where TT = document type, YY = reporting year, and '
                                      'NNNNNNNNN = assigned number with a check digit.',
                      'REACH_CODE': 'A reach code is a unique 14-digit code that identifies a continuous piece of '
                                    'surface water with similar hydrologic characteristics. It is assigned to each '
                                    "receiving water body by the United States Geological Survey's (USGS) National "
                                    'Hydrography Dataset (NHD).',
                      'STORM_WATER_NA': "Indicates that 'NA' (Not Applicable) was entered on Form R for the percent of "
                                        "a release that came from stormwater runoff.  Values: 1 = 'Yes', 0 = 'No'.",
                      'STORM_WATER_PERCENT': 'The amount of the release, by weight percent, to water bodies, that came '
                                             'from stormwater runoff.This figure is only required when data are '
                                             'available.',
                      'STREAM_NAME': 'The name of the stream, river, lake, or other water body to which the chemical '
                                     'is discharged.  The name is listed as it appears on the NPDES permit, or, if the '
                                     'facility does not have a NPDES permit, as the water body is publicly known.  '
                                     'This is not a list of all streams through which the toxic chemical flows but is '
                                     'a list of direct discharges.  If more than one name is listed on form R, the '
                                     'facility has a separate discharge to each water body listed.',
                      'WATER_SEQUENCE_NUM': 'Sequence in which a release to water is reported on a Form R submission.'},
 'TRI_ZIP_CODE': {'CITY_NAME': 'The city where the facility or establishment is physically located.',
                  'COUNTRY_NAME': 'The country where the facility is located, if outside the United States.',
                  'REGION': 'The EPA region in which the facility is located.',
                  'STATE_ABBR': 'The state abbreviation where the tribe is located.',
                  'TRI_CENTROID_LAT': 'The assigned centroid latitude based on zip code.',
                  'TRI_CENTROID_LONG': 'The assigned centroid longitude based on zip code.',
                  'ZIP_CODE': 'The Zone Improvement Plan (ZIP) code assigned by the U.S. Postal Service as part of the '
                              'address of a facility.'}}
