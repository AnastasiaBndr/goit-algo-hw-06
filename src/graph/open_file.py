import csv

def open_file(path:str):
    arr=[]
    with open(path, encoding='utf-8',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arr.append(row)
    return arr