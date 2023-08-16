import json

def read_file(filename):
    with open(filename, 'r') as infile:
        return json.loads(infile.read())

def rkey(row):
    return row['Предложение']

data = read_file('tmp.json')

for row in data:
    row['Предложение'] = int(row['Предложение'])

# data = sorted(data, key=lambda k: k['Предложение'], reverse=True)
data = sorted(data, key=rkey, reverse=True)

for row in data:
    print(row)
