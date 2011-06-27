#!/usr/bin/env python

lookup_table = {
    'facility': {

    },
    'facility_type': {
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
    'geo': {

    },
    'regulation': {
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
    'regulatory_program': {
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
