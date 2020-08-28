
DesireSchema = {
    'title': {
        'type': 'string',
        'required': True
    },
    'amount': {
        'type': 'integer',
        'required': True
    },
    'currency': {
        'type': 'string',
        'required': True,
        'default': 'EUR'
    },
    'person': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'people',
            'field': '_id'
        }
    }
}

