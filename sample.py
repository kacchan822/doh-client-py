import pprint

from dohjsonclient.client import DohJsonClient

client = DohJsonClient()

print('-----\nby default server(Google)\n-----\n')
result = client.resolve({'name': 'example.com', 'type': 'AAAA'})
pprint.pprint(result)
print('\n\n')

print('-----\nby Google public dns\n------\n')
result_google = client.resolve_google({'name': 'example.com', 'type': 'AAAA'})
pprint.pprint(result_google)
print('\n\n')

print('-----\nby Cloudflare public dns\n-----\n')
result_cloudflare = client.resolve_cloudflare({'name': 'example.com', 'type': 'AAAA'})
pprint.pprint(result_cloudflare)
print('\n\n')

print('-----\nby all\n-----\n')
result_all = client.resolve_all({'name': 'example.com', 'type': 'AAAA'})
pprint.pprint(result_all)
