import json
import requests
from datetime import datetime,date,timedelta
import sys


try:
    myage = sys.argv[2]
    pin=sys.argv[1]
    days=30
    d=date.today()
    
    for i in range(1,8):
        d+=timedelta(days=1)
        
        date=datetime.strftime(d,"%d-%m-%Y")
        print(date)
        URL='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(str(pin),str(date))
        
        
        data= requests.get(url=URL,headers={'User-Agent':'Mozilla/5.0', "Accept-Language": "hi_IN","accept": "application/json"} ).json()

        mylist = data.get("sessions")
        print(type(mylist))
        print(len(mylist))

        mydict = mylist[0]

        mysession = mydict.get("sessions")
        print(mydict.get("name"))
        for i in mylist:
            if i.get("available_capacity_dose1")>0 and i.get("min_age_limit")==int(myage):
                print("{0:10}{1:20}".format(str(i.get("available_capacity")),str(i.get("slots"))))
            else:
                print("No slots available")

except IndexError:
    print("Usage: python vaccine_drive.py [District_ID] [AGE]")