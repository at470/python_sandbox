import json

path = '/Users/akikot/python_sandbox/trainline_extras/extras_sample.json'

all_data = json.load(open(path, "r"))

# print(type(all_data)) # dict

print(all_data['data'])

#
# data = []
#
# for i in raw_data:
#     for j in i:
#         data.append(j)
#
#
# print(data)

# print(data[1])
