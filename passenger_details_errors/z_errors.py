#path = '/Users/akikot/python_sandbox/passenger_details_errors/errors.txt'
path = '/Users/akikot/python_sandbox/passenger_details_errors/sample.txt'

raw_data = open(path, "r").read().splitlines()

# print(raw_data)

data = []
for i in raw_data:
    x = i.split('::')
    data.append(x)

# print(data)


# keep only error codes
for i in data:
    del i[::2]

print(data)
[['[{"field":"Pr√©nom","rule":"Caract√®res sp√©ciaux exclus (sauf accents). Doit contenir entre 2 et 54 caract√®res."},{"field":"Nom","rule":"Caract√®res sp√©ciaux exclus (sauf accents). Doit contenir entre 2 et 54 caract√®res."},{"field":"Date de naissance","rule":"Une date de naissance valide doit √™tre renseign√©e."}]']]


#
# error_codes = []
# for data in all_data:
#     for i in data:
#         y = i.split(',')
#         error_codes.append(y)
#
# print(error_codes)
#
# [['[{"field":"Pr√©nom"', '"rule":"Caract√®res sp√©ciaux exclus (sauf accents). Doit contenir entre 2 et 54 caract√®res."}', '{"field":"Nom"', '"rule":"Caract√®res sp√©ciaux exclus (sauf accents). Doit contenir entre 2 et 54 caract√®res."}', '{"field":"Date de naissance"', '"rule":"Une date de naissance valide doit √™tre renseign√©e."}]']]



#Ideal outcome
#Language, number of errors, which field has problem, flag if DoB error, return exact DoB error
