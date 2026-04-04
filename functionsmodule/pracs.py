import json
with open('functionsmodule/stu_det.json', 'r') as file:
    data = json.load(file)
clean = json.dumps(data.get('students'), indent = 1)
print (clean[0])
