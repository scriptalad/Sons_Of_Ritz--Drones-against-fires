import requests
weather_readings=requests.get('https://data.gov.sg/api/action/datastore_search?resource_id=4631174f-9858-463d-8a88-f3cb21588c67')
response=weather_readings.json()
month_count_lst=[0,0,0,0,0,0,0,0,0,0,0,0]
month_sum_lst=[0,0,0,0,0,0,0,0,0,0,0,0]
month_index_lst=['01','02','03','04','05','06','07','08','09','10','11','12']
for month in range(len(response['result']['records'])):
    for i in range(12):
        if (response['result']['records'][month]['month'][-2:])==month_index_lst[i]:
            month_sum_lst[i]+=float((response['result']['records'][month]['mean_rh']))
            month_count_lst[i]+=1

month_average_humidity_lst=[round((month_sum_lst[i]/month_count_lst[i]),1) for i in range(12)]

temp_readings=requests.get('https://data.gov.sg/api/action/datastore_search?resource_id=07654ce7-f97f-49c9-81c6-bd41beba4e96')
response_temp=temp_readings.json()
month_tempcount_lst=[0,0,0,0,0,0,0,0,0,0,0,0]
month_tempsum_lst=[0,0,0,0,0,0,0,0,0,0,0,0]
for month in range(len(response_temp['result']['records'])):
    for i in range(12):
        if (response_temp['result']['records'][month]['month'][-2:])==month_index_lst[i]:
            month_tempsum_lst[i]+=float((response_temp['result']['records'][month]['mean_temp']))
            month_tempcount_lst[i]+=1
    

month_average_temp_lst=[round((month_tempsum_lst[i]/month_tempcount_lst[i]),1) for i in range(12)]

average_monthly_temp=round(sum(month_average_temp_lst)/12,1)
average_monthly_humidity=round(sum(month_average_humidity_lst)/12,1)

both_conditions=[]
temp_condition=[]
humidity_condition=[]
neither_condition=[]
monthlst=['January','February','March','April','May','June','July','August','September','October','November','December']

for month in range(12):
    humidity_low=False
    temp_high=False
    if month_average_temp_lst[month]>average_monthly_temp:
        temp_high=True
        
    if month_average_humidity_lst[month]<average_monthly_humidity:
        humidity_low=True
        
    if humidity_low==True and temp_high==True:
        both_conditions.append(monthlst[month])
    elif humidity_low==True:
        humidity_condition.append(monthlst[month])
    elif temp_high==True:
        temp_condition.append(monthlst[month])
    else:
        neither_condition.append(monthlst[month])

print('{:<15}{:32}{:34}{:30}'.format('month of year','Humidity(compared to average)','Temperature(compared to average)','Risk of fires (relative)'))
for month in monthlst:
    risk='Low'
    temp='Lower than average'
    humidity='Higher than average'
    if month in both_conditions:
        risk='High'
        temp='Higher than average'
        humidity='Lower than average'
    elif month in temp_condition:
        risk='Medium'
        temp='Higher than average'
    elif month in humidity_condition:
        risk='Medium'
        humidity='Lower than average'
    print('{:<15}{:32}{:34}{:30}'.format(month,humidity,temp,risk))
print()
print('Maintenance,updating and sources of dataset(s) used in program are listed below:')
print('1. (Surface Air Temperature) dataset used in this program is from https://data.gov.sg/dataset/surface-air-temperature-monthly-mean and is updated and maintained monthly by the Singapore Government')
print('2. (Relative Humidity) dataset used in this program is from https://data.gov.sg/dataset/relative-humidity-monthly-mean and is updated and maintained monthly by the Singapore Government')

##################################################################################################### Code below is for alternative output formatting (up to your disgression) ##############################################################
#### Alternate output format 1      
##for elem in monthlst:
##    risk=''
##    if elem in both_conditions:
##        risk='Relatively high risk of fires (due to higher temperatures and lower humidity than average throughout the month)'
##    elif elem in temp_condition:
##        risk='Medium risk of fires (due to higher temperatures than average throughout the month)'
##    elif elem in humidity_condition:
##        risk='Medium risk of fires (due to lower humidity than average throughout the month)'
##    else:
##        risk='Relatively low risk of fires (due to lower temperatures and higher humidity than average throughout the month)'
##    print(elem+': '+risk)

####Alternate output format 2
##print('Relatively high risk of fires during month(due to higher temperatures and lower humidity than average throughout the month):')
##for month in both_conditions:
##    print(month)
##print()
##print('Medium risk of fires during month(due to higher temperatures than average throughout the month):')
##for month in temp_condition:
##    print(month)
##print()
##print('Medium risk of fires during month(due to lower humidity than average throughout the month):')
##for month in humidity_condition:
##    print(month)
##print()
##print('Relatively low risk of fires during month(due to lower temperatures and higher humidity than average throughout the month):')
##for month in neither_condition:
##    print(month)

####Alternate output format 3    
##if len(both_conditions)>0:
##    print('The month(s) of ('+', '.join(both_conditions)+') have a high risk of fires due to higher temperature and lower humidity than average')
##if len(temp_condition)>0:
##    print('The month(s) of ('+', '.join(temp_condition)+') have a medium risk of fires due to higher temperature than average')
##if len(humidity_condition)>0:
##    print('The month(s) of ('+', '.join(humidity_condition)+') have a medium risk of fires due to lower humidity than average')
##if len(neither_condition)>0:
##    print('The month(s) of ('+', '.join(neither_condition)+') have a low risk of fires due to lower temperature and higher humidity than average')

    
    



    
    
