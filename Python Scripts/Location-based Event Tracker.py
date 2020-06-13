import time

months_list=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
month_len_list=[31,28,31,30,31,30,31,31,30,31,30,31]

location_count={"tengah":0,"bukit timah":0,"ccnr":0}
location_monthly={"tengah":[0,0,0,0,0,0,0,0,0,0,0,0],"bukit timah":[0,0,0,0,0,0,0,0,0,0,0,0],\
                  "ccnr":[0,0,0,0,0,0,0,0,0,0,0,0]}

functions=["Display Total -view alltime totals for each location",\
           "Display Annual -view current year numbers",\
           "Display All Years -view all past year numbers",\
           "Display Total Risk -view ratio of event at each location",\
           "Display Monthly Risk -view risk for each location per month"]

location_years_list=[]
location_list=["tengah","bukit timah","ccnr"]

def disp_total():
    print("{:12}{}".format("Location:","Total Instances:"))
    for instance in location_count:
        if instance==0:
            instance="-"
        print("{:12}{:<4}".format(instance,location_count[instance]))

def disp_annual(location_monthly):
    print("{:12}".format("Location:"),end="")
    for month in months_list:
        print("{:4}".format(month),end="")
    print()
    for location in location_monthly:
        print("{:12}".format(location),end="")
        for instance in location_monthly[location]:
            if instance==0:
                instance="-"
            print("{:<4}".format(instance),end="")
        print()
        
def disp_annual_all(location_monthly):
    print("{:12}".format("Location:"),end="")
    for month in months_list:
        print("{:4}".format(month),end="")
    print()
    index=0
    for location in location_monthly:
        print("{:12}".format(location_list[index]),end="")
        for instance in location:
            if instance==0:
                instance="-"
            print("{:<4}".format(instance),end="")
        index+=1
        print()
        
def disp_total_risk(total):
    print("{:12}{}".format("Location:","Total Risk:"))
    for instance in location_count:
        if instance==0:
            instance="-"
        print("{:12}{:.2f}%".format(instance,location_count[instance]/total*100))
        
def disp_annual_risk(location_monthly):
    print("{:12}".format("Location:"),end="")
    for month in months_list:
        print("{:7}".format(month),end="")
    print()
    for location in location_monthly:
        print("{:12}".format(location),end="")
        for instance in location_monthly[location]:
            print("{:<4.2f}%  ".format(instance),end="")
        print()


time_now=time.localtime()
prev_year=time_now.tm_year

while True:
    location=input("Enter location of drone being deployed or a display function:")
    
    time_now=time.localtime()
    month=time_now.tm_mon
    year=time_now.tm_year
    print("Date: "+str(month)+"/"+str(year))
        
    lst=[]   
    for locations in location_monthly:
        lst+=[location_monthly[locations]]
    if prev_year!=year:
        location_years_list.append([prev_year,lst])
        print(location_years_list)
        for item in location_monthly:
            location_monthly[item]=[0,0,0,0,0,0,0,0,0,0,0,0]
        print(location_years_list)
    prev_year=year
    
    if location in location_count:
        location_count[location]+=1
        location_monthly[location][month-1]+=1
    elif location=="Display Total":
        disp_total()
    elif location=="Display Annual":
        disp_annual(location_monthly)
    elif location=="Display All Years":
        for years in location_years_list:
            print("Year:",years[0])
            disp_annual_all(years[1])
            print()
    elif location=="Display Total Risk":
        total_events=sum(location_count.values())
        disp_total_risk(total_events)
    elif location=="Display Monthly Risk":
        monthly_risk=location_monthly
        location_index=0
        for location in monthly_risk:
            count_month=0
            for month in monthly_risk[location]:
                total_len=0
                total_month=0
                for year in location_years_list:
                    total_len+=month_len_list[count_month]
                    total_month+=year[1][location_index][count_month]
                monthly_risk[location][count_month]=total_month/total_len*100
                count_month+=1
            location_index+=1
        disp_annual_risk(monthly_risk)
        
    elif location=="help":
        print("Locations:")
        for item in location_count:
            print(item)
        print("\nFunctions:")
        for item in functions:
            print(item)
        print("\nOthers:\nhelp\n!add_new\nexit")

    elif location=="!add_new":
        new=input("New location: ")
        location_count[new]=0
        location_monthly[new]=[0,0,0,0,0,0,0,0,0,0,0,0]
        location_list+=[new]
        print(new,"added")
        
    elif location=="exit":
        print("Warning! All data will be lost!")
        pw=input("Password[or 'cancel']: ")
        if pw=="scdf": #scdf=19346 s=19 c=3 d=4 f=6
            print("end")
            break
        elif pw=="cancel":
            print("Cancelling")
        else:
            print("Incorrect password")
    else:
        print("Invalid input.\nTo see a list of possible inputs, enter 'help'")
    print()
