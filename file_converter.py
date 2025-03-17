import csv
import json

def csv_to_json(csv_filename, json_filename):
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)  
            data = list(reader)

        with open(json_filename, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)  
        
        print(f"CSV successfully converted to JSON: {json_filename}")
    except Exception as e:
        print(f"Haiya! Error converting CSV to JSON: {e}")

def json_to_csv(json_filename, csv_filename):
    try:
        with open(json_filename, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)  

        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
            if len(data) > 0:  #
                writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())  
                writer.writeheader()
                writer.writerows(data)

        print(f"JSON successfully converted to CSV: {csv_filename}")
    except Exception as e:
        print(f"Error converting JSON to CSV: {e}")

csv_file = "delicious_in_dungeon.csv"    
json_file = "delicious_in_dungeon.json"  

csv_to_json(csv_file, json_file)

json_to_csv(json_file, "output.csv")
