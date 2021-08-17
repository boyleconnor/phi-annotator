import connexion
from openapi_server.get_annotations import get_annotations
from openapi_server.models import TextContactAnnotation
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_contact_annotation_request import TextContactAnnotationRequest  # noqa: E501
from openapi_server.annotator.phi_types import PhiType


def create_text_contact_annotations(text_contact_annotation_request=None):  # noqa: E501
    """Annotate contacts in a clinical note
    Return the Contact annotations found in a clinical note # noqa: E501
    :param text_contact_annotation_request:
    :type text_contact_annotation_request: dict | bytes
    :rtype: TextContactAnnotationResponse
    """
    res, status = None, None
    if connexion.request.is_json:
        try:
            annotation_request = TextContactAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
            note = annotation_request.note
            annotations = get_annotations(note, phi_type=PhiType.CONTACT)

            res = TextContactAnnotationResponse(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    return res, status
