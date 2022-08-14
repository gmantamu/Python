import json

#uses conversions to organize data in proper order

employee_data='''
    {
        "people":[
        {
            "name":"Garrett"
            "email":["gm@gmail.com", "cm@gmail.com"],
            "married":false
        },
        {
            "name":"Garrett"
            "email":["gwm@gmail.com", "cbm@gmail.com"],
            "married":false
        } 
    ]}
'''

print(employee_data)

data = json.loads(employee_data)
print(data)
    

