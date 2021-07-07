from enum import IntEnum


class PhiType(IntEnum):
    PERSON_NAME = 1
    LOCATION = 2
    DATE = 3
    CONTACT = 4
    ID = 5


ALL_I2B2_TYPES = {'AGE', 'BIOID', 'CITY', 'COUNTRY', 'DATE', 'DEVICE',
                  'DOCTOR', 'EMAIL', 'FAX', 'HEALTHPLAN', 'HOSPITAL', 'IDNUM',
                  'LOCATION-OTHER', 'MEDICALRECORD', 'ORGANIZATION', 'PATIENT',
                  'PHONE', 'PROFESSION', 'STATE', 'STREET', 'URL', 'USERNAME',
                  'ZIP'}


I2B2_TYPES = {
    PhiType.PERSON_NAME: ('PATIENT', 'DOCTOR'),
    PhiType.LOCATION: ('CITY', 'COUNTRY', 'LOCATION-OTHER', 'HOSPITAL',
                       'STATE', 'STREET', 'ZIP'),
    PhiType.DATE: ('AGE', 'DATE'),
    PhiType.CONTACT: ('URL', 'EMAIL', 'FAX', 'PHONE', 'USERNAME'),
    PhiType.ID: ('IDNUM', 'BIOID')
}


ANNOTATOR_TYPES = {i2b2_type: annotator_type for annotator_type, i2b2_types in
                   I2B2_TYPES.items() for i2b2_type in i2b2_types}
