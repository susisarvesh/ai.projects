import json
with open("dummy.json","r") as f:
    data1 = json.load(f)

with open("newfile.json","r") as f:
    data2 = json.load(f)
merged_data = data1 | data2
with open("mergeddata.json","w") as f:
    json.dump(merged_data ,f)