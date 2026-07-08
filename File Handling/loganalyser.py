from collections import defaultdict
logs = defaultdict(list)
with open("log.txt", "r") as f:
    for line in f:
        words = line.split()       
        if len(words) >0 and words[2].isupper():
            logs[words[2]].append(" ".join(words[3:]))
        # for word in words:
        #         logs[words[2]].append(" ".join([details for details in words[3:]]))

# print(f"Total Logs :{count}")
print(f"INFO :",len(logs["INFO"]))  
print(f"WARN :",len(logs["WARN"])) 
print(f"ERROR :",len(logs["ERROR"])) 
print()

for key,values in logs.items():
    print(f"{key} Logs")
    print("---------")
    for sub_values in logs[key]:
        print(f"{sub_values} \n")

