#!/usr/bin/env python3
import requests #imports the requests library
from datetime import date #imports the date class from datetime lbrary

market_type = "Marktkauf" #var to set the market type

market_name = ["Loehne", "Herford", "Buende", "Espelkamp", "Belm", "Rinteln", "Bad_Salzuflen" ,"Hameln", "Osnabrueck", "Luebbecke", "Meppen",
"Wilhelmshaven", "Osterholz_Scharmbeck", "Wunstorf", "Hannover"] # array of market names

weekNumber = date.today().isocalendar()[1] #var which stores the ISO week number

url_parts = ["20018_Loehne", "20004_Herford", "20009_Buende", "20071_Espelkamp", "20015_Belm", "20014_Rinteln", "20013_Bad_Salzuflen", 
"20046_Hameln", "20002_Osnabrueck", "20007_Luebbecke", "20017_Meppen", "20026_Wilhelmshaven", "20102_Osterholz_Scharmbeck", "20022_Wunstorf", 
"20025_Hannover"]

for part in url_parts: #for loop to loop through the location keys
 url = "https://static.edeka.de/media/handzettel/MINDEN/MARKTKAUF_"+part+"/blaetterkatalog/pdf/complete.pdf" #API URL
 myfile = requests.get(url) #gettting the info from the API using the get method of the requests library
 for name in market_name: #for loop to loop through the nomenclature variables
  with open('{0}_{1}_{2}.pdf'.format(market_type,name,str(weekNumber)), 'wb') as pdf: #opening file to save the PDF
    pdf.write(myfile.content) #writing of the PDF

