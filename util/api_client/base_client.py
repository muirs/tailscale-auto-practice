from requests import Session
from requests.auth import HTTPBasicAuth


class BaseClient():
    """
    Base client for API interactions.
    """

    def __init__(self, token: str, tailnet = "-"):
        """
        Initialize the BaseClient with a base URL and an optional session.
        
        :param token: The API token for authentication.
        :param tailnet: The tailnet to use (default is "-").
        """
        self.base_url = "https://api.tailscale.com/api/v2/"
        self.tailnet = tailnet

        basic = HTTPBasicAuth(token)
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Tailscale Python API Client",
        }
        self.session.auth = basic

    def get(self, endpoint: str, params=None):
        """
        Make a GET request to the specified endpoint.

        :param endpoint: The API endpoint to call.
        :param params: Optional query parameters for the request.
        :return: The response from the API.
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, data=None, json=None):
        """
        Make a POST request to the specified endpoint.

        :param endpoint: The API endpoint to call.
        :param data: Optional form data for the request.
        :param json: Optional JSON data for the request.
        :return: The response from the API.
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json)
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint: str, data=None, json=None):
        """
        Make a PUT request to the specified endpoint.

        :param endpoint: The API endpoint to call.
        :param data: Optional form data for the request.
        :param json: Optional JSON data for the request.
        :return: The response from the API.
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data, json=json)
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint: str):
        """
        Make a DELETE request to the specified endpoint.

        :param endpoint: The API endpoint to call.
        :return: The response from the API.
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url)
        response.raise_for_status()
        return response.json()
    
    def close(self):
        """
        Close the session.
        """
        self.session.close()

