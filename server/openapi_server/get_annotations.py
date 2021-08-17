from openapi_server.annotator.phi_types import PhiType
from openapi_server.annotator.annotate import Annotator
from openapi_server.models import Note, TextContactAnnotation, \
    TextPersonNameAnnotation, TextIdAnnotation, TextDateAnnotation, \
    TextLocationAnnotation

annotator: Annotator = Annotator.load(
    'openapi_server/annotator/cached/annotator_model.joblib')


def get_annotations(note: Note, phi_type: PhiType):
    """Get list of Annotations of given PHI type for the inputted note
    """
    annotation_set, = annotator.annotate([note.text])
    if phi_type == PhiType.CONTACT:
        annotations = [TextContactAnnotation(
            start=annotation['start'],
            length=annotation['end'] - annotation['start'],
            text=annotation['text'],
            contact_type='other',
            confidence=95.0
        ) for annotation in annotation_set if
            annotation['type'] == phi_type.name]
    elif phi_type == PhiType.PERSON_NAME:
        annotations = [TextPersonNameAnnotation(
            start=annotation['start'],
            length=annotation['end'] - annotation['start'],
            text=annotation['text'],
            confidence=95.0
        ) for annotation in annotation_set if
            annotation['type'] == phi_type.name]
    elif phi_type == PhiType.ID:
        annotations = [TextIdAnnotation(
            start=annotation['start'],
            length=annotation['end'] - annotation['start'],
            text=annotation['text'],
            id_type='other',
            confidence=95.0
        ) for annotation in annotation_set if
            annotation['type'] == phi_type.name]
    elif phi_type == PhiType.DATE:
        annotations = [TextDateAnnotation(
            start=annotation['start'],
            length=annotation['end'] - annotation['start'],
            text=annotation['text'],
            confidence=95.0
        ) for annotation in annotation_set if
            annotation['type'] == phi_type.name]
    else:  # phi_type == PhiType.LOCATION:
        annotations = [TextLocationAnnotation(
            start=annotation['start'],
            length=annotation['end'] - annotation['start'],
            text=annotation['text'],
            location_type='other',
            confidence=95.0
        ) for annotation in annotation_set if
            annotation['type'] == phi_type.name]
    return annotations
