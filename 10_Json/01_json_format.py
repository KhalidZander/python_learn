import json

data = [{"name":"zs","age":11},{"name":"ls","age":15}]

json_str = json.dumps(data,ensure_ascii=False)

print(json_str)

l = json.loads(json_str)

print(type(l))

print(l)

print(l[0])