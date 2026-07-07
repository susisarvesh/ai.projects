from collections import defaultdict
logs = defaultdict(list)
log_data =[]
count = 0
groups = ["INFO","WARN","ERROR"]
with open("log.txt", "r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in groups:
                logs[word].append(" ".join([details for details in words[3:]]))

         
        count += 1

# for key,values in logs.items():
#     print(f"{key}:{values}")

print(f"Total Logs :{count}")
print(f"INFO :",len(logs["INFO"]))  
print(f"WARN :",len(logs["WARN"])) 
print(f"ERROR :",len(logs["ERROR"])) 
print()

for key,values in logs.items():
    print(f"{key} Logs")
    print("---------")
    for sub_values in logs[key]:
        print(f"{sub_values} \n")
 




