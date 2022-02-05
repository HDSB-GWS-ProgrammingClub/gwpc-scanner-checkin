import requests


class Internet:
    """Methods to interact with the internet"""

    @staticmethod
    def connected_to_internet() -> bool:
        """
        Check if connected to the internet

        Returns: boolean
        """
        try:
            requests.get('https://google.com')
            return True
        except requests.exceptions.ConnectionError:
            return False
