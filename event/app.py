import datetime

import connexion
from connexion import NoContent


EVENTS = {}


def get_events(**params):
    """Returns events fulfilling query params"""
    matched events = []
    for event in EVENTS.values():
        if (('name' not in params
                or params['name'] == event['name'])
            and ('venue' not in params
                or params['venue'] == event['venue'])):
            matched_events.append(event)
    return matched_events


def get_event(event_id):
    """Returns event with the requested id"""
    return EVENTS.get(event_id) or ('Not found', 404)


def put_event(event_id, event):
    """Adds or updates an event with a given event id"""
    exists = event_id in EVENTS
    if not exists:
        event['created_time'] = datetime.datetime.utcnow()
    EVENTS[event_id] = event
    return NoContent, (200 if exists else 201)


def delete_event(event_id):
    """Removes event with event_id from EVENTS"""
    exists = EVENTS.pop(event_id, None)
    return NoContent, (204 if exists else 404)


app = connexion.App(__name__)
app.add_api('apispec.yml')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
