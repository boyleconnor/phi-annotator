import connexion
import pandas as pd
from openapi_server.annotator.phi_types import PhiType
from openapi_server.get_annotations import get_annotations
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_location_annotation_request import TextLocationAnnotationRequest  # noqa: E501
from openapi_server.models.text_location_annotation_response import TextLocationAnnotationResponse  # noqa: E501


class Data:
    def __init__(self):
        df = pd.read_csv("data/streets.csv")
        self._streets = df['Street'].str.lower().unique().tolist()

        df = pd.read_csv("data/cities.csv")
        self._cities = df['City'].str.lower().unique().tolist()

        df = pd.read_csv("data/states.csv")
        self._states = df['State'].str.lower().unique().tolist()

        df = pd.read_csv("data/countries.csv")
        self._countries = df['Name'].str.lower().unique().tolist()

        df = pd.read_csv("data/other_locations.csv")
        self._others = df['Other'].str.lower().unique().tolist()


data = Data()


def create_text_location_annotations():  # noqa: E501
    """Annotate locations in a clinical note

    Return the location annotations found in a clinical note # noqa: E501

    :param text_location_annotation_request:
    :type text_location_annotation_request: dict | bytes

    :rtype: TextLocationAnnotationResponse
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            annotation_request = TextLocationAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
            note = annotation_request.note
            annotations = get_annotations(
                note, phi_type=PhiType.LOCATION)

            res = TextLocationAnnotationResponse(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    return res, status


def add_annotations(annotations, matches, location_type):
    """
    Converts matches to TextLocationAnnotation objects and adds them
    to the annotations array specified.
    """
    for match in matches:
        annotations.append(
            TextLocationAnnotation(
                start=match.start(),
                length=len(match[0]),
                text=match[0],
                location_type=location_type,
                confidence=95.5
            ))
