from util.api_client.base_client import BaseClient


class TailscaleApi(BaseClient):
    """
    Tailscale API client for interacting with the Tailscale API.
    """

    def __init__(self, token: str, tailnet: str = "-"):
        """
        Initialize the TailscaleApi client with a token and an optional tailnet.

        :param token: The API token for authentication.
        :param tailnet: The tailnet to use (default is "-").
        """
        super().__init__(token, tailnet)
        self.base_url = "https://api.tailscale.com/api/v2/"

    def get_devices(self):
        """
        Get the list of devices in the tailnet.

        :return: A list of devices.
        """
        return self.get("/devices")