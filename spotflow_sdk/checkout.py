import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class SpotflowCheckout:
    """
    This class provides a simplified interface for initializing payment sessions 
    via the Spotflow payment gateway. It handles network retries, request headers, 
    and session persistence to ensure reliable API communication.
    """

    def __init__(self, api_key:str, timeout_in_sec:int, max_retries:int):
        self.api_key = api_key
        self.timeout = timeout_in_sec
        self.base_url = "https://api.spotflow.co/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        self.session = requests.Session()
        retries = Retry(
            total=max_retries,
            backoff_factor=0.3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["POST"]
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))
        

    def initialize_payment(self, amount: float, currency: str, local_currency: str, email: str, reference:str = None, callback_url:str = None, meta_data: dict = None, plan_id:str = None):
        """
        Initialize a Spotflow payment session.

        Args:
            amount (float): Amount to charge
            currency (str): Currency code for the payment charge(e.g., "NGN", "USD")
            local_currency (str): This is the local currency of your region (e.g., "NGN, GHS or KSH")
            email (str): Customer's email
            reference (str): A unique reference ID to identify each customer's transaction.
            callback_url (str): This is the URL the browser redirects to on success of a payment
            meta_data : additional details
            plan_id : This is the plan ID for a subscription plan

        Returns:
        dict: A dictionary containing the initialized payment session details.

        Example:
            {
                "reference": str,       # Unique transaction reference ID
                "checkoutUrl": str,     # URL for completing the payment
                "paymentCode": str,     # Spotflow's internal payment code
                "status": str,          # Payment status (e.g., "pending")
                "metadata": dict        # Any extra data associated with the transaction
            }

        Raises:
            requests.exceptions.HTTPError: If the API returns an error response.
            requests.exceptions.RequestException: For general network errors.
        """

        url = f"{self.base_url}/payments/initialize"

        payload = {
            "amount": amount,
            "currency": currency,
            "localCurrency" : local_currency,
            "customer": {
                "email": email
            }
        }

        if reference:
            payload["reference"] = reference
        
        if callback_url:
            payload["callBackUrl"] = callback_url
        
        if meta_data:
            payload["metadata"] = meta_data

        if plan_id:
            payload['planId'] = plan_id
       
        response = self.session.post(url, headers=self.headers, json=payload, timeout=self.timeout)
        return response

