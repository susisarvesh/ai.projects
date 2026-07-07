import csv
def read_csv(file_path):
    with open (file_path,mode="r" , encoding="utf-8",newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(f"Headers: {header}")
        
        for row in reader:
            print(row) 
read_csv("acs.csv")
