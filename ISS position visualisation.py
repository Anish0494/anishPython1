import urllib
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#from netCDF4 import Dataset as NetCDFFile
url='http://api.open-notify.org/astros.json'
url2='http://api.open-notify.org/iss-now.json'
response=urllib.request.urlopen(url)
response2=urllib.request.urlopen(url2)
result =json.loads(response.read())
coordinates =json.loads(response2.read())
#getting information from url dictionary
number=result['number']
people=result['people']
name=[]
for i in range(number):
    name.append(people[i]['name'])
#getting information from url2 dictionary
message=coordinates['message']
timestamp=coordinates['timestamp']
latitude=coordinates['iss_position']['latitude']
longitude=coordinates['iss_position']['longitude']
#plotting the longitude and latitude on the world map
m = Basemap(projection='robin',lon_0=180)
m.drawcoastlines(linewidth=0.8)
m.drawcountries(linewidth=0.5)
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')
x,y=m(longitude,latitude)
m.plot(x,y,'^',markersize=10,color='black')
plt.show()
#Showing information about the ISS
print('Number Of People In ISS:-',number)
print('Name Of People In ISS')
for i in range(3):
    print(':-',name[i])
print('Latitude And Longitude Of ISS',latitude,'And',longitude)