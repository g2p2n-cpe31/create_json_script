import json

myKeys = ['prod_id', 'prod_name','store_id', 'username (owner)', 'price', 'rating', 'total', 'prod_pic', 'catagories', 'region', 'date_added']

item = int(input("Enter numbers of item: "))

result = ''

for i in range(item):
    temp = dict()
    for key in myKeys:
        value = str(input('Enter value of ' + key + ' : '))
        temp[key] =  value
    #  { ... }
    result += (str(temp) + ', ') #  { ... },  { ... },  { ... }

result_string = json.dumps(result)          # dict to string
result_json = json.loads(result_string)     # string to json

print(result_json)