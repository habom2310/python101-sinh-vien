import os
import csv

def check_data_dir_created(fname):
    return os.path.isdir(fname)

def check_data_file_created(fname):
    return os.path.isfile(fname)

def create_data_dir(fname):
    os.mkdir(fname)

def create_data_file(fname, field_names):
    with open(fname, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()

def get_all_data(fname):
    result = [] # list của dictionary - theo fields ở header file csv
    with open(fname, 'r') as f:
        reader = csv.DictReader(f)        
        for row in reader:
            result.append(row)
    return result

def update_data(fname, fieldsname, data): # mở file - ghi DL - đóng file 
    with open(fname, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldsname)
        writer.writeheader()
        writer.writerows([element.__dict__ for element in data])