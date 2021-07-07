from collections import defaultdict
from typing import Tuple, List
from openapi_server.annotator.load_data import AnnotationSet
from openapi_server.annotator.phi_types import ANNOTATOR_TYPES, PhiType

Tokens = List[str]
Label = int
Labels = List[int]
Span = Tuple[int, int]
Spans = List[Span]


def label_token(token: str, span: Span,
                annotation_set: AnnotationSet) -> Label:
    """Return majority annotation type for a given span
    """
    start, end = span

    # Count annotated characters
    overlap = defaultdict(int)
    for annotation in annotation_set:
        annotator_type = ANNOTATOR_TYPES.get(annotation['TYPE'], None)
        if annotator_type is not None:
            overlap[annotator_type] += max(
                min(end, annotation['end']) - max(start, annotation['start']),
                0
            )
    overlap = dict(overlap)

    # Return type index if most of the characters in the range are inside a
    # relevant annotation, else 0.
    span_length = end - start
    if overlap:
        max_type: PhiType = max(overlap.keys(), key=overlap.get)
        if overlap[max_type] > (span_length / 2) and \
                any(c.isalpha() for c in token):
            return max_type.value
    return 0


def label_tokens(tokens: Tokens, spans: Spans,
                 annotation_set: AnnotationSet) -> Labels:
    """Take list of spans and iterable of annotations; use those annotations to
    make list of labels parallel to list of spans
    """
    return [label_token(token, span, annotation_set) for token, span in
            zip(tokens, spans)]
