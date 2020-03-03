import datetime
import requests
from datetime import date, timedelta
import glob
from defined import zip_folder,csv_folder
from zipfile import ZipFile
import csv
import pandas as pd
symbol=[]
holiday_list=[]
class nse:
    
    def read_zip_files_from_folder(self):
        
        zip_files=glob.glob(zip_folder)
        return zip_files

    def read_csv_files_from_folder(self):
        csv_files=glob.glob(csv_folder)
        print(csv_files)
        return csv_files

    def keep_particular_column(self,files):
        for i in files:
            f=pd.read_csv(i)
            keep_col = ['SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TIMESTAMP']
            print(f[keep_col])
            new_f=f[keep_col]
            new_f.to_csv(i, index=False)
    def getting_all_symbols(self):
    
        with open('cm03FEB2020bhav.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #print(csv_reader )
            for x in csv_reader:
        #print()
                symbol.append(x["SYMBOL"])
                #print(symbol)        
            return symbol
    def convert_zip_files_to_csv(self,z_file):
    
        try:
            for i in z_file:
                 file_name = i
                 with ZipFile(file_name, 'r') as zip: 
        
                    print(zip.extractall())
            

        except Exception as e:
            print(str(e))
                
    def passing_all_files(self,files,symbol):
        print(len(symbol))
        for i in range(len(symbol)):
          for j in files:
            print(j)
            with open(j, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                count=0
                for row in csv_reader:
                    print(row)
                    print(row["SYMBOL"])
                    element=row["SYMBOL"]
                #if element in symbol:
                
                
                    if(row["SYMBOL"]==symbol[i]):
                        print("hi")
                    #count+=1
                        with open(row["SYMBOL"],'a')as myfile:
                            writer=csv.writer(myfile)
                            print(type(row))
                            #writer.writerow([row])
                            writer.writerow([row["SYMBOL"],row["SERIES"],row["OPEN"],row["HIGH"],row["LOW"],row["CLOSE"],row["LAST"],row["PREVCLOSE"],row["TOTTRDQTY"],row["TIMESTAMP"]])
                    #print(count)
                        break    
         
    def generate_zip_files(self):
        start_date=date.today()
        start_date = start_date - timedelta(days=29)
         #   Description
#         1   21-Feb-2020 Friday  Mahashivratri
#         2   10-Mar-2020 Tuesday Holi
#         3   02-Apr-2020 Thursday    Ram Navami
#         4   06-Apr-2020 Monday  Mahavir Jayanti
#         5   10-Apr-2020 Friday  Good Friday
#         6   14-Apr-2020 Tuesday Dr.Baba Saheb Ambedkar Jayanti
#         7   01-May-2020 Friday  Maharashtra Day
#         8   25-May-2020 Monday  Id-Ul-Fitr (Ramzan ID)
#         9   02-Oct-2020 Friday  Mahatma Gandhi Jayanti
#         10  16-Nov-2020 Monday  Diwali-Balipratipada
#         11  30-Nov-2020 Monday  Gurunanak Jayanti
#         12  25-Dec-2020 Friday  Christmas
#                 
        holidays_list=['21FEB2020','10MAR2020','02APR2020',] 
        day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
     
        for i in range(0,30):
             str_date=start_date.strftime("%d %m %Y")
# #         
             year=start_date.strftime("%Y")
        
             month=start_date.strftime("%b")
        
             day=start_date.strftime("%d")
        
             month=month.upper()
        
        
             date1=start_date.strftime("%d%b%Y")
             #print(date)
        
             date1=date1.upper()
        
             day = datetime.datetime.strptime(str_date, '%d %m %Y').weekday()
        
             if(date1 not in holidays_list):
               if(day_name[day]!='Sunday' and day_name[day]!='Saturday'):
                     url='https://archives.nseindia.com/content/historical/EQUITIES/'+str(year)+'/'+str(month)+'/cm'+str(date1)+'bhav.csv.zip'
            
                     print(url)
                     r = requests.get(url, allow_redirects=True)
         
                     with open('cm'+str(date1)+'.zip', 'wb') as file:
            
                        file.write(r.content)
                        file.close()
               else:
                  print("No data")
             start_date=start_date + timedelta(days=1)
            
    
        
        #response=requests.get ('https://archives.nseindia.com/content/historical/EQUITIES/2020/FEB/cm27FEB2020bhav.csv.zip')
         #print(response)  
        
