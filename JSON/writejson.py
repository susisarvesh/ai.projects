import json 
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_employee": True
}
with open("newfile.json","w") as file:
    json.dump(data, file, indent=4)