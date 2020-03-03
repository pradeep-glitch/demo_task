import csv
from zipfile import ZipFile 
import glob
from defined import zip_folder,csv_folder
#import pandas as pd
symbol=[]
import requests
import json
import datetime
from datetime import date, timedelta
from nse_functions import nse


symbol=[]

try:
    
    obj_nse=nse()
    #today=datetime.datetime.now()
    obj_nse.generate_zip_files()
    zip_files=obj_nse.read_zip_files_from_folder()
    print(zip_files)
    obj_nse.convert_zip_files_to_csv(zip_files)

    csv_files=obj_nse.read_csv_files_from_folder()
    obj_nse.keep_particular_column(csv_files)
    csv_files=obj_nse.read_csv_files_from_folder()
    symbol=obj_nse.getting_all_symbols()
    print(symbol)
    obj_nse.passing_all_files(csv_files,symbol)
except Exception as e:
    print(str(e))
# except Exception as e:
#     prin    print(files)
#     for i in files:
#         print(i)
#         #i='cm04FEB2020bhav.csv'
#         #with open(i,'rb')as csv:
#           #  print(csv)
#         for line in i():
#             array=line.split(',')
#             first_item=array[0]
#             print(first_item)
#      