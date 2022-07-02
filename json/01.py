import json
data = '''
{
    "name": "Heitor",
    "phone": {
        "type": "intl",
        "number": "+55 8894166553"
    },
    "email": {
        "hide": "yes"
    }
}
'''
info = json.loads(data)
print('Name:', info['name'])
print('Phone:', info['phone']['number'])
print('Hide:', info['email']['hide'])

