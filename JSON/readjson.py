import json
with open ("dummy.json","r",encoding="utf-8") as file:
    content = json.load(file)
    
    print(content)