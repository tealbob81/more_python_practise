import requests
#import pyfiglet

key = '3c0d6d88-29fa-4ec8-b212-5dbfe9c3f607'
kettering = 324198
desborough = 351201


url = f'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/{desborough}?res=3hourly&key={key}'
#'http://datapoint.metoffice.gov.uk/public/data/wxfcs/all/json/sitelist&key={key}'
#f'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/324198?res=3hourly&key={key}'
#f'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key={key}'

res = requests.get(url).json()
temperature = res['SiteRep']['DV']['Location']['Period'][0]['Rep'][2]['T'] # key path to temperature
time = int(res['SiteRep']['DV']['Location']['Period'][0]['Rep'][2]['$'])/60 # key path to time value
place = res['SiteRep']['DV']['Location']['name'] # key to location name
tommorow = res['SiteRep']['DV']['Location']['Period'][1]['Rep'][4]['T'] 
#current_time = datetime.datetime.now()
deg = u"\N{DEGREE SIGN}"

##if current_time.hour <= 15:
##    temperature = res['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['T']
##    time = int(res['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['$'])/60
##elif current_time.hour > 15 and current_time.hour < 18:
##    temperature = res['SiteRep']['DV']['Location']['Period'][0]['Rep'][1]['T']
##    time = int(res['SiteRep']['DV']['Location']['Period'][1]['Rep'][2]['$'])/60
##else:
##    temperature = res['SiteRep']['DV']['Location']['Period'][0]['Rep'][2]['T']
##    time = int(res['SiteRep']['DV']['Location']['Period'][0]['Rep'][2]['$'])/60
##    
    
    

print(f"The temperature in {place.title()} is {temperature}{deg} at {round(time)}:00. Tommorow will be {tommorow}{deg}")
#print(current_time.hour)
#print(res['SiteRep']['DV']['Location']['Period'][1]['Rep'][3]['T'])


#print(res['Locations']['id'])

#for k in res['Locations']['Location'][0].keys():
##print(res['Locations']['Location'][3]['id'])
###print(res['Locations']['Location'])
##print(res['Locations']['Location'][3].get(''))
##print('Kettering' in res['Locations']['Location'][1])
##print(res['Locations']['Location'][0]['name'])
##for i in res['Locations']['Location']:
##    if i['name'] == 'Desborough':
##        print(i['id'])
##

