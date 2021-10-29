# import demistomock as demisto
# from CommonServerPython import *
# from CommonServerUserPython import *
"""Base Integration for Cortex XSOAR - Unit Tests file

Pytest Unit Tests: all funcion names must start with "test_"

More details: https://xsoar.pan.dev/docs/integrations/unit-testing

MAKE SURE YOU REVIEW/REPLACE ALL THE COMMENTS MARKED AS "TODO"

You must add at least a Unit Test function for every XSOAR command
you are implementing with your integration
"""
from CommonServerPython import *
import io
import json
import requests
BASE_URL = "https://outbount-integration-tenant.armorblox.io/api/v1beta1/organizations/outbount-integration-tenant/incidents"
API_KEY = "QCOHlUilBVF6LRbA+IB6K+T5gISrs8Nwzaek5yadj9s="
payload: Dict = {}
headers = {
    'x-ab-authorization': API_KEY
}


def util_load_json(path):
    with io.open(path, mode='r', encoding='utf-8') as f:
        return json.loads(f.read())


def get_incident_message_ids(incident_id):
    incident_details_url = f"{BASE_URL}/{incident_id}"
    detail_response = requests.request("GET", incident_details_url, headers=headers, data=payload).json()
    message_ids = []
    # loop through all the events of this incident
    if 'events' in detail_response.keys():
        for event in detail_response['events']:
            message_ids.append(event['message_id'])

    if 'abuse_events' in detail_response.keys():
        for event in detail_response['abuse_events']:
            message_ids.append(event['message_id'])
    return message_ids


def test_get_incident_message_ids():
    result = get_incident_message_ids('3785')

    assert result == ["CAGEoyMdivjNP14oyLChhPmqgYaX-hTFTVwGEh2aGmT8BMekZMQ@mail.gmail.com"]


def test_response_status():
    detail_response = requests.request("GET", BASE_URL, headers=headers, data=payload)
    assert detail_response.ok is True
