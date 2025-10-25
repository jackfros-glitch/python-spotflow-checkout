import os 
import pytest
import requests_mock
from spotflow_sdk.checkout import SpotflowCheckout
from tests.conftest import (
    api_key, 
    payment_data, 
    payment_data_response, 
    invalid_payment_data,
    invalid_payment_data_response
    )

def test_initialize_payment_with_valid_data_returns_success(api_key, payment_data, payment_data_response):
    checkout = SpotflowCheckout(api_key=api_key, timeout=10, max_retries=3)
    with requests_mock.Mocker() as m:
        m.post("https://api.spotflow.co/api/v1/payments/initialize", 
               json=payment_data_response, 
               status_code=200
               )
        response = checkout.initialize_payment(**payment_data)
    assert response.status_code == 200
    assert response.json()['status'] == "pending"

def test_initialize_payment_raises_type_error_for_missing_required_field(
        api_key,
        invalid_payment_data,
        invalid_payment_data_response
        ):
    checkout = SpotflowCheckout(api_key=api_key, timeout=10, max_retries=3)
    with requests_mock.Mocker() as m:
        m.post("https://api.spotflow.co/api/v1/payments/initialize", 
               json=invalid_payment_data_response, 
               status_code=400
               )
        with pytest.raises(TypeError)as excinfo:
            checkout.initialize_payment(**invalid_payment_data)
        
    assert "missing 1 required positional argument: 'currency'" in str(excinfo.value)

