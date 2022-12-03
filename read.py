from json import loads

with open("近义词.json") as f:
    data = loads(f.read())
    print(len(data))