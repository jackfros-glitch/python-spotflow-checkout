import os 
import pytest
import requests_mock
from spotflow_sdk import SpotflowApiClient
from spotflow_sdk.checkout import SpotflowCheckout
from tests.conftest import (
    api_key, 
    payment_data, 
    payment_data_response, 
    invalid_api_key,
    invalid_payment_data,
    invalid_payment_data_response,
    initialize_payment_url
    )

def test_client_creates_checkout_instance(api_key):
    client = SpotflowApiClient(api_key=api_key)
    assert isinstance(client.checkout, SpotflowCheckout)
    assert client.checkout.api_key == api_key
    assert client.checkout.timeout == client.timeout

def test_initializes_payment_with_client_returns_success(
        api_key, 
        payment_data, 
        payment_data_response,
        initialize_payment_url
        ):
    client = SpotflowApiClient(api_key)
    with requests_mock.Mocker() as m:
        url = initialize_payment_url
        m.post(
            url, 
            json=payment_data_response,
            status_code=200
            )
        response = client.checkout.initialize_payment(**payment_data)

    assert response.status_code == 200
    assert response.json()['status'] == "pending"


def test_initialize_payment_with_invalid_api_key_returns_error(invalid_api_key, initialize_payment_url, payment_data):
    client = SpotflowApiClient(api_key=invalid_api_key)
    with requests_mock.Mocker() as m:
        url = initialize_payment_url
        m.post(
            url, 
            json={
                "code": "6112",
                "message": "Invalid secret key format. Expected secret key or redirect credentials.",
                "statusCode": 400,
                "requestMarker": "e122efa4-965a-4fe7-8b10-d3b51fd35b92"
            },
            status_code=400
            )
        response = client.checkout.initialize_payment(**payment_data)
    assert response.status_code == 400
    assert "Invalid secret key format" in response.json()['message']


