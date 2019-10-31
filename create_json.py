import json

myKeys = ['prod_id', 'prod_name','store_id', 'username (owner)', 'price', 'rating', 'total', 'prod_pic', 'catagories', 'region', 'date_added']

item = int(input("Enter numbers of item: "))

result = []

for i in range(item):
    temp = dict()
    for key in myKeys:
        value = str(input('Enter value of ' + key + ' : '))
        temp[key] =  value
    #  { ... }
    result.append(temp)  # [{ ... },  { ... },  { ... }]

result_json = json.dumps(result, indent=4, separators=(',', ': '), sort_keys=False)          # list to json

print(result_json)
