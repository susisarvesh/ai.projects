import json
with open ("config.json","r") as file:
    load = json.load(file)

#  load["app"].items()
app_items = {
     
   "app": ["name",  "version","environment"],
   "database":["host",
    "port",
    "username",
    "password",
    "database_name"],
   
    "features":["enable_logging",  "max_connections"]
    
}
for item in load:
        for key ,value in app_items.items():
            for val in value:
                 print(val)
                #  if item[val]:
                #       print("ok")
                #  else:
                #     print(value)
                
                # if each_sub[item] not in load[item]:
                # print(value)

    # for sub_item in load[item]:
    #     print(sub_item)
    #         # if load[item][sub_item] == "":
    #                 print(item)
    #            
