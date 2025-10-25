<<<<<<< Updated upstream:spotflow_checkout/client.py
from checkout import SpotflowCheckout
=======
from spotflow_sdk.checkout import SpotflowCheckout
>>>>>>> Stashed changes:spotflow_sdk/client.py

class SpotflowApiClient:
    """
    A high-level API client for interacting with the Spotflow platform.

    This class serves as the main entry point for Python developers integrating Spotflow's 
    payment and financial services into their applications. It provides access to the
    checkout module for handling payments operations.
    """
    def __init__(self, api_key: str,  timeout:int =10, max_retries:int = 3):
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.checkout = SpotflowCheckout(api_key=self.api_key, timeout=self.timeout, max_retries=self.max_retries)