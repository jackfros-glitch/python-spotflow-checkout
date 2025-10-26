import os
import pytest
from dotenv import load_dotenv

load_dotenv 

@pytest.fixture
def api_key():
    key = os.getenv("SPOTFLOW_API_KEY")
    return key

@pytest.fixture
def payment_data():
    return {
        "amount": 2, 
        "currency": "USD",
        "local_currency": "NGN",
        "email": "test@testdemo.com"
    }

@pytest.fixture
def payment_data_response():
    return {
        'reference': 'e82b2ac955fd41519692e16f6e4a10d3', 
        'checkoutUrl': 'https://checkout.spotflow.co/QUL1HI5aGRV14gi', 
        'paymentCode': 'QUL1HI5aGRV14gi', 
        'status': 'pending', 
        'metadata': {}
    }


@pytest.fixture
def invalid_payment_data():
    return {
        "amount": 2, 
        "local_currency": "NGN",
        "email": "test@testdemo.com"
    }

@pytest.fixture
def invalid_payment_data_response():
    return {
        "code": "300",
        "message": "Invalid field in request",
        "statusCode": 400,
        "additionalDetails": {
            "currency": "Currency is required."
        }
    }

@pytest.fixture
def invalid_api_key():
    return "invalid_key"

@pytest.fixture
def initialize_payment_url():
    return "https://api.spotflow.co/api/v1/payments/initialize"

