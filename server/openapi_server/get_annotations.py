from openapi_server.annotator.phi_types import PhiType
from openapi_server.annotator.annotate import Annotator
from openapi_server.models import Note


annotator: Annotator = Annotator.load(
    'openapi_server/annotator/cached/annotator_model.joblib')


def get_annotations(note: Note, phi_type: PhiType, annotation_class):
    """Get list of Annotations of given PHI type for the inputted note
    """
    annotation_set, = annotator.annotate([note.text])
    annotations = [annotation_class(
        start=annotation['start'],
        length=annotation['end'] - annotation['start'],
        text=annotation['text'],
        confidence=95.0
    ) for annotation in annotation_set if
        annotation['type'] == phi_type.name]
    return annotations
