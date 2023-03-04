table_column_lookup = \
{'ICIS_ACTIVITY': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular site.',
                   'ACTIVITY_NAME': 'The user-created name for an activity.',
                   'ACTIVITY_STATUS_DATE': 'The date on which the status of the activity was changed.',
                   'ACTIVITY_STATUS_DESC': 'The status of the compliance event or enforcement action.',
                   'ACTIVITY_TYPE_DESC': 'Full text description for ACTIVTY_TYPE_CODE.',
                   'ACTUAL_BEGIN_DATE': 'The actual date on which the activity began.',
                   'ACTUAL_END_DATE': 'Identifies the calendar date of the listed inspection (MM/DD/YYYY).',
                   'CANCELLATION_DATE': 'The date on which the activity was cancelled.',
                   'CANCELLATION_REASON_DESC': 'The description for the reason the activity was cancelled.',
                   'COMP_INCENTIVE_DESC': 'The geographic/community initiative for which the activity was developed.',
                   'CONSOLIDATED_FLAG': 'The flag indicating that a single inspection covered two or more programs '
                                        'under different statutes.  A consolidated inspection might be conducted by '
                                        'one fully trained inspector.  Single program inspections using a multimedia '
                                        'checklist should not be credited as a consolidated inspection.',
                   'COORDINATED_FLAG': 'The flag indicating that no more than three months may have elapsed between '
                                       'the inspection by one program and a subsequent inspection by another program.  '
                                       'The coordinated inspection must be a result of prior collaboration and '
                                       'planning between programs or based on information obtained during the initial '
                                       'inspection.',
                   'DURATION': 'The duration of the activity.',
                   'EPA_ASSIST_FLAG': 'The flag indicating whether the EPA assisted with an activity when either the '
                                      'state, local, or tribal agency was the lead.',
                   'FISCAL_YEAR': 'The fiscal year in which the activity occurred.',
                   'INTERNAL_REVIEW_FLAG': 'The flag indicating whether the activity is under internal regional '
                                           'review.',
                   'MULTIMEDIA_FLAG': 'The flag indicating whether the activity was a multimedia action.',
                   'PLANNED_BEGIN_DATE': 'The planned date on which the activity is scheduled to begin.',
                   'PLANNED_END_DATE': 'The planned date on which the activity is scheduled to end.',
                   'REGION_DESC': 'The text description for the unique code that identifies the EPA region.',
                   'SENSITIVE_DATA_FLAG': 'The flag indicating whether the activity contains sensitive or '
                                          'non-sensitive data.',
                   'STATE_CODE': 'A two-character field that contains the state postal abbreviation for the state in '
                                 'which the facility is located.',
                   'STATE_DESC': 'The name of a principal administrative subdivision of the U.S., Canada, or Mexico.',
                   'STATE_EPA_FLAG': 'Identifies the agency lead (S = State, E = EPA) for the listed inspection.',
                   'TOTAL_HOURS': 'The total number of hours spent on the activity.'},
 'ICIS_ACTIVITY_COMMENT': {'ACTIVITY_COMMENT_ID': 'The unique identifier for comments associated with an activity.',
                           'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                          'particular site.',
                           'COMMENT_BY': 'The individual responsible for the comment.',
                           'COMMENT_DATE': 'The date on which the comment was made.',
                           'COMMENT_TEXT': 'The free-form textual comments entered by the user/analyst to further '
                                           'describe the corresponding data.',
                           'COMMENT_TYPE_DESC': 'A text description of the type of comments.',
                           'SENSITIVITY_LEVEL': 'Column combining the user/data geography and sensitivity flag for the '
                                                'data to determine access to the data for reporting.  1 represents no '
                                                'sensitive access, 2 represents state sensitive access, and 3 '
                                                'represents federal sensitive access. Populated by a trigger.'},
 'ICIS_ACTIVITY_CREDIT': {'ACTIVITY_CREDIT_ID': 'The unique identifier for the credit requested/granted for an '
                                                'activity.',
                          'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                         'particular site.',
                          'MULTIFACILITY_CREDIT_GRANTED': 'The number of extra credits granted for a multi-facility '
                                                          'enforcement action.',
                          'MULTIFACILITY_CREDIT_REQUESTED': 'The number of extra credits requested  for a '
                                                            'multi-facility enforcement action.',
                          'MULTIMEDIA_CREDIT_GRANTED': 'The number of extra credits granted for a multimedia '
                                                       'enforcement action.',
                          'MULTIMEDIA_CREDIT_REQUESTED': 'The number of extra credits requested for a multimedia '
                                                         'enforcement action.',
                          'STATUTE_DESC': 'The name of the law authorizing the activity or being violated.'},
 'ICIS_ACTIVITY_RPT': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                      'site.',
                       'ACTIVITY_NAME': 'The user-created name for an activity.',
                       'ACTIVITY_STATUS_DATE': 'The date on which the status of the activity was changed.',
                       'ACTIVITY_STATUS_DESC': 'The status of the compliance event or enforcement action.',
                       'ACTIVITY_TYPE_CODE': 'A code describing the type of civil enforcement activity. Valid values '
                                             'are:',
                       'ACTIVITY_TYPE_DESC': 'Full text description for ACTIVTY_TYPE_CODE.',
                       'ACTUAL_BEGIN_DATE': 'The actual date on which the activity began.',
                       'ACTUAL_BEGIN_DATE_FY': 'The fiscal year in which the activity began.',
                       'ACTUAL_BEGIN_DATE_FYQ': 'The fiscal year quarter in which the activity began.',
                       'ACTUAL_END_DATE': 'Identifies the calendar date of the listed inspection (MM/DD/YYYY).',
                       'ACTUAL_END_DATE_FY': 'The fiscal year in which the activity ended.',
                       'ACTUAL_END_DATE_FYQ': 'The fiscal year quarter in which the activity ended.',
                       'CANCELLATION_DATE': 'The date on which the activity was cancelled.',
                       'CANCELLATION_REASON_DESC': 'The description for the reason the activity was cancelled.',
                       'COMP_INCENTIVE_DESC': 'The geographic/community initiative for which the activity was '
                                              'developed.',
                       'CONSOLIDATED_FLAG': 'The flag indicating that a single inspection covered two or more programs '
                                            'under different statutes.  A consolidated inspection might be conducted '
                                            'by one fully trained inspector.  Single program inspections using a '
                                            'multimedia checklist should not be credited as a consolidated inspection.',
                       'COORDINATED_FLAG': 'The flag indicating that no more than three months may have elapsed '
                                           'between the inspection by one program and a subsequent inspection by '
                                           'another program.  The coordinated inspection must be a result of prior '
                                           'collaboration and planning between programs or based on information '
                                           'obtained during the initial inspection.',
                       'DURATION': 'The duration of the activity.',
                       'EPA_ASSIST_FLAG': 'The flag indicating whether the EPA assisted with an activity when either '
                                          'the state, local, or tribal agency was the lead.',
                       'FISCAL_YEAR': 'The fiscal year in which the activity occurred.',
                       'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the facility '
                                                    'interest.',
                       'INTERNAL_REVIEW_FLAG': 'The flag indicating whether the activity is under internal regional '
                                               'review.',
                       'MOST_RECENT_ADOPT_DATE': 'The date on which the Pretreatment Control Authority adopted local '
                                                 'limits for pollutants.',
                       'MULTIMEDIA_FLAG': 'The flag indicating whether the activity was a multimedia action.',
                       'PLANNED_BEGIN_DATE': 'The planned date on which the activity is scheduled to begin.',
                       'PLANNED_BEGIN_DATE_FY': 'The fiscal year in which the activity was planned to begin.',
                       'PLANNED_BEGIN_DATE_FYQ': 'The fiscal year quarter in which the activity was planned to begin.',
                       'PLANNED_END_DATE': 'The planned date on which the activity is scheduled to end.',
                       'PLANNED_END_DATE_FY': 'The fiscal year in which the activity was planned to end.',
                       'PLANNED_END_DATE_FYQ': 'The fiscal year quarter in which the activity was planned to end.',
                       'REGION_DESC': 'The text description for the unique code that identifies the EPA region.',
                       'SENSITIVE_DATA_FLAG': 'The flag indicating whether the activity contains sensitive or '
                                              'non-sensitive data.',
                       'STATE_CODE': 'A two-character field that contains the state postal abbreviation for the state '
                                     'in which the facility is located.',
                       'STATE_DESC': 'The name of a principal administrative subdivision of the U.S., Canada, or '
                                     'Mexico.',
                       'STATE_EPA_FLAG': 'Identifies the agency lead (S = State, E = EPA) for the listed inspection.',
                       'TOTAL_HOURS': 'The total number of hours spent on the activity.'},
 'ICIS_COMP_MONITOR': {'ACCEPT_HAULED_DOMESTIC_FLAG': 'The flag indicating the acceptance of hauled domestic wastes.',
                       'ACCEPT_HAULED_NON_HAZ_FLAG': 'The flag indicating the acceptance of hauled industrial '
                                                     'non-hazardous waste.',
                       'ACCEPT_HAZ_FLAG': 'The flag indicating the acceptance of hazardous waste.',
                       'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                      'site.',
                       'ACTIVITY_OUTCOME_DESC': 'Full text description for ACTIVITY_OUTCOME_CODE.',
                       'ADEQUATE_RESOURCE_FLAG': 'The flag indicating if the resources are adequate for the activity.',
                       'AGENCY_DESC': 'The name of the government agency associated to Compliance Monitor activity.',
                       'ANNUAL_BUDGET': 'The total level of annual funding used to implement the Control Authority\'s '
                                        'Pretreatment program.',
                       'AREA_OF_EVALUATION': 'The area that was evaluated when inspection occurred.',
                       'AUTHORIZED_DISCHARGE_DESC': 'The description for a Compliance Monitoring CAFO component of '
                                                    'whether discharge is authorized.',
                       'BIOMONITORING_METHOD_DESC': 'Description of the biomonitoring inspection method.',
                       'BMP_OTHER': 'This is additional information relating to a Permit CAFO component BMP.',
                       'CAFO_CLASSIFICATION_DESC': 'The text that describes how the facility was classified as a '
                                                   '"Concentrated Animal Feeding Operation."  Options are Large, '
                                                   'Medium and Small (Designation).',
                       'CAFO_FLAG': 'The flag to indicate if the facility is classified as a CAFO or not.',
                       'CAFO_REASON_TEXT': 'The reason the facility was designated, such as severe water quality '
                                           'impact in a basin planning area of a TMDL area.',
                       'CIU_IN_SNC_NMBR': 'The number of CIUs in SNC.',
                       'CIU_NMBR': 'The total number of CIUs.',
                       'COMMUNICATE_DEFICIENCY_FLAG': 'The flag indicating whether the user communicated the '
                                                      'deficiencies to the facility at that time of the inspection.',
                       'COMMUNICATE_FACILITY_FLAG': 'The flag indicating whether the facility took any actions during '
                                                    'the inspection to address the deficiencies noted.',
                       'COMP_ASSISTANCE_FLAG': 'Column no longer used; superseded by '
                                               'icis_comp_monitor.general_comp_assistance_flag and '
                                               'icis_comp_monitor.specific_comp_asisstance_flag.',
                       'COMP_ASSISTANT_TIER_FLAG': 'The flag indicating the type of compliance assistance provided '
                                                   'during the inspection (e.g., Tier 1, Tier 2, or Both).',
                       'COMP_MONITOR_CATEGORY_DESC': 'The text description for the inspection category code.',
                       'COMP_MONITOR_TEXT': 'The descriptive text for the compliance monitoring activity.',
                       'CORRECTIVE_ACTION': 'The actions that were taken to prevent reoccurrences of event when it '
                                            'happened during dry weather.',
                       'DEFICIENCY_CONTROL_MECH_FLAG': 'Flag to indicate components that are not sufficient or are not '
                                                       'contained in the Pretreatment Control Authority control '
                                                       'mechanism.',
                       'DEFICIENCY_DATA_MGNT_FLAG': 'Flag to indicate deficiencies in the Pretreatment Control '
                                                    'Authority\'s data management and public participation effort.',
                       'DEFICIENCY_IDENTIFIED_FLAG': 'Flag to indicate deficiencies were noted during the review of IU '
                                                     'files.',
                       'DEFICIENCY_INTREPRETATION_FLAG': 'Flag to indicate deficiencies noted in the Pretreatment '
                                                         'Control Authority\'s interpretation and application of '
                                                         'pretreatment standards.',
                       'DEFICIENCY_LEGAL_FLAG': 'The flag indicates there are deficiencies in the legal authority.',
                       'DESIGNATION_DATE': 'The date on which the facility is designated as a CAFO.',
                       'DISCHARGE_FROM_PROD_FLAG': 'The flag indicates if there was any discharge from the production '
                                                   'area during the year.',
                       'DISCHARGE_VOLUME_TREATED': 'The total volume of discharge (in gallons) receiving primary '
                                                   'treatment and disinfection (where appropriate).',
                       'DISCHARGE_VOLUME_UNTREATED': 'The total volume discharge (in gallons) receiving no treatment.',
                       'EMS_DEVELOPED_DATE': 'This is the date that an EMS was developed by the facility.',
                       'EMS_FLAG': 'This field indicates whether the facility has some form of environmental '
                                   'management system.',
                       'EMS_LAST_UPDATED_DATE': 'This is the date that the EMS was last updated by the facility.',
                       'ESTIMATED_AREA_DISTURBED': 'This identifies the estimated area disturbed by entire project, '
                                                   'measured in acres.',
                       'ESTIMATED_BEGIN_DATE': 'This identifies the estimated start date of project.',
                       'ESTIMATED_END_DATE': 'This identifies the estimated completion date of project.',
                       'FACILITY_ACTION_FLAG': 'This column is not currently being used.',
                       'FIELD_DESCRIPTION': 'The description of the field where the inspection occurred.',
                       'FORMAL_RESPONSE_FLAG': 'The flag indicating whether a formal Enforcement Action has been taken '
                                               'in response to a violation of any schedule for implementation of '
                                               'needed remedial measures identified.',
                       'FREQ_EFFLUENT_TOXICANT_NMBR': 'The number of times that toxicant sampling of effluent was '
                                                      'performed at the POTW over the past year.',
                       'FREQ_INFLUENT_TOXICANT_NMBR': 'The number of times that toxicant sampling of effluent was '
                                                      'performed at the POTW over the past year.',
                       'FREQ_SLUDGE_TOXICANT_NMBR': 'The number of times that toxicant sampling of sludge was '
                                                    'performed at the POTW over the past year.',
                       'GENERAL_COMP_ASSISTANCE_FLAG': 'The flag indicating whether a general compliance assistance '
                                                       'activity was provided during the inspection.',
                       'INADEQUACY_SAMPLE_INSPECT_FLAG': 'The flag indicating whether sampling or inspection was '
                                                         'inadequate.',
                       'INDUSTRIAL_USER_NMBR': 'The total number of significant industrial users.',
                       'INSP_RATING_DESC': 'The descriptive text for the rating given by inspector.',
                       'IU_PENALTIES_COLLECTED_NMBR': 'Number of IUs from which penalties have been collected.',
                       'JOINT_INSPECTION_FLAG': 'The flag indicating if the inspection is a joint inspection of '
                                                'federal and state.',
                       'JOINT_INSPECTION_PURPOSE_DESC': 'This describes the reason for a joint Inspection.',
                       'JOINT_LEAD_FLAG': 'The flag indicating who is the lead of the joint inspection.',
                       'LAND_AVAILABLE': 'The number of acres of land under the control of the applicant that are '
                                         'suitable for land application of the CAFO manure, litter, or wastewater.',
                       'LATITUDE_MEASURE': 'The horizontal position coordinate for the point of discharge location in '
                                           'units of decimal degrees. Latitude and longitude coordinates are not '
                                           'required to be entered into ICIS-NPDES. Searching on coordinates will only '
                                           'return results for permit features that have latitude and longitude data '
                                           'in ICIS-NPDES.',
                       'LATITUDE_MEASURE_SSO': 'The measure of the angular distance on a meridian north or south of '
                                               'the equator.',
                       'LIQUID_MANURE_GENERATED_AMT': 'The total amount of manure in gallons generated annually by the '
                                                      'facility.',
                       'LIQUID_MANURE_TRANSFERRED_AMT': 'The total amount of manure in gallons produced by the CAFO '
                                                        'that will be transferred to other persons.',
                       'LIVESTOCK_AUTHORIZED_CAPACITY': 'This is the maximum number of animals that the facility is '
                                                        'authorized to handle and may be the same as the Designed '
                                                        'Maximum Capacity.',
                       'LIVESTOCK_DETERMIN_CAPACITY': 'The number of animals that the AFO/CAFO determination was based '
                                                      'on.',
                       'LIVESTOCK_MAX_CAPACITY': 'The maximum number of animals that the facility is permitted to '
                                                 'handle.',
                       'LONGITUDE_MEASURE': 'The vertical position coordinate for the point of discharge location in '
                                            'units of decimal degrees. ICIS-NPDES does not require Latitude and '
                                            'longitude coordinates to be entered. Searching on coordinates will only '
                                            'return results for permit features that have latitude and longitude data '
                                            'in ICIS-NPDES.',
                       'LONGITUDE_MEASURE_SSO': 'The measure of the angular distance on a meridian east or west of the '
                                                'prime meridian for a Permitted Feature; stored in decimal degrees.',
                       'MAJOR_OUTFALL_EST_MEASURE_FLAG': 'The flag indicating whether the number of  major MS4 '
                                                         'outfalls were estimated or measured.',
                       'MAJOR_OUTFALL_NMBR': 'This is the number of major outfalls for the MS4.',
                       'MEDIA_DESC': 'The description of a media associated with a compliance monitoring activity.',
                       'MINOR_OUTFALL_EST_MEASURE_FLAG': 'The flag indicating whether the number of minor MS4 outfalls '
                                                         'was estimated or measured.',
                       'MINOR_OUTFALL_NMBR': 'This is the number of minor outfalls for the MS4.',
                       'MOST_RECENT_ADOPT_DATE': 'The date on which the Pretreatment Control Authority adopted local '
                                                 'limits for pollutants.',
                       'MOST_RECENT_CREDIT_APPROV_DATE': 'The date the application for removal credits was approved.',
                       'MOST_RECENT_EVAL_DATE': 'The date on which the Pretreatment Control Authority has technically '
                                                'evaluated the need for local limits.',
                       'MS4_ANNUAL_EXPENDITURE': 'The expenses for the year for the MS4.',
                       'MS4_ANNUAL_EXPENDITURE_YEAR': 'This is the year associated with the MS4 Annual Expenditure.',
                       'MS4_BUDGET': 'This is the budget for the next year for the MS4.',
                       'MS4_BUDGET_YEAR': 'This is the year associated with the MS4 Budget.',
                       'NMBR_OF_ACRES_DRAINAGE': 'This is the number of acres that are drained and collected in the '
                                                 'production area.',
                       'NMBR_OF_DAY': 'The length of inspection in days.',
                       'NMP_DEVELOPED_DATE': 'The date that an NMP was developed by the facility.',
                       'NMP_FLAG': 'The yes/no flag indicating whether the facility has Nutrient Manure Management '
                                   'Plan developed or approved by a certified planner.',
                       'NMP_LAST_UPDATED_DATE': 'The date that the NMP was last updated by the facility.',
                       'NO_EXPOSURE_AUTH_DATE': 'The date the no exposure to a facility was authorized.',
                       'OBSERVED_DEFICIENCY_FLAG': 'The flag indicating whether a deficiency was observed during the '
                                                   'inspection.',
                       'OTHER_COMPONENT': 'Free-form text to describe the system component code if other is selected '
                                          'for the system component code.',
                       'OTHER_SSO_REACTION': 'The narrative description of steps taken if the Reaction code selected '
                                             'is Other.',
                       'OVERFLOW_CAUSE': 'The SSO event cause (e.g., blockage, equipment failure, precipitation).',
                       'OVERFLOW_DATE': 'The date for which the SSO event is being reported.',
                       'OVERFLOW_DATE_SSO': 'The date for which the SSO event is being reported.',
                       'OVERFLOW_DURATION': 'The time elapsed between the beginning and end of CSO event.',
                       'OVERFLOW_DURATION_SSO': 'The time elapsed between the beginning and end of SSO event.',
                       'OVERFLOW_LOCATION': 'The street address location of the overflow (e.g., manhole cover, pump '
                                            'station).',
                       'OVERFLOW_LOCATION_SSO': 'The street address location of the overflow (e.g., manhole cover, '
                                                'pump station).',
                       'OVERFLOW_VOLUME': 'The estimated volume (in gallons) of SSO discharge.',
                       'PASSTHROUGH_FLAG': 'The flag indicating if there has been any incidents of pass-through or '
                                           'interference at the POTW in the past year.',
                       'PENALTIES_COLLECTED_AMT': 'The amount of penalties collected.',
                       'PERM_FEATURE_ID': 'The unique system identifier for a permitted feature.',
                       'PRECIPITATION': 'The total precipitation (rainfall or snowmelt) in inches triggered by the '
                                        'event during the wet weather.',
                       'PROJECT_PLAN_SIZE_DESC': 'This text describes the planned size of the project.',
                       'PROJECT_TYPE_DESC': 'This text describing the type of construction project.',
                       'PROJECT_TYPE_OTHER': 'The free-form text field when other is selected for the construction '
                                             'project type.',
                       'RECEIVING_WATER': 'The name of receiving water where the SSO discharged.',
                       'RECOMMENDATION': 'Recommendation for inspections of activity conducted.',
                       'REMOVAL_STATUS_DESC': 'The description of the status of the application for removal credit for '
                                              'the pretreatment control authority.',
                       'REPORT_FUTURE_ACTION_FLAG': 'A flag indicating weather or not an action is required as a '
                                                    'follow up to the inspection conducted.',
                       'SIU_ADMIN_ORDER_NMBR': 'The number of administrative orders issued to SIUs.',
                       'SIU_ADMIN_SUIT_NMBR': 'The number of civil suits filed against SIUs.',
                       'SIU_CRIMINAL_SUIT_NMBR': 'The number of criminal suits filed against SIUs.',
                       'SIU_NMBR': 'The total number of SIUs.',
                       'SIU_NOT_INSPECTED_NMBR': 'The number of SIUs not inspected.',
                       'SIU_NOT_SAMPLED_NMBR': 'The number of SIUs not sampled.',
                       'SIU_SCHEDULE': 'This is the number of Significant Industrial Users on Pretreatment or '
                                       'Compliance Schedules.',
                       'SIU_SIGNIFICANT_VIOLATION_NMBR': 'The number of significant industrial users with significant '
                                                         'violations published in the newspaper.',
                       'SIU_SNC_PRETREATMENT_SCHEDULE': 'The number of Significant industrial users in SNC with '
                                                        'pretreatment schedule.',
                       'SIU_SNC_PRE_STD_NMBR': 'The significant industrial users in SNC with pretreatment standards.',
                       'SIU_SNC_PUBLISHED_NEWS': 'The number of Significant industrial users in SNC published in '
                                                 'newspaper.',
                       'SIU_SNC_RPT_REQUIREMENT_NMBR': 'The significant industrial users in SNC with reporting '
                                                       'requirements.',
                       'SIU_VIOLATION_NOTICE_NMBR': 'The number of formal notices of violation or equivalent actions '
                                                    'that have been issued to SIUs.',
                       'SIU_WO_CONTROL_MECH_NMBR': 'The number of SIUs for which a current control mechanism is '
                                                   'required but not yet issued.',
                       'SOLID_MANURE_GENERATED_AMT': 'The total amount of manure in tons generated annually by the '
                                                     'facility.',
                       'SOLID_MANURE_TRANSFERRED_AMT': 'The number of tons of manure or litter produced by the CAFO '
                                                       'that will be transferred to other persons.',
                       'SPECIFIC_COMP_ASSISTANCE_FLAG': 'The flag indicating whether a specific compliance assistance '
                                                        'activity was provided during the inspection.',
                       'STATE_STATUTE_TEXT': 'This is user entered information about the State law that is authorizing '
                                             'the Activity or being violated.',
                       'STEPS_TAKEN': 'The description of the steps taken to reduce prevent or mitigate SSO.',
                       'SUO_DATE': 'The date that the SUO was most recently adopted at the POTW and Control Authority '
                                   'level.',
                       'SUO_REFERENCE': 'The reference to the actual local sewer use ordinance (SUO) number and '
                                        'chapter at the POTW and Control Authority level.',
                       'SWPPP_EVALUATION_DATE': 'The date the SWPPP evaluation is done.',
                       'SWPPP_EVALUATION_TEXT': 'Comments regarding SWPPP evaluation.',
                       'SWPPP_EVAL_BASIS_DESC': 'The basis on which the Storm Water Pollution Prevention Plan was '
                                                'evaluated.',
                       'TOTAL_HOURS': 'The total number of hours spent on the activity.',
                       'VIOLATION_OF_SCHEDULE_FLAG': 'The flag indicating whether there has been a violation of any '
                                                     'schedule issued.',
                       'WEATHER_CONDITION': 'The weather conditions throughout the duration of the inspection.',
                       'WEATHER_DRY_WET_FLAG': 'The flag that tells whether the overflow event occurred during wet '
                                               'weather or dry weather.'},
 'ICIS_CONTACT': {'CONTACT_ID': 'The unique identifier for a contact related to a particular number.',
                  'FIRST_NAME': 'The given name of an individual.',
                  'FULL_NAME': 'The complete name of the contact including first name, middle name or initial, and '
                               'surname.',
                  'LAST_NAME': 'The surname of an individual.',
                  'MIDDLE_NAME': 'The middle name or initial of an individual.',
                  'ORGANIZATION_FORMAL_NAME': 'The legal, formal name of an organization that is affiliated with the '
                                              'facility site.',
                  'TITLE': 'The title held by a person in an organization.'},
 'ICIS_CONTACT_ELECTRONIC_ADDR': {'CONTACT_ELECTRONIC_ADDRESS_ID': 'The unique identifier for a contacts electronic '
                                                                   'address.',
                                  'CONTACT_ID': 'The unique identifier for a contact related to a particular number.',
                                  'ELECTRONIC_ADDRESS_TEXT': 'A resource address, usually consisting of the access '
                                                             'protocol, the domain name, and optionally, the path to a '
                                                             'file or location.',
                                  'ELECTRONIC_ADDRESS_TYPE_DESC': 'A resource address, usually consisting of the '
                                                                  'access protocol, the domain name, and optionally, '
                                                                  'the path to a file or location.'},
 'ICIS_CONTACT_PHONE': {'CONTACT_ID': 'The unique identifier for a contact related to a particular number.',
                        'CONTACT_PHONE_ID': 'The unique identifier for a Phone number related to a contact.',
                        'PHONE_TYPE_DESC': 'The text description of the Phone type.',
                        'TELEPHONE_EXTENSION_NMBR': 'The number assigned within an organization to an individual '
                                                    'telephone that extends the external telephone number.',
                        'TELEPHONE_NMBR': 'The number that identifies a particular telephone connection.'},
 'ICIS_DEFAULT_STATISTICAL_BASE': {'DEFAULT_STATISTICAL_BASE_ID': 'The unique identifier of the default statistical '
                                                                  'base code for a value for a limit set.',
                                   'LIMIT_SET_ID': 'The unique identifier of the Limit Set which has the default '
                                                   'statistical base code for its limits.',
                                   'STATISTICAL_BASE_DESC': 'The description of the statistical base type.',
                                   'STATISTICAL_BASE_LONG_DESC': 'The long description of the statistical base code.',
                                   'STATISTICAL_BASE_MONTHLY_AVG': 'The data element indicating whether the '
                                                                   'statistical base code is a monthly average, '
                                                                   'non-monthly average, or neither for purposes of '
                                                                   'calculating RNC.',
                                   'STATISTICAL_BASE_SHORT_DESC': 'The short description of the statistical base code.',
                                   'VALUE_TYPE_DESC': 'The description for the value type.'},
 'ICIS_DMR': {'DMR_COMMENT_TEXT': 'The comments that are entered by the permittee at the bottom of the pre-printed DMR '
                                  'form.',
              'DMR_EVENT_ID': 'The sequence ID identifying the DMR Event.',
              'DMR_FORM_ID': 'The sequence ID identifying the DMR Form.',
              'DMR_ID': 'The sequence ID identifying the DMR form.',
              'EXECUTIVE_OFFICER_FIRST_NAME': 'The first name of the principal executive officer who supervises the '
                                              'DMR form.',
              'EXECUTIVE_OFFICER_LAST_NAME': 'The last name of the principal executive officer who supervises the DMR '
                                             'form.',
              'EXECUTIVE_OFFICER_PHONE': 'The phone number of the executive officer who is responsible for the DMR.',
              'EXECUTIVE_OFFICER_TITLE': 'The title of the principal executive who supervises the DMR form.',
              'SIGNATORY_FIRST_NAME': 'The first name of the principal executive officer or authorized delegate who '
                                      'signs the DMR form.',
              'SIGNATORY_LAST_NAME': 'The last name of the principal executive officer or authorized delegate who '
                                     'signs the DMR form.',
              'SIGNATORY_PHONE': 'The phone number of the principal executive officer or authorized delegate who signs '
                                 'the DMR form.',
              'SIGNATURE_DATE': 'The date the DMR form was signed.'},
 'ICIS_DMR_EVENT': {'DMR_DUE_DATE': 'The date upon which the DMR is due for submission to the regulatory authority.',
                    'DMR_EVENT_ID': 'The sequence ID identifying the DMR Event.',
                    'LIMIT_SET_ID': 'The unique identifier of the Limit Set which has the default statistical base '
                                    'code for its limits.',
                    'LIMIT_SET_SCHEDULE_ID': 'The sequence ID identifying the Limit Set Schedule.',
                    'MONITORING_PERIOD_END_DATE': 'The date that the monitoring period for the values covered by this '
                                                  'DMR Form ends (YYYYMMDD).'},
 'ICIS_DMR_FORM_PARAMETER': {'CHEMICAL_ABSTRACT_SERVICE_NMBR': 'This is the unique number assigned to a chemical '
                                                               'substance by the Chemical Abstracts Service.',
                             'CHEMICAL_FORMULA': 'This is the pollutant chemical formula name.',
                             'DMR_EVENT_ID': 'The sequence ID identifying the DMR Event.',
                             'DMR_FORM_ID': 'The sequence ID identifying the DMR Form.',
                             'DMR_FORM_PARAMETER_ID': 'The sequence ID identifying the DMR Form Parameter.',
                             'EPA_ID': 'This is the EPA Identifier for substances.',
                             'LIMIT_ID': 'The unique identifier for a limit parameter record.',
                             'MONITORING_LOCATION_DESC': 'The description that the monitoring location at which the '
                                                         'monitoring requirement (and effluent limit if limited) '
                                                         'applies.  One parameter may have several monitoring location '
                                                         'requirements pertaining to the same permitted feature.',
                             'PARAMETER_DESC': 'Text description of the PARAMETER_CODE.',
                             'PERCENT_EXCEEDENCE_FLAG': 'The flag indicating whether percent exceedence can be '
                                                        'calculated for the parameter.',
                             'PERCENT_REMOVAL_FLAG': 'The flag indicating whether the parameter is a percent removal '
                                                     'parameter for determining the formula to use for calculating the '
                                                     'percent exceedence for the parameter.',
                             'POLLUTANT_CATEGORY_DESC': 'The description of the pollutant category.',
                             'POLLUTANT_DESC': 'The name that EPA has selected as its preferred name for a substance '
                                               '(also known as registry name). If the registry name is not available, '
                                               'use the systematic name instead.',
                             'SRS_ID': 'This is the unique identifier assigned to a substance for internal tracking '
                                       'within EPA systems.',
                             'SRS_SYSTEMATIC_NAME': 'The Substance Registry System (SRS) name for the pollutant.',
                             'UNIT_GROUP_DESC': 'The short description of the unit of measure applicable to limit or '
                                                'DMR values.'},
 'ICIS_DMR_FORM_VALUE': {'DMR_FORM_PARAMETER_ID': 'The sequence ID identifying the DMR Form Parameter.',
                         'DMR_FORM_VALUE_ID': 'The sequence ID identifying the DMR Form Value.',
                         'LIMIT_VALUE_ID': 'The system-generated unique identifier for the Limit Value.',
                         'VALUE_TYPE_DESC': 'The description for the value type.'},
 'ICIS_DMR_PARAMETER': {'DMR_FORM_PARAMETER_ID': 'The sequence ID identifying the DMR Form Parameter.',
                        'DMR_ID': 'The sequence ID identifying the DMR form.',
                        'DMR_PARAMETER_ID': 'The flag indicating whether the permit is subject to the DMR run. Value '
                                            'is (Y)es or No (null value). DMR_PARAMETER_ID - The system-generated '
                                            'unique identifier for the DMR parameter to which the DMR value belongs.',
                        'FREQUENCY_OF_ANALYSIS_DESC': 'The description of the frequency with which the permittee must '
                                                      'analyze the sampled data.',
                        'REPORTED_EXCURSION_NMBR': 'The number of times a limit was exceeded as reported on the DMR '
                                                   'form.',
                        'SAMPLE_TYPE_DESC': 'The description of the unique code identifying the sampling method '
                                            'required by the permit to be used to provide measurement values on the '
                                            'DMR.',
                        'USER_ENTERED_INDEX': 'The number indicating the sort order in which the parameter appears on '
                                              'the DMR; based upon the order of data entry for data entered through '
                                              'DMR screens and Parameter Code/Monitoring Location Code for data '
                                              'entered via migration.'},
 'ICIS_DMR_VALUE': {'ADJUSTED_DMR_STANDARD_UNITS': 'The Adjusted DMR value expressed in standard units as calculated '
                                                   'by the system.',
                    'ADJUSTED_DMR_VALUE_NMBR': 'The Adjusted DMR value number reported on the DMR if an effluent '
                                               'trade(s) has taken place for a Limit parameter that has at least one '
                                               'effluent trade partner.',
                    'DAYS_LATE': 'The system-generated number of days the Discharge Monitoring Report value was late '
                                 '(as compared to the DMR_DUE_DATE) in ICIS.',
                    'DMR_FORM_VALUE_ID': 'The sequence ID identifying the DMR Form Value.',
                    'DMR_PARAMETER_ID': 'The flag indicating whether the permit is subject to the DMR run. Value is '
                                        '(Y)es or No (null value). DMR_PARAMETER_ID - The system-generated unique '
                                        'identifier for the DMR parameter to which the DMR value belongs.',
                    'DMR_VALUE_ID': 'The system-generated unique identifier for the DMR value.',
                    'DMR_VALUE_NMBR': 'The Adjusted DMR value number reported on the DMR if an effluent trade(s) has '
                                      'taken place for a Limit parameter that has at least one effluent trade partner.',
                    'EXCEEDENCE_PCT': 'The system-generated percent by which the DMR value (or Adjusted Value) '
                                      'exceeded its Limit (or stay) value.',
                    'NODI_DESC': 'The description of the reason why no DMR Value was submitted by the permittee for a '
                                 'Monitoring Period End Date.',
                    'UNIT_DESC': 'The description of the unit of measure applicable to limit or DMR values.',
                    'UNIT_SHORT_DESC': 'The short description of the unit of measure applicable to limit or DMR '
                                       'values.',
                    'VALUE_QUALIFIER_DESC': 'The code that allows a user to indicate the direction of the value when '
                                            'an alternate limit value is possible (e.g., less than, greater than, and '
                                            'too numerous).',
                    'VALUE_RECEIVED_DATE': 'VALUE_RECEIVED_DATE'},
 'ICIS_ENFORCEMENT': {'ACHIEVED_DATE': 'The date on which an Informal Enforcement Action is achieved. For an informal '
                                       'action based on only oral notification, it is the date the regulated entity '
                                       'actually received such notification.',
                      'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                     'site.',
                      'AGENCY_NAME': 'The name of the agency, department, or organization that submitted the '
                                     'Enforcement Action data to EPA.',
                      'ARCHIVE_FLAG': 'This column is not currently being used.',
                      'BRANCH': 'The Branch or Unit of the Office of Regional Counsel assigned for the case.',
                      'CORE_FLAG': 'A flag that indicates whether the Enforcement Action is being brought under the '
                                   'Core program as opposed to under a National or Regional Priority.',
                      'COST_OF_HEARING_ACTUAL': 'The actual cost of the hearing for an Enforcement Action.',
                      'COST_OF_HEARING_PROPOSED': 'The proposed cost of a hearing for the Enforcement Action.',
                      'COST_RECOVERY_SOUGHT_AMT': 'The dollar amount of any proposed cost recovery set forth in a '
                                                  'Complaint/Proposed Order.  If the Enforcement Action seeks '
                                                  'reimbursement of future government costs not yet expended and the '
                                                  'among of such future costs can be accurately estimated within '
                                                  'reason, such costs can be considered a Cost Recovery Sought Amount.',
                      'COURT_ENF_NAME': 'The name of the Enforcement Action as referred to by the Court in which the '
                                        'action was filed.',
                      'DOJ_DOCKET_NMBR': "The docket number assigned by the Department of Justice to EPA''s "
                                         'Enforcement Action.',
                      'DOJ_ENF_NAME': 'The name assigned by the Department of Justice to the Enforcement Action.',
                      'ENF_IDENTIFIER': 'Limited enforcement action data are provided from ICIS FE&C where a NPDES '
                                        'program interest linkage exists. More detailed information about linked '
                                        'enforcement actions can be obtained from the ICIS FE&C download files, by '
                                        'using the Enforcement Action Identifier (ENF_IDENTIFIER).',
                      'ENF_NAME': 'The name assigned to the Enforcement Action by the lead attorney; generally the '
                                  "primary defendant''s name is used as the enforcement name.",
                      'ENF_OUTCOME_DESC': 'A description of the mechanism by which the Enforcement Action is resolved.',
                      'ENF_SUMMARY_TEXT': 'The summary of the violation environmental problem and a description of the '
                                          'cause of action (basis of legal action).  The summary could be extracted '
                                          'from the referral transmission memo or letter or it could be required as '
                                          'the first section of a revised standardized referral document.',
                      'FILED_DATE': 'The date on which the Enforcement Action was filed with the Court.',
                      'GEO_INITIATIVE_NARRATIVE': 'A description of the geographic/community initiative as a part of '
                                                  'which the Responsible Office developed the case.',
                      'HIST_COURT_DOCKET_NMBR': 'Legacy data no longer displayed on the screens or in reporting.',
                      'HQ_DIVISION': 'The EPA Headquarters division that is tracking the case.',
                      'JUDICIAL_DISTRICT_DESC': 'The name of the Judicial District Court where the case is filed or '
                                                'the consent decree is lodged and entered.',
                      'LAST_UPDATED_BY': 'The last user to update the data in any of the ICIS_ENFORCEMENT child '
                                         'tables.',
                      'LAST_UPDATED_DATE': 'The date on which the data for any of the ICIS_ENFORCEMENT child tables '
                                           'was updated.',
                      'LEGAL_ID': 'The Regional Hearing Clerk number.',
                      'MULTIREGIONAL_FLAG': 'A flag that indicates whether the Enforcement Action is part of a '
                                            'National case.',
                      'NOTICE_PLEADING_FLAG': 'A flag that indicates that EPA will seek the maximum penalty allowed by '
                                              'the law (I.e., the statutory maximum) when a specific penalty amount is '
                                              'not given.',
                      'OTHER_WATER_PROGRAM_VIOLATED': 'A free-form text description of other alleged violation(s) '
                                                      'addressed a federal Enforcement Action.',
                      'OVERFILE_FLAG': 'A flag that indicates whether the EPA has taken an Enforcement Action in a '
                                       'delegated program where the state has already taken action.',
                      'PENALTY_SOUGHT_AMT': 'The dollar amount of any proposed cash civil penalty set forth in the '
                                            'filed complaint or issued order. This does not include the value of any '
                                            'SEPs that may be included in any resolution of the Enforcement Action, '
                                            'the value of any Stipulated Penalties that may be sought for '
                                            'noncompliance with a Final Order, or the value of any injunctive relief '
                                            'that might be required by the Final Order.',
                      'REFERRED_DATE': 'The date on which the Enforcement Action was referred.',
                      'REFERRED_OFFICE_ID': 'The unique identifier of the office referring the Enforcement Action.',
                      'STATE_LAW_SECTION_VIOLATED': 'The section of the federal statute violated in a state-issued '
                                                    'Enforcement Action.',
                      'TOTAL_COMP_ACTION_AMT': 'The total dollar value of all complying actions (I.e., Direct '
                                               'Environmental Reduction, Preventative, and Facility Management and '
                                               'Information Practices) for the Enforcement Action.',
                      'TOTAL_COST_RECOVERY_AMT': 'The total dollar amount of cost recovery awarded for the Enforcement '
                                                 'Action.',
                      'TOTAL_PENALTY_ASSESSED_AMT': 'The total dollar amount of penalties assessed for the Enforcement '
                                                    'Action.',
                      'VOLUNTARY_SELF_DISCLOSURE_FLAG': 'A flag that indicates the Enforcement Action was the result '
                                                        'of a self disclosure.'},
 'ICIS_ENF_CONCLUSION': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                        'site.',
                         'ACTUAL_TERMINATION_DATE': 'The date on which the Final Order was terminated.',
                         'AGREEMENT_IN_PRINCIPLE_DATE': 'The date on which an agreement is reached between the '
                                                        'defendants and EPA on the terms of the Final Order.',
                         'ALT_DISPUTE_RESOLUTION_FLAG': 'A flag that indicates whether an alternative dispute '
                                                        'resolution (ADR) was used to settle the Enforcement Action.  '
                                                        'ADR is a procedure such as mediation or arbitration that is '
                                                        'used by EPA is resolving differences with companies over '
                                                        'enforcement related issues in lieu of traditional enforcement '
                                                        'methods.',
                         'COST_RECOVERY_AWARDED_AMT': 'The amount of cost recovery ordered or agreed to be repaid by '
                                                      'the responsible party or parties and due the Superfund in '
                                                      'accordance with either an administrative or judicial '
                                                      'settlement.',
                         'COST_RECOVERY_COLLECTED_AMT': 'The total cost recovery amount collected by the EPA.',
                         'COST_RECOVERY_OTHER_AMT': 'Duplicate of Other_Cost_Recovery_AMT.  It is not currently being '
                                                    'used.',
                         'DOCKET_CONSENT_ID': 'The Consent ID of the Final Order from legacy Docket (i.e., converted '
                                              'data).  This is for historical purposes only and is not captured in '
                                              'ICIS through the application.',
                         'EMS_REQUESTED_FLAG': 'A flag that indicates whether Environmental Management Systems (EMS) '
                                               'input was requested for this Final Order.',
                         'ENF_CONCLUSION_ACTION_DESC': 'A description of the  enforcement instrument used by EPA to '
                                                       'settle the case.',
                         'ENF_CONCLUSION_ID': 'The system generated unique identifier of the Final Order record.',
                         'ENF_CONCLUSION_NAME': 'The name of a Final Order associated with an Enforcement Action as '
                                                'assigned by the Lead EPA Attorney for federal actions.',
                         'ENF_CONCLUSION_NMBR': 'A sequential number indicating the Final Order number within the '
                                                'Enforcement Action (e.g., if the Final Order ID is 4, the Final Order '
                                                'is the 4th Final Order entered into ICIS for the parent Enforcement '
                                                'Action).',
                         'ENF_CONCLUSION_TEXT': 'The free-form text description of the Final Order.',
                         'ESTIMATED_TERMINATION_DATE': 'The date on which the Final Order is scheduled to terminate.',
                         'FEDERAL_AGENCY_NAME': 'The Federal Agency/Bureau name.',
                         'FED_PENALTY_ASSESSED_AMT': 'The dollar amount of federal civil penalties assessed or agreed '
                                                     'to at a formal enforcement action. Where the enforcement case '
                                                     'results in multiple settlements, this represents the sum of '
                                                     'penalty amounts for all of the settlements.',
                         'HISTORIC_SEP_AMT': 'The SEP amount that was converted from Docket into ICIS Phase I but is '
                                             'not captured in ICIS-NPDES because it is considered historic.',
                         'IFMS_NMBR': 'The Financial Management System (IFMS) number. (This number is not captured in '
                                      'ICIS through the application.)',
                         'MOST_RECENT_AMENDMENT_DATE': 'The date of the last amendment made to the Final Order.',
                         'NPDES_CLOSED_DATE': 'Date when the Final Order is closed for all of its NPDES components.',
                         'NPDES_CLOSED_SYS_GEN_FLAG': "Flag indicating whether the Final Order''s NPDES closed date "
                                                      'was entered by the user or by the closure of the source '
                                                      'Enforcement Action.',
                         'OTHER_COST_RECOVERY_AMT': 'Other cost recovery amounts collected by EPA pursuant to a Final '
                                                    'Order.',
                         'PENALTY_COLLECTED_AMT': 'The total Federal Penalty amount collected pursuant to a Final '
                                                  'Order.',
                         'PENALTY_COLLECTED_FLAG': 'A flag that indicates whether the penalty has been collected.  '
                                                   '(This flag is not captured in ICIS through the application.).',
                         'QNCR_COMMENT_TEXT': 'This is a short EA Final Order comment that appears on the QNCR.',
                         'REGIONAL_DOCUMENT_NICK_NAME': 'The regionally defined name of the Final Order.  (Captured in '
                                                        'ICIS Phase l and kept in the database for historical purposes '
                                                        'but not captured in ICIS-NPDES.).',
                         'SETTLEMENT_ENTERED_DATE': 'The date of the enforcement action (MM/DD/YYYY). Where multiple '
                                                    'settlements are associated with a single enforcement action, this '
                                                    'represents the earliest date entered.',
                         'SETTLEMENT_LODGED_DATE': 'The date the settlement document is given to the Clerk of the '
                                                   'Court for lodging in the District Court; it is the date the Clerk '
                                                   'stamps on the document. (Federal Judicial EAs only).',
                         'STATE_LOCAL_COST_RECOVERY_AMT': 'The share due to the state/local government of the cost '
                                                          'recovery awarded pursuant to a Final Order.',
                         'STATE_LOCAL_PENALTY_AMT': 'The dollar amount of state or local civil penalties assessed or '
                                                    'agreed to at a formal enforcement action. Where the enforcement '
                                                    'case results in multiple settlements, this represents the sum of '
                                                    'penalty amounts for all of the settlements.'},
 'ICIS_ENF_CONCL_POLLUTANT': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                             'particular site.',
                              'CHEMICAL_ABSTRACT_SERVICE_NMBR': 'This is the unique number assigned to a chemical '
                                                                'substance by the Chemical Abstracts Service.',
                              'CHEMICAL_FORMULA': 'This is the pollutant chemical formula name.',
                              'ENF_CONCLUSION_ID': 'The system generated unique identifier of the Final Order record.',
                              'POLLUTANT_CATEGORY_CODE': 'This is the code identifying the pollutant category for '
                                                         'media and reporting purposes.',
                              'POLLUTANT_CATEGORY_DESC': 'The description of the pollutant category.',
                              'POLLUTANT_CODE': 'A code that uniquely identifies the pollutant associated to a '
                                                'compliance/enforcement activity.',
                              'POLLUTANT_DESC': 'The name that EPA has selected as its preferred name for a substance '
                                                '(also known as registry name). If the registry name is not available, '
                                                'use the systematic name instead.',
                              'SRS_ID': 'This is the unique identifier assigned to a substance for internal tracking '
                                        'within EPA systems.',
                              'SRS_SYSTEMATIC_NAME': 'The Substance Registry System (SRS) name for the pollutant.'},
 'ICIS_ENF_CONCL_STATUTE': {'ENF_CONCLUSION_ID': 'The system generated unique identifier of the Final Order record.',
                            'STATUTE_CODE': 'The unique code that identifies the law which is authorizing the activity '
                                            'or being violated.',
                            'STATUTE_DESC': 'The name of the law authorizing the activity or being violated.'},
 'ICIS_ENF_CONCL_VIOLATION': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                             'particular site.',
                              'ENF_CONCLUSION_ID': 'The system generated unique identifier of the Final Order record.',
                              'VIOLATION_TYPE_CODE': 'A derived code to differentiate violation records. Valid code '
                                                     'values are:',
                              'VIOLATION_TYPE_DESC': 'VIOLATION_TYPE_DESC'},
 'ICIS_ENF_ENVIRON_JUSTICE': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                             'particular site.',
                              'ENVIRONMENTAL_JUSTICE_CODE': 'The code identifying the type of Environmental Justice '
                                                            'Concern affecting the enforcement action.',
                              'ENVIRONMENTAL_JUSTICE_DESC': 'A text description of the Environmental Justice Concern '
                                                            'affecting the facility or Enforcement Action.'},
 'ICIS_ENF_REGIONAL_DOCKET': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                             'particular site.',
                              'ENF_REGIONAL_DOCKET_ID': 'The sequence ID identifying the Enforcement Action regional '
                                                        'docket information.',
                              'REGIONAL_DOCKET_NMBR': 'The number the Clerk of the Court assigns to a case that is '
                                                      'filed or to a consent decree when it is lodged.  For '
                                                      'administrative cases, it is the number assigned to the case by '
                                                      'the Regional Hearing Clerk.'},
 'ICIS_ENF_RELIEF': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                    'site.',
                     'RELIEF_CODE': 'The code indicating the type of relief requested in the complaint.',
                     'RELIEF_DESC': 'The description for the type of relief requested in the complaint.'},
 'ICIS_ENF_TYPE': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular site.',
                   'ENF_TYPE_CODE': 'A code describing which enforcement action was taken in response to a violation.',
                   'ENF_TYPE_DESC': 'A text description of the ENF_TYPE_CODE value.'},
 'ICIS_ENF_VIOLATION': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                       'site.',
                        'RANK_ORDER': 'The sort order for the Violation type on the Enforcement Action.',
                        'VIOLATION_TYPE_CODE': 'A derived code to differentiate violation records. Valid code values '
                                               'are:',
                        'VIOLATION_TYPE_DESC': 'VIOLATION_TYPE_DESC'},
 'ICIS_FACILITY_ADDRESS': {'ADDRESS_ID': 'The unique identifier for an address related to a particular site.',
                           'AFFILIATION_TYPE_DESC': 'uniquely identifies the Affiliation type of the address to the '
                                                    'facility interest.',
                           'BEGIN_DATE': 'The date at which the affiliation between facility interest and contact '
                                         'initiated.',
                           'CITY': 'A 60 character field that contains the name of the city in which the facility is '
                                   'located.',
                           'COUNTRY_DESC': 'The name of the country.',
                           'COUNTY': 'The code that represents the county or county equivalent.',
                           'DIVISION_NAME': 'The name of a division or a department of a company.',
                           'END_DATE': 'The date on which the affiliation between the facility interest and the '
                                       'organization and/or individual person ended.',
                           'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the facility '
                                                        'interest.',
                           'ORGANIZATION_DUNS_NMBR': 'The Data Universal Numbering System (DUNS) number assigned by '
                                                     'Dun and Bradstreet identifying the unique business '
                                                     'establishments.',
                           'ORGANIZATION_FORMAL_NAME': 'The legal, formal name of an organization that is affiliated '
                                                       'with the facility site.',
                           'PROVINCE': 'The Province or City District of a Trade Partner for an international address.',
                           'STATE_DESC': 'The name of a principal administrative subdivision of the U.S., Canada, or '
                                         'Mexico.',
                           'STATE_REGION': 'Unique code identifying particular regions (e.g., counties) within a '
                                           'state.',
                           'STREET_ADDRESS': 'The address that describes the physical (geographic) location of the '
                                             'front door or main entrance of a facility site, including urban-style '
                                             'street address or rural address.',
                           'SUPPLEMENTAL_ADDRESS_TEXT': 'The name of the supplemental location for the facility.',
                           'ZIP': 'A 9-character field that contains the U.S. Postal Zone Improvement Plan (ZIP) code '
                                  'for the area in which the facility is located.'},
 'ICIS_FACILITY_INTEREST': {'CITY': 'A 60 character field that contains the name of the city in which the facility is '
                                    'located.',
                            'CITY_NAME': 'The name of the city in which the address exists.',
                            'COMMENT_TEXT': 'The free-form textual comments entered by the user/analyst to further '
                                            'describe the corresponding data.',
                            'CONGRESSIONAL_DIST_NUM': 'The number of the Congressional District in which the facility '
                                                      'site is located.',
                            'CONSTRUCTION_PROJECT_LAT': 'The measure of the angular distance on a meridian north or '
                                                        'south of the equator for a Construction Project; stored in '
                                                        'decimal degrees.',
                            'CONSTRUCTION_PROJECT_LONG': 'The measure of the angular distance on a meridian east or '
                                                         'west of the prime meridian for a Construction Project; '
                                                         'stored in decimal degrees.',
                            'CONSTRUCTION_PROJECT_NAME': 'The name of the construction project.',
                            'COUNTRY_DESC': 'The name of the country.',
                            'COUNTY_NAME': 'The name of the county from FIPS.',
                            'ENVIRONMENTAL_JUSTICE_DESC': 'A text description of the Environmental Justice Concern '
                                                          'affecting the facility or Enforcement Action.',
                            'FACILITY_NAME': 'An 80-character field that contains the name of the facility.',
                            'FACILITY_TYPE_DESC': 'The description identifying the type of facility (e.g., State '
                                                  'Government, Municipal or Water Distric, Federal Facility).  This '
                                                  'data element is used by the system to populate the Permit Facility '
                                                  'Type data element (i.e., POTW, Non-POTW, Federal).',
                            'FACILITY_UIN': 'The number assigned by the Facility Linkage Application that is used to '
                                            'associate facility records from multiple environmental database systems '
                                            'that are known or believed to represent the same facility.',
                            'FEDERAL_AGENCY_NAME': 'The Federal Agency/Bureau name.',
                            'FEDERAL_FACILITY_FLAG': 'Flag indicating if the Facility interest is a Federal Facility '
                                                     'Interest.',
                            'FEDERAL_FACILITY_ID': 'The unique code of a federal facility.',
                            'GEOCODE_LATITUDE': 'The latitude of the facility or permit holder as maintained in each '
                                                'data system. The FRS lat/long is from the EPA Locational Reference '
                                                'Tables (LRT) file which represents the "best" value for the latitude '
                                                'and longitude coordinates.',
                            'GEOCODE_LONGITUDE': 'The longitude of the facility or permit holder as maintained in each '
                                                 'data system. The FRS lat/long is from the EPA Locational Reference '
                                                 'Tables (LRT) file.',
                            'GEOMETRIC_TYPE_NAME': 'The name that identifies the geometric entity represented by one '
                                                   'point or a sequence of latitude and longitude points.',
                            'HORIZONTAL_ACCURACY_MEASURE': 'The measure of the accuracy (in meters) of the latitude '
                                                           'and longitude coordinates.',
                            'HORIZONTAL_COLLECT_METHOD_TEXT': 'The text that describes the method used to determine '
                                                              'the latitude and longitude coordinates for a point on '
                                                              'the earth.',
                            'HORIZONTAL_REF_DATUM_NAME': 'The text to define the DATUM reference for geographic '
                                                         'coordinates.',
                            'HUC_CODE': 'This is the Hydrologic Basin Code for non-discharging facilities.',
                            'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the facility '
                                                         'interest.',
                            'LEGISLATIVE_DIST_NUM': 'The number of the State Legislative District in which the '
                                                    'facility site is located.',
                            'LOCATION_ADDRESS': 'The street address of the facility.',
                            'NPL_FLAG': 'The flag that indicates whether the regulated entity is a National Priority '
                                        'List (NPL) site.',
                            'ORGANIZATION_DUNS_NMBR': 'The Data Universal Numbering System (DUNS) number assigned by '
                                                      'Dun and Bradstreet identifying the unique business '
                                                      'establishments.',
                            'PGM_SYS_ACRNM': 'The abbreviated name that represents the name of an information '
                                             'management system for an environmental program.',
                            'PGM_SYS_ID': 'The unique ID used by the environmental programs when identifying the '
                                          'facility interest.',
                            'REFERENCE_POINT_CODE': 'The place for which geographic coordinates were established.',
                            'REFERENCE_POINT_DESC': 'The code to define the DATUM reference for Permit feature source '
                                                    'coordinates.',
                            'REGION_DESC': 'The text description for the unique code that identifies the EPA region.',
                            'SECTION_TOWNSHIP_RANGE': 'The township, section, range etc. of the facility interest.',
                            'SENSITIVE_DATA_FLAG': 'The flag indicating whether the activity contains sensitive or '
                                                   'non-sensitive data.',
                            'SMALL_BUSINESS_FLAG': 'The flag indicating if the facility meets the requirements of the '
                                                   'EPA Small Business Policy.',
                            'SOURCE_MAP_SCALE_NMBR': 'The number that represents the proportional distance on the '
                                                     'ground for one unit of measure on the map or photo.',
                            'STATE_CODE': 'A two-character field that contains the state postal abbreviation for the '
                                          'state in which the facility is located.',
                            'STATE_DESC': 'The name of a principal administrative subdivision of the U.S., Canada, or '
                                          'Mexico.',
                            'STATE_FACILITY_ID': 'Unique identifier within a state for a Facility Interest.',
                            'STATE_REGION': 'Unique code identifying particular regions (e.g., counties) within a '
                                            'state.',
                            'SUPPLEMENTAL_ADDRESS_TEXT': 'The name of the supplemental location for the facility.',
                            'TRIBAL_LAND_FLAG': 'The flag indicating whether or not the facility interest is located '
                                                'on tribal lands.',
                            'TRIBAL_LAND_R_CODE': 'The unique identifier for every unit of land within Indian Country.',
                            'UDF1': 'The user defines this field.',
                            'UDF2': 'The user defines this field.',
                            'UDF3': 'The user defines this field.',
                            'UDF4': 'The user defines this field.',
                            'UDF5': 'The user defines this field.',
                            'ZIP': 'A 9-character field that contains the U.S. Postal Zone Improvement Plan (ZIP) code '
                                   'for the area in which the facility is located.'},
 'ICIS_FACILITY_NAICS': {'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the facility '
                                                      'interest.',
                         'NAICS_CODE': 'The 6-digit North American Industry Classification System (NAICS) code that '
                                       'represents a subdivision of an industry that accommodates user needs in the '
                                       'United States. For detailed information about NAICS and for a crosswalk '
                                       'between NAICS and SIC codes, please check the',
                         'NAICS_DESC': 'The corresponding description of North American Industry Classification System '
                                       '(NAICS) code.',
                         'PRIMARY_INDICATOR_FLAG': 'The flag indicating whether the NAICS or SIC code is the primary '
                                                   'code for the Facility. Value is (Y)es or No (null value).'},
 'ICIS_FACILITY_POLICY': {'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the facility '
                                                       'interest.',
                          'POLICY_CODE': 'The code identifying the policy type associated with the facility interest.',
                          'POLICY_DESC': 'The description of the policy associated with the facility interest.'},
 'ICIS_FACILITY_PROGRAM': {'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the facility '
                                                        'interest.',
                           'PROGRAM_CODE': 'The code that identifies the program associated with an activity.',
                           'PROGRAM_DESC': 'The description of an EPA program associated with an activity.'},
 'ICIS_FACILITY_SIC': {'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the facility '
                                                    'interest.',
                       'PRIMARY_INDICATOR_FLAG': 'The flag indicating whether the NAICS or SIC code is the primary '
                                                 'code for the Facility. Value is (Y)es or No (null value).',
                       'SIC_CODE': 'The 4-digit Standard Industrial Classification (SIC) code that represents the '
                                   'economic activity of a company. Note the NAICS classification system replaced the '
                                   'SIC classification system in 1997. These SIC codes are no longer collected by some '
                                   'EPA programs. A list of codes may be found at the',
                       'SIC_DESC': 'The corresponding description of the Standard Industrial Classification (SIC) '
                                   'code.'},
 'ICIS_LIMIT': {'BASIS_OF_LIMIT_DESC': 'The description of the source of the limit.',
                'BURDEN_REDUCTION_FLAG': 'The indication of whether a limit parameter is eligible for monitoring '
                                         'burden reduction.',
                'CHANGE_LIMIT_STATUS_DESC': 'The description that describes circumstances affecting limits such as '
                                            'formal enforcement action final orders or permit modifications.',
                'CHEMICAL_ABSTRACT_SERVICE_NMBR': 'This is the unique number assigned to a chemical substance by the '
                                                  'Chemical Abstracts Service.',
                'CHEMICAL_FORMULA': 'This is the pollutant chemical formula name.',
                'CREATION_TYPE_DESC': 'The description of how a record was created.',
                'ENF_CONCLUSION_ID': 'The system generated unique identifier of the Final Order record.',
                'EPA_ID': 'This is the EPA Identifier for substances.',
                'FREQUENCY_OF_ANALYSIS_DESC': 'The description of the frequency with which the permittee must analyze '
                                              'the sampled data.',
                'LIMIT_BEGIN_DATE': 'The date on which a limit starts being in effect for a particular parameter in a '
                                    'limit set.',
                'LIMIT_END_DATE': 'The date on which a limit stops being in effect for a particular parameter in a '
                                  'limit set.',
                'LIMIT_ID': 'The unique identifier for a limit parameter record.',
                'LIMIT_SEASON_ID': 'Indicates the season of a limit and is used to enter different seasonal limits for '
                                   'the same parameter within a single limit start and end date.',
                'LIMIT_SET_ID': 'The unique identifier of the Limit Set which has the default statistical base code '
                                'for its limits.',
                'LIMIT_TYPE_DESC': 'The description that indicates whether a limit is an effluent or alert limit.',
                'MODIFICATION_EFFECTIVE_DATE': 'The type of Permit Modification that created this Limit (e.g., Major, '
                                               'Minor, Permit Authorized Change).',
                'MODIFICATION_TYPE_DESC': 'The description of the type of permit modification which spawned the change '
                                          'to the limit set or limit.',
                'MONITORING_LOCATION_DESC': 'The description that the monitoring location at which the monitoring '
                                            'requirement (and effluent limit if limited) applies.  One parameter may '
                                            'have several monitoring location requirements pertaining to the same '
                                            'permitted feature.',
                'PARAMETER_DESC': 'Text description of the PARAMETER_CODE.',
                'PERCENT_EXCEEDENCE_FLAG': 'The flag indicating whether percent exceedence can be calculated for the '
                                           'parameter.',
                'PERCENT_REMOVAL_FLAG': 'The flag indicating whether the parameter is a percent removal parameter for '
                                        'determining the formula to use for calculating the percent exceedence for the '
                                        'parameter.',
                'POLLUTANT_CATEGORY_DESC': 'The description of the pollutant category.',
                'POLLUTANT_DESC': 'The name that EPA has selected as its preferred name for a substance (also known as '
                                  'registry name). If the registry name is not available, use the systematic name '
                                  'instead.',
                'SAMPLE_TYPE_DESC': 'The description of the unique code identifying the sampling method required by '
                                    'the permit to be used to provide measurement values on the DMR.',
                'SRS_ID': 'This is the unique identifier assigned to a substance for internal tracking within EPA '
                          'systems.',
                'SRS_SYSTEMATIC_NAME': 'The Substance Registry System (SRS) name for the pollutant.',
                'STAY_BEGIN_DATE': 'The date on which a limit stay begins.',
                'STAY_END_DATE': 'The placeholder for the end date of a stay applied against the permit schedule '
                                 'event. Not currently used.',
                'STAY_REASON_TEXT': 'The text describing the reason for the stay on the narrative condition. Not '
                                    'currently used.',
                'STAY_TYPE_DESC': 'The description of the stay type.',
                'STAY_VALUE_CALC_FLAG': 'The flag indicating if the system will calculate violations for the DMR '
                                        'values for the limit after the stay is lifted.',
                'UDF1': 'The user defines this field.',
                'UDF2': 'The user defines this field.',
                'UDF3': 'The user defines this field.',
                'UNIT_GROUP_DESC': 'The short description of the unit of measure applicable to limit or DMR values.'},
 'ICIS_LIMIT_MONTH': {'LIMIT_ID': 'The unique identifier for a limit parameter record.',
                      'MONTH_DESC': 'The description of the calendar month.',
                      'XREF_LIMIT_MONTH_ID': 'The sequence ID identifying the Limit and Month relationship.'},
 'ICIS_LIMIT_SET': {'AGENCY_REVIEWER': 'The code indicating the person and/or department responsible for administering '
                                       'each DMR; the agency reviewer is displayed at the top of each pre-printed DMR '
                                       'form for the limit set.',
                    'CREATION_TYPE_DESC': 'The description of how a record was created.',
                    'DMR_COMMENT_TEXT': 'The comments that are entered by the permittee at the bottom of the '
                                        'pre-printed DMR form.',
                    'LIMIT_SET_DESIGNATOR': 'The alphanumeric field that is used to designate a particular grouping of '
                                            'parameters within a limit set.',
                    'LIMIT_SET_ID': 'The unique identifier of the Limit Set which has the default statistical base '
                                    'code for its limits.',
                    'LIMIT_SET_NAME': 'The name of the limit set; this data element is reported on the DMR Pre-Print.',
                    'LIMIT_SET_TYPE_DESC': 'The description identifying the type of limit set.',
                    'MASTER_LIMIT_SET_ID': 'The placeholder for identifying a Master General Permit Limit Set for a '
                                           'General Permit Covered Facility Limit Set. Not currently used.',
                    'PERM_FEATURE_ID': 'The unique system identifier for a permitted feature.',
                    'REPORT_FREQUENCY_DESC': 'This is the description of the unit to be used for measuring DMR '
                                             'frequency.',
                    'UDF1': 'The user defines this field.',
                    'UDF2': 'The user defines this field.'},
 'ICIS_LIMIT_SET_MONTH': {'LIMIT_SET_ID': 'The unique identifier of the Limit Set which has the default statistical '
                                          'base code for its limits.',
                          'MONTH_DESC': 'The description of the calendar month.',
                          'XREF_LIMIT_SET_MONTH_ID': 'The sequence ID identifying the Limit Set and Month '
                                                     'relationship.'},
 'ICIS_LIMIT_SET_SCHEDULE': {'INITIAL_DMR_DUE_DATE': 'The date that the first DMR for the limit set is due to the '
                                                     'regulatory authority; this date will be blank for Unscheduled '
                                                     'Limit Sets.',
                             'INITIAL_MONITORING_DATE': 'The date on which monitoring starts for the first monitoring '
                                                        'period for the limit set; this date will be blank for '
                                                        'Unscheduled Limit Sets.',
                             'LIMIT_SET_ID': 'The unique identifier of the Limit Set which has the default statistical '
                                             'base code for its limits.',
                             'LIMIT_SET_SCHEDULE_ID': 'The sequence ID identifying the Limit Set Schedule.',
                             'MODIFICATION_EFFECTIVE_DATE': 'The type of Permit Modification that created this Limit '
                                                            '(e.g., Major, Minor, Permit Authorized Change).',
                             'MODIFICATION_TYPE_DESC': 'The description of the type of permit modification which '
                                                       'spawned the change to the limit set or limit.',
                             'NMBR_OF_REPORT': 'The number of months covered by the DMR for which the effluent '
                                               'violation was generated (e.g., monthly = 1, quarterly = 3, '
                                               'semi-annually = 6).',
                             'NMBR_OF_SUBMISSION': 'The attribute stores the number of months for submitting the DMRs '
                                                   'for the limit set (e.g., monthly = 1, semi-annually = 6, quarterly '
                                                   '= 3); this data element will be blank for Unscheduled Limit Sets.'},
 'ICIS_LIMIT_SET_STATUS': {'LIMIT_SET_ID': 'The unique identifier of the Limit Set which has the default statistical '
                                           'base code for its limits.',
                           'LIMIT_SET_STATUS_ID': 'The system-generated unique ID of the Limit Set Status record.',
                           'STATUS_BEGIN_DATE': 'The date that the Limit Set Status started.',
                           'STATUS_CHANGE_REASON_TEXT': 'The reason the Limit Set Status changed.',
                           'STATUS_END_DATE': 'This is the date on which the permit\'s on or off period for compliance '
                                              'tracking status ended.',
                           'STATUS_FLAG': 'The status of the Limit Set (i.e., Active or Inactive); Limit Sets will not '
                                          'have violations generated when a Limit Set is Inactive unless an '
                                          'Enforcement Action Limit is present.'},
 'ICIS_LIMIT_TRADE_PARTNER': {'CITY': 'A 60 character field that contains the name of the city in which the facility '
                                      'is located.',
                              'COUNTRY_CODE': 'The unique code that identifies a country .',
                              'COUNTY': 'The code that represents the county or county equivalent.',
                              'DIVISION_NAME': 'The name of a division or a department of a company.',
                              'LIMIT_ID': 'The unique identifier for a limit parameter record.',
                              'LIMIT_TRADE_PARTNER_ID': 'Unique identifier for an effluent trade partner for a limit.',
                              'LOCATION_NAME': 'The name of the location for the trade partner.',
                              'ORGANIZATION_DUNS_NMBR': 'The Data Universal Numbering System (DUNS) number assigned by '
                                                        'Dun and Bradstreet identifying the unique business '
                                                        'establishments.',
                              'ORGANIZATION_FORMAL_NAME': 'The legal, formal name of an organization that is '
                                                          'affiliated with the facility site.',
                              'PROVINCE': 'The Province or City District of a Trade Partner for an international '
                                          'address.',
                              'STATE_CODE': 'A two-character field that contains the state postal abbreviation for the '
                                            'state in which the facility is located.',
                              'STREET_ADDRESS': 'The address that describes the physical (geographic) location of the '
                                                'front door or main entrance of a facility site, including urban-style '
                                                'street address or rural address.',
                              'SUPPLEMENTAL_ADDRESS_TEXT': 'The name of the supplemental location for the facility.',
                              'TRADE_ID': 'The ID identifying the Trade in the business world.',
                              'TRADE_PARTNER_BEGIN_DATE': 'The start date of a trade partner\'s association with a '
                                                          'limit.',
                              'TRADE_PARTNER_END_DATE': 'The end date of a trade partner\'s association with a limit.',
                              'TRADE_PARTNER_NPDES_ID': 'The NPDES ID of a Point Source or Non-Point Source trade '
                                                        'partner that is also tracked in the system.',
                              'TRADE_PARTNER_OTHER_ID': 'The Non-NPDES ID of a Non-Point Source or a Bank that is not '
                                                        'tracked in the system.',
                              'TRADE_PARTNER_TYPE_DESC': 'The description of the trade partner type.',
                              'ZIP': 'A 9-character field that contains the U.S. Postal Zone Improvement Plan (ZIP) '
                                     'code for the area in which the facility is located.'},
 'ICIS_LIMIT_VALUE': {'CREATION_TYPE_DESC': 'The description of how a record was created.',
                      'LIMIT_ID': 'The unique identifier for a limit parameter record.',
                      'LIMIT_VALUE_ID': 'The system-generated unique identifier for the Limit Value.',
                      'LIMIT_VALUE_NMBR': 'The actual limit value number from the Permit or Enforcement Action Final '
                                          'Order.',
                      'LIMIT_VALUE_STANDARD_UNITS': 'The limit value expressed in standard units as calculated by the '
                                                    'system.',
                      'OPTIONAL_MONITORING_FLAG': 'The flag allowing users to indicate that monitoring is optional  '
                                                  'but not required (i.e., effluent violation generation will be '
                                                  'suppressed for optional columns).',
                      'STATISTICAL_BASE_DESC': 'The description of the statistical base type.',
                      'STATISTICAL_BASE_LONG_DESC': 'The long description of the statistical base code.',
                      'STATISTICAL_BASE_MONTHLY_AVG': 'The data element indicating whether the statistical base code '
                                                      'is a monthly average, non-monthly average, or neither for '
                                                      'purposes of calculating RNC.',
                      'STATISTICAL_BASE_SHORT_DESC': 'The short description of the statistical base code.',
                      'STAY_VALUE_NMBR': 'The numeric limit value imposed during the period of the stay for the limit; '
                                         'if entered, during the stay period, the system will use this limit value for '
                                         'calculating compliance rather than the actual limit value.',
                      'STAY_VALUE_STANDARD_UNITS': 'The stay value expressed in standard units as calculated by the '
                                                   'system.',
                      'UNIT_DESC': 'The description of the unit of measure applicable to limit or DMR values.',
                      'UNIT_SHORT_DESC': 'The short description of the unit of measure applicable to limit or DMR '
                                         'values.',
                      'VALUE_QUALIFIER_DESC': 'The code that allows a user to indicate the direction of the value when '
                                              'an alternate limit value is possible (e.g., less than, greater than, '
                                              'and too numerous).',
                      'VALUE_TYPE_DESC': 'The description for the value type.'},
 'ICIS_NPDES_VIOLATION': {'AGENCY_TYPE_DESC': 'The name of the government agency identified by Agency code.',
                          'COMP_SCHEDULE_EVENT_ID': '(Compliance Schedule Event ID) The unique identifier of the '
                                                    'Compliance Schedule Event to which the Violation is associated; '
                                                    'it is only used for Schedule Violations of a Final Order.',
                          'DMR_FORM_VALUE_ID': 'The sequence ID identifying the DMR Form Value.',
                          'NPDES_VIOLATION_ID': 'The system-generated unique identifier for the NPDES Violation.',
                          'PERMIT_ACTIVITY_ID': 'The activity ID of the Permit to which the Violation is associated.',
                          'PERM_SCHEDULE_EVENT_ID': 'The unique identifier of the Permit Schedule Event to which the '
                                                    'Violation is associated; it is only used for Schedule Violations '
                                                    'of a Permit.',
                          'RNC_DETECTION_DATE': 'The date associated with RNC_DETECTION_CODE (MM/DD/YYYY).',
                          'RNC_DETECTION_DESC': 'Text description of the code value RNC_DETECTION_CODE.',
                          'RNC_RESOLUTION_DATE': 'The date associated with VIORNRC (MM/DD/YYYY).',
                          'RNC_RESOLUTION_DESC': 'Text description of the code value RNC_RESOLUTION_CODE.',
                          'SINGLE_EVENT_BEGIN_DATE': 'If the Single Event Violation occurred over multiple days, the '
                                                     'date the occurrence began.',
                          'SINGLE_EVENT_END_DATE': 'If the Single Event Violation occurred over multiple days, the '
                                                   'date the occurrence ended.',
                          'SINGLE_EVENT_VIOLATION_COMMENT': 'Comments about the Single Event Violation.',
                          'SINGLE_EVENT_VIOLATION_DATE': 'The date of a single event violation (MM/DD/YYYY).',
                          'SINGLE_EVENT_VIOLATION_UDF1': 'The user defines this field; it is only used for Single '
                                                         'Event Violations.',
                          'SINGLE_EVENT_VIOLATION_UDF2': 'The user defines this field; it is only used for Single '
                                                         'Event Violations.',
                          'SINGLE_EVENT_VIOLATION_UDF3': 'The user defines this field; it is only used for Single '
                                                         'Event Violations.',
                          'SINGLE_EVENT_VIOLATION_UDF4': 'The user defines this field; it is only used for Single '
                                                         'Event Violations.',
                          'SINGLE_EVENT_VIOLATION_UDF5': 'The user defines this field; it is only used for Single '
                                                         'Event Violations.',
                          'VIOLATION_DESC': 'Text description of the VIOLATION_CODE.'},
 'ICIS_PERMIT': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular site.',
                 'ACTUAL_AVERAGE_FLOW_NMBR': 'The flow that a permitted feature actually had at the time of '
                                             'application., expressed as millions of gallons per day (MGD).',
                 'AGENCY_TYPE_DESC': 'The name of the government agency identified by Agency code.',
                 'APPEAL_FLAG': 'This is a flag that indicates if the permit is currently under appeal.',
                 'APP_RECEIVED_DATE': 'This is the date on which the application for a NPDES permit was received.',
                 'BACKLOG_REASON': 'This indicates the reason a permit is backlogged.',
                 'COMMENT_TEXT': 'The free-form textual comments entered by the user/analyst to further describe the '
                                 'corresponding data.',
                 'COMPLETE_APP_RECEIVED_DATE': 'This is the date on which the complete application for a NPDES permit '
                                               'was received.',
                 'CONTROL_AUTH_PERMIT_ID': "The permit ID of the POTW''s or IU''s control authority.",
                 'COVERAGE_EFFECTIVE_DATE': 'This is the date the GPCF was covered by the Master General Permit.',
                 'CREATION_TYPE_DESC': 'The description of how a record was created.',
                 'DMR_COGNIZANT_OFFCL_TELEPHONE': "This is the telephone number of the Permittee''s representative "
                                                  'responsible for completing the DMR.',
                 'DMR_COGNIZANT_OFFICIAL': "This is the name and/or department of the Permittee''s representative "
                                           'responsible for completing the DMR.',
                 'DMR_NON_RECEIPT_FLAG': 'The flag indicating whether the permit is subject to the DMR run. Value is '
                                         '(Y)es or No (null value). DMR_PARAMETER_ID - The system-generated unique '
                                         'identifier for the DMR parameter to which the DMR value belongs.',
                 'EDMR_AUTHORIZATION_FLAG': 'This indicates whether DMRs for the Permit may be submitted '
                                            'electronically.',
                 'EFFECTIVE_DATE': 'The date the permit became effective or is scheduled to become effective '
                                   '(MM/DD/YYYY).',
                 'EXPIRATION_DATE': 'The date the permit expired or is scheduled to expire (MM/DD/YYYY).',
                 'EXTERNAL_PERMIT_NMBR': 'The unique identifier for a Permit.',
                 'FACILITY_TYPE_INDICATOR': 'A 10-character code indicating the facility as either a POTW, non-POTW, '
                                            'or federal entity.',
                 'FEDERAL_GRANT_FLAG': 'This indicates the facility applied for and received Federal grant dollars for '
                                       'construction.  This data provides historical insight into POTW funding.',
                 'GRACE_PERIOD_END_DATE': 'This is the end date of the grace period.',
                 'ISSUE_DATE': 'The date the permit was issued (MM/DD/YYYY).',
                 'ISSUING_AGENCY': 'This is the name of the organization issuing or granting a permit.',
                 'IU_SIGNIFICANT_FLAG': 'This is the equivalent of major/minor determination to determine significant '
                                        'IUs versus non-significant IUs for a POTW.',
                 'LIFECYCLE_STATUS_DESC': 'The description of the lifecycle status of a record.',
                 'MAJOR_MINOR_STATUS_FLAG': 'A 1-character code that designates the facility as a major discharger '
                                            '(M), non-major or minor discharger (N), or that no data is available '
                                            '(null value), such as for unpermitted facilities.\xa0Under the Clean '
                                            'Water Act, a major facility is any NPDES facility or activity classified '
                                            'as such by the regional administrator, or in the case of approved state '
                                            'programs, the regional administrator in conjunction with the state '
                                            'director. Major municipal dischargers include all facilities with design '
                                            'flows of greater than one million gallons per day and facilities with '
                                            'EPA/state approved industrial pretreatment programs. Major industrial '
                                            'facilities are determined based on specific ratings criteria developed by '
                                            'EPA/state. Non-major facilities are those not designated as major.',
                 'MAJOR_RATING_NMBR': 'This is the numeric total of ranking points assigned to non-POTW facilities and '
                                      'used to delineate them as a major or minor facility.  The numeric value entered '
                                      'for this data element comes from the total score assigned to the facility on '
                                      'the NPDES Permit Ranking Work Sheet.',
                 'MASTER_EXTERNAL_PERMIT_NMBR': 'This is the unique identifier for the Master General Permit for a '
                                                'General Permit Covered Facility.',
                 'MODIFICATION_TYPE_DESC': 'The description of the type of permit modification which spawned the '
                                           'change to the limit set or limit.',
                 'MOD_EFFECTIVE_DATE': 'This is the date that the permit modification became (or will become) '
                                       'effective.',
                 'NEW_SOURCE_FLAG': 'This indicates that the permit has a new source of discharge since the last '
                                    'issuance of the permit.',
                 'ORIGINAL_ISSUE_DATE': 'This is the date the first permit was issued for a facility.',
                 'PERMIT_COMP_STATUS_FLAG': 'This is a code that indicates whether the permit is currently on or off '
                                            'for compliance tracking purposes. Value is (Y)es or No (null value).',
                 'PERMIT_NAME': 'This is the name of the facility having the National Pollutant Discharge Elimination '
                                'System (NPDES) permit to discharge pollutants in the waters of the United States.',
                 'PERMIT_STATUS_DESC': 'This is the text that describes whether the permit is Effective, Expired, '
                                       'Administratively Continued, Pending, Not Needed, Retired, or Terminated.',
                 'PERMIT_TYPE_DESC': 'The text describing the type of permit.',
                 'PERM_INDUSTRIAL_CAT_DESC': 'This text that identifies the industrial category of a general permit.',
                 'PERM_STAY_FLAG': 'This field indicates that the permit (or part of the permit) is currently under a '
                                   'stay.',
                 'RECEIVING_POTW_ID': 'These are municipal POTWs that receive discharge from Industrial Users (IUs) to '
                                      'be monitored by PPETS.',
                 'REISSUANCE_PRIORITY': 'This acts as a management tool used by HQ to assign priorities to '
                                        'facilities.  It will allow HQ users to indicate priorities for addressing '
                                        'backlogged or other candidates for reissuance.',
                 'RETIREMENT_DATE': 'The date the permit was retired (YYYYMMDD).',
                 'RNC_TRACKING_FLAG': 'The flag indicating if the RNC tracking is on. Value is (Y)es or No (null '
                                      'value).',
                 'SOURCE_ACTIVITY_ID': 'This is the activity ID of the source.',
                 'STATE_WATER_BODY': "The state's code to identify the water body into which the effluent is "
                                     'discharged for a Permitted Feature.',
                 'STATE_WATER_BODY_NAME': "The state's name for the water body into which the effluent is discharged "
                                          'for a Permitted Feature.',
                 'STAY_REASON_TEXT': 'The text describing the reason for the stay on the narrative condition. Not '
                                     'currently used.',
                 'TERMINATION_DATE': 'The date the permit was terminated (MM/DD/YYYY).',
                 'TMDL_INTERFACE_FLAG': 'This field indicates whether a Permit has received TMDL information.',
                 'TOTAL_DESIGN_FLOW_NMBR': 'This is the flow that a permitted facility was designed to accommodate, '
                                           'expressed as millions of gallons per day (MGD).',
                 'UDF1': 'The user defines this field.',
                 'UDF2': 'The user defines this field.',
                 'UDF3': 'The user defines this field.',
                 'UDF4': 'The user defines this field.',
                 'UDF5': 'The user defines this field.',
                 'VERSION_NMBR': 'The version of the permit when a modification or reissuance is applied to the '
                                 'permit. A "0" indicates the most recent or current permit version.'},
 'ICIS_PERM_ASSOCIATION': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                          'particular site.',
                           'PERM_ASSOCIATION_DESC': 'The description of the type of association between the permits.',
                           'PERM_ASSOCIATION_ID': 'The sequence ID identifying the Permit Association.',
                           'RELATED_EXTERNAL_PERMIT_NMBR': 'This is the unique identifier for a NPDES Permit that is '
                                                           'related to the Permit.'},
 'ICIS_PERM_BIOSOLID': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                       'site.',
                        'ANNUAL_DRY_SLUDGE': 'The amount of sludge a facility produces in DMT/year on a dry weight '
                                             'basis.  Facility monitoring requirements are dependent upon this value.',
                        'CO_DISPOSED_AMT': 'The amount of dry metric tons co-disposed in a MSW landfill.',
                        'EQ_PRODUCT_AMT': 'The amount (dry metric tons) of EQ product distributed.',
                        'INCINERATED_AMT': 'The amount (dry metric tons) of biosolids incinerated.',
                        'LAND_APPLIED_AMT': 'The amount (dry metric tons) of biosolids land applied.',
                        'OS_BENEFICIALLY_USED_AMT': 'The amount (dry metric tons) of biosolids beneficially used out '
                                                    'of state.',
                        'OS_DISPOSED_AMT': 'The amount (dry metric tons) of biosolids disposed out of state.',
                        'OS_OTHER_METHOD_AMT': 'The dry metric tons of biosolids managed by other methods out of '
                                               'state.',
                        'OS_SOURCE_AMT': 'The amount (dry metric tons) of biosolids received from off site sources.',
                        'OTHER_METHOD_AMT': 'The amount (dry metric tons) of biosolids managed using  methods not '
                                            'previously described.',
                        'PERM_BIOSOLID_ID': 'The sequence ID identifying the Permit Biosolid Component.',
                        'SURFACE_DISPOSAL_AMT': 'The amount (dry metric tons) of  biosolids used for surface disposal.',
                        'TOTAL_REMOVED_AMT': 'The total amount (dry metric tons) of biosolids removed.',
                        'TRANSFERRED_AMT': 'The amount (dry metric tons) of biosolids transferred.'},
 'ICIS_PERM_CAFO': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                   'site.',
                    'CAFO_ANIMAL_FACILITY_FLAG': 'The flag to indicate whether  the facility is a Concentrated Animal '
                                                 'Feeding Operation.',
                    'CAFO_CLASSIFICATION_DESC': 'The text that describes how the facility was classified as a '
                                                '"Concentrated Animal Feeding Operation."  Options are Large, Medium '
                                                'and Small (Designation).',
                    'CAFO_REASON_TEXT': 'The reason the facility was designated, such as severe water quality impact '
                                        'in a basin planning area of a TMDL area.',
                    'DESIGNATION_DATE': 'The date on which the facility is designated as a CAFO.',
                    'EMS_DEVELOPED_DATE': 'This is the date that an EMS was developed by the facility.',
                    'EMS_FLAG': 'This field indicates whether the facility has some form of environmental management '
                                'system.',
                    'EMS_LAST_UPDATED_DATE': 'This is the date that the EMS was last updated by the facility.',
                    'LAND_AVAILABLE': 'The number of acres of land under the control of the applicant that are '
                                      'suitable for land application of the CAFO manure, litter, or wastewater.',
                    'LEGAL_DESC': 'This is the legal description of the Township, Section, Range, etc. of the CAFO '
                                  'facility.',
                    'LIQUID_MANURE_GENERATED_AMT': 'The total amount of manure in gallons generated annually by the '
                                                   'facility.',
                    'LIQUID_MANURE_TRANSFERRED_AMT': 'The total amount of manure in gallons produced by the CAFO that '
                                                     'will be transferred to other persons.',
                    'LIVESTOCK_AUTHORIZED_CAPACITY': 'This is the maximum number of animals that the facility is '
                                                     'authorized to handle and may be the same as the Designed Maximum '
                                                     'Capacity.',
                    'LIVESTOCK_DETERMIN_CAPACITY': 'The number of animals that the AFO/CAFO determination was based '
                                                   'on.',
                    'LIVESTOCK_MAX_CAPACITY': 'The maximum number of animals that the facility is permitted to handle.',
                    'NMBR_OF_ACRES_DRAINAGE': 'This is the number of acres that are drained and collected in the '
                                              'production area.',
                    'NMP_DEVELOPED_DATE': 'The date that an NMP was developed by the facility.',
                    'NMP_FLAG': 'The yes/no flag indicating whether the facility has Nutrient Manure Management Plan '
                                'developed or approved by a certified planner.',
                    'NMP_LAST_UPDATED_DATE': 'The date that the NMP was last updated by the facility.',
                    'PERM_CAFO_ID': 'The sequence ID identifying the Permit CAFO Component.',
                    'PRODUCTION_AREA_SIZE': 'This is the number of acres that are drained and collected in the '
                                            'production area.',
                    'SOLID_MANURE_GENERATED_AMT': 'The total amount of manure in tons generated annually by the '
                                                  'facility.',
                    'SOLID_MANURE_TRANSFERRED_AMT': 'The number of tons of manure or litter produced by the CAFO that '
                                                    'will be transferred to other persons.'},
 'ICIS_PERM_CAFO_ANIMAL_TYPE': {'ANIMAL_TYPE_DESC': "This is text that describes the CAFO''s applicable animal "
                                                    'sector(s).',
                                'ANIMAL_TYPE_OTHER': 'The free-form text field to describe the CAFO applicable animal '
                                                     'sector if Other is selected for Animal Type Code.',
                                'OPEN_CONFINEMENT_COUNT': 'The number of animals, by type, in open confinement that '
                                                          'are held at the facility for a total of 45 days or more in '
                                                          'any 12-month period.',
                                'PERM_CAFO_ANIMAL_TYPE_ID': 'This is an identifier for the Animal Type value.',
                                'PERM_CAFO_ID': 'The sequence ID identifying the Permit CAFO Component.',
                                'TOTAL_NMBR': 'The total number of each type of livestock at the facility.',
                                'UNDER_ROOF_CONFINEMENT_COUNT': 'The number of animals, by type, housed under a roof '
                                                                '(either partially or totally) that are held at the '
                                                                'facility for a total of 45 days or more in any '
                                                                '12-month period.'},
 'ICIS_PERM_CAFO_BMP': {'BMP_DESC': 'The description of the conservation Best Management Practices (BMP) the facility '
                                    'implements to control runoff and protect water quality.',
                        'BMP_OTHER': 'This is additional information relating to a Permit CAFO component BMP.',
                        'PERM_CAFO_BMP_ID': 'The sequence ID identifying the Permit CAFO Component Best Management '
                                            'Practice.',
                        'PERM_CAFO_ID': 'The sequence ID identifying the Permit CAFO Component.'},
 'ICIS_PERM_CAFO_CONTAINMENT': {'CONTAINMENT_CAPACITY': 'The total capacity, in gallons, of the containment structure.',
                                'CONTAINMENT_TYPE_DESC': 'The  text that describes the type of containment used by the '
                                                         'CAFO.',
                                'CONTAINMENT_TYPE_OTHER': 'The free-form text field to describe the type of '
                                                          'containment if Other is selected for Containment Type Code.',
                                'PERM_CAFO_CONTAINMENT_ID': 'This is an identifier for the CAFO Containment value.',
                                'PERM_CAFO_ID': 'The sequence ID identifying the Permit CAFO Component.',
                                'STORAGE_TYPE_OTHER': 'The free-form text field to describe the type of storage used '
                                                      'by the operation if the Other code is selected for storage type '
                                                      'code attribute.'},
 'ICIS_PERM_CAFO_STORAGE': {'DAYS_OF_STORAGE': 'This is how many days of storage there were for each storage type '
                                               'selected.',
                            'PERM_CAFO_ID': 'The sequence ID identifying the Permit CAFO Component.',
                            'PERM_CAFO_STORAGE_TYPE_ID': 'This is an identifier for the CAFO Storage value.',
                            'STORAGE_TYPE_DESC': 'The description of the type of storage used by the CAFO.',
                            'STORAGE_TYPE_OTHER': 'The free-form text field to describe the type of storage used by '
                                                  'the operation if the Other code is selected for storage type code '
                                                  'attribute.',
                            'TOTAL_CAPACITY_MEASURE': 'The total capacity, in tons or gallons, of the storage '
                                                      'structure.'},
 'ICIS_PERM_COMP_STATUS': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                          'particular site.',
                           'PERMIT_COMP_STATUS_FLAG': 'This is a code that indicates whether the permit is currently '
                                                      'on or off for compliance tracking purposes. Value is (Y)es or '
                                                      'No (null value).',
                           'PERM_COMP_STATUS_ID': 'This is an identifier for the Permit Compliance Status value.',
                           'STATUS_BEGIN_DATE': 'The date that the Limit Set Status started.',
                           'STATUS_END_DATE': 'This is the date on which the permit\'s on or off period for compliance '
                                              'tracking status ended.',
                           'STATUS_REASON_TEXT': "The reason a permit''s compliance tracking status changed."},
 'ICIS_PERM_CONSTRUCTION': {'CONST_WAIVER_AUTH_DATE': 'This is the date on which the Construction Waiver was '
                                                      'authorized.',
                            'CONST_WAIVER_CRITERIA_MET_FLAG': 'This field indicates whether the Construction Waiver '
                                                              'criteria was met by the facility.',
                            'CONST_WAIVER_EVAL_DATE': 'This is the date on which the Construction Waiver evaluation '
                                                      'was performed.',
                            'CONST_WAIVER_POSTMARK_DATE': 'This is the date on which the Construction Waiver was '
                                                          'postmarked.',
                            'CONST_WAIVER_SIGNATURE_DATE': 'This is the date on which the Construction Waiver was '
                                                           'signed.',
                            'CONST_WAVER_EVAL_BASIS_DESC': 'This is the text that describes the basis for the '
                                                           'construction waiver.',
                            'EROSIVITY_INDEX_ZONE': 'This field indicates optimal periods of either wet or dry weather '
                                                    'measuring the potential for soil to wash off disturbed, divagated '
                                                    'earth into waterways during storms.',
                            'ESTIMATED_AREA_DISTURBED': 'This identifies the estimated area disturbed by entire '
                                                        'project, measured in acres.',
                            'ESTIMATED_BEGIN_DATE': 'This identifies the estimated start date of project.',
                            'ESTIMATED_END_DATE': 'This identifies the estimated completion date of project.',
                            'NOT_POSTMARK_DATE': 'This is the date Notice of Termination (NOT) was postmarked.',
                            'NOT_RECEIVED_DATE': 'This is the date the NOT was received.',
                            'NOT_SIGNATURE_DATE': 'This is the date the NOT was signed.',
                            'NOT_TERMINATION_DATE': 'This is the date on which the coverage was terminated.',
                            'PERM_CONSTRUCTION_ID': 'The sequence ID identifying the Permit Construction Component.',
                            'PERM_STORM_WATER_ID': 'This is the identifier of the Storm Water component to which this '
                                                   'data relates.',
                            'PROJECT_ISOERODENT_VALUE': 'This is the isoerodent value for the project for the portion '
                                                        'of the year that the construction project will take place.  '
                                                        'Isoerodent value is statistically calculated and based on the '
                                                        'annual summation of rainfall energy in every storm.',
                            'PROJECT_PLAN_SIZE_DESC': 'This text describes the planned size of the project.',
                            'PROJECT_TYPE_DESC': 'This text describing the type of construction project.',
                            'SITE_ISOERODENT_VALUE': 'This is the iserodent value for the site on which construction '
                                                     'is to take place.  Iserodent value is statistically calculated '
                                                     'and based on the annual summation of rainfall energy in every '
                                                     'storm.',
                            'TERMINATION_REASON_DESC': 'This is the text describing the reason why the permit was '
                                                       'terminated.'},
 'ICIS_PERM_CSO': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular site.',
                   'CSS_LENGTH': 'This is the miles of pipe in the system.',
                   'CSS_POPULATION': 'This is the population served by the combined sewer system (individuals or '
                                     'households).',
                   'PERCENT_OF_COLLECTION': 'This is the percentage of the total collection system that is combined.',
                   'PERM_CSO_ID': 'The sequence ID identifying the Permit CSO Component.'},
 'ICIS_PERM_EFFLUENT': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                       'site.',
                        'CFR_PART': 'The CFR Part that is related to the effluent guideline.',
                        'PERM_EFFLUENT_DESC': 'The description of the effluent guideline that applies to the permit.',
                        'PERM_EFFLUENT_GUIDE_ID': 'This is the identifier for the Effluent Guideline in this table.'},
 'ICIS_PERM_FEATURE': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                      'site.',
                       'ACTUAL_AVERAGE_FLOW_NMBR': 'The flow that a permitted feature actually had at the time of '
                                                   'application., expressed as millions of gallons per day (MGD).',
                       'CREATION_TYPE_DESC': 'The description of how a record was created.',
                       'DAILY_COVER_FLAG': 'This indicates whether a Permitted Feature active surface disposal unit '
                                           'has daily cover.',
                       'DESIGN_FLOW_NMBR': 'The flow that a permitted feature was designed to accommodate.',
                       'DISTANCE_TO_BOUNDARY': 'This indicates the distance of the surface disposal site to the '
                                               'property boundary.',
                       'FIELD_SIZE': 'This indicates the size of the field if the Permitted Feature is a land '
                                     'application or surface disposal site.',
                       'LEACHATE_COLLECTION_FLAG': 'This indicates whether the surface disposal site is lined with a '
                                                   'leachate collection system.',
                       'MASTER_GENERAL_CATEGORY_TEXT': 'The placeholder for storing the text describing a Master '
                                                       'General Permit Permitted Feature for a General Permit Covered '
                                                       'Facility Permitted Feature. Not currently used.',
                       'NITRATE_MONITORING_FLAG': 'This indicates whether nitrate ground water monitoring is required '
                                                  'for the Permitted Feature.',
                       'OWNED_BY_FACILITY_FLAG': 'The yes/no flag indicating if the permitted feature is owned by the '
                                                 'facility.',
                       'PERM_FEATURE_ID': 'The unique system identifier for a permitted feature.',
                       'PERM_FEATURE_NMBR': 'The 3-digit code representing the permitted outfall or pipe of interest '
                                            'in ICIS-NPDES (e.g., 001). This is the identifier assigned for each '
                                            'location at which permit conditions are being applied.',
                       'PERM_FEATURE_TEXT': 'The description of the permitted feature.',
                       'PERM_FEATURE_TYPE_DESC': 'The description of the permitted feature type.',
                       'RAD_INTERFACE_FLAG': 'This indicates whether the Permitted Feature data have been exchanged '
                                             'with the RAD system.',
                       'REACH_ID': 'The 14-digit field identifying the water body into which the effluent is '
                                   'discharged; data provided by WebRIT/RAD based on the permitted feature\'s '
                                   'latitude/longitude data.',
                       'SOURCE_PERM_FEATURE_ID': 'The placeholder for linking a SUM permitted feature to its source. '
                                                 'Not currently used.',
                       'SOURCE_PERM_FEA_DETAILS': 'This contains information on source Permitted Features if the '
                                                  'Permitted Feature type is Sum.',
                       'STATE_WATER_BODY': "The state's code to identify the water body into which the effluent is "
                                           'discharged for a Permitted Feature.',
                       'STATE_WATER_BODY_NAME': "The state's name for the water body into which the effluent is "
                                                'discharged for a Permitted Feature.',
                       'UDF1': 'The user defines this field.',
                       'UDF2': 'The user defines this field.',
                       'WATER_BODY_NAME': 'The name of the water body into which the effluent is discharged; data '
                                          'provided by WebRIT/RAD based on the permitted feature\'s latitude/longitude '
                                          'data.',
                       'WELL_NMBR': 'This indicates the well number for the Permitted Feature.'},
 'ICIS_PERM_FEATURE_CHARACTER': {'CHARACTERISTIC_DESC': 'The description of the code identifying the characteristic of '
                                                        'a permitted feature.',
                                 'PERM_FEATURE_ID': 'The unique system identifier for a permitted feature.',
                                 'XREF_PERM_FEATURE_CHARACTER_ID': 'The sequence identifying the linkage between the '
                                                                   'Permitted Feature and the characteristic.'},
 'ICIS_PERM_FEATURE_COORD': {'GEOMETRIC_TYPE_NAME': 'The name that identifies the geometric entity represented by one '
                                                    'point or a sequence of latitude and longitude points.',
                             'HORIZONTAL_ACCURACY_MEASURE': 'The measure of the accuracy (in meters) of the latitude '
                                                            'and longitude coordinates.',
                             'HORIZONTAL_COLLECT_METHOD_TEXT': 'The text that describes the method used to determine '
                                                               'the latitude and longitude coordinates for a point on '
                                                               'the earth.',
                             'HORIZONTAL_REF_DATUM_NAME': 'The text to define the DATUM reference for geographic '
                                                          'coordinates.',
                             'LATITUDE_MEASURE': 'The horizontal position coordinate for the point of discharge '
                                                 'location in units of decimal degrees. Latitude and longitude '
                                                 'coordinates are not required to be entered into ICIS-NPDES. '
                                                 'Searching on coordinates will only return results for permit '
                                                 'features that have latitude and longitude data in ICIS-NPDES.',
                             'LONGITUDE_MEASURE': 'The vertical position coordinate for the point of discharge '
                                                  'location in units of decimal degrees. ICIS-NPDES does not require '
                                                  'Latitude and longitude coordinates to be entered. Searching on '
                                                  'coordinates will only return results for permit features that have '
                                                  'latitude and longitude data in ICIS-NPDES.',
                             'PERM_FEATURE_COORD_ID': 'The unique identifier for a geographic coordinate of a '
                                                      'permitted feature.',
                             'PERM_FEATURE_ID': 'The unique system identifier for a permitted feature.',
                             'REFERENCE_POINT_DESC': 'The code to define the DATUM reference for Permit feature source '
                                                     'coordinates.',
                             'SOURCE_MAP_SCALE_NMBR': 'The number that represents the proportional distance on the '
                                                      'ground for one unit of measure on the map or photo.'},
 'ICIS_PERM_FEATURE_TREATMENT': {'PERM_FEATURE_ID': 'The unique system identifier for a permitted feature.',
                                 'TREATMENT_TYPE_DESC': 'The description of the permitted feature treatment type.',
                                 'XREF_PERM_FEATURE_TREATMENT_ID': 'The sequence identifying the linkage between the '
                                                                   'Permitted Feature and the treatment type.'},
 'ICIS_PERM_INDUSTRIAL': {'INDUSTRIAL_ACTIVITY_SIZE': 'This identifies the size of the site for which No Exposure '
                                                      'Certification is being requested.',
                          'NOT_POSTMARK_DATE': 'This is the date Notice of Termination (NOT) was postmarked.',
                          'NOT_RECEIVED_DATE': 'This is the date the NOT was received.',
                          'NOT_SIGNATURE_DATE': 'This is the date the NOT was signed.',
                          'NOT_TERMINATION_DATE': 'This is the date on which the coverage was terminated.',
                          'NO_EXPO_AUTH_DATE': 'This is the date on which the No Exposure Waiver was authorized.',
                          'NO_EXPO_CRITERIA_MET_FLAG': 'This identifies if no exposure criteria were met in '
                                                       'Certification.',
                          'NO_EXPO_EVAL_BASIS_DESC': 'The description for the evaluation basis for the SWPPP.',
                          'NO_EXPO_EVAL_DATE': 'This is the date the facility was evaluated for a No Exposure Waiver.',
                          'NO_EXPO_POSTMARK_DATE': 'This is the date No Exposure Certification is postmarked.',
                          'NO_EXPO_SIGNATURE_DATE': 'This is the date No Exposure Certification is signed.',
                          'PAVED_ROOF_SIZE': 'This identifies the amount of area paved or roofed over to qualify for '
                                             'no exposure.',
                          'PERM_INDUSTRIAL_ID': 'The sequence ID identifying the Permit Industrial Storm Water '
                                                'Component.',
                          'PERM_STORM_WATER_ID': 'This is the identifier of the Storm Water component to which this '
                                                 'data relates.'},
 'ICIS_PERM_NARRATIVE_CONDITION': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                                  'particular site.',
                                   'CREATION_TYPE_DESC': 'The description of how a record was created.',
                                   'INHERITED_FLAG': 'The placeholder flag indicating if the permit schedule event is '
                                                     'inherited from the Master General Permit. Not currently used.',
                                   'NARRATIVE_CONDITION_DESC': 'The text of the narrative condition.',
                                   'NARRATIVE_CONDITION_NMBR': 'This identifies a narrative condition and its elements '
                                                               'uniquely for a permit.',
                                   'NARRATIVE_CONDITION_TEXT': 'The full text description of the narrative condition.',
                                   'NARRATIVE_CONDITION_TYPE_FLAG': 'The code that identifies the source of the '
                                                                    'narrative condition as a permit.',
                                   'PERM_NARRATIVE_CONDITION_ID': 'The ID of the narrative condition to which the '
                                                                  'permit schedule event belongs.',
                                   'STAY_BEGIN_DATE': 'The date on which a limit stay begins.',
                                   'STAY_END_DATE': 'The placeholder for the end date of a stay applied against the '
                                                    'permit schedule event. Not currently used.',
                                   'STAY_REASON_TEXT': 'The text describing the reason for the stay on the narrative '
                                                       'condition. Not currently used.',
                                   'STAY_VIOLATION_FLAG': 'The placeholder flag indicating if violations should be '
                                                          'calculated for the narrative condition after the stay is '
                                                          'lifted. Not currently used.'},
 'ICIS_PERM_OTHER_PERMIT': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                           'particular site.',
                            'IDENTIFIER_CONTEXT_DESC': 'This is a brief description of the other permit '
                                                       'number/identifier context.',
                            'ORGANIZATION_NAME': 'This is the name of the organization issuing the other permit '
                                                 'number/identifier.',
                            'OTHER_EXTERNAL_PERMIT_NMBR': 'This is the unique identifier for a Non-NPDES Permit that '
                                                          'is related to the Permit.',
                            'OTHER_PERMIT_ID': 'These are other alphanumeric identifiers used to identify a permit.'},
 'ICIS_PERM_PRETREATMENT': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                           'particular site.',
                            'CONTROL_AUTH_PERMIT_ID': "The permit ID of the POTW''s or IU''s control authority.",
                            'PERM_PRETREATMENT_ID': 'The sequence ID identifying the Permit Pretreatment Component.',
                            'PRETREATMENT_APPROVED_DATE': 'The date the pretreatment program is approved.',
                            'PRETREATMENT_INDICATOR_DESC': 'The text that describes the pretreatment type for the '
                                                           'pretreatment permit.',
                            'SIGNIFICANT_IU_FLAG': 'The equivalent of major/minor determination to determine '
                                                   'significant IUs versus non-significant IUs for a POTW.'},
 'ICIS_PERM_RNC_HISTORY': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                          'particular site.',
                           'PERM_RNC_AUTO_STATUS_DESC': 'The status of reportable noncompliance as it was calculated '
                                                        'by the system during the official RNC run for the RNC quarter '
                                                        'for the permit.',
                           'PERM_RNC_CORR_AUTO_STATUS_DESC': 'The placeholder for the corrected status of reportable '
                                                             'noncompliance as it was calculated by the system after '
                                                             'the official RNC run for the RNC quarter for the permit. '
                                                             'Not currently used.',
                           'PERM_RNC_CORR_MAN_STATUS_DESC': 'The corrected status of reportable noncompliance as it '
                                                            'was entered by the user after the official QNCR run for '
                                                            'the RNC quarter for the permit.',
                           'PERM_RNC_HISTORY_ID': 'The unique identifier of a permit RNC history record.',
                           'PERM_RNC_MAN_STATUS_DESC': 'The status of reportable noncompliance as it was entered by '
                                                       'the user before the official QNCR for the RNC quarter for the '
                                                       'permit.',
                           'QUARTER': 'The quarter of the RNC status.',
                           'YEAR': 'The year of the RNC status.'},
 'ICIS_PERM_SCHED_EVENT': {'ACTUAL_DATE': 'The date on which the milestone was achieved/sub activity was conducted.',
                           'COMMENT_TEXT': 'The free-form textual comments entered by the user/analyst to further '
                                           'describe the corresponding data.',
                           'CREATION_TYPE_DESC': 'The description of how a record was created.',
                           'INHERITED_FLAG': 'The placeholder flag indicating if the permit schedule event is '
                                             'inherited from the Master General Permit. Not currently used.',
                           'PERM_NARRATIVE_CONDITION_ID': 'The ID of the narrative condition to which the permit '
                                                          'schedule event belongs.',
                           'PERM_SCHEDULE_EVENT_ID': 'The unique identifier of the Permit Schedule Event to which the '
                                                     'Violation is associated; it is only used for Schedule Violations '
                                                     'of a Permit.',
                           'PROJECTED_DATE': 'The date an event is projected to be completed when the permittee knows '
                                             'in advance that the Schedule Date will not be met on time.',
                           'RELATIVE_OFFSET_MONTH': 'The placeholder for indicating the amount to offset a General '
                                                    "Permit Covered Facility''s related permit schedule event when "
                                                    'adding a linked permit schedule event. Not currently used.',
                           'REPORT_RECEIVED_DATE': 'The date on which the regulatory authority receives a report '
                                                   '(generally a letter) from the permittee indicating that a Schedule '
                                                   'Event was completed (e.g., Start Construction) or the required '
                                                   'report was enclosed.',
                           'SCHEDULE_DATE': 'The date the compliance schedule or permit schedule event is scheduled to '
                                            'be completed (i.e., the due date).',
                           'SCHEDULE_EVENT_DESC': 'Text description of the code value for SCHEDULE_EVENT_CODE.',
                           'SOURCE_NARR_CONDITION_EVENT_ID': 'The placeholder for linking a narrative condition to its '
                                                             'Master General Permit source. Not currently used.',
                           'STAY_BEGIN_DATE': 'The date on which a limit stay begins.',
                           'STAY_END_DATE': 'The placeholder for the end date of a stay applied against the permit '
                                            'schedule event. Not currently used.',
                           'STAY_REASON_TEXT': 'The text describing the reason for the stay on the narrative '
                                               'condition. Not currently used.',
                           'STAY_VIOLATION_FLAG': 'The placeholder flag indicating if violations should be calculated '
                                                  'for the narrative condition after the stay is lifted. Not currently '
                                                  'used.',
                           'UDF1': 'The user defines this field.',
                           'UDF2': 'The user defines this field.',
                           'VIOLATION_EVALUATION_FLAG': 'The placeholder system generated flag indicating to Schedule '
                                                        'Violation Processing whether to evaluate this schedule event. '
                                                        'Not currently used.'},
 'ICIS_PERM_SSO': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular site.',
                   'PERM_SSO_ID': 'The sequence ID identifying the Permit SSO Component.',
                   'SSCS_LENGTH': 'This is the number of miles of pipe in the sanitary sewer collection system.',
                   'SSCS_POPULATION': 'This is the population served by the sanitary sewer collection system '
                                      '(individuals or households).  This data element applies to all POTWs.'},
 'ICIS_PERM_STORM_WATER': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                          'particular site.',
                           'COMPLETE_NOI_RECEIVED_DATE': 'The date the complete NOI was received.',
                           'HISTORIC_CRITERION_DESC': 'The text that describes the basis for meeting NHPA.',
                           'HIST_PROP_FLAG': 'This flag indicates whether the storm water component applies to a '
                                             'historical property.',
                           'IMPAIRED_WATER_FLAG': 'This field indicates whether or not the receiving water is '
                                                  'impaired.',
                           'NOI_POSTMARK_DATE': 'This is the date the NOI is postmarked.',
                           'NOI_RECEIVED_DATE': 'The date that NOI was received.',
                           'NOI_SIGNATURE_DATE': 'This is the date the Notice of Intent (NOI) was signed.',
                           'PERM_STORM_WATER_DESC': 'This is the text that describes the type of storm water that '
                                                    'applies to the permit.',
                           'PERM_STORM_WATER_ID': 'This is the identifier of the Storm Water component to which this '
                                                  'data relates.',
                           'SPECIES_CRITERION_DESC': 'The description of species/critical habitat information for a '
                                                     'Storm Water Permit.',
                           'SPECIES_CRITICAL_HABITAL_FLAG': 'This identifies if Endangered Species Act (ESA) '
                                                            'provisions are met.'},
 'ICIS_PERM_STORM_WATER_BODY': {'PERM_STORM_WATER_BODY_ID': 'This is the identifier for the water body in this table.',
                                'PERM_STORM_WATER_ID': 'This is the identifier of the Storm Water component to which '
                                                       'this data relates.',
                                'STATE_WATER_BODY_NAME': "The state's name for the water body into which the effluent "
                                                         'is discharged for a Permitted Feature.'},
 'ICIS_PERM_STORM_WATER_MS4_NM': {'PERM_STORM_WATER_ID': 'This is the identifier of the Storm Water component to which '
                                                         'this data relates.',
                                  'PERM_STORM_WATER_MS4_NAME_ID': 'This is the identifier of the record in this table.',
                                  'RECEIVING_MS4_NAME': 'This is the name of the receiving MS4(s).'},
 'ICIS_PERM_TMDL': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                   'site.',
                    'PERM_TMDL_ID': 'The sequence ID identifying the TMDL.',
                    'TMDL_ID': 'This is the tracking number used in the OWOW TMDL tracking system.'},
 'ICIS_PERM_TRACK_EVENT': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                          'particular site.',
                           'PERM_TRACK_EVENT_DESC': 'This is the text that describes the permit tracking milestone '
                                                    'event.',
                           'PERM_TRACK_EVENT_ID': 'The system-generated unique identifier for a permit tracking event.',
                           'TRACK_EVENT_COMMENT_TEXT': 'This allows free format entry of descriptive permit tracking '
                                                       'information.',
                           'TRACK_EVENT_DATE': 'This is the actual date the permit tracking event (PTEV) was '
                                               'completed.'},
 'ICIS_PRETREAT_PERFORM_SUMMARY': {'ACCEPT_HAULED_DOMESTIC_FLAG': 'The flag indicating the acceptance of hauled '
                                                                  'domestic wastes.',
                                   'ACCEPT_HAULED_NON_HAZ_FLAG': 'The flag indicating the acceptance of hauled '
                                                                 'industrial non-hazardous waste.',
                                   'ACCEPT_HAZ_FLAG': 'The flag indicating the acceptance of hazardous waste.',
                                   'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                                  'particular site.',
                                   'ADEQUATE_RESOURCE_FLAG': 'The flag indicating if the resources are adequate for '
                                                             'the activity.',
                                   'ANNUAL_BUDGET': 'The total level of annual funding used to implement the Control '
                                                    'Authority\'s Pretreatment program.',
                                   'CIU_IN_SNC_NMBR': 'The number of CIUs in SNC.',
                                   'CIU_NMBR': 'The total number of CIUs.',
                                   'DEFICIENCY_CONTROL_MECH_FLAG': 'Flag to indicate components that are not '
                                                                   'sufficient or are not contained in the '
                                                                   'Pretreatment Control Authority control mechanism.',
                                   'DEFICIENCY_DATA_MGNT_FLAG': 'Flag to indicate deficiencies in the Pretreatment '
                                                                'Control Authority\'s data management and public '
                                                                'participation effort.',
                                   'DEFICIENCY_IDENTIFIED_FLAG': 'Flag to indicate deficiencies were noted during the '
                                                                 'review of IU files.',
                                   'DEFICIENCY_INTREPRETATION_FLAG': 'Flag to indicate deficiencies noted in the '
                                                                     'Pretreatment Control Authority\'s interpretation '
                                                                     'and application of pretreatment standards.',
                                   'DEFICIENCY_LEGAL_FLAG': 'The flag indicates there are deficiencies in the legal '
                                                            'authority.',
                                   'FORMAL_RESPONSE_FLAG': 'The flag indicating whether a formal Enforcement Action '
                                                           'has been taken in response to a violation of any schedule '
                                                           'for implementation of needed remedial measures identified.',
                                   'FREQ_EFFLUENT_TOXICANT_NMBR': 'The number of times that toxicant sampling of '
                                                                  'effluent was performed at the POTW over the past '
                                                                  'year.',
                                   'FREQ_INFLUENT_TOXICANT_NMBR': 'The number of times that toxicant sampling of '
                                                                  'effluent was performed at the POTW over the past '
                                                                  'year.',
                                   'FREQ_SLUDGE_TOXICANT_NMBR': 'The number of times that toxicant sampling of sludge '
                                                                'was performed at the POTW over the past year.',
                                   'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the '
                                                                'facility interest.',
                                   'ICIS_PRETREAT_PERFORM_SUMM_SEQ': 'Informatica generated unique key to the table',
                                   'INDUSTRIAL_USER_NMBR': 'The total number of significant industrial users.',
                                   'IU_PENALTIES_COLLECTED_NMBR': 'Number of IUs from which penalties have been '
                                                                  'collected.',
                                   'MOST_RECENT_ADOPT_DATE': 'The date on which the Pretreatment Control Authority '
                                                             'adopted local limits for pollutants.',
                                   'MOST_RECENT_CREDIT_APPROV_DATE': 'The date the application for removal credits was '
                                                                     'approved.',
                                   'MOST_RECENT_EVAL_DATE': 'The date on which the Pretreatment Control Authority has '
                                                            'technically evaluated the need for local limits.',
                                   'PASSTHROUGH_FLAG': 'The flag indicating if there has been any incidents of '
                                                       'pass-through or interference at the POTW in the past year.',
                                   'PENALTIES_COLLECTED_AMT': 'The amount of penalties collected.',
                                   'PERFORMANCE_START_DATE': 'The date on which the Pretreatment Performance Summary '
                                                             'report starts.',
                                   'PROGRAM_REPORT_TYPE_DESC': 'The text description for the unique code that '
                                                               'identifies the type of Program Report.',
                                   'PROG_RPT_ID': 'The system-generated unique identifier for the program report.',
                                   'PROG_RPT_PRETREATMENT_ID': 'The system-generated unique identifier for the program '
                                                               'report.',
                                   'REMOVAL_STATUS_CODE': 'The unique code that identifies the status of the '
                                                          'application for removal credit for the pretreatment control '
                                                          'authority.',
                                   'REPORT_DATE': 'The date the report was received by EPA.',
                                   'SIU_ADMIN_ORDER_NMBR': 'The number of administrative orders issued to SIUs.',
                                   'SIU_ADMIN_SUIT_NMBR': 'The number of civil suits filed against SIUs.',
                                   'SIU_CRIMINAL_SUIT_NMBR': 'The number of criminal suits filed against SIUs.',
                                   'SIU_NMBR': 'The total number of SIUs.',
                                   'SIU_NOT_INSPECTED_NMBR': 'The number of SIUs not inspected.',
                                   'SIU_NOT_SAMPLED_NMBR': 'The number of SIUs not sampled.',
                                   'SIU_SCHEDULE': 'This is the number of Significant Industrial Users on Pretreatment '
                                                   'or Compliance Schedules.',
                                   'SIU_SIGNIFICANT_VIOLATION_NMBR': 'The number of significant industrial users with '
                                                                     'significant violations published in the '
                                                                     'newspaper.',
                                   'SIU_SNC_PRETREATMENT_SCHEDULE': 'The number of Significant industrial users in SNC '
                                                                    'with pretreatment schedule.',
                                   'SIU_SNC_PRE_STD_NMBR': 'The significant industrial users in SNC with pretreatment '
                                                           'standards.',
                                   'SIU_SNC_PUBLISHED_NEWS': 'The number of Significant industrial users in SNC '
                                                             'published in newspaper.',
                                   'SIU_SNC_RPT_REQUIREMENT_NMBR': 'The significant industrial users in SNC with '
                                                                   'reporting requirements.',
                                   'SIU_VIOLATION_NOTICE_NMBR': 'The number of formal notices of violation or '
                                                                'equivalent actions that have been issued to SIUs.',
                                   'SIU_WO_CONTROL_MECH_NMBR': 'The number of SIUs for which a current control '
                                                               'mechanism is required but not yet issued.',
                                   'SUO_DATE': 'The date that the SUO was most recently adopted at the POTW and '
                                               'Control Authority level.',
                                   'SUO_REFERENCE': 'The reference to the actual local sewer use ordinance (SUO) '
                                                    'number and chapter at the POTW and Control Authority level.',
                                   'VIOLATION_OF_SCHEDULE_FLAG': 'The flag indicating whether there has been a '
                                                                 'violation of any schedule issued.'},
 'ICIS_SUB_ACTIVITY': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a particular '
                                      'site.',
                       'ACTUAL_DATE': 'The date on which the milestone was achieved/sub activity was conducted.',
                       'EPA_STATE_FILTER_FLAG': 'The flag indicating whether the Final Order action type is for EPA '
                                                'only (E) or both EPA and States (B).',
                       'PLANNED_DATE': 'The date on which the sub activity/milestone is planned to occur.',
                       'RANK_ORDER': 'The sort order for the Violation type on the Enforcement Action.',
                       'REVISED_PLANNED_DATE': 'The revised date on which the sub activity/milestone was planned.  '
                                               'This column is not currently being used.',
                       'SUB_ACTIVITY_ID': 'The system-generated unique identifier of the sub activity record.',
                       'SUB_ACTIVITY_TEXT': 'Description of milestone or sub activity.',
                       'SUB_ACTIVITY_TYPE_DESC': 'The name or description of a sub activity and/or Enforcement Action '
                                                 'milestone.'},
 'ICIS_XREF_ACTIVITY_CONTACT': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                               'particular site.',
                                'AFFILIATION_TYPE_DESC': 'uniquely identifies the Affiliation type of the address to '
                                                         'the facility interest.',
                                'BEGIN_DATE': 'The date at which the affiliation between facility interest and contact '
                                              'initiated.',
                                'CONTACT_ID': 'The unique identifier for a contact related to a particular number.',
                                'END_DATE': 'The date on which the affiliation between the facility interest and the '
                                            'organization and/or individual person ended.'},
 'ICIS_XREF_ACTIVITY_FACILITY': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                                'particular site.',
                                 'ACTIVITY_TYPE_CODE': 'A code describing the type of civil enforcement activity. '
                                                       'Valid values are:',
                                 'ACTIVITY_TYPE_DESC': 'Full text description for ACTIVTY_TYPE_CODE.',
                                 'FACILITY_UIN': 'The number assigned by the Facility Linkage Application that is used '
                                                 'to associate facility records from multiple environmental database '
                                                 'systems that are known or believed to represent the same facility.',
                                 'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the '
                                                              'facility interest.'},
 'ICIS_XREF_ENF_CONCL_FAC_ACT': {'ACTIVITY_ID': 'The unique identifier for an activity performed at or related to a '
                                                'particular site.',
                                 'ENF_CONCLUSION_ID': 'The system generated unique identifier of the Final Order '
                                                      'record.',
                                 'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the '
                                                              'facility interest.'},
 'ICIS_XREF_FACILITY_CONTACT': {'AFFILIATION_TYPE_DESC': 'uniquely identifies the Affiliation type of the address to '
                                                         'the facility interest.',
                                'BEGIN_DATE': 'The date at which the affiliation between facility interest and contact '
                                              'initiated.',
                                'CONTACT_ID': 'The unique identifier for a contact related to a particular number.',
                                'END_DATE': 'The date on which the affiliation between the facility interest and the '
                                            'organization and/or individual person ended.',
                                'ICIS_FACILITY_INTEREST_ID': 'The system-generated unique ID for identifying the '
                                                             'facility interest.'},
 'ICIS_XREF_PERM_FEATURE_CNTC': {'AFFILIATION_TYPE_DESC': 'uniquely identifies the Affiliation type of the address to '
                                                          'the facility interest.',
                                 'BEGIN_DATE': 'The date at which the affiliation between facility interest and '
                                               'contact initiated.',
                                 'CONTACT_ID': 'The unique identifier for a contact related to a particular number.',
                                 'END_DATE': 'The date on which the affiliation between the facility interest and the '
                                             'organization and/or individual person ended.',
                                 'PERM_FEATURE_ID': 'The unique system identifier for a permitted feature.'},
 'PCS_CMPL_SCHD': {},
 'PCS_CMPL_SCHD_VIOL': {},
 'PCS_CODE_DESC': {'CODE': 'A ten-digit (max) code indicating the code that is being described.',
                   'DESCRIPT': 'A text description of a code, such as a permit tracking event code.',
                   'TABLE_ID': 'A three-digit code indicating the type of code that is being described.  For example, '
                               '010 refers to COUNTY codes, while 110 refers to PERMIT TRACKING EVENT codes.'},
 'PCS_DMR_MEASUREMENT': {'CONCENTRATION_UNIT_CODE': 'The concentration unit code as reported on the returned DMR.  '
                                                    'During the update, the system will compare the entered value to '
                                                    'the limited value and print warning messages identifying all '
                                                    'differences.',
                         'CONCENTR_AVG': 'The reported value for concentration average.',
                         'CONCENTR_MAX': 'The reported value for concentration maximum.',
                         'CONCENTR_MIN': 'The reported value for concentration minimum.',
                         'DISCHARGE_NUM': 'A three-digit code assigned for each point of discharge. Links a '
                                          'measurement record to the related limit record.',
                         'LIMIT_TYPE': 'The limit type of a Measurement/Violation record.',
                         'MEAS_VIOL_CODE': 'The effluent violation code describing the worst violation detected for '
                                           "this report parameter's measurements.",
                         'MODIF_NUM': 'The modification number on the measurement/violation record that matches the '
                                      'corresponding parameter limit record.',
                         'MONITORING_LOC': 'The location where the measurement sample was taken.',
                         'MONITORING_PERIOD_END_DATE': 'For effluent measurements violations: the monitoring period '
                                                       'end date as stated on the DMR.',
                         'NO_DISCHARGE_IND': 'Indicates the reason that "No Discharge" or "No Data" was reported in '
                                             'place of the measurement on the DMR.',
                         'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to uniquely '
                                  'identify a permitted NPDES facility.',
                         'PARAM_CODE': 'The parameter code of the measurement violation.',
                         'PIPE_SET_QUALIFIER': 'A one-digit code used to provide unique linkage between Pipe '
                                               'Schedules, Parameter Limits, and Measurement/Violations.',
                         'QTY_AVG': 'The reported value for quantity average.',
                         'QTY_MAX': 'The reported value for quantity maximum.',
                         'QUANTITY_UNIT_CODE': 'The quantity unit code as reported on the returned DMR.  During the '
                                               'update, the system will compare the entered value to the limited value '
                                               'and print warning messages identifying all differences.',
                         'REPORT_DESIG': 'A one-character code used to designate a particular grouping of parameters '
                                         'for reporting purposes.  Links a measurement/violation record to the related '
                                         'limit record.',
                         'SEASON_NUM': 'The effluent season number of the measurement or violation.'},
 'PCS_EFFL_LIM': {},
 'PCS_EFFL_LIM_CONCENTR': {},
 'PCS_EFFL_LIM_QTY': {},
 'PCS_EVIDENTIARY_HEARING_EVENT': {'EVENT_CODE': 'Code identifying each evidentiary hearing event.',
                                   'EVENT_DATE': 'Date corresponding to each evidentiary event.',
                                   'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to '
                                            'uniquely identify a permitted NPDES facility.'},
 'PCS_INDUSTRIAL_USER_INFO': {'CATEGORICAL_INDUSTRIAL_USERS': 'A four digit field representing the number of '
                                                              'categorical industrial u sers (CIUs) which discharge to '
                                                              "a particular pretreatment control authority's treatment "
                                                              'works (i.e., a POTW with an approved pre treatment '
                                                              'program.) Categorical industrial users are those users '
                                                              'in a particular industrial category (e.g., metal '
                                                              'chemicals , etc.) for which pretreatment standards have '
                                                              'been established or proposed. Industrial facilities in '
                                                              'categories such as t extiles or plastics molding and '
                                                              'forming for which specific effluent standards were '
                                                              'apparently considered but never proposed or es '
                                                              'tablished will not be included as categorical '
                                                              'industrial users.',
                              'INSP_DATE': 'The date of the actual inspection.',
                              'INSP_TYPE': 'Identifies the type of inspection performed.',
                              'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to '
                                       'uniquely identify a permitted NPDES facility.',
                              'SIGNIFICANT_INDUSTRIAL_USERS': 'A four digit field representing the number of '
                                                              'significant industrial users (SIUs) which discharge to '
                                                              "a particular pretreatment control authority's treatment "
                                                              'works (i.e., a POTW with an approved pretreatment '
                                                              'program). Significant industrial users include all '
                                                              'categorical industrial users and significant '
                                                              'non-categorical industrial users. (Note: Although SIU '
                                                              'is defined in the 7/86 Pretreatment Compliance '
                                                              'Monitoring and Enforcement Guidance and may be defined '
                                                              'in regulation in the future, some POTWs still use a '
                                                              'slightly different definition of SIU. At this time, '
                                                              'report the number of identified SIUs subject to the '
                                                              "POTW's definition of SIU.)",
                              'SIUS_IN_SNC_WITH_PRETR_STDS': 'A three-digit field representing the number of '
                                                             'significant industrial users (SIUs)  in significant '
                                                             'noncompliance (SNC) in the past year (as defined in the '
                                                             '7/86 Pretreatment Compliance Monitoring and Enforcement '
                                                             'Guidance and possibly soon to be defined in regulation) '
                                                             'with applicable pretreatment standards (categorical '
                                                             'standards, local limits, and prohibited discharge '
                                                             'standards)  or reporting standards.  Such significant '
                                                             'noncompliance could be identified either through '
                                                             'monotoring by the Control Authority or through IU '
                                                             'self-monitoring.  Until this appears  in regulation '
                                                             '(probably incorported into the definition of significant '
                                                             'violation), POTWs may use their existing criteria for '
                                                             'SNC although use of the aforementined definition in '
                                                             'guidance is strongly encouraged.  (ote: The PCI supplies '
                                                             'this information as percentage of all SIUs; mulitply the '
                                                             'percentage by the total number of SIUs (contained in '
                                                             'SIGNIFICANT_INDUSTRIAL_USERS) to determine the correct '
                                                             'value for this field.)',
                              'SIUS_NOT_INSP_SAMPLED': 'A three digit field representing the number of significant '
                                                       'industrial  users (SIUs) which were not inspected or sampled '
                                                       'by the pretreatment control authority in the past year. (Note: '
                                                       'The PCI suppli es this information as a percentage of all '
                                                       'SIUs; multiply the percentage by the total number of SIUs '
                                                       '(contained in SIGNIFICANT_INDUSTRIAL_USERS) to determine the '
                                                       'correct value for this field.',
                              'SIUS_WITHOUT_CTL_MECHANISM': 'A three digit field representing the number of '
                                                            'significant industrial  users (SIUs) for which a current '
                                                            '(unexpired) control mechanism (e.g., permit, sewer use '
                                                            'ordinance, or formal contract), as  defined in the 10/83 '
                                                            'Guidance Manual for POTW Pretreatment Program '
                                                            'Development, is required but not yet issued. Alth ough '
                                                            'SIUs may be subject to a sewer user ordinance, there may '
                                                            'still be a need for the control authority to issue '
                                                            'certain S IUs individual control mechanisms to establish '
                                                            'more specific pretreatment standards, reporting '
                                                            'requirements, monitoring frequencies , etc. (Note: The '
                                                            'PCI supplies this information as a percentage of all '
                                                            'SIUs; multiply the percentage by the total number of  '
                                                            'SIUs [data element SIUS] to determine the correct entry '
                                                            'for the data element NOCM.)'},
 'PCS_INSPECTION': {'INSP_CODE': 'Identifies the type of inspector who performed the inspection.',
                    'INSP_DATE': 'The date of the actual inspection.',
                    'INSP_TYPE': 'Identifies the type of inspection performed.',
                    'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to uniquely identify '
                             'a permitted NPDES facility.'},
 'PCS_PCI_AUDIT': {'ADOPT_LOCAL_LIMITS': 'A one character field, related to TECH_EVAL_LOCAL_LIMIT, indicating whether '
                                         'the pretreatment control authority has adopted local limits for certain '
                                         'pollutants, if a technical evaluation  indicated the need for such local '
                                         'limits. These pollutants include cadmium, chromium, copper, lead, nickel, '
                                         'and zinc.',
                   'INSP_DATE': 'The date of the actual inspection.',
                   'INSP_TYPE': 'Identifies the type of inspection performed.',
                   'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to uniquely identify '
                            'a permitted NPDES facility.',
                   'PERMIT_MOD_FOR_PRETR_DATE': 'A six-character date field representing the date when pretreatment '
                                                "con trol authority's NPDES permit was modified to require "
                                                'pretreatment implementation.',
                   'SLUDGE_DISPOSAL_METHOD': 'A variable-length character field representing the sludge disposal met '
                                             'hods utilized by any of the POTWs covered by the pretreatment control '
                                             'authority.',
                   'TECH_EVAL_LOCAL_LIMIT': 'A one-character field indicating whether the pretreatment control auth '
                                            'ority has technically evaluated the need for local limits for all of the '
                                            'following pollutants: cadmium, chromium, copper, lead, nick el, zinc, and '
                                            'any others required by the pretreatment approval authority (i.e., EPA '
                                            'Region or State).'},
 'PCS_PERMIT_EVENT': {'EVENT_ACTUAL_DATE': 'The actual date the permit tracking event was completed.',
                      'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to uniquely '
                               'identify a permitted NPDES facility.',
                      'TRACKING_EVENT_CODE': 'Code which describes the permit tracking milestone event.'},
 'PCS_PERMIT_FACILITY': {'APPL_RECEIVED_DATE': 'The date on which the application for a National Pollutant Discharge '
                                               'Elimination System (NPDES) permit was received.',
                         'CITY_CODE': 'The five digit code defined in the city master file and maintained by EPA, '
                                      'Monitoring and Data Support Division. The codes are unique for each city and '
                                      'place in a particular state or territory.',
                         'CITY_NAME': 'The name of the city where the facility is located. Each city name is defined '
                                      "with its corresponding city code in the system's city/state code table.",
                         'CODE_OF_ACCURACY': 'Code describing technical accuracy of latitude and longitude data.',
                         'COGN_OFFICIAL': "The name and/or department of the permittee's representative responsible "
                                          'for completing Discharge Monitoring Reports (DMR); also referred to as '
                                          'Facility Contact Person.',
                         'COGN_OFFICIAL_TELE_NUMBER': 'The telephone number of the permittee representative '
                                                      'responsible for administration of the DMRs.',
                         'COUNTY_CODE': 'The standard three digit Federal Information Processing Standards (FIPS) code '
                                        'which defines the county in which the facility is located.',
                         'COUNTY_NAME': 'The county name is the name of the county where the facility is located.',
                         'CURR_YEAR_AUTO_QNCR_STAT': 'Automatically set to indicate the status of reportable '
                                                     'non-compliance as it appeared on the quarterly non-compliance '
                                                     'report (QNCR) for the current year.',
                         'CURR_YEAR_MANL_QNCR_STAT': 'Manually set to indicate the status of reportable noncompliance '
                                                     'as it appeared on the quarterly noncompliance report for the '
                                                     'current year for major facilities. May be used for reportable '
                                                     'noncompliance indication for minor facilities.',
                         'DATUM': 'Describes the datum used to determine the latitude and longitude coord inates.  A '
                                  'datum is a network of monuments and reference points defining a mathematical '
                                  'surface from which geographic computations can be made (see EPA Locational Data '
                                  'Policy Implementation Guidance).',
                         'DESCRIPT': 'A text description of a code, such as a permit tracking event code.',
                         'DRAFT_PERM_PUB_NOTIF_DATE': 'The date on which public notification is given, indicating a '
                                                      'National Pollutant Discharge Elimination System (NPDES) permit '
                                                      'will be issued to a facility.',
                         'FEDERAL_GRANT_IND': 'Used to identify a publicly owned waste treatment works (POTW) with a '
                                              'SIC code of 4952 which obtained federal grant money to construct. The '
                                              "only value, '$', is to be entered as soon as a permittee who "
                                              'constructed using P.L. 92500 funding is completed and operational, and '
                                              'the final inspection is approved.',
                         'FINAL_LIMITS_IND': 'A facility is considered to be on final effluent limits when the '
                                             'permittee has completed all necessary construction to achieve the '
                                             'ultimate effluent limitation in the permit reflecting secondary '
                                             'treatment, best practicable control technology (BPT), best available '
                                             'technology (BAT), or more stringent limitations, such as state required '
                                             'limitations or water quality based limitations, or less stringent '
                                             'limitations established by a variance or a waiver. Refer to the Office '
                                             'of Water Evaluation Guide for the complete definition.',
                         'FLOW_RATE': 'The average flow, in millions of gallons per day, that a permitted facility was '
                                      'designed to accommodate.',
                         'INACTIVE_CODE': 'Code which indicates whether the facility is currently active.',
                         'INACTIVE_DATE': 'Date on which the facility became inactive or active.',
                         'INDUSTRY_CLASS': 'Identifies the industrial classification of a facility.',
                         'LATITUDE': 'Latitude describing facility location.',
                         'LONGITUDE': 'Longitude describing facility location.',
                         'MAILING_CITY': 'The city in the primary facility mailing address.',
                         'MAILING_NAME': 'The facility mailing name.',
                         'MAILING_STATE': 'The state in the primary facility mailing address.',
                         'MAILING_STREET_1': 'The first of two lines of street information in the primary facility '
                                             'mailing address.',
                         'MAILING_STREET_2': 'The second line of street information in the primary facility mailing '
                                             'address.',
                         'MAILING_ZIP_CODE': 'The zip code in the primary facility mailing address.',
                         'MAJOR_DISCHARGE_INDICATOR': 'A one character code designating that the facility has been '
                                                      'identified as a major or minor discharger.',
                         'METHOD': 'Code describing the procedure used to determine the latitude and longitude '
                                   'coordinates.',
                         'MILEAGE_IND': 'A five-character field giving the length of a particular facility stream '
                                        'segment in miles downstream from the beginning of the stream segment.',
                         'NAME_1': 'The first 30 characters of the official name of the facility which appears on the '
                                   'National Pollutant Discharge Elimination System (NPDES) permit application.',
                         'NAME_2': 'The next 30 characters of the official name of the facility which appears on the '
                                   'NPDES permit application. See NAME_1.',
                         'NMP_FINAL_SCHED': 'Indicates whether a final and enforceable Municipal Compliance Plan (MCP) '
                                            'schedule has been established to meet all statutory requirements in '
                                            'accordance with the National Municipal Policy (NMP). If a schedule has '
                                            'not been established, indicates reason for delay.',
                         'NMP_FINAN_STAT_CODE': 'Indicates the financial fitness of the Publicly Owned Treatment Works '
                                                '(POTW) to comply with the municipal compliance plan (MCP) schedule '
                                                'and meet the statutory requirements in accordance with the National '
                                                'Municipal Policy (NMP).',
                         'NMP_QUARTER': 'Indicates the fiscal quarter during which the final enforceable municipal '
                                        'compliance plan (MCP) schedule is anticipated to be or was established.',
                         'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to uniquely '
                                  'identify a permitted NPDES facility.',
                         'ORIGINL_PERMIT_ISSUE_DATE': 'The date the first permit was issued for a facility.',
                         'PERMIT_EXPIRED_DATE': 'The date the current permit will expire.',
                         'PERMIT_ISSUED_DATE': 'The date the current permit was issued/signed.',
                         'PRETREATMENT_CODE': 'A one-character code which indicates if the permitted municipality is '
                                              'required to develop a pretreatment program.',
                         'PREV_YEAR_AUTO_QNCR_STAT': 'Automatically set to indicate the status of reportable '
                                                     'non-compliance as it appeared on the quarterly non-compliance '
                                                     'report for the previous year.',
                         'PREV_YEAR_MANL_QNCR_STAT': 'Manually set to indicate the status of reportable non-compliance '
                                                     'as it appeared on the quarterly non-compliance report for the '
                                                     'previous year for major facilities. May be used for reportable '
                                                     'non-compliance for minor facilities.',
                         'RECEIVING_WATERS': 'The name of the river, stream, tributary, lake or other body of water '
                                             'into which the effluent is discharged.',
                         'RECVNG_STREAM_CLASS_CODE': 'A two-character field containing a code which describes the '
                                                     'related facility stream segment type.',
                         'REGION': 'A two-digit code, 01 through 10, used to identify the EPA region in which the '
                                   'facility is located.',
                         'RIVER_BASIN': 'A six-digit field used to identify the river basin in which the facility '
                                        'lies.',
                         'SCALE': 'Describes the scale used to determine the latitude and longitude coordinates.',
                         'SIC_CODE': 'The four digit code for the principal activity causing the discharge at the '
                                     'facility as defined by the 1987 Standard Industrial Classification (SIC) Manual.',
                         'STREAM_SEGMENT': 'A four-character code assigned for facilities by EPA to identify stretches '
                                           "of water from one significant event to another, where 'significant event' "
                                           'represents the mouth of a body of water, the confluence of two streams, '
                                           'etc.',
                         'TYPE_OF_OWNERSHIP': 'A three digit code describing ownership classification.',
                         'TYPE_OF_PERMIT_ISSUED': 'A one-character code indicating whether EPA or a state has issued '
                                                  'the  permit.',
                         'USGS_HYDRO_BASIN_CODE': 'A code assigned by the United States Geological Survey to identify '
                                                  'drainage water basins for facilities by their geographic location. '
                                                  'Also referred to as Cataloging Unit and as HUC by frequent users of '
                                                  'Reach information.'},
 'PCS_PERMIT_NPID': {},
 'PCS_PIPE_SCHED': {'DISCHARGE_NUM': 'A three-digit code assigned for each point of discharge. Links a measurement '
                                     'record to the related limit record.',
                    'EPA_SUBMISSION_UNITS': 'A one character code used to designate that the submission period for '
                                            "reports due at the EPA regional office is based on months ('M').",
                    'FINAL_LIMITS_END_DATE': 'The date on which final limits end for the discharge number and report '
                                             'designator; usually the same as the permit expiration date.',
                    'FINAL_LIMITS_START_DATE': 'The date on which final limits begin for the discharge and report '
                                               'designator.',
                    'INIT_EPA_SUBMISSION_DATE': 'Date the first discharge monitoring report (or batch of reports) is '
                                                'due at the EPA regional office.',
                    'INIT_LIMITS_END_DATE': 'The date on which initial limits ended for the discharge number and '
                                            'report designator.',
                    'INIT_LIMITS_START_DATE': 'The date on which initial limits began for the discharge number and '
                                              'report designator.',
                    'INIT_RPT_DATE': 'The beginning date of the first reporting period. This is the date that '
                                     'collection of DMR information begins at the facility.',
                    'INIT_STATE_SUBMISSION_DATE': 'Date the first discharge monitoring report (or batch of reports) is '
                                                  'due at the state office.',
                    'INTERIM_LIMITS_END_DATE': 'The date on which interim limits end for the discharge number and '
                                               'report designator.',
                    'INTERIM_LIMITS_START_DATE': 'The date on which interim limits begin for the discharge number and '
                                                 'report designator.',
                    'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to uniquely identify '
                             'a permitted NPDES facility.',
                    'OUTFALL_TYPE_CODE': 'The type of outfall (pipe) being tracked (e.g., Effluent, Sludge, '
                                         'Stormwater).',
                    'PIPE_DESC': 'The free-form description of a pipe (discharge/designator). This field appears on '
                                 'the preprinted Discharge Monitoring Report (DMR).',
                    'PIPE_INACTIVE_CODE': 'Code specifying the active or inactive status of the pipe (discharge number '
                                          'and report designator).',
                    'PIPE_INACTIVE_DATE': 'The date on which the pipe became inactive.',
                    'PIPE_SET_QUALIFIER': 'A one-digit code used to provide unique linkage between Pipe Schedules, '
                                          'Parameter Limits, and Measurement/Violations.',
                    'REPORTING_UNITS': 'A one-character code used to designate that the reporting period is based on '
                                       "months ('M') or days ('D').",
                    'REPORT_DESIG': 'A one-character code used to designate a particular grouping of parameters for '
                                    'reporting purposes.  Links a measurement/violation record to the related limit '
                                    'record.',
                    'STATE_SUBMISSION_UNITS': 'A one-character code used to designate that the submission period for '
                                              "reports due at the state is based on months ('M').",
                    'UNITS_IN_EPA_SUBM_PERIOD': 'A two-digit number indicating the number of units, in months or days, '
                                                'in the submission period.',
                    'UNITS_IN_RPT_PERIOD': 'A three-digit number indicating the number of units, in months or days, in '
                                           'the report period.',
                    'UNITS_IN_STATE_SUBM_PERIOD': 'A two-digit number indicating the number of units, in months or '
                                                  'days, in the submission period.'},
 'PCS_PIPE_SCHED_LAT_LONG': {'DISCHARGE_NUM': 'A three-digit code assigned for each point of discharge. Links a '
                                              'measurement record to the related limit record.',
                             'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to uniquely '
                                      'identify a permitted NPDES facility.',
                             'PIPE_LAT': "Latitude describing the pipe's location.",
                             'PIPE_LAT_LONG_ACCURACY': "Code to describe the technical accuracy of the pipe's "
                                                       'longitude and latitude characteristics.',
                             'PIPE_LAT_LONG_DATUM': 'Describes the datum used to determine the pipe latitude and '
                                                    'longitude  coordinates. A datum is a network of monuments and '
                                                    'reference points defining a mathematical surface from which '
                                                    'geographic  computations can be made (see EPA Locational Data '
                                                    'Policy Implementation Guidance).',
                             'PIPE_LAT_LONG_DESC': 'Describes the exact place where the pipe latitude and longitude '
                                                   'coordinates were collected.',
                             'PIPE_LAT_LONG_METHOD': 'Describes the procedure used to determine the pipe latitude and '
                                                     'longitude coordinates.',
                             'PIPE_LAT_LONG_SCALE': 'Describes the scale used to determine the pipe latitude and '
                                                    'longitude coordinates.',
                             'PIPE_LONG': "Longitude describing the pipe's location.",
                             'PIPE_RECEIVING_STR_CLASS_CODE': 'A two-character field containing a code which describes '
                                                              'the related outfall stream segment type.',
                             'PIPE_SCHED_MILEAGE_IND': 'A five-character field giving the length of a particular '
                                                       'facility stre am segment in miles downstream from the '
                                                       'beginning of the stream segment.',
                             'PIPE_SCHED_STREAM_SEGMENT': 'A four-character code assigned for facilities by EPA to '
                                                          'identify stret ches of water from one significant event to '
                                                          "another, where 'significant event' represents the mouth of "
                                                          'a body of water, the confl uence of two streams, etc.',
                             'PIPE_SET_QUALIFIER': 'A one-digit code used to provide unique linkage between Pipe '
                                                   'Schedules, Parameter Limits, and Measurement/Violations.',
                             'PIPE_USGS_HYDRO_BASIN_CODE': 'A code assigned by the United States Geological Survey to '
                                                           'identify dra inage water basins for facilities by their '
                                                           'geographic location. Also referred to as Cataloging Unit '
                                                           'and as HUC by frequent users of Reach information.',
                             'REPORT_DESIG': 'A one-character code used to designate a particular grouping of '
                                             'parameters for reporting purposes.  Links a measurement/violation record '
                                             'to the related limit record.'},
 'PCS_PRETREATMENT_PERF_SUMMARY': {'CIVIL_OR_CRIM_JUDICIAL_ACTS': 'A two-digit field representing the number of civil '
                                                                  'or criminal judicial suits filed in court by '
                                                                  'pretreatment control authorities against '
                                                                  'significant industrial users (SIUs) in the past '
                                                                  'year.',
                                   'IUS_THAT_PAID_PENALTIES': 'A three-digit field representing the number of '
                                                              'industrial users from which monetary penalties/fines '
                                                              '(beyond typical user charges) have been collected by '
                                                              'the pretreatment control authority in the past year.',
                                   'NOVS_AND_AOS_AGAINST_SIUS': 'A three-digit field representing the number of '
                                                                'notices of violation, administrative orders, and '
                                                                'equivalent actions which have been issued against '
                                                                'significant industrial users by the pretreatment '
                                                                'control authority in the past year.',
                                   'NPDES': 'A National Pollutant Discharge Elimination System (NPDES) code used to '
                                            'uniquely identify a permitted NPDES facility.',
                                   'REPORT_END_DATE': 'A six digit date field representing the end date of the period '
                                                      'that the Pretreatment Performance Summary covers.',
                                   'REPORT_START_DATE': 'A six digit date field representing the start date of the '
                                                        'period that the Pretreatment Performance Summary covers.',
                                   'SIUS_IN_SNC_COMPL_SCHED': 'A three-digit field representing the total number of '
                                                              'all significant industrial users (SIUs) in significant '
                                                              'noncompliance (SNC) with pretreatment compliance '
                                                              'schedules by violating compliance schedule milestones '
                                                              'by 90 days or by violating compliance schedule '
                                                              'reporting deadlines by 3 days. Until this definition '
                                                              'appears in regulation (probably incorporated into the '
                                                              'definition of significant violation), POTWs may use '
                                                              'their existing criteria for SNC although use of the '
                                                              'aforementioned definition in guidance is strongly '
                                                              'encouraged.  NOTE: The PPS provides the number of SIUs '
                                                              'not meeting compliance schedules; additional research '
                                                              'may be needed to determine whether these violations '
                                                              'constitute significant noncompliance.',
                                   'SIUS_WITH_PUBLISHED_VIOLS': 'A three-digit field representing the number of '
                                                                'significant industrial  users (SIUs) with significant '
                                                                'violations (as defined in 40 CFR 403.8(f)(2)(vii)) in '
                                                                'the past year published by the pretreatment control '
                                                                'authority in the largest local daily newspaper '
                                                                'located in the municipality services by the control '
                                                                'authority.'}}
