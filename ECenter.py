import requests
from datetime import date

market_type = "ECenter"

market_name = ["Minden", "Porta-Westfalica", "Osnabruck", "Melle", "Bad Nenndorf", "Herford"]

weekNumber = date.today().isocalendar()[1]

city_codes = ["3315", "3317", "3309", "3323", "3325", "3328"]

for city in city_codes:
 url = "https://static.edeka.de/media/handzettel/MINDEN/"+city+"/blaetterkatalog/pdf/complete.pdf"
 myfile = requests.get(url)
 for name in market_name:
  with open('C:\Users\user\Desktop\LeafletFiles\{0}_{1}_{2}.pdf'.format(market_type,name,str(weekNumber)), 'w') as pdf:
    pdf.write(myfile.content)

