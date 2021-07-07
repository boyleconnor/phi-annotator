from openapi_server.annotator.label_spans import label_tokens


TEXT = "Hi my name is John Smith, I live in Minnesota. It is Tuesday"
SPANS = [(0, 2), (3, 5), (6, 10), (11, 13), (14, 18), (19, 24), (24, 25),
         (26, 27), (28, 32), (33, 35), (36, 45), (45, 46), (47, 49), (50, 52),
         (53, 60)]
TOKENS = [TEXT[start:end] for start, end in SPANS]
ANNOTATION_SET_ONE = [{'TYPE': 'PATIENT', 'start': 14, 'end': 18},
                      {'TYPE': 'PATIENT', 'start': 19, 'end': 24},
                      {'TYPE': 'STATE', 'start': 36, 'end': 45},
                      {'TYPE': 'DATE', 'start': 53, 'end': 60}]
ANNOTATION_SET_TWO = [{'TYPE': 'PATIENT', 'start': 14, 'end': 24}]
OVERLAPPING_ANNOTATION_SET_ONE = [
    {'TYPE': 'PATIENT', 'start': 14, 'end': 20},
    {'TYPE': 'DOCTOR', 'start': 19, 'end': 24},
]
OVERLAPPING_ANNOTATION_SET_TWO = [
    {'TYPE': 'DOCTOR', 'start': 14, 'end': 20},
    {'TYPE': 'PATIENT', 'start': 19, 'end': 24},
]


def test_label_span_one():
    labels = label_tokens(TOKENS, SPANS, ANNOTATION_SET_ONE)
    assert labels == [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 3]


def test_label_span_two():
    labels = label_tokens(TOKENS, SPANS, ANNOTATION_SET_TWO)
    assert labels == [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_label_span_three():
    labels = label_tokens(TOKENS, SPANS, OVERLAPPING_ANNOTATION_SET_ONE)
    assert labels == [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_label_span_four():
    labels = label_tokens(TOKENS, SPANS, OVERLAPPING_ANNOTATION_SET_TWO)
    assert labels == [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
