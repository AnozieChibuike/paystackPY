from random import randint
import requests


class Paystack:
    def __init__(self, api_key):
        self.api_key = api_key
        self.paystack_init_url = "https://api.paystack.co/transaction/initialize"
        self.paystack_verify_url = f"https://api.paystack.co/transaction/verify/"

    def initializeTransaction(self, email, amount, reference=randint(100000, 999999), callback_url=None):
        """
        This is a function that Initializes a paystack transaction.

        Parameters:
            - self: A reference to the current class, you can live empty when calling the function
            - email: Email of user
            - amount: For v1.0 Amount in Naira
            - reference: You can either specify a reference or one will be generated for you
            - callback_url: You can either specify a callback url in the function or your paystack dashboard (It used in returning back to your server)
        Returns:
            - A dictionary of the details of the api call
        """
        if not email or not amount:
            raise Exception("Arguments Missing")
        url = self.paystack_init_url
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "email": email,
            "amount": int(str(amount + '00')),
            "reference": reference,
            "callback_url": callback_url
        }

        response = requests.post(url, headers=headers, json=data)

        # Check the response
        if response.status_code == 200:
            return {'data': response.json(), 'message': 'success'}
        else:
            return {'data': response.json(), 'message': 'error calling the api'}

    def verifyTransaction(self, reference):
        """
                This is a function that Initializes a paystack transaction.
                Parameters:
                    - self: A reference to the current class, you can live empty when calling the function
                    - reference: Reference of transaction you want to verify
                Returns:
                    - A dictionary of the details of the api call
                """
        if not reference:
            raise Exception("Arguments Missing")
        url = f"{self.paystack_verify_url}{reference}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        response = requests.get(url, headers=headers)
        # Check the response
        if response.status_code == 200:
            return {'data': response.json(), 'message': 'success'}
        else:
            return {'data': response.json(), 'message': 'error'}