class Ip(object):
    """Flutterwave IP class
    """

    def __init__(self, util):
        self.util = util

    def check(self, ip_address, country):
        """Request location and information on a specified IP
        
        ip_address -> IP address to search
        country -> Country code (NGN)
        '"""
        payload = {
            'ip': ip_address,
            'country': country
        }
        return self.util.sendRequest(self.util.ipCheckRoute, payload)
