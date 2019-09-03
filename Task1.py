import json

data = {}
data['students'] = []
data['students'].append({
    'name': 'Ryan Orem',
    'GitHubID': '54821916',
    'NetID': '625003103'
})

with open('identity.txt', 'w') as outfile:
    json.dump(data, outfile)