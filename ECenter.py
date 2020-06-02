#!/usr/bin/env python3
import requests #imports the requests library
from datetime import date #imports the date class from datetime lbrary

market_type = "ECenter" #var to set the market type

market_name = ["Minden", "Porta-Westfalica", "Osnabruck", "Melle", "Bad Nenndorf", "Herford"] # array of market names

weekNumber = date.today().isocalendar()[1] #var which stores the ISO week number

city_codes = ["3315", "3317", "3309", "3323", "3325", "3328"] #array of respective location keys from accuweather

for city in city_codes: #for loop to loop through the location keys
 url = "https://static.edeka.de/media/handzettel/MINDEN/"+city+"/blaetterkatalog/pdf/complete.pdf" #API URL
 myfile = requests.get(url) #gettting the info from the API using the get method of the requests library
 for name in market_name: #for loop to loop through the nomenclature variables
  with open('{0}_{1}_{2}.pdf'.format(market_type,name,str(weekNumber)), 'wb') as pdf: #opening file to save the PDF
    pdf.write(myfile.content) #writing of the PDF

