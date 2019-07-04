import json
import urllib.parse
import urllib.request
from urllib.error import HTTPError


PUBLIC_DNS_SERVERS = {
    'Google': 'https://dns.google/resolve',
    'Cloudflare': 'https://cloudflare-dns.com/dns-query',
}


class DohJsonClient:

    def __init__(self, *args, **kwargs):
        self.servers = kwargs.get('servers', PUBLIC_DNS_SERVERS)
        self.default_server = kwargs.get('default_server', PUBLIC_DNS_SERVERS['Google'])

    def resolve(self, query, server=None):
        _server = server or self.default_server
        result = self._request(_server, query)
        result.update({'DOHServer': _server})
        return result

    def resolve_google(self, query):
        server = PUBLIC_DNS_SERVERS['Google'] 
        return self.resolve(query, server)

    def resolve_cloudflare(self, query):
        server = PUBLIC_DNS_SERVERS['Cloudflare'] 
        return self.resolve(query, server)

    def resolve_all(self, query):
        results = []
        for server in PUBLIC_DNS_SERVERS.values(): 
            results.append(self.resolve(query, server))
        return results

    def _request(self, base_url, data_dict={}):
        headers = {
            'Accept': 'application/dns-json'
        }
        data = urllib.parse.urlencode(data_dict)
        request = urllib.request.Request(
            base_url+'?'+data, headers=headers, method='GET')
        try:
            response = urllib.request.urlopen(request)  # nosec
        except HTTPError as error:
            response = error
        try:
            result = json.loads(response.read())
        except json.JSONDecodeError:
            raise
            result = {}
        return result

