from spotflow_sdk.checkout import SpotflowCheckout

class SpotflowApiClient:
    """
    A high-level API client for interacting with the Spotflow platform.

    This class serves as the main entry point for Python developers integrating Spotflow's 
    payment and financial services into their applications. It provides access to the
    checkout module for handling payments operations.
    """
    def __init__(self, secret_key: str,  timeout_in_sec:int =10, max_retries:int = 3):
        self.secret_key = secret_key
        self.timeout = timeout_in_sec
        self.max_retries = max_retries
        self.checkout = SpotflowCheckout(secret_key=self.secret_key, timeout_in_sec=self.timeout, max_retries=self.max_retries)