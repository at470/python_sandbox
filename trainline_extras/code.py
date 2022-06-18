import json
import pprint as pp
import csv

# 1. sample dataset
##path for work computer
#path = '/Users/akikot/python_sandbox/trainline_extras/extras_sample.json'
##path for personal computer
# path = '/Users/akiko/python_sandbox/trainline_extras/extras_sample.json'


# 2. full dataset
##path for work computer
# path = '/Users/akikot/python_sandbox/trainline_extras/et2_extra_types_full_list.json'
##path for personal computer
path = '/Users/akiko/python_sandbox/trainline_extras/et2_extra_types_full_list.json'

original_json = json.load(open(path, "r"))

# pp.pprint(original_json.keys()) # get the keys to my dictionary input

all_properties_not_cleaned = []
for every_extra in original_json['data']:
    all_properties_not_cleaned.append(every_extra)

# extract the attributes values
all_offered_extras_attributes = []
for every_extra in all_properties_not_cleaned:
    all_offered_extras_attributes.append(every_extra['attributes'])

# clean data to extract only code, name and group from attributes
all_offered_extras = []
offered_extras_codes = []
for every_extra in all_offered_extras_attributes:
    # extract carrier from code string, will always be index 2 of code list (split by delimiter :)
    code_split_list = every_extra['code'].split(':')
    carrier = code_split_list[2]
    every_extra_properties = [carrier, every_extra['code'], every_extra['name'], every_extra['group']]
    all_offered_extras.append(every_extra_properties)
    every_extra_code_carrier = [carrier, every_extra['code']]
    offered_extras_codes.append(every_extra_code_carrier)

# print(len(all_offered_extras)) #500 extras
# print(all_offered_extras_codes)

distinct_extra_codes = set()
for every_code in offered_extras_codes:
    distinct_extra_codes.add(every_code[1])

# print(len(distinct_extra_codes)) #283 distinct codes

# # export list of list as csv
# with open("output.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(all_offered_extras)
#print('csv save done - extras with descriptions')

# export distinct list of urn codes as csv
with open("extras_codes.csv", "w") as f:
    data = list(distinct_extra_codes)
    header = ['urn_code']
    writer = csv.writer(f)
    writer.writerow(header)
    for each_extra_code in data:
        writer.writerow([each_extra_code])
# print('csv save done of extras codes')
