import json
import pprint as pp
import csv

def process_line(line):
    output = []

    length = len(line)
    output.append(length)

    fields = []
    for i in line:
        fields.append(i['field'])
    output.append(fields)

    contains_dob = False
    dateOfBirthRefData = ['Date de naissance','Date of birth','Data di nascita''Fecha de nacimiento','Geburtsdatum','F√∏dselsdato','Geboortedatum','Data de nascimento']
    for i in line:
        if i['field'] in dateOfBirthRefData:
            contains_dob = True
            dob_error_msg = i['rule']
        else:
            contains_dob = False
            dob_error_msg = None
    output.append(contains_dob)
    output.append(dob_error_msg)

    return output

# dateOfBirthDict = {'Date de naissance': 'fr',
# 'Date of birth': 'en',
# 'Data di nascita': 'it',
# 'Fecha de nacimiento':'es',
# 'Geburtsdatum':'de',
# 'F√∏dselsdato': 'da|no',
# 'Geboortedatum':'nl',
# 'Data de nascimento':'pt'}

path = '/Users/akikot/python_sandbox/passenger_details_errors/errors.txt'
# path = '/Users/akikot/python_sandbox/passenger_details_errors/sample.txt'

raw_data = open(path, "r").read().splitlines()

# print(raw_data)

data = []
for i in raw_data:
    x = i.split('::')
    data.append(x)

# print(len(data))
# print(data)


# keep only error codes
for i in data:
    del i[::2]

# print(len(data))

list_of_errors = []

for j in data:
    for i in j:
        json_list = json.loads(i)
        output = process_line(json_list)
        list_of_errors.append(output)

# print(len(list_of_errors))

# pp.pprint(list_of_errors)

fields = ['num_errors', 'error_type', 'dob_error_flag', 'dob_error_msg']

with open('cleaned_errors.csv', 'w') as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(fields)
    write.writerows(list_of_errors)
